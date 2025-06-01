<script setup lang = "ts">
import { onUpdated, onMounted, onBeforeUnmount, watch, ref } from 'vue';
import { useRouter } from 'vue-router';
import { hintDateChinese, toDateChinese, toDateChineseSlim } from '@/utils/DataTimeFomatter'
import { deleteTag } from '@/utils/Updater'

const router = useRouter(); // 获取路由实例

import tlStore from '@/store/modules/TimelineScheduleStore'
import ScheduleItem from "@/type/ScheduleItem";
import { computed } from 'vue';
const timelineStore = tlStore()


const DeleteTagDialog = ref(false)
const DtName = ref("")
const DtValue = ref(0)

const DtLoading = ref(false)


const showFliter = ref(false)
const fliterStartTime = ref("")
const StartTimeStamp = ref(0)
const fliterFinishTime = ref("")
const FinishTimeStamp = ref(0)
const fliterStars = ref("全部")
const fliterType = ref("全部")
const FliterSelectedTag = ref(Array())

const DeleteTag = () => {
	DtLoading.value = true
	deleteTag(DtValue.value).then((result) => {
		if (result) {
			timelineStore.tagList = timelineStore.tagList.filter((item) => item.value != DtValue.value)
			timelineStore.upToDate = false
			FliterSelectedTag.value = FliterSelectedTag.value.filter((item) => item != DtValue.value)
		}
		DtLoading.value = false
		DeleteTagDialog.value = false
	})
}

if (!timelineStore.upToDate) timelineStore.reloadAll()

watch(() => timelineStore.upToDate, (newValue) => {
	if (newValue == false) {
		timelineStore.reloadAll()
	}
});

watch(() => fliterStartTime.value, (newValue) => {
	if (newValue != "") {
		const date = new Date();
		date.setHours(0, 0, 0, 0)
		newValue.split('/').forEach((element, index) => {
			const num = parseInt(element)
			if (!isNaN(num)) {
				if (index == 2) date.setDate(num)
				else if (index == 1) date.setMonth(num - 1)
				else if (index == 0) {
					if (num < 100) date.setFullYear(2000 + num)
					else date.setFullYear(num)
				}
			}
		});
		StartTimeStamp.value = date.getTime()
	}
	else StartTimeStamp.value = 0
});

watch(() => fliterFinishTime.value, (newValue) => {
	if (newValue != "") {
		const date = new Date();
		date.setHours(0, 0, 0, 0)
		newValue.split('/').forEach((element, index) => {
			const num = parseInt(element)
			if (!isNaN(num)) {
				if (index == 2) date.setDate(num)
				else if (index == 1) date.setMonth(num - 1)
				else if (index == 0) {
					if (num < 100) date.setFullYear(2000 + num)
					else date.setFullYear(num)
				}
			}
		});
		FinishTimeStamp.value = date.getTime()
	}
	else FinishTimeStamp.value = 0
});

const dateDiff = (date1: Date, date2: Date) => {
	const d1 = new Date(date1.getTime())
	const d2 = new Date(date2.getTime())
	d1.setHours(0, 0, 0, 0)
	d2.setHours(0, 0, 0, 0)
	return Math.floor((d2.getTime() - d1.getTime()) / (1000 * 60 * 60 * 24))
}

const scheduleBeginTime = (Sche: ScheduleItem) => {
	if (Sche.Type == 3) {
		if (Sche.StartTime.toDateString() == Sche.FinishTime.toDateString())
			return [toDateChinese(Sche.StartTime), Sche.StartTime.toTimeString().slice(0, 5), '~' + Sche.FinishTime.toTimeString().slice(0, 5)]
		else
			return [toDateChinese(Sche.StartTime), Sche.StartTime.toTimeString().slice(0, 5), '~(+' + dateDiff(Sche.StartTime, Sche.FinishTime) + ')' + Sche.FinishTime.toTimeString().slice(0, 5)]
	}
	else return [toDateChinese(Sche.StartTime), Sche.StartTime.toTimeString().slice(0, 5), '']
}

const calcIcon = (type: number, key: number) => {
	if (timelineStore.curPos >= key) return ['grey-lighten-1', type == 3 ? 'mdi-clock-time-eight' : 'mdi-text-box']
	else return type == 3 ? ['blue-lighten-2', 'mdi-clock-time-eight'] : ['green-lighten-2', 'mdi-text-box']
}

const isSameDay = (key: number, list: ScheduleItem[]) => {
	if (key == 0) return false
	else return list[key].StartTime.toDateString() == list[key - 1].StartTime.toDateString()
}

