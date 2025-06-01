<script setup lang ="ts">

import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { bindToken } from '@/utils/Updater'

const router = useRouter(); // 获取路由实例
const UserName = ref('')
const PassWord = ref('')
const Logging = ref(false)
const showLoginError = ref(false)
const LoginErrorText = ref("")
const bind = () => {
    Logging.value = true
    const welinkuid = sessionStorage.getItem("WeLinkUID")?.toString()
    if(welinkuid == undefined)
    {
        LoginErrorText.value = "请先登录后再绑定！"
        showLoginError.value = true
        router.push("Login")
        return
    }
    console.log(welinkuid)
    bindToken(welinkuid, UserName.value, PassWord.value).then((res) => {
        if (res == "failed") {
            Logging.value = false
            LoginErrorText.value = "绑定失败，请检查用户名密码是否正确！"
            showLoginError.value = true
        } 
        else if(res == "bindtwice"){
            Logging.value = false
            LoginErrorText.value = "单个WelinkID不能绑定多个账户!"
            showLoginError.value = true
        } 
        else {
            localStorage.setItem('Authorization', res)
            router.push('Schedule')
        }
        Logging.value = false
    })
}
const welinkuid = sessionStorage.getItem("WeLinkUID")?.toString()
if(welinkuid == undefined)
{
    LoginErrorText.value = "请先登录后再绑定！"
    showLoginError.value = true
    router.push("Login")
}
</script>
<template>
    <div class="bgColor"></div>
    <v-container class="imgContainer">
        <v-img src="../assets/logo.png" alt="logo" width="100px" style="margin-left: -20px;"></v-img>
        <p class="text-h5 mb-2" style="color: #ffffff;">账号绑定</p>
        <p class="hint mt-3" style="color: #ffffff;">首次使用请将Welink账户与本系统账户绑定!</p>
        <v-form fast-fail @submit.prevent="bind()" class="ValidateForm">
            <v-text-field type="text" label="用户名" v-model="UserName" variant="solo-filled" density="compact" class="mt-3"
                style="width: 300px;" required
                :rules="[(value: string | any[]) => { if (value?.length > 4) return true; else return '用户名太短!' },]"></v-text-field>
            <v-text-field type="password" label="密码" v-model="PassWord" variant="solo-filled" density="compact" class="mt-3"
                style="width: 300px;" required
                :rules="[(value: string | any[]) => { if (value?.length > 8) return true; else return '密码太短!' },]"></v-text-field>
            <v-btn type="submit" width="250px" elevation="1" color="light-blue-darken-3" @click="bind()" class="mt-3"
                :loading="Logging">绑定</v-btn>
        </v-form>
    </v-container>
    <v-container class="BottomPanel">
        <v-container class="HintPanel">
            <v-icon color="#212121" size="x-large">mdi-pan-right</v-icon>
            <div class="hint">在您完成绑定之后，可以直接通过welink完成免登录。</div>
        </v-container>
        <v-container class="HintPanel">
            <v-icon color="#212121" size="x-large">mdi-pan-right</v-icon>
            <div class="hint">测试用账号：eQANX <br>密码：G46oJkEs8h9U</div>
        </v-container>
    </v-container>
    <v-snackbar v-model="showLoginError" timeout="1000">
        {{ LoginErrorText }}
        <template v-slot:actions>
            <v-btn color="blue" variant="text" @click="showLoginError = false">关闭</v-btn>
        </template>
    </v-snackbar>
</template>
<style>
.ValidateForm {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.imgContainer {
    z-index: 2;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    transform: translate(-50%, -50%);
    position: fixed;
    left: 50%;
    top: 42%;
}

.bgColor {
    position: fixed;
    background-color: #00bff4fc;
    height: 100%;
    width: 100%;
}

.hint {
    width: 300px;
    font-size: 15px;
    color: #363636;
}

.HintPanel {
    z-index: 1;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 10px;
}

.BottomPanel {
    transform: translate(-50%, 0);
    position: fixed;
    bottom: 0%;
    margin-left: -10px;
    left: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>