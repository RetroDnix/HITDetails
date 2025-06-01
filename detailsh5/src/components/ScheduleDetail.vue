<script setup lang = "ts">
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { getScheduleByID } from '@/utils/Getter'
import { updateScheduleByID, postSchedule, deleteScheduleByID, addTag, updateTag } from '@/utils/Updater'
import { parseTime, toDateTimeChineseWeekDay, toDateTimeChineseSlim } from '@/utils/DataTimeFomatter'

import tlStore from '@/store/modules/TimelineScheduleStore'
import ScheduleItem, { TagItem } from "@/type/ScheduleItem";
const timelineStore = tlStore()
import mesStore from '@/store/modules/MessageStore'
import { computed } from 'vue';
const messageStore = mesStore()

const router = useRouter(); // 获取路由实例
const route = useRoute();
const isloading = ref(true)
const isupdating = ref(false)
const isdeleting = ref(false)
const showTimePickerError = ref(false)
const TimePickerErrorText = ref('')
const isDDL = ref(false)
const WindowTitle = ref('')

const OriginID = ref(0)
const Title = ref("null")
const Location = ref("null")
const StartTime = ref("null")
//const StartTimeStamp = ref(0)
const FinishTime = ref("null")
//const FinishTimeStamp = ref(0)
const Stars = ref(0)
const Body = ref("null")
const Tags = ref(Array<TagItem>())
const TagsOrigin = ref(Array<TagItem>())
const TagsSelected = ref(Array<TagItem>())

//const showTimePicker = ref(false)
//const currentPickerTime = ref(0)
//const PickerDate = ref(Array())
//const Hours = ref('')
//const Minutes = ref('')

const SaveButtonText = computed(() => {
    if (route.name == 'createNewSchedule') return '创建日程'
    else return '保存更改'
})

// const initTimePicker = () => {
//     PickerDate.value = Array()
//     Hours.value = ''
//     Minutes.value = ''
// }

// const confirmPickedTime = () => {
//     // 将字符串"Fri Aug 05 2016 00:00:00 GMT+0800"格式化为时间
//     const date = new Date(
//         PickerDate.value.toString().replace(/-/g, "/")
//     );
//     date.setHours(parseInt(Hours.value))
//     date.setMinutes(parseInt(Minutes.value))
//     if (isNaN(date.getTime())) {
//         TimePickerErrorText.value = '输入了无效的时间'
//         showTimePickerError.value = !showTimePickerError.value
//     }
//     else if (currentPickerTime.value == 0) {
//         StartTime.value = toDateTimeChinese(date)
//         StartTimeStamp.value = date.getTime()
//     }
//     else if (currentPickerTime.value == 1) {
//         FinishTime.value = toDateTimeChinese(date)
//         FinishTimeStamp.value = date.getTime()
//     }
// }

const dataCheck = () => {
    if (Title.value == '') {
        TimePickerErrorText.value = "标题不能为空"
        showTimePickerError.value = true
        return false
    }
    if (!Number.isInteger(Stars.value) || Stars.value < 0 || Stars.value > 3) {
        TimePickerErrorText.value = "重要程度必须是0~3的整数"
        showTimePickerError.value = true
        return false
    }
    const st = parseTime(StartTime.value).getTime()
    const ft = parseTime(FinishTime.value).getTime()
    if (isDDL.value && st == 0) {
        showTimePickerError.value = true
        TimePickerErrorText.value = '非法的时间！'
        return false
    }
    if (!isDDL.value && (st == 0 || ft == 0)) {
        showTimePickerError.value = true
        TimePickerErrorText.value = '非法的时间！'
        return false
    }
    if (!isDDL.value && (st > ft)) {
        showTimePickerError.value = true
        TimePickerErrorText.value = '结束时间必须晚于开始时间！'
        return false
    }
    // if (isDDL.value == true && StartTimeStamp.value == 0) {
    //     TimePickerErrorText.value = "填入的时间无效"
    //     showTimePickerError.value = true
    //     return false
    // }
    // if (isDDL.value == false && (StartTimeStamp.value > FinishTimeStamp.value || StartTimeStamp.value == 0 || FinishTimeStamp.value == 0)) {
    //     TimePickerErrorText.value = "填入的时间无效"
    //     showTimePickerError.value = true
    //     return false
    // }
    return true
}