const FliterButton = computed(() => {
	if (timelineStore.fliterStartTime == 0 && timelineStore.fliterFinishTime == 0 && timelineStore.fliterStars == 0 && timelineStore.fliterType == 0 && timelineStore.fliterTags.length == 0)
		return "筛选"
	else
		return "已筛选"
})
const initFliter = () => {
	const TypeName = ["全部", '', '', '普通日程(具有开始/结束时间)', '任务日程(仅有时间点)']
	fliterStartTime.value = timelineStore.fliterStartTime == 0 ? '' : toDateChineseSlim(new Date(timelineStore.fliterStartTime))
	fliterFinishTime.value = timelineStore.fliterFinishTime == 0 ? '' : toDateChineseSlim(new Date(timelineStore.fliterFinishTime))
	fliterStars.value = (timelineStore.fliterStars == 0 ? '全部' : timelineStore.fliterStars.toString())
	fliterType.value = TypeName[timelineStore.fliterType]
	FliterSelectedTag.value = timelineStore.fliterTags
	showFliter.value = true
}
const confirmFliter = () => {
	timelineStore.fliterStartTime = StartTimeStamp.value
	timelineStore.fliterFinishTime = FinishTimeStamp.value
	timelineStore.fliterStars = (fliterStars.value == '全部' ? 0 : parseInt(fliterStars.value))
	timelineStore.fliterType = (fliterType.value == '全部' ? 0 : (fliterType.value == '普通日程(具有开始/结束时间)' ? 3 : 4))
	timelineStore.fliterTags = FliterSelectedTag.value
	timelineStore.upToDate = false
}

const size = ref(window.innerWidth);
function onResize() {
	size.value = window.innerWidth;
}

onUpdated(() => {
	document.getElementById('targetDivider')?.scrollIntoView({ behavior: 'smooth', block: 'start' })
})

onMounted(() => {
	window.addEventListener("resize", onResize);
});

onBeforeUnmount(() => {
	window.removeEventListener("resize", onResize);
});

