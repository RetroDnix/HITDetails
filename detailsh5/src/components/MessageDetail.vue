<script setup lang = "ts">
import { ref, watch, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { toDateTimeChinese, toDateTimeChineseSlim, toDateTimeChineseWeekDay, parseTime } from '@/utils/DataTimeFomatter';
import { getGroupByID, getSubGroupList } from '@/utils/Getter'
import { CreateScheduleFlip, postMessage } from '@/utils/Updater'

import ScheduleItem from '@/type/ScheduleItem';

import mesStore from '@/store/modules/MessageStore'
const messageStore = mesStore()

const router = useRouter(); // 获取路由实例
const route = useRoute();
const isloading = ref(true)

import grStore from '@/store/modules/GroupStore'
const groupStore = grStore()

const WindowTitle = ref('')
const OriginID = ref(0)
const Title = ref("null")
const Stars = ref('0')
const Body = ref("null")
const Type = ref(1)
const Sender = ref("")
const Schedules = ref(Array<ScheduleItem>())
const TagsSelected = ref(Array<any>())
const SelectedOriGroup = ref(Array<any>())
const CurGroup = ref(0)
const ReceiverSelectLoading = ref(false)
const SelectItem = ref(Array())
const SelectedItem = ref(Array())
const SelectedMethod = ref(Array<any>())
const PostMethod = [
	{ title: '仅选中的组织', value: 0, subtitle: '发送给所选组织' },
	{ title: '广播本消息', value: 1, subtitle: '发送给所选组织的所有子组织' },
	{ title: '透传途径组织', value: 2, subtitle: '发送给源头组织至所选组织之间的所有组织' }
]


const Overlay = ref(false)
const CurSche = ref(0)
const ScheTitle = ref("null")
const ScheLocation = ref("null")
const ScheisDDL = ref(false)
const ScheStartTime = ref("")
const ScheFinishTime = ref("")
const ScheBody = ref("null")

const showError = ref(false)
const ErrorText = ref("")

const IsSendingMes = ref(false)

const InitSchedule = (key?: number) => {
	if (key == undefined) {
		CurSche.value = -1
		ScheTitle.value = ''
		ScheLocation.value = ''
		ScheisDDL.value = false
		ScheStartTime.value = ''
		ScheFinishTime.value = ''
		ScheBody.value = ''
	}
	else {
		CurSche.value = key
		ScheTitle.value = Schedules.value[key].Title
		ScheLocation.value = Schedules.value[key].Location
		ScheisDDL.value = Schedules.value[key].Type == 4
		ScheStartTime.value = toDateTimeChineseSlim(Schedules.value[key].StartTime)
		ScheFinishTime.value = Schedules.value[key].Type == 4 ? '' : toDateTimeChineseSlim(Schedules.value[key].FinishTime)
		ScheBody.value = Schedules.value[key].Body
	}
}

const addSchedule = () => {
	if (ScheTitle.value == '') {
		showError.value = true
		ErrorText.value = '标题不能为空！'
		return
	}
	const st = parseTime(ScheStartTime.value).getTime()
	const ft = parseTime(ScheFinishTime.value).getTime()
	if (ScheisDDL.value && st == 0) {
		showError.value = true
		ErrorText.value = '非法的时间！'
		return
	}
	if (!ScheisDDL.value && (st == 0 || ft == 0)) {
		showError.value = true
		ErrorText.value = '非法的时间！'
		return
	}
	if (!ScheisDDL.value && (st > ft)) {
		showError.value = true
		ErrorText.value = '结束时间必须晚于开始时间！'
		return
	}
	if (CurSche.value == -1)
		Schedules.value.push({
			ScheduleID: 0,
			Title: ScheTitle.value,
			Body: ScheBody.value,
			Location: ScheLocation.value,
			Type: ScheisDDL.value ? 4 : 3,
			StartTime: parseTime(ScheStartTime.value),
			FinishTime: parseTime(ScheFinishTime.value),
			Stars: 0,
			Created: false,
			Tags: [],
		})
	else {
		Schedules.value[CurSche.value].Title = ScheTitle.value
		Schedules.value[CurSche.value].Body = ScheBody.value
		Schedules.value[CurSche.value].Location = ScheLocation.value
		Schedules.value[CurSche.value].Type = ScheisDDL.value ? 4 : 3
		Schedules.value[CurSche.value].StartTime = parseTime(ScheStartTime.value)
		Schedules.value[CurSche.value].FinishTime = parseTime(ScheFinishTime.value)
	}
	Overlay.value = false
}

const ScheParsedStartTime = computed(() => {
	const result = parseTime(ScheStartTime.value)
	return result.getTime() == 0 ? '' : toDateTimeChineseWeekDay(result)
})

const ScheParsedFinishTime = computed(() => {
	const result = parseTime(ScheFinishTime.value)
	return result.getTime() == 0 ? '' : toDateTimeChineseWeekDay(result)
})

if (route.name == 'createNewMessage') {
	WindowTitle.value = '新建通知'
	OriginID.value = -1
	Title.value = ''
	Stars.value = '0'
	Body.value = ''
	Type.value = 1
	Sender.value = ''
	isloading.value = false
}

const SendMes = async () => {
	IsSendingMes.value = true
	//console.log(SelectedOriGroup.value)
	if (Title.value == '') {
		ErrorText.value = '标题不能为空！'
		showError.value = true
		IsSendingMes.value = false
		return
	}
	const SelectedOriGroupID = parseInt(SelectedOriGroup.value.toString())
	if (Number.isNaN(SelectedOriGroupID)) {
		ErrorText.value = '请选择源头组织！'
		showError.value = true
		IsSendingMes.value = false
		return
	}
	if (SelectedItem.value.length == 0) {
		ErrorText.value = '请选择收件人！'
		showError.value = true
		IsSendingMes.value = false
		return
	}
	if (SelectedMethod.value.length == 0) {
		ErrorText.value = '请选择发送方式！'
		showError.value = true
		IsSendingMes.value = false
		return
	}
	const StarsNum = parseInt(Stars.value)
	if (Number.isNaN(StarsNum) || StarsNum < 0 || StarsNum > 3) {
		ErrorText.value = '重要程度必须是0~3的整数！'
		showError.value = true
		IsSendingMes.value = false
		return
	}
	const ScheIDList = Array<number>()
	for (let i = 0; i < Schedules.value.length; i++) {
		const result = await CreateScheduleFlip(Schedules.value[i])
		if (result == -1) {
			ErrorText.value = '日程附件创建失败！'
			showError.value = true
			IsSendingMes.value = false
			return
		}
		else ScheIDList.push(result)
	}

	const TarGroupIDList = Array<number>()
	SelectedItem.value.forEach((item: any) => {
		TarGroupIDList.push(parseInt(item.toString()))
	})
	const TarMethodList = Array<number>()
	SelectedMethod.value.forEach((item: any) => {
		TarMethodList.push(parseInt(item.toString()))
	})
	// console.log(SelectedOriGroupID)
	// console.log(TarGroupIDList)
	// console.log(TarMethodList)
	// console.log(ScheIDList)
	const result = await postMessage(SelectedOriGroupID, TarGroupIDList, TarMethodList, Title.value, Sender.value, Body.value, TagsSelected.value.toString(), StarsNum, ScheIDList, SourceList.value)
	if (result == false) {
		ErrorText.value = '通知发送失败！'
		showError.value = true
		IsSendingMes.value = false
		return
	}
	else {
		IsSendingMes.value = false
		messageStore.upToDate = false
		router.push('/Notification')
		return
	}
}


interface groupPathName { [propname: number]: string; }
watch(SelectedOriGroup, (newValue) => {
	//console.log(newValue)
	const newID = parseInt(newValue.toString())
	if (!Number.isNaN(newID)) {
		CurGroup.value = newID
		ReceiverSelectLoading.value = true
		SelectItem.value.length = 0
		SelectedItem.value.length = 0
		Promise.all([getSubGroupList(CurGroup.value), getGroupByID(CurGroup.value)]).then((results) => {
			const GroupDetail = results[1]
			const subgroupList = Array()
			const groupPath: groupPathName = {}
			subgroupList.push({ 'FatherGroupID': 0, 'GroupID': GroupDetail.GroupID, 'Name': GroupDetail.GroupName })
			results[0].forEach((item) => {
				subgroupList.push({ 'FatherGroupID': item.FatherGroupID, 'GroupID': item.GroupID, 'Name': item.Name })
			});

			subgroupList.forEach((item) => {
				groupPath[item.GroupID] = item.FatherGroupID == 0 ? item.Name : groupPath[item.FatherGroupID] + '/' + item.Name
				SelectItem.value.push({ 'title': item.Name, 'value': item.GroupID, 'subtitle': groupPath[item.GroupID] })
			});
			ReceiverSelectLoading.value = false
		})
	}
});

const ImageList = ref(Array<any>())
const SourceList = ref(Array<any>())
const fileInput = ref()
function handleFileChange(event: any) {

	let x = 0;
	while (event.target?.files[x] != undefined) {
		const file = event.target?.files[x];
		if (file) {
			const reader = new FileReader();
			// ToDo:文件类型/大小验证
			reader.onload = () => {
				ImageList.value.push(reader.result);
			};

			SourceList.value.push(file);
			reader.readAsDataURL(file);
			x++;
		}
	}
}

</script>
<template>
	<!-- 顶部导航栏 -->
	<v-app-bar density="compact" color='cyan-lighten-3'>
		<v-btn icon="mdi-chevron-left" @click="router.push('/Notification')">
		</v-btn>
		<v-app-bar-title>{{ WindowTitle }}</v-app-bar-title>
	</v-app-bar>

	<v-container v-if="!isloading" class="messageDetailBody">
		<!-- 标题 -->
		<v-text-field v-model="Title" label="标题" variant="outlined"
			:readonly="IsSendingMes"></v-text-field>
		<v-card class="itemCard">
			<!-- 收件人 -->
			<v-select label="源头组织" prepend-icon="mdi-account-supervisor" v-model="SelectedOriGroup"
				:items="groupStore.authoredGroupList" :loading="groupStore.isloading" density="compact"
				:readonly="ReceiverSelectLoading || IsSendingMes"></v-select>

			<!-- 目标组织 -->
			<v-select label="目标组织" :items="SelectItem" v-model="SelectedItem" multiple chips density="compact"
				prepend-icon="mdi-account-supervisor-circle" :readonly="ReceiverSelectLoading || IsSendingMes"
				:loading="ReceiverSelectLoading">
				<template v-slot:item="{ item, props }">
					<v-list-item v-bind="props">
						<v-list-item-subtitle>{{ item.raw.subtitle }}</v-list-item-subtitle>
						<template v-slot:prepend="{ isActive }">
							<v-list-item-action start>
								<v-checkbox-btn :model-value="isActive"></v-checkbox-btn>
							</v-list-item-action>
						</template>
					</v-list-item>
				</template>
			</v-select>

			<v-select label="通知发送方式" class="mt-2" :items="PostMethod" v-model="SelectedMethod" multiple chips
				density="compact" prepend-icon="mdi-tools" :readonly="IsSendingMes">
				<template v-slot:item="{ item, props }">
					<v-list-item v-bind="props">
						<v-list-item-subtitle>{{ item.raw.subtitle }}</v-list-item-subtitle>
						<template v-slot:prepend="{ isActive }">
							<v-list-item-action start>
								<v-checkbox-btn :model-value="isActive"></v-checkbox-btn>
							</v-list-item-action>
						</template>
					</v-list-item>
				</template>
			</v-select>

			<!-- 发送人名称 -->
			<v-text-field v-model="Sender" label="发送人名称" prepend-icon="mdi-account" variant="underlined"
				:readonly="IsSendingMes"></v-text-field>
		</v-card>
		<v-card class="itemCard">
			<!-- 重要程度 -->
            <v-row class="flex flex-row align-center" style="margin-top: 0px;margin-left: 0px;">
                <v-icon color="grey-darken-1" style="margin-right: 6px;">mdi-flag</v-icon>
                <div class="ma-2" style="color: grey;">重要程度</div>
                <v-rating hover v-model=Stars size="x-large" length="3" density="comfortable" color="yellow-darken-3" active-color="yellow-darken-2"
                    :readonly="IsSendingMes" style="margin-left: 15px;"></v-rating>
            </v-row>
		</v-card>
		<!-- <v-text-field class="mt-4" v-model="Stars" label="重要程度" prepend-icon="mdi-star" variant="outlined"
			hint="0~3的整数，数字越大，重要性越高" :readonly="IsSendingMes" density="compact"
			:rules="[value => (parseInt(value) >= 0 && parseInt(value) <= 3) || '必须是0~3的整数']"></v-text-field> -->
			
		<v-card class="itemCard">
			<!-- Tags -->
			<v-combobox class="mt-2" prepend-icon="mdi-label-multiple" label="标签" hint="输入通知的标签" persistent-hint chips
				multiple v-model="TagsSelected" :readonly="IsSendingMes" density="compact"></v-combobox>
		</v-card>
		<v-card class="itemCard">
			<!-- 备注 -->
			<v-textarea class="mt-4" v-model="Body" label="正文" prepend-icon="mdi-file-document" variant="outlined" rows="7"
				:readonly="IsSendingMes"></v-textarea>
		</v-card>
		<!-- 图片网格 -->
		<v-row v-if="ImageList.length" class="ImageGrid">
			<div v-for="(item, j) in ImageList" :key="j">
				<v-dialog
					:width="$vuetify.display.width < $vuetify.display.height ? $vuetify.display.width * 0.8 : $vuetify.display.height * 0.8">
					<template v-slot:activator="{ props }">
						<v-card class="rounded-l" v-bind="props" style="width: 150;">
							<v-img class="ImageItem" :src="item" cover :max-width="600" aspect-ratio="1/1">
								<v-row class="ma-2">
									<v-spacer></v-spacer>
									<v-btn icon="mdi-close" color="blue-lighten-4" size="xx-small"
										@click="ImageList.splice(j, 1);">
									</v-btn>
								</v-row>
							</v-img>
						</v-card>
					</template>
					<template v-slot:default="{ isActive }">
						<v-card style="width: 100%;">
							<v-img class="ImageItem" :src="item" aspect-ratio="1/1">
							</v-img>
							<v-card-actions class="justify-end">
								<v-btn variant="text" @click="isActive.value = false">关闭</v-btn>
							</v-card-actions>
						</v-card>
					</template>
				</v-dialog>
			</div>
		</v-row>

		<v-divider></v-divider>

		<v-btn class="mt-6" color="green-lighten-2" prepend-icon="mdi-camera" style="margin-left: 30%;width: 40%;"
			@click="fileInput.click()">添加图片</v-btn>

		<!-- 文件输入框，设置为隐藏 -->
		<input type="file" ref="fileInput" accept="image/*" style="display: none" multiple @change="handleFileChange">

		<!-- 显示日程附件 -->
		<div class="text-subtitle-1 mt-1" v-if="Schedules.length > 0">日程附件：</div>
		<v-list v-if="Schedules.length > 0">
			<v-list-item v-for="(Sch, j) in Schedules" :key="j" @click="InitSchedule(j); Overlay = true"
				:prepend-icon="Sch.Type == 4 ? 'mdi-text-box' : 'mdi-clock-time-eight'">
				<v-list-item-title>
					{{ Sch.Title }}
				</v-list-item-title>
				<v-list-item-subtitle v-if="Sch.Type == 4">
					{{ toDateTimeChinese(Sch.StartTime) }}
				</v-list-item-subtitle>
				<v-list-item-subtitle v-else>
					{{ toDateTimeChinese(Sch.StartTime, Sch.FinishTime) }}
				</v-list-item-subtitle>
				<template v-slot:append>
					<v-btn variant="tonal" size="x-small" icon="mdi-close" @click.stop="Schedules.splice(j, 1);"
						:active="!IsSendingMes"></v-btn>
				</template>
			</v-list-item>
		</v-list>
		<v-btn class="mt-6 mb-12" color="blue-lighten-2" prepend-icon="mdi-plus" style="margin-left: 30%;width: 40%;"
			@click="InitSchedule(); Overlay = true" :active="!IsSendingMes">添加日程附件</v-btn>
	</v-container>

	<!-- 底部操作栏 -->
	<v-sheet class="messageDetailBar">
		<v-divider></v-divider>
		<v-card-actions>
			<v-spacer></v-spacer>
			<v-btn variant="tonal" :disabled="isloading" :loading="IsSendingMes" @click="SendMes()">发布通知</v-btn>
		</v-card-actions>
	</v-sheet>

	<v-bottom-sheet v-model="Overlay">
		<v-card style="margin-left: 10px;margin-right: 10px; margin-bottom: 10px;">
			<v-card-title>
				添加日程附件
			</v-card-title>
			<v-card-text>
				<!-- 标题 -->
				<v-text-field v-model="ScheTitle" class="mt-3" label="标题" variant="underlined"
					prepend-icon="mdi-subtitles-outline"></v-text-field>
				<!-- 地点 -->
				<v-text-field v-model="ScheLocation" label="地点" prepend-icon="mdi-map-marker"
					variant="underlined"></v-text-field>
				<!-- 选择时间表示模式 -->
				<v-switch label="单时间模式" v-model="ScheisDDL"></v-switch>
				<!-- 时间选择框 -->
				<v-expand-transition>
					<v-text-field v-if="!ScheisDDL" v-model="ScheStartTime" :hint="ScheParsedStartTime" label="开始"
						placeholder="yy/mm/dd hh:mm" prepend-icon="mdi-clock-time-nine-outline" persistent-hint
						variant="underlined"></v-text-field>
				</v-expand-transition>
				<v-expand-transition>
					<v-text-field v-if="!ScheisDDL" v-model="ScheFinishTime" :hint="ScheParsedFinishTime" label="结束"
						prepend-icon="mdi" placeholder="yy/mm/dd hh:mm" variant="underlined" persistent-hint
						class="mt-2"></v-text-field>
				</v-expand-transition>
				<v-expand-transition>
					<v-text-field v-if="ScheisDDL" v-model="ScheStartTime" :hint="ScheParsedStartTime" label="时间点"
						placeholder="yy/mm/dd hh:mm" prepend-icon="mdi-clock-time-five-outline" persistent-hint
						variant="underlined"></v-text-field>
				</v-expand-transition>
				<!-- 备注 -->
				<v-textarea class="mt-6" v-model="ScheBody" label="备注" prepend-icon="mdi-file-document"
					variant="outlined"></v-textarea>
			</v-card-text>
			<v-card-actions>
				<v-spacer />
				<v-btn @click="addSchedule()">添加</v-btn>
				<v-btn @click="Overlay = !Overlay">取消</v-btn>
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
	<!-- 加载进度条 -->
	<v-progress-circular v-if="isloading" indeterminate class="messageDetailCircular"></v-progress-circular>
</template>
<style>
.itemCard {
	padding: 10px 20px 20px 20px;
	margin-top: 10px;
	margin-bottom: 10px;
}

.ImageGrid {
	display: grid;
	grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
	gap: 5px;
	margin-top: 1px;
	margin-bottom: 20px;
	margin-right: 5px;
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

.messageDetailBar {
	position: fixed;
	bottom: 0px;
	width: 100%;
}

.messageDetailBody {
	display: flex;
	flex-direction: column;
	align-items: normal;
	margin-bottom: 20px;
}

.messageDetailCircular {
	position: fixed;
	left: 50%;
	top: 50%;
}
</style>