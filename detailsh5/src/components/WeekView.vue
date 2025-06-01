<script setup lang="ts">
import ScheduleItem from '@/type/ScheduleItem';
import upperBound, { getItemTime } from '@/utils/UpperBound';
import { ref, computed, watch } from 'vue';

import tlStore from '@/store/modules/TimelineScheduleStore'
const timelineStore = tlStore()
timelineStore.reloadAll()

const curDate = ref<number>(new Date().getTime());
const curWeekOffset = new Date().getDay();
const modifyDay = (offset: number) => {
	const realDate = new Date(curDate.value);
	realDate.setDate(realDate.getDate() + offset);
	curDate.value = realDate.getTime();
	//console.log(realDate.toDateString());
}

const curWeekString = computed(() => {
	const realDate = new Date(curDate.value);
	const StartDate = new Date(curDate.value);
	StartDate.setDate(realDate.getDate() - curWeekOffset + 1)
	const EndDate = new Date(curDate.value)
	EndDate.setDate(realDate.getDate() - curWeekOffset + 7)
	//console.log(realDate.getDate());
	return StartDate.toDateString().slice(4, 10) + ' - ' + EndDate.toDateString().slice(4, 10);
})

const weekDayList = ['日', '一', '二', '三', '四', '五', '六']
const curWeekList = computed(() => {
	const realDate = new Date(curDate.value);
	const StartDate = new Date(curDate.value);
	StartDate.setDate(realDate.getDate() - curWeekOffset + 1)
	let i = 0
	let res = new Array<String>()
	while (i < 7) {
		const curDate = new Date(StartDate.getTime());
		curDate.setDate(curDate.getDate() + i);
		if (curDate.toDateString() == (new Date().toDateString())) res.push("today", weekDayList[curDate.getDay()])
		else res.push(curDate.getDate().toString(), weekDayList[curDate.getDay()])
		i++;
	}
	//console.log(res);
	return res;
})

const curScheduleList = computed(() => {
	const realDate = new Date(curDate.value);
	const StartDate = new Date(curDate.value);
	StartDate.setDate(realDate.getDate() - curWeekOffset + 1)
	StartDate.setHours(0, 0, 0, 0);
	let res = new Array<ScheduleItem[]>();
	let pos = upperBound(timelineStore.scheduleList, StartDate.getTime());
	let i = 0;
	while (i < 7) {
		res.push(new Array<ScheduleItem>());
		StartDate.setDate(StartDate.getDate() + 1)
		while (pos < timelineStore.scheduleList.length && getItemTime(timelineStore.scheduleList[pos]) < StartDate.getTime()) {
			res[i].push(timelineStore.scheduleList[pos]);
			pos++;
		}
		i++;
	}
	//console.log(res);
	return res;
})

</script>
<template>
	<v-container>
		<v-row class="WeekDay-container" justify="center" dense>
			<v-col cols="auto" align-items="center">
				<v-btn @click="modifyDay(-7)" density="compact" icon="mdi-chevron-double-left"></v-btn>
			</v-col>
			<v-col cols="auto" align-items="center">
				<v-btn @click="modifyDay(-1)" density="compact" icon="mdi-menu-left"></v-btn>
			</v-col>
			<v-col cols="auto" align-items="center">
				<v-btn variant="tonal" density="compact">
					{{ curWeekString }}
				</v-btn>
			</v-col>
			<v-col cols="auto" align-items="center">
				<v-btn @click="modifyDay(1)" density="compact" icon="mdi-menu-right"></v-btn>
			</v-col>
			<v-col cols="auto" align-items="center">
				<v-btn @click="modifyDay(7)" density="compact" icon="mdi-chevron-double-right"></v-btn>
			</v-col>
		</v-row>
		<v-row class="WeekDay-container mt-4" justify="center" dense>
			<v-col v-for="i in 7" :key="i">
				<v-sheet class="ma-1 pa-1">
					<div class="text-caption WeekDay">{{ curWeekList[(i - 1) * 2 + 1] }}</div>
					<v-btn variant="text" size="small" v-if="curWeekList[(i - 1) * 2] != 'today'" class="text-subtitle-1 WeekDay mt-2">{{ curWeekList[(i - 1) * 2]
					}}</v-btn>
					<v-btn variant="text" size="small" v-else class="text-subtitle-1 WeekDay mt-2 font-weight-black">{{ new Date().getDate() }}</v-btn>
				</v-sheet>
			</v-col>
		</v-row>
	</v-container>
	<!-- <v-container class="weekViewScheduleContainer" v-if="!timelineStore.isloading">
		<v-expansion-panels multiple>
			<v-expansion-panel v-for="i in 7" :key="i">
				<v-expansion-panel-title>
					<v-row no-gutters>
						<v-col cols="4" class="d-flex justify-start">
							Trip name
						</v-col>
						<v-col cols="8" class="text-grey">
							Enter a name for the trip
						</v-col>
					</v-row>
				</v-expansion-panel-title>
			</v-expansion-panel>
		</v-expansion-panels>
	</v-container> -->

	<v-container v-if="!timelineStore.isloading">
		<v-row class="Wv-sche-container" justify="center" dense>
			<v-col v-for="i in 7" :key="i" cols="auto">
				<v-container class="Sche-item-container">
					<div style="width:50px;border: 1px solid red;">Col</div>
					<!-- <div v-for="j in curScheduleList[i-1].length" :key="j" class="Sche-item">
						{{ curScheduleList[i-1][j-1].Title }}
					</div> -->
				</v-container>
			</v-col>
		</v-row>

	</v-container>
	<v-progress-circular v-if="timelineStore.isloading" indeterminate class="scheduleCircular"></v-progress-circular>
</template>
<style>
.WeekDay-container {
	position: static;
	display: flex;
	flex-wrap: nowrap;
	overflow-x: visible;
	outline: 1px solid red;
}

.Wv-sche-container {
	position: static;
	flex-wrap: nowrap;
	margin-top: -10px;
	overflow-x: hidden;
	overflow-y: scroll;
	outline: 1px solid red;
	align-self: center;
}

.Sche-item-container {
	display: flex;
	flex-direction: column;
	flex-wrap: nowrap;
	justify-content: space-evenly;
}

.WeekDay {
	height: 24px;
	text-align: center;
}

.Sche-item {
	width: 40px;
	height: 128px;
	text-align: center;
	font-size: xx-small;
	border: 1px solid blue;
}

.scheduleCircular {
	position: fixed;
	left: 50%;
	top: 50%;
}

.weekViewScheduleContainer {
	overflow-y: scroll;
	position: fixed;
	top: 250px;
	bottom: 50px;
	left: 10px;
	width: 95%;
}
</style>