</script>
<template>
	<!-- 顶部导航栏 -->
	<v-app-bar color="light-blue-lighten-3" density="compact" style="position: fixed;">
		<v-app-bar-title>日程</v-app-bar-title>

		<v-spacer></v-spacer>

		<v-btn prepend-icon="mdi-menu-open" style="margin-left: 5px;" variant="tonal" size="small"
			:disabled="timelineStore.isloading" @click="initFliter()">{{ FliterButton }}</v-btn>

		<v-btn prepend-icon="mdi-plus" style="margin-left: 5px;" variant="tonal" size="small"
			:disabled="timelineStore.isloading" @click="router.push({ name: 'createNewSchedule' })">新日程</v-btn>

		<v-btn prepend-icon="mdi-refresh" style="margin-left: 5px;" variant="tonal" size="small"
			:disabled="timelineStore.isloading" @click="timelineStore.setUpdate()">刷新</v-btn>

		<!-- <v-btn icon="mdi-account" @click="router.push({ name: 'user' })"></v-btn> -->

	</v-app-bar>
	<!-- 时间线主体 -->
	<v-container style="padding-left: 5px;padding-right: 10px;" fluid>
		<v-timeline side="end" v-if="!timelineStore.isloading">
			<v-timeline-item v-for="(item, i) in timelineStore.scheduleList" :key="i"
				:dot-color="calcIcon(item.Type, i)[0]" :icon="calcIcon(item.Type, i)[1]" fill-dot
				style="border: 1px solid;">
				<template v-slot:opposite>
					<v-container class="datePanel">
						<div class="pt-1 headline text-subtitle-2" v-text="scheduleBeginTime(item)[0]"
							v-if="!isSameDay(i, timelineStore.scheduleList)"></div>
						<div class="pt-1 headline text-caption" v-text="scheduleBeginTime(item)[1]"></div>
						<div class="pt-1 headline text-caption" v-text="scheduleBeginTime(item)[2]"></div>
					</v-container>
				</template>
				<v-hover>
					<template v-slot:default="{ isHovering, props }">
						<v-card class="timelineCard" v-bind="props" :elevation="isHovering ? 12 : 2"
							@click="router.push('/ScheduleDetail/' + item.ScheduleID)" fluid style="border: 1px solid;">
							<v-card-title :class="['text-subtitle-1', `bg-${calcIcon(item.Type, i)[0]}`]">
								{{ item.Title }}
								<!-- {{ item.Title.substring(0, 9) + (item.Title.length > 9 ? '...' : '') }} -->
							</v-card-title>
							<v-card-subtitle v-if="item.Stars > 0" class="mt-2 text-subtitle-2 textSubtitle">
								{{ item.Location }}
								<!-- <span v-if="item.Location != ''"> | </span> -->
							</v-card-subtitle>
							<v-card-subtitle v-if="item.Stars > 0" class="mt-2 text-subtitle-2 textSubtitle">
								<span v-if="item.Stars == 3" style="color: #cd2c2c;">重要性：{{ item.Stars }}</span>
								<span v-else>重要性：{{ item.Stars }}</span>
							</v-card-subtitle>
							<v-card-subtitle v-if="item.Stars == 0" class="mt-2  text-subtitle-2 textSubtitle">
								{{ item.Location }}
							</v-card-subtitle>
							<v-card-item class="mb-2 text-body-2 textSubtitle">
								{{ item.Body.substring(0, 50) + (item.Body.length > 50 ? '...' : '') }}
							</v-card-item>
							<v-chip-group class="scheduleTag">
								<v-chip style="color: gray;" size="x-small" v-for="(tag, i) in item.Tags" :key="i">{{
									tag.title }}</v-chip>
							</v-chip-group>
						</v-card>
					</template>
				</v-hover>
				<v-divider :thickness="4" class="mt-6" color="info" id="targetDivider"
					v-if="timelineStore.curPos == i"></v-divider>
			</v-timeline-item>
		</v-timeline>
		<!-- 筛选框 -->
		<v-bottom-sheet v-model="showFliter">
			<v-card class="fliter">
				<v-card-title class="fliteritem mt-2" style="text-align: center;">筛选日程</v-card-title>
				<v-select class="fliteritem mt-1" v-model="fliterStars" label=" 重要性" :items="['全部', '1', '2', '3']"
					prepend-icon="mdi-information-outline" density="compact"></v-select>
				<v-select class="fliteritem mt-1" v-model="fliterType" label="日程类型"
					:items="['全部', '普通日程(具有开始/结束时间)', '任务日程(仅有时间点)']" prepend-icon="mdi-file-document"
					density="compact"></v-select>
				<v-select class="fliteritem mt-1" v-model="FliterSelectedTag" label="日程标签" :items="timelineStore.tagList"
					prepend-icon="mdi-tag-outline" density="compact" multiple chips>
					<template v-slot:item="{ item, props }">
						<v-list-item v-bind="props">
							<template v-slot:append="{ }">
								<v-btn icon="mdi-close-circle-outline" size="small" variant="plain"
									@click.stop="DtName = item.title; DtValue = item.value; DeleteTagDialog = true"></v-btn>
							</template>
							<template v-slot:prepend="{ isActive }">
								<v-list-item-action start>
									<v-checkbox-btn :model-value="isActive"></v-checkbox-btn>
								</v-list-item-action>
							</template>
						</v-list-item>
					</template>
				</v-select>
				<v-text-field class="fliteritem mt-1" v-model="fliterStartTime" label="起始时间"
					prepend-icon="mdi-clock-time-nine-outline" placeholder="yy/mm/dd" variant="underlined"
					:hint="hintDateChinese(StartTimeStamp)" persistent-hint></v-text-field>
				<v-text-field class="fliteritem mt-1" v-model="fliterFinishTime" label="截止时间" prepend-icon="mdi"
					placeholder="yy/mm/dd" variant="underlined" :hint="hintDateChinese(FinishTimeStamp)"
					persistent-hint></v-text-field>
				<v-card-actions class="fliterButtonGroup mt-1">
					<v-btn variant="tonal" @click="showFliter = !showFliter">取消</v-btn>
					<v-card elevation="0"><v-card-title class="text-h6"></v-card-title></v-card>
					<v-btn variant="tonal" @click="confirmFliter(); showFliter = !showFliter">确定</v-btn>
				</v-card-actions>
			</v-card>
		</v-bottom-sheet>
		<v-dialog v-model="DeleteTagDialog" width="80%">
			<v-card>
				<v-card-title>删除标签</v-card-title>
				<v-card-text style="color: grey;">确定要从所有日程中删除标签“{{ DtName }}”吗?</v-card-text>
				<v-card-actions>
					<v-spacer />
					<v-btn @click="DeleteTag()" :loading="DtLoading">删除</v-btn>
					<v-btn @click="DeleteTagDialog = !DeleteTagDialog">取消</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
		<!-- 加载进度条 -->
		<v-progress-circular v-if="timelineStore.isloading" indeterminate class="scheduleCircular"></v-progress-circular>
		<div v-if="!timelineStore.isloading && timelineStore.scheduleList.length == 0" class="emptyNotice text-h6">暂无日程
		</div>
	</v-container>
</template>
<style>
.timelineCard {
	width: min(100%, v-bind((size - 175) + 'px'));
}

.textSubtitle {
	font-size: small;
	color: #303030;
}

.scheduleCircular {
	position: fixed;
	left: 50%;
	top: 50%;
}

.scheduleTimeline {
	left: 2.5%;
	width: 95%;
}

.datePanel {
	display: flex;
	flex-direction: column;
	align-items: end;
	margin-left: -30px;
	margin-right: -20px;
	min-width: 100px;
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

.emptyNotice {
	position: fixed;
	left: 50%;
	top: 50%;
	transform: translate(-50%, -50%);
}

.scheduleTag {
	margin-left: 20px;
	margin-top: -15px;
	max-width: 100%;
}
</style>