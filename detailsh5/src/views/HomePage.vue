<script setup lang ="ts">
declare const HWH5: any;
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { getToken, getSysToken } from '@/utils/Getter'
import { ProxyLogin } from '@/utils/WeLinkLogin';
import { onMounted } from 'vue';
const router = useRouter(); // 获取路由实例
const UserName = ref('')
const PassWord = ref('')
const Logging = ref(false)
const showLoginError = ref(false)
const LoginErrorText = ref("")
const login = () => {
    // if (welink == true) WelinkLogin()
    // else {
    Logging.value = true
    getToken(UserName.value, PassWord.value).then((res) => {
        if (res == 'failed') {
            LoginErrorText.value = "登录失败，请检查用户名和密码是否正确"
            showLoginError.value = true
        } else {
            localStorage.setItem('Authorization', res)
            router.push('Schedule')
        }
        Logging.value = false
    })

}
const authCode = ref('')
const WelinkUID = ref('')
const getAuthCode = () => {
    HWH5.getAuthCode().then((data: any) => {
        console.log(data);
        if (data.code == undefined) return
        else authCode.value = data.code;
        ProxyLogin(authCode.value).then((uid) => {
            if (uid == "err") return
            else WelinkUID.value = uid
            //alert(WelinkUID.value)
        })
        // getAccessToken().then((access_token) => {
        //     if (access_token == undefined) return
        //     alert(access_token)
        //     getUserID(access_token, authCode.value).then((uid) => {
        //         if (uid == undefined) return
        //         else WelinkUID.value = uid
        //         alert(WelinkUID.value)
        //     });
        // })
    }).catch((error: any) => {
        console.log('免登录异常', error);
    });
}
const WelinkLogin = async () => {
    //alert("Start Login")
    try {
        let uid = undefined
        if (authCode.value == '') {
            LoginErrorText.value = "获取authCode失败，请检查Welink环境与网络连接是否正常。"
            showLoginError.value = true
            return
        }
        if (WelinkUID.value == '') {
            ProxyLogin(authCode.value).then((res) => {
                if (res == "err") {
                    LoginErrorText.value = "Welink免登录失败，请检查Welink环境与网络连接是否正常。"
                    showLoginError.value = true
                    return
                }
                else WelinkUID.value = res
                uid = res
            })
        }
        else uid = WelinkUID.value
        //alert(uid)
        if (uid == "err" || uid == undefined) {
            LoginErrorText.value = "获取uid失败，请检查Welink环境与网络连接是否正常。"
            showLoginError.value = true
            return
        }
        const token = await getSysToken(uid);
        if (token == 'null') {
            sessionStorage.setItem("WeLinkUID", uid)
            router.push("Bind")
        }
        else if(token == 'failed')
        {
            LoginErrorText.value = "登录失败，请检查网络连接"
            showLoginError.value = true
        }
        else {
            //alert(token)
            localStorage.setItem('Authorization', token)
            router.push('Schedule')
            Logging.value = false
        }
    }
    catch (error: any) {
        console.log(error.toString())
        return
    }
}
onMounted(() => {
    const script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://open-doc.welink.huaweicloud.com/docs/jsapi/2.0.10/hwh5-cloudonline.js';
    script.onload = getAuthCode;
    document.body.appendChild(script);
})
//WelinkLogin(false)
</script>
<template>
    <div class="bgColor"></div>
    <v-container class="imgContainer">
        <v-img src="../assets/logo.png" alt="logo" width="100px" style="margin-left: -20px;"></v-img>
        <div class="text-h4 mt-4" style="color: #ffffff;">HITDetails</div>
        <div class="text-h6 mt-4 mb-3" style="color: #ffffff;">妥善管理你的通知与日程</div>
        <v-form fast-fail @submit.prevent="login()" class="ValidateForm">
            <v-text-field type="text" label="用户名" v-model="UserName" variant="solo-filled" density="compact" class="mt-3"
                style="width: 300px;" required
                :rules="[(value: string | any[]) => { if (value?.length > 4) return true; else return '用户名太短!' },]"></v-text-field>
            <v-text-field type="password" label="密码" v-model="PassWord" variant="solo-filled" density="compact" class="mt-3"
                style="width: 300px;" required
                :rules="[(value: string | any[]) => { if (value?.length > 8) return true; else return '密码太短!' },]"></v-text-field>
            <v-btn type="submit" width="250px" elevation="1" color="light-blue-darken-3" @click="login()" class="mt-3"
                :loading="Logging">登录</v-btn>
        </v-form>
        <v-btn width="250px" elevation="1" color="light-blue-darken-3" class="mt-3"
            @click="WelinkLogin()">微信登录</v-btn>
        <v-btn width="250px" elevation="1" color="green" @click="router.push('Help')" class="mt-3">使用教程</v-btn>
    </v-container>
    <v-container class="BottomPanel">
        <v-container class="HintPanel mt-4">
            <v-icon color="#212121" size="x-large">mdi-pan-right</v-icon>
            <div class="hint">测试用账号：eQANX <br>测试用密码：G46oJkEs8h9U</div>
        </v-container>
        <v-container class="HintPanel">
            <v-icon color="#212121" size="x-large">mdi-pan-right</v-icon>
            <div class="hint">请在手机上访问本页或将浏览器调整至竖屏比例以获得最佳体验</div>
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
    margin-top: -7px;
    margin-bottom: -15px;
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