<script setup lang ="ts">

import { useRouter } from 'vue-router';
const router = useRouter(); // 获取路由实例

import uStore from '@/store/modules/UserStore'
const userStore = uStore()
userStore.reloadAll()
const LogOut = () => {
    localStorage.removeItem('Authorization')
    router.push('/')
}
</script>
<template>
    <v-app-bar color="teal-lighten-3" density="compact" style="position: fixed;">
        <v-btn icon="mdi-chevron-left" @click="router.back()"></v-btn>
        <v-app-bar-title>用户页</v-app-bar-title>
        <v-spacer></v-spacer>
    </v-app-bar>
    <v-col style="padding-left: 5%;padding-right: 5%;padding-top: 3%;" v-if="!userStore.isloading">
        <v-card style="margin-top: 10px;">
            <!-- 用户信息 -->
            <v-card-title>{{ '已登录用户： ' + userStore.userName }}</v-card-title>
            <v-card-text>UID: {{ userStore.UID }}</v-card-text>
            <v-btn prepend-icon="mdi-logout" color="red-lighten-3" class="logoutBtn" @click="LogOut()">注销</v-btn>
        </v-card>
    </v-col>
    <v-progress-circular v-if="userStore.isloading" indeterminate class="userCircular"></v-progress-circular>
</template>
<style>
.logoutBtn {
    position: absolute;
    right: 5%;
    top: 25%;
}

.userCircular {
    position: fixed;
    left: 50%;
    top: 50%;
}
</style>