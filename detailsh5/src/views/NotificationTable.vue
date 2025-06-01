<!-- 这个文件使得Notification页面能够记住滚动位置 -->
<script setup lang = "ts">
import { ref, onUpdated } from 'vue';
import mesStore from '@/store/modules/MessageStore'
import Notification from '@/components/Notification.vue'

const tab = ref<string | null>(null);
const messageStore = mesStore()

const timelineScrollHandler = (e: Event) => {
	messageStore.windowscroll = (e.target as Element).scrollTop
}

onUpdated(() => {
	document.getElementById('MesWindow')?.scrollTo(0, messageStore.windowscroll)
})
</script>

<template>
	<v-window class="ScheduleWindow" v-model="tab">
		<v-window-item>
			<v-container class="TimeLineContainer" @scroll="timelineScrollHandler" id="MesWindow" fluid>
				<Notification />
			</v-container>
		</v-window-item>
	</v-window>
</template>

<style>
.ScheduleWindow {
	position: fixed;
	width: 100%;
	overflow-y: hidden;
}

.TimeLineContainer {
	position: fixed;
	width: 100%;
	top: 20px;
	bottom: 40px;
	overflow-y: scroll;
}
</style>