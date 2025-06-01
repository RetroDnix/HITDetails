<!-- 这个文件使得Notification页面能够记住滚动位置 -->
<script setup lang = "ts">
import { ref, onUpdated } from 'vue';
import grStore from '@/store/modules/GroupStore'
import GroupList from '@/components/GroupList.vue'

const tab = ref<string | null>(null);
const GroupStore = grStore()

const timelineScrollHandler = (e: Event) => {
	GroupStore.windowscroll = (e.target as Element).scrollTop
}

onUpdated(() => {
	document.getElementById('GrWindow')?.scrollTo(0, GroupStore.windowscroll)
})
</script>

<template>
	<v-window class="GroupWindow" v-model="tab">
		<v-window-item>
			<v-container class="GroupContainer" @scroll="timelineScrollHandler" id="GrWindow" fluid>
				<GroupList />
			</v-container>
		</v-window-item>
	</v-window>
</template>

<style>
.GroupWindow {
	position: fixed;
	width: 100%;
	overflow-y: hidden;
}

.GroupContainer {
	position: fixed;
	width: 100%;
	top: 20px;
	bottom: 40px;
	overflow-y: scroll;
}
</style>