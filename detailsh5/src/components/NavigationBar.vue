<script lang="ts" setup>
import { watch } from 'vue';
import { useRouter, useRoute } from 'vue-router'; // 导入Vue Router相关功能
const router = useRouter(); // 获取路由实例
const route = useRoute()
const navigateToPage = (routeName: any) => {
	// if (router.currentRoute.value.name != routeName)
	// 	console.log(router.currentRoute.value.name);
	router.push({ name: routeName }); // 利用路由名称进行页面切换
};
import { ref, computed } from 'vue';
const btNav = ref(0);
watch(() => route.name, () => {
	switch (route.name) {
		case "Schedule":
			btNav.value = 0;
			break;
		case "Notification":
			btNav.value = 1;
			break;
		case "Group":
			btNav.value = 2;
			break;
		default:
			btNav.value = 0;
			break;
	}
});
const color: any = computed(() => {
	switch (route.name) {
		case "Schedule":
			return 'light-blue-lighten-3';
		case "Notification":
			return 'cyan-lighten-3';
		case "Group":
			return 'teal-lighten-3';
		default:
			return color.value;
	}
});

import mesStore from '@/store/modules/MessageStore'
const messageStore = mesStore()
import tlStore from '@/store/modules/TimelineScheduleStore'
const timelineStore = tlStore()
import grStore from '@/store/modules/GroupStore'
const groupStore = grStore()
import uStore from '@/store/modules/UserStore'
const userStore = uStore()

if (localStorage.getItem('Authorization') != null)
{
	if (route.name != "Notification" && !messageStore.upToDate) messageStore.reloadAll()
	if (route.name != "Schedule" && !timelineStore.upToDate) timelineStore.reloadAll()
	if (route.name != "Group" && !groupStore.upToDate) groupStore.reloadAll()
	userStore.reloadAll()
}
const UnReadNum = computed(() => {
	let num = 0
	for (let i = 0; i < messageStore.messageList.length; i++) {
		if (!messageStore.messageList[i].HaveRead) num++
	}
	return num
})
</script>

<template>

	<v-bottom-navigation v-model="btNav" :bg-color="color" mode="shift" style="position: fixed;" mandatory="force"
		v-if="route.name == 'Schedule' || route.name == 'Group' || route.name == 'Notification'">
		<v-btn @click="navigateToPage('Schedule')">
			<v-icon>mdi-clock</v-icon>
			<span>日程表</span>
		</v-btn>
		<v-btn @click="navigateToPage('Notification')">
			<v-badge v-if="UnReadNum != 0" :content="UnReadNum" color="red-darken-4" offset-x="-10">
				<v-icon>mdi-message-alert</v-icon>
			</v-badge>
			<v-icon v-else>mdi-message-alert</v-icon>
			<span>通知</span>
		</v-btn>
		<v-btn @click="navigateToPage('Group')">
			<v-icon>mdi-account-group</v-icon>
			<span>组织</span>
		</v-btn>
	</v-bottom-navigation>
</template>