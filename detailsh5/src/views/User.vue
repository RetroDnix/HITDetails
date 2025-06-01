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
        <v-card style="margin-top: 20px;">
            <!-- 关于我们 -->
            <v-card-title>关于</v-card-title>
            <v-card-text>
                <v-divider></v-divider>
                <div style="margin-top: 15px;">
                    <v-row>
                        <v-container style="height: 125px;width: 125px;">
                            <v-img src="../assets/logo.png" alt="logo"  height="125" aspect-ratio="1/1" cover></v-img>
                        </v-container>
                        <v-col style="text-align: start;">
                            <v-card-title class="text-h5">HITDetails</v-card-title>
                            <v-card-text style="font-size: 16px;">妥善管理你的通知与日程</v-card-text>
                        </v-col>
                    </v-row>
                </div>
                <v-container style="text-indent: 1.5em;font-size: 15px;line-height: 1.7em;">
                    <p>HITDetails是一款在线通知与日程管理软件。其初衷是改变通知集中在微信、QQ群中的现状，帮助大学生们高效管理收到的通知以及自身的日程。</p>
                    <p>软件后端使用Flask框架开发，前端使用Vue框架与Vuetify组件库构建。</p>
                    <p>开发组成员：郑欢洋、王绎普、刘嘉琪。</p>
                </v-container>
            </v-card-text>
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