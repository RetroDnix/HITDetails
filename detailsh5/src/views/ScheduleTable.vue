<script setup lang = "ts">
import { ref, onUpdated } from 'vue';
import tlStore from '@/store/modules/TimelineScheduleStore'
import Timeline from '@/components/TimeLine.vue'

const tab = ref<string | null>(null)
const timelineStore = tlStore()

const timelineScrollHandler = (e: Event) => {
	timelineStore.windowscroll = (e.target as Element).scrollTop
	//if ((e.target as Element).scrollTop + (e.target as Element).clientHeight >= (e.target as Element).scrollHeight - 20) {
	// 	console.log('到底了');
	// 	if(!ScheduleStore.noMore)
	// 		ScheduleStore.setUpdate();
	// 		ScheduleStore.applyUpdate();
}

onUpdated(() => {
	document.getElementById('TLwindow')?.scrollTo(0, timelineStore.windowscroll)
})

</script>

<template>
	<div>
		<!-- <v-tabs class="ScheduleTabs" v-model="tab" color='light-blue-lighten-3' bg-color="white" align-tabs="center" grow>
			<v-tab value="TimeLine">日程总览</v-tab>
			<v-tab value="WeekView">周视图</v-tab>
		</v-tabs> -->
		<v-window class="ScheduleWindow" v-model="tab">
			<v-window-item value="TimeLine">
				<v-container class="TimeLineContainer" @scroll="timelineScrollHandler" id="TLwindow" fluid>
					<timeline />
				</v-container>
			</v-window-item>
			<!-- <v-window-item value="WeekView">
				<v-container class="WeekViewContainer">
					<weekview />
				</v-container>
			</v-window-item>
			<v-window-item value="Summary">
				Summary
			</v-window-item> -->
		</v-window>
	</div>
</template>

<style>
.ScheduleWindow {
	position: fixed;
	overflow-y: hidden;
}

.TimeLineContainer {
	position: fixed;
	top: 20px;
	bottom: 40px;
	overflow-y: scroll;
	overflow-x: hidden;
}

.WeekViewContainer {
	position: static;
	margin-top: 30px;
	width: 100%;
	overflow-y: hidden;
}
</style>