const saveChanges = async () => {
    // 保存对日程的更改
    if (!dataCheck()) return
    const newSchedule: ScheduleItem = {
        ScheduleID: OriginID.value,
        Title: Title.value,
        Location: Location.value,
        StartTime: parseTime(StartTime.value),
        FinishTime: isDDL.value ? new Date(0) : parseTime(FinishTime.value),
        Stars: Stars.value,
        Type: isDDL.value ? 4 : 3,
        Body: Body.value,
        Created: false,
        Tags: []
    }
    isupdating.value = true
    if (route.name == 'ScheduleDetail') {
        //console.log(newSchedule)
        await updateScheduleByID(newSchedule)
        for (let i = 0; i < TagsSelected.value.length; i++) {
            const tag = TagsSelected.value[i]
            let tagID = tag.value
            let text = (tag.title == undefined ? tag.toString() : tag.title.toString())
            const tar = TagsOrigin.value.find(item => item.title == text)
            if (tagID == undefined && tar == undefined) {
                tagID = await addTag(text)
                updateTag(tagID, OriginID.value, 0)
            }
            else if (tagID != undefined && tar == undefined)
                updateTag(tagID, OriginID.value, 0)
        }
        for (let i = 0; i < TagsOrigin.value.length; i++) {
            const tag = TagsOrigin.value[i]
            let text = tag.title
            const tar = TagsSelected.value.find(item => item.title == text)
            if (tar == undefined) // 原来有,现在没有
                updateTag(tag.value, OriginID.value, 1)
        }
        isupdating.value = false
        router.push('/Schedule')
        timelineStore.upToDate = false
    }
    else if (route.name == 'createNewSchedule') {
        postSchedule(newSchedule).then(() => {
            isupdating.value = false
            router.push('/Schedule')
            timelineStore.upToDate = false
        }
        )
    }
}

const deleteSchedule = () => {
    // 删除日程
    isdeleting.value = true
    deleteScheduleByID(OriginID.value).then(() => {
        isdeleting.value = false
        timelineStore.upToDate = false
        messageStore.upToDate = false
        router.push('/Schedule')
    }
    )
}

if (route.name == 'ScheduleDetail') {
    WindowTitle.value = '日程详情'
    getScheduleByID(parseInt(router.currentRoute.value.params.id.toString())).then((res: ScheduleItem) => {
        OriginID.value = res.ScheduleID
        Title.value = res.Title
        Location.value = res.Location
        isDDL.value = res.Type == 4 ? true : false
        if (isDDL.value) {
            StartTime.value = toDateTimeChineseSlim(res.StartTime)
            //StartTimeStamp.value = res.StartTime.getTime()
            FinishTime.value = ''
            //FinishTimeStamp.value = res.FinishTime.getTime()
        }
        else {
            StartTime.value = toDateTimeChineseSlim(res.StartTime)
            //StartTimeStamp.value = res.StartTime.getTime()
            FinishTime.value = toDateTimeChineseSlim(res.FinishTime)
            //FinishTimeStamp.value = res.FinishTime.getTime()
        }
        if (res.Stars == undefined) Stars.value = 0
        else Stars.value = res.Stars
        Body.value = res.Body
        //console.log(curScheudle)
        isloading.value = false
        TagsSelected.value = res.Tags
        TagsOrigin.value = res.Tags
        Tags.value = timelineStore.tagList
    })
}
else if (route.name == 'createNewSchedule') {
    WindowTitle.value = '新建日程'
    OriginID.value = -1
    Title.value = ''
    Location.value = ''
    isDDL.value = false
    StartTime.value = toDateTimeChineseSlim(new Date())
    //StartTimeStamp.value = new Date().getTime()
    FinishTime.value = toDateTimeChineseSlim(new Date())
    //FinishTimeStamp.value = new Date().getTime()
    Stars.value = 0
    Body.value = ''
    isloading.value = false
    Tags.value = timelineStore.tagList
}

const ParsedStartTime = computed(() => {
    const result = parseTime(StartTime.value)
    return result.getTime() == 0 ? '' : toDateTimeChineseWeekDay(result)
})

const ParsedFinishTime = computed(() => {
    const result = parseTime(FinishTime.value)
    return result.getTime() == 0 ? '' : toDateTimeChineseWeekDay(result)
})

