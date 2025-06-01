<script setup lang = "ts">
import { watch, ref } from 'vue';


import grStore from '@/store/modules/GroupStore'
import { useRouter } from 'vue-router';
import { createGroup } from '@/utils/Updater'

const groupStore = grStore()
const router = useRouter(); // 获取路由实例

const Overlay = ref(false)
const OpTextFieldString = ref("")
const OpLoading = ref(false)
const showError = ref(false)
const ErrorText = ref("")
const CreateGroup = (groupName: string) => {
	OpLoading.value = true
	if (groupName == "") {
		ErrorText.value = "组织名称不能为空"
		showError.value = true
		OpLoading.value = false
		return
	}
	createGroup(groupName).then((result) => {
		OpLoading.value = false
		if (!result) {
			ErrorText.value = "创建组织失败!"
			showError.value = true
			OpLoading.value = false
		}
		else 
		{
			groupStore.upToDate = false
			Overlay.value = false
		}
	})
}

if (!groupStore.upToDate) groupStore.reloadAll()

watch(() => groupStore.upToDate, (newValue) => {
	if (newValue == false) {
		groupStore.reloadAll()
	}
});

const getAuthority = (admin: number, IsMember: boolean) => {
	let res = ''
	if (IsMember) res += '成员 '
	if (admin == 1) res += '通知发布者 '
	else if (admin == 2) res += '管理员 '
	else if (admin == 3) res += '超级管理员 '
	return res
}

const getType = (type: number) => {
	if (type == 0) return '行政班'
	else if (type == 1) return '教学班'
	else return '学生组织'
}
</script>
<template>
	<v-app-bar color="teal-lighten-3" density="compact" style="position: fixed;">
		<v-app-bar-title>组织</v-app-bar-title>

		<v-spacer></v-spacer>

		<v-btn prepend-icon="mdi-plus" variant="tonal" size="small" :disabled="groupStore.isloading"
			@click="Overlay = true">创建组</v-btn>

		<v-btn style="margin-left: 5px;" prepend-icon="mdi-refresh" variant="tonal" size="small"
			:disabled="groupStore.isloading" @click="groupStore.setUpdate()">刷新</v-btn>

		<v-btn size="small" icon="mdi-account" @click="router.push({ name: 'user' })"></v-btn>
		<v-btn size="small" icon="mdi-help-circle-outline" @click="router.push({ name: 'Help' })"></v-btn>
		
	</v-app-bar>
	<v-container v-if="!groupStore.isloading" class="groupContainer">
		<div v-for="(item, i) in groupStore.groupList" :key="i">
			<v-hover>
				<template v-slot:default="{ isHovering, props }">
					<v-card class="mt-2 mb-2 groupCard" v-bind="props" :elevation="isHovering ? 12 : 2"
						@click="router.push('/GroupDetail/' + item.GroupID)">
						<v-card-title>{{ item.GroupName }}</v-card-title>
						<v-card-text>
							<div>{{ "ID：" + item.GroupID + ' | ' + getType(item.Type) }}</div>
							<div class="mt-2">权限：{{ getAuthority(item.Admin, item.IsMember) }}</div>
						</v-card-text>
					</v-card>
				</template>
			</v-hover>
		</div>
	</v-container>
	<v-dialog v-model="Overlay" width="80%">
		<v-card>
			<v-card-title>
				创建组织
			</v-card-title>
			<v-card-text>
				<v-text-field label="请输入组织的名称" v-model="OpTextFieldString" :readonly="OpLoading"></v-text-field>
			</v-card-text>
			<v-card-actions>
				<v-spacer />
				<v-btn @click="CreateGroup(OpTextFieldString)" :loading="OpLoading">创建</v-btn>
				<v-btn @click="Overlay = !Overlay">取消</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
	<!-- 信息提示条 -->
	<v-snackbar v-model="showError" timeout="1000">
		{{ ErrorText }}
		<template v-slot:actions>
			<v-btn color="blue" variant="text" @click="showError = false">关闭</v-btn>
		</template>
	</v-snackbar>
	<v-progress-circular v-if="groupStore.isloading" indeterminate class="groupCircular"></v-progress-circular>
	<div v-if="!groupStore.isloading && groupStore.groupList.length == 0" class="emptyNotice text-h6">暂无加入的组织</div>
</template>

<style>
.CgCard {
	position: fixed;
	width: 400px;
}

.groupContainer {
	padding-left: 5px;
	padding-right: 5px;
	display: grid;
	grid-template-columns: 1fr 1fr;
	grid-column-gap: 10px;
	grid-row-gap: 10px;
	width: 100%;
}

.groupCircular {
	position: fixed;
	left: 50%;
	top: 50%;
}
</style>