<script setup lang = "ts">
import { ref, watch } from 'vue';
import { toDateTimeChinese, toDateTimeChineseSlim } from '@/utils/DataTimeFomatter';
import { markMessageRead, deleteMessageByID, addToSchedule, addTag, updateTag } from '@/utils/Updater';
import ScheduleItem, { TagItem } from "@/type/ScheduleItem";

import mesStore from '@/store/modules/MessageStore'
import tlStore from '@/store/modules/TimelineScheduleStore'
import { useRouter } from 'vue-router';
import { computed } from 'vue';
const calcIcon = (type: number) => {
	return type == 1 ? ['blue-lighten-2', 'mdi-clock-time-eight'] : ['green-lighten-2', 'mdi-text-box']
}

const router = useRouter(); // 获取路由实例


const timelineStore = tlStore()
const messageStore = mesStore()

if (!messageStore.upToDate) messageStore.reloadAll()

watch(() => messageStore.upToDate, (newValue) => {
	if (newValue == false) {
		messageStore.reloadAll()
	}
});

const showError = ref(false)
const ErrorText = ref("")

// 处理确认日程的操作
const Overlay = ref(false)
const OpLoading = ref(false)

const Title = ref("null")
const Location = ref("null")
const isDDL = ref(false)
const StartTime = ref("null")
const FinishTime = ref("null")
const Stars = ref('0')
const Body = ref("null")
const Tags = ref(Array<TagItem>())
const TagsSelected = ref(Array<TagItem>())
const ScheID = ref(Array<number>())
const InitSchedule = (Sche: ScheduleItem, MID: number, i: number, j: number) => {
	OpLoading.value = false
	Title.value = Sche.Title
	Location.value = Sche.Location
	isDDL.value = Sche.Type == 4
	StartTime.value = toDateTimeChinese(Sche.StartTime)
	FinishTime.value = toDateTimeChinese(Sche.FinishTime)
	Stars.value = '0'
	Body.value = Sche.Body
	Tags.value = timelineStore.tagList
	TagsSelected.value = []
	ScheID.value = [Sche.ScheduleID, MID, i, j]
}
//

const showFliter = ref(false)
const fliterStars = ref("全部")
//const fliterType = ref("全部")
const fliterOrigin = ref(0)
const FliterButton = computed(() => {
	if (messageStore.fliterStars == 0 && messageStore.fliterOrigin == 0) return "筛选"
	else return "已筛选"
})
const initFliter = () => {
	fliterStars.value = (messageStore.fliterStars == 0 ? '全部' : messageStore.fliterStars.toString())
	fliterOrigin.value = messageStore.fliterOrigin
	showFliter.value = true
}
const confirmFliter = () => {
	messageStore.fliterStars = (fliterStars.value == '全部' ? 0 : parseInt(fliterStars.value))
	//messageStore.fliterType = (fliterType.value == '全部' ? 0 : (fliterType.value == '通知' ? 1 : 2))
	messageStore.fliterOrigin = fliterOrigin.value
	messageStore.upToDate = false
}

interface expandIf {
	[propname: number]: Array<number>;
}
const expand = ref<expandIf>({})

interface Loading { [propname: number]: boolean; }
const LoadingArrayHaveRead = ref<Loading>({})
const LoadingArrayDelete = ref<Loading>({})

interface LoadingS { [propname: string]: boolean; }
const LAAdd2Mes = ref<LoadingS>({})

const unfoldAll = () => {
	for (let i = 0; i < messageStore.messageList.length; i++)
		expand.value[messageStore.messageList[i].MessageID] = [messageStore.messageList[i].MessageID];
}

const foldAll = () => {
	//清空expand.value的每个属性
	for (let i = 0; i < messageStore.messageList.length; i++)
		expand.value[messageStore.messageList[i].MessageID] = [];
}

const markRead = (MID: number, key: number) => {
	LoadingArrayHaveRead.value[MID] = true
	markMessageRead(MID).then((status) => {
		if (status) messageStore.messageList[key].HaveRead = true;
		LoadingArrayHaveRead.value[MID] = false
	})
}