</script>
<template>
    <!-- 顶部导航栏 -->
    <v-app-bar density="compact" color='light-blue-lighten-3'>
        <v-btn icon="mdi-chevron-left" @click="router.push('/Schedule')">
        </v-btn>
        <v-app-bar-title>{{ WindowTitle }}</v-app-bar-title>
    </v-app-bar>

    <!-- 日程信息填写界面 -->
    <v-container v-if="!isloading" class="scheduleDetailBody">
        <!-- 标题 -->
            <v-text-field v-model="Title" label="标题" variant="outlined" :readonly="isupdating || isdeleting"></v-text-field>
        <!-- <h1 style="margin-bottom: 10px;">{{ Title }}</h1> -->
        <!-- 选择时间表示模式 -->

        <v-card class="d-flex flex-column itemCard">
            <v-row class="d-flex flex-row align-center">
                <v-card class="d-flex" variant="flat">
                    <v-container class="mb-2 text-h6">
                        单时间模式
                    </v-container>
                </v-card>
                <v-card style="margin-left: auto; padding-left:10px;padding-right:10px; margin-top: 5px;" variant="flat">
                    <v-switch v-model="isDDL" :readonly="isupdating || isdeleting"></v-switch>
                </v-card>
            </v-row>
            <v-divider></v-divider>
            <!-- 时间选择框 -->
            <v-expand-transition style="padding-top: 20px;">
                <v-text-field v-if="!isDDL" v-model="StartTime" :hint="ParsedStartTime" label="开始"
                    placeholder="yy/mm/dd hh:mm" prepend-icon="mdi-clock-time-nine-outline" persistent-hint
                    variant="underlined" :readonly="isupdating || isdeleting"
                    :active="!(isupdating || isdeleting)"></v-text-field>
            </v-expand-transition>
            <v-expand-transition>
                <v-text-field v-if="!isDDL" v-model="FinishTime" :hint="ParsedFinishTime" label="结束" prepend-icon="mdi"
                    placeholder="yy/mm/dd hh:mm" variant="underlined" persistent-hint class="mt-4"
                    :readonly="isupdating || isdeleting" :active="!(isupdating || isdeleting)"></v-text-field>
            </v-expand-transition>
            <v-expand-transition style="padding-top: 20px;">
                <v-text-field v-if="isDDL" v-model="StartTime" :hint="ParsedStartTime" label="时间点"
                    placeholder="yy/mm/dd hh:mm" prepend-icon="mdi-clock-time-five-outline" persistent-hint
                    variant="underlined" :readonly="isupdating || isdeleting"
                    :active="!(isupdating || isdeleting)"></v-text-field>
            </v-expand-transition>
        </v-card>
        <!-- 地点 -->
        <v-card class="itemCard">
            <v-text-field v-model="Location" label="地点" prepend-icon="mdi-map-marker" variant="underlined"
                :readonly="isupdating || isdeleting"></v-text-field>
        </v-card>
        <!-- <v-expand-transition>
            <v-text-field v-if="!isDDL" v-model="StartTime" label="开始" prepend-icon="mdi-clock-time-nine-outline"
                variant="underlined" readonly :active="!(isupdating || isdeleting)"
                @click="initTimePicker(); showTimePicker = !showTimePicker; currentPickerTime = 0"></v-text-field>
        </v-expand-transition>
        <v-expand-transition>
            <v-text-field v-if="!isDDL" v-model="FinishTime" label="结束" prepend-icon="mdi" variant="underlined" readonly
                @click="(isupdating || isdeleting)?0:initTimePicker(); showTimePicker = !showTimePicker; currentPickerTime = 1"></v-text-field>
        </v-expand-transition>
        <v-expand-transition>
            <v-text-field v-if="isDDL" v-model="StartTime" label="时间点" prepend-icon="mdi-clock-time-five-outline"
                variant="underlined" :readonly="isupdating || isdeleting"
                @click="(isupdating || isdeleting)?0:initTimePicker(); showTimePicker = !showTimePicker; currentPickerTime = 0"></v-text-field>
        </v-expand-transition> -->
        <!-- <v-text-field class="mt-6" v-model="Stars" label="重要程度" prepend-icon="mdi-star" variant="outlined" persistent-hint
            hint="0~3的整数，数字越大，重要性越高" density="compact" :readonly="isupdating || isdeleting"
            :rules="[value => (parseInt(value) >= 0 && parseInt(value) <= 3) || '必须是0~3的整数']"></v-text-field> -->

        <!-- <v-row class="d-flex flex-row justify-space-between" style="margin: 1px;"> -->
            <!-- 重要程度 -->
        <v-card class="d-flex itemCard">
            <v-row class="flex flex-row align-center" style="margin-top: 0px;margin-left: 0px;">
                <v-icon color="grey-darken-1" style="margin-right: 6px;">mdi-flag</v-icon>
                <div class="ma-2" style="color: grey;">重要程度</div>
                <v-rating hover v-model=Stars size="x-large" length="3" density="comfortable" color="yellow-darken-3" active-color="yellow-darken-2"
                    :readonly="isupdating || isdeleting" style="margin-left: 15px;"></v-rating>
            </v-row>
        </v-card>
            <!-- </v-row> -->
        <!-- Tags -->
        <v-card class="itemCard">
            <v-combobox variant="underlined" transition="scroll-y-transition" class="mt-2"
                prepend-icon="mdi-label-multiple" label="标签" hint="在下拉选择框中选择标签，或者输入新标签！" persistent-hint
                :readonly="isupdating || isdeleting" chips multiple v-model="TagsSelected" :items="Tags"
                density="compact"></v-combobox>
        </v-card>
        <v-card class="itemCard">
            <!-- 备注 -->
            <v-textarea class="mt-6" v-model="Body" label="备注" prepend-icon="mdi-file-document" variant="outlined"
                :readonly="isupdating || isdeleting" rows="7"></v-textarea>
        </v-card>
    </v-container>
    <!-- <div>{{ console.log(TagsSelected) }}</div> -->
    <!-- 底部操作栏 -->
    <v-sheet class="scheduleDetailBar">
        <v-divider></v-divider>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn variant="tonal" color="warning" v-if="!(route.name == 'createNewSchedule')" :disabled="isloading"
                :loading="isdeleting" @click="deleteSchedule()">删除日程</v-btn>
            <v-btn variant="tonal" :disabled="isloading" :loading="isupdating" @click="saveChanges()">{{ SaveButtonText
            }}</v-btn>
        </v-card-actions>
    </v-sheet>

    <!-- 加载进度条 -->
    <v-progress-circular v-if="isloading" indeterminate class="scheduleDetailCircular"></v-progress-circular>

    <!-- 时间选择器 -->
    <!-- <v-bottom-sheet v-model="showTimePicker">
        <v-card class="dateTimePicker">
            <v-date-picker class="mt-5" title="选择日期与时间" hide-actions elevation="0" header="日期" input-mode="calendar"
                v-model="PickerDate"></v-date-picker>
            <v-container class="timePicker">
                <v-card elevation="0"><v-card-title class="text-h6"></v-card-title></v-card>
                <v-text-field v-model="Hours" class="timeInputField" variant="underlined"></v-text-field>
                <v-card elevation="0">
                    <v-card-title class="text-h6">时</v-card-title>
                </v-card>
                <v-text-field v-model="Minutes" class="timeInputField" variant="underlined"></v-text-field>
                <v-card elevation="0">
                    <v-card-title class="text-h6">分</v-card-title>
                </v-card>
            </v-container>
            <v-card-actions class="timePickerButtonGroup">
                <v-btn variant="tonal" @click="showTimePicker = !showTimePicker">取消</v-btn>
                <v-card elevation="0"><v-card-title class="text-h6"></v-card-title></v-card>
                <v-btn variant="tonal" @click="confirmPickedTime(); showTimePicker = !showTimePicker">确定</v-btn>
            </v-card-actions>
        </v-card>
    </v-bottom-sheet> -->

    <!-- 信息提示条 -->
    <v-snackbar v-model="showTimePickerError" timeout="1000">
        {{ TimePickerErrorText }}
        <template v-slot:actions>
            <v-btn color="blue" variant="text" @click="showTimePickerError = false">关闭</v-btn>
        </template>
    </v-snackbar>
</template>
<style>
.itemCard {
    padding: 10px 20px 20px 20px;
    margin-top: 10px;
    margin-bottom: 10px;
}

.scheduleDetailBar {
    position: fixed;
    bottom: 0px;
    width: 100%;
}

.scheduleDetailBody {
    display: flex;
    flex-direction: column;
    align-items: normal;
    margin-bottom: 100px;
}

.scheduleDetailCircular {
    position: fixed;
    left: 50%;
    top: 50%;
}

.dateTimePicker {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 95%;
    left: 2.5%;
    margin-bottom: 10px;
}

.timePicker {
    display: flex;
    width: 80%;
    flex-direction: row;
    align-items: center;
    margin-top: -30px;
}

.timePickerButtonGroup {
    position: static;
    margin-bottom: 10px;
}

.timeInputField {
    width: 10px;
    left: 5%;
}
</style>