const deletemessage = (MID: number, key: number) => {
	LoadingArrayDelete.value[MID] = true
	deleteMessageByID(MID).then((status) => {
		if (status) messageStore.messageList[key].HaveRead = true;
		LoadingArrayDelete.value[MID] = false
		messageStore.messageList.splice(key, 1)
	})
}

// const calcIcon = (type: number) => {
// 	return type == 3 ? ['blue-lighten-2', 'mdi-clock-time-eight'] : ['green-lighten-2', 'mdi-text-box']
// }

const getMarker = (SID: number, MID: number) => {
	return MID.toString() + ' ' + SID.toString()
}
const addIntoSchedule = async () => {
	const StarValue = parseInt(Stars.value)
	if (Number.isNaN(StarValue) || StarValue < 0 || StarValue > 3) {
		ErrorText.value = "重要程度必须是0~3的整数"
		showError.value = true
		return
	}
	OpLoading.value = true
	const SID = ScheID.value[0]
	const MID = ScheID.value[1]
	const i = ScheID.value[2]
	const j = ScheID.value[3]
	LAAdd2Mes.value[getMarker(SID, MID)] = true
	const result = await addToSchedule(SID, MID, StarValue)

	if (result != -1) {
		for (let i = 0; i < TagsSelected.value.length; i++) {
			const tag = TagsSelected.value[i]
			let tagID = tag.value
			let text = (tag.title == undefined ? tag.toString() : tag.title.toString())
			if (tagID == undefined) tagID = await addTag(text)
			updateTag(tagID, result, 0)
		}
		messageStore.messageList[i].Schedules[j].Created = true
		timelineStore.upToDate = false
		timelineStore.reloadAll()
		Overlay.value = false
	}
	else {
		ErrorText.value = "添加失败"
		showError.value = true
	}
	LAAdd2Mes.value[getMarker(SID, MID)] = false
	OpLoading.value = false
}
</script>
<template>
	<v-app-bar color="cyan-lighten-3" density="compact" style="position: fixed;">
		<v-app-bar-title>通知</v-app-bar-title>

		<v-spacer></v-spacer>

		<v-btn prepend-icon="mdi-menu-open" variant="tonal" size="small" :disabled="messageStore.isloading"
			@click="initFliter()">{{ FliterButton }}</v-btn>

		<v-btn prepend-icon="mdi-plus" style="margin-left: 5px;" variant="tonal" size="small"
			:disabled="messageStore.isloading" @click="router.push({ name: 'createNewMessage' })">新通知</v-btn>

		<v-btn prepend-icon="mdi-refresh" style="margin-left: 5px;" variant="tonal" size="small"
			:disabled="messageStore.isloading" @click="messageStore.setUpdate()">刷新</v-btn>

		<!-- <v-btn icon="mdi-account" @click="router.push({ name: 'user' })"></v-btn> -->
	</v-app-bar>
	<v-container v-if="!messageStore.isloading" style="padding-left: 5px;padding-right: 5px">
		<v-row class="mt-2 mb-2" style="padding-right: 3% ;">
			<v-spacer></v-spacer>
			<v-btn variant="tonal" size="small" @click="foldAll()" style="margin-right: 10px;" color="secondry">
				全部折叠
			</v-btn>
			<v-btn variant="tonal" size="small" @click="unfoldAll()" color="primary">
				全部展开
			</v-btn>
		</v-row>
		<v-expansion-panels v-model="expand[item.MessageID]" class="messagePanel"
			v-for="(item, i) in messageStore.messageList" :key="i">
			<v-expansion-panel :value=item.MessageID>
				<v-expansion-panel-title>
					<v-icon v-if="item.HaveRead == false" size="x-large" class="newMesNotice">mdi-circle-small</v-icon>
					<v-container class="ExPanelTitle">
						<div class="text-h6">
							{{ item.Title }}
						</div>
						<div style="padding-left: 2px;">
							<div v-if="item.Sender!=''" class="text-subtitle-2 textSubtitle">
								{{ item.Sender }} | {{ toDateTimeChinese(item.SendTime) }}
							</div>
							<div v-else class="text-subtitle-2 textSubtitle">
								{{ toDateTimeChinese(item.SendTime) }}
							</div>
							<div class="text-subtitle-2 textSubtitle">
								{{ "来自：" + item.OriginGroupName }}
							</div>
							<div>
								<!-- <v-rating :model-value="item.Stars" size="small" density="compact" readonly></v-rating> -->
								<div v-if="item.Stars != 0 && item.Schedules.length" class="text-subtitle-2 textSubtitle">
									<span v-if="item.Stars == 3" style="color: #cd2c2c;">{{ "重要性：" + item.Stars }}</span>
									<span v-else>{{ "重要性：" + item.Stars }}</span>
									<span>{{" | 带有" + item.Schedules.length + "条日程" }}</span>
								</div>
								<div v-if="item.Stars == 0 && item.Schedules.length" class="text-subtitle-2 textSubtitle">
									{{"带有" + item.Schedules.length + "条日程" }}</div>
								<div v-if="item.Stars != 0 && item.Schedules.length == 0"
									class="text-subtitle-2 textSubtitle">
									<span v-if="item.Stars == 3" style="color: #cd2c2c;">{{ "重要性：" + item.Stars }}</span>
									<span v-else>{{ "重要性：" + item.Stars }}</span>
								</div>
							</div>
						</div>
					</v-container>
				</v-expansion-panel-title>
				<v-expansion-panel-text>
					<v-container class="ExPanelContent">
						<div class="text-subtitle-1 mt-1 mb-2" style="white-space: pre-wrap;word-break: break-all;">
							{{ item.Body }}
						</div>
						<div v-if="item.Images != undefined">
							<v-row v-if="item.Images.split(';').length > 1" class="ImageGrid mb-3">
								<div v-for="(img, j) in item.Images.split(';')" :key="j">
									<v-dialog v-if="img != ''"
										:width="$vuetify.display.width < $vuetify.display.height ? $vuetify.display.width * 0.8 : $vuetify.display.height * 0.8">
										<template v-slot:activator="{ props }">
											<v-card class="rounded-l" v-bind="props" style="width: 150;">
												<v-img class="ImageItem" :src="img" cover :max-width="600"
													aspect-ratio="1/1"></v-img>
											</v-card>
										</template>
										<template v-slot:default="{ isActive }">
											<v-card style="width: 100%;">
												<v-img class="ImageItem" :src="img" aspect-ratio="1/1"></v-img>
												<v-card-actions class="justify-end">
													<v-btn variant="text" @click="isActive.value = false">关闭</v-btn>
												</v-card-actions>
											</v-card>
										</template>
									</v-dialog>
								</div>
							</v-row>
						</div>
					</v-container>
					<v-container v-if="item.Schedules.length" class="ExPanelContent">
						<v-divider></v-divider>
						<v-expansion-panels class="mt-2 mb-2">
							<v-expansion-panel :title="'点击展示' + item.Schedules.length + '条日程'">
								<v-expansion-panel-text>
									<v-list style="margin-left: -22px;margin-right: -24px;">
										<v-list-item v-for="(Sch, j) in item.Schedules" :key="j" :value="Sch.Title"
											:prepend-icon="calcIcon(Sch.Type)[1]">
											<v-list-item-title style="margin-right: 25px;">
												{{ Sch.Title }}
											</v-list-item-title>
											<v-list-item-subtitle v-if="Sch.Type == 4">
												{{ toDateTimeChineseSlim(Sch.StartTime) }}
											</v-list-item-subtitle>
											<v-list-item-subtitle v-else>
												{{ toDateTimeChineseSlim(Sch.StartTime, Sch.FinishTime) }}
											</v-list-item-subtitle>
											<template v-slot:append>
												<v-tooltip text="加入到日程" close-on-content-click>
													<template v-slot:activator="{ props }">
														<v-btn variant="text" v-bind="props" class="addToListButton"
															@click="InitSchedule(Sch, item.MessageID, i, j); Overlay = true"
															:loading="LAAdd2Mes[getMarker(Sch.ScheduleID, item.MessageID)]"
															:disabled="Sch.Created">
															<v-icon v-if="!Sch.Created">mdi-plus</v-icon>
															<v-icon v-else>mdi-check</v-icon>
														</v-btn>
													</template>
												</v-tooltip>
											</template>
										</v-list-item>
									</v-list>
								</v-expansion-panel-text>
							</v-expansion-panel>
						</v-expansion-panels>
						<v-divider></v-divider>
					</v-container>
					<v-container class="d-flex align-center ExPanelContent">
						<v-card variant="flat" class="me-auto">
							<v-chip-group v-if="item.Tags.length" style="margin-left: 3%;">
								<v-chip v-for="(tag, j) in item.Tags" :key="j" color="primary" label outlined>
									{{ tag }}
								</v-chip>
							</v-chip-group>
						</v-card>
						<v-divider class="ms-3" inset vertical></v-divider>
						<v-card variant="flat" class="d-flex flex-row-reverse">
							<v-spacer></v-spacer>
							<v-btn variant="text" color="primary" style="margin-left: 15px;"
								@click="markRead(item.MessageID, i)" :loading="LoadingArrayHaveRead[item.MessageID]"
								:disabled="item.HaveRead">
								已读
							</v-btn>
							<v-btn variant="text" color="warning" style=";margin-left: 15px;"
								@click="deletemessage(item.MessageID, i)" :loading="LoadingArrayDelete[item.MessageID]">
								删除
							</v-btn>
						</v-card>
					</v-container>
				</v-expansion-panel-text>
			</v-expansion-panel>
		</v-expansion-panels>

	</v-container>
	<v-progress-circular v-if="messageStore.isloading" indeterminate class="scheduleCircular"></v-progress-circular>
	<div v-if="!messageStore.isloading && messageStore.messageList.length == 0" class="emptyNotice text-h6">暂无通知</div>

	<v-bottom-sheet v-model="Overlay">
		<!-- <v-overlay v-model="Overlay" activator="parent" location-strategy="connected"> -->
		<v-card class="NotificationOpCard">
			<v-card-title>
				确认添加日程
			</v-card-title>
			<v-container>
				<!-- 标题 -->
				<v-text-field v-model="Title" class="mt-3" label="标题" variant="underlined" readonly></v-text-field>
				<!-- 地点 -->
				<v-text-field v-model="Location" label="地点" prepend-icon="mdi-map-marker" readonly
					variant="underlined"></v-text-field>
				<!-- 选择时间表示模式 -->
				<v-switch label="单时间模式" v-model="isDDL" readonly></v-switch>
				<!-- 时间选择框 -->
				<v-text-field v-if="!isDDL" v-model="StartTime" label="开始" prepend-icon="mdi-clock-time-nine-outline"
					variant="underlined" readonly></v-text-field>
				<v-text-field v-if="!isDDL" v-model="FinishTime" label="结束" prepend-icon="mdi" variant="underlined" readonly
					class="mt-2"></v-text-field>
				<v-text-field v-if="isDDL" v-model="StartTime" label="时间点" prepend-icon="mdi-clock-time-five-outline"
					variant="underlined" readonly></v-text-field>
				<!-- 备注 -->
				<v-textarea class="mt-6" v-model="Body" label="备注" prepend-icon="mdi-file-document" readonly
					variant="outlined"></v-textarea>
				<v-divider />
				<!-- 重要程度 -->
				<v-text-field class="mt-4" v-model="Stars" label="设置本日程的重要程度" prepend-icon="mdi-star" variant="outlined"
					hint="0~3的整数，数字越大，重要性越高" :readonly="OpLoading"
					:rules="[value => (parseInt(value) >= 0 && parseInt(value) <= 3) || '必须是0~3的整数']"></v-text-field>
				<!-- Tags -->
				<v-combobox class="mt-2" prepend-icon="mdi-label-multiple" label="选择本日程的标签" hint="在下拉选择框中选择标签，或者输入新标签！"
					persistent-hint chips multiple v-model="TagsSelected" :items="Tags" :readonly="OpLoading"></v-combobox>
			</v-container>
			<v-card-actions>
				<v-spacer />
				<v-btn @click="addIntoSchedule();" :loading="OpLoading">添加</v-btn>
				<v-btn @click="Overlay = !Overlay">取消</v-btn>
			</v-card-actions>
		</v-card>
		<!-- </v-overlay>
	</v-container> -->
	</v-bottom-sheet>

	<!-- 筛选框 -->
	<v-bottom-sheet v-model="showFliter">
		<v-card class="fliter">
			<v-card-title class="fliteritem mt-2" style="text-align: center;">筛选通知</v-card-title>
			<v-select class="fliteritem mt-1" v-model="fliterStars" label="重要性" :items="['全部', '1', '2', '3']"
				prepend-icon="mdi-information-outline" density="compact"></v-select>
			<!-- <v-select class="fliteritem mt-1" v-model="fliterType" label="通知类型" :items="['全部', '通知', '推广']"
				prepend-icon="mdi-file-document" density="compact"></v-select> -->
			<v-select class="fliteritem mt-1" v-model="fliterOrigin" label="来源组织" :items="messageStore.GroupSelectList"
				prepend-icon="mdi-account-supervisor" density="compact"></v-select>
			<v-card-actions class="fliterButtonGroup mt-1">
				<v-btn variant="tonal" @click="showFliter = !showFliter">取消</v-btn>
				<v-card elevation="0"><v-card-title class="text-h6"></v-card-title></v-card>
				<v-btn variant="tonal" @click="confirmFliter(); showFliter = !showFliter">确定</v-btn>
			</v-card-actions>
		</v-card>
	</v-bottom-sheet>
	<!-- 信息提示条 -->
	<v-snackbar v-model="showError" timeout="1000">
		{{ ErrorText }}
		<template v-slot:actions>
			<v-btn color="blue" variant="text" @click="showError = false">关闭</v-btn>
		</template>
	</v-snackbar>
</template>

<style>
.ImageGrid {
	display: grid;
	grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
	gap: 5px;
	margin-top: 1px;
	margin-left: 2px;
}

.ImageItem {
	position: relative;
	overflow: hidden;
	aspect-ratio: 1;
	/* 保持图片宽高比例 */
}

.Image {
	width: 100%;
	height: 100%;
	object-fit: cover;
	/* 保持图片不变形，填充整个容器 */
}

.addToListButton {
	z-index: 3;
	right: 0px;
	position: absolute;
}

.textSubtitle {
	font-size: small;
	color: gray;
}

.ExPanelTitle {
	padding-left: 2.5px;
	padding-right: 2.5px
}

.ExPanelContent {
	padding-left: 5px;
	padding-right: 5px
}

.NotificationOpCard {
	display: flex;
	flex-direction: column;
	align-items: center;
	max-height: 600px;
	bottom: 10px;
	padding-left: 20px;
	padding-right: 20px;
	margin-left: 10px;
	margin-right: 10px;
}

.chipContainer {
	margin-bottom: -30px;
}

.messageContainer {
	display: flex;
	flex-direction: column;
	width: 95%;
}

.scheduleCircular {
	position: fixed;
	left: 50%;
	top: 50%;
}

.emptyNotice {
	position: fixed;
	left: 50%;
	top: 50%;
	transform: translate(-50%, -50%);
}

.fliter {
	display: flex;
	flex-direction: column;
	align-items: center;
	width: 95%;
	left: 2.5%;
	margin-bottom: 10px;
}

.fliteritem {
	width: 75%;
}

.fliterButtonGroup {
	position: static;
	margin-bottom: 10px;
}

.messagePanel {
	margin-top: 15px;
	margin-bottom: 10px;
}

.newMesNotice {
	z-index: 2;
	right: 2px;
	top: 1px;
	position: absolute;
	margin-bottom: 2px;
	color: red;
}
</style>