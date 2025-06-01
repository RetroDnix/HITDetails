<script setup lang = "ts">
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';

import { getGroupByID, getSubGroupList } from '@/utils/Getter'
import { modifyMember, modifyAdmin, deleteCurGroup, modifyFatherGroup } from '@/utils/Updater'
import { DetailedGroupItem } from "@/type/GroupItem";
import { computed } from 'vue';

import grStore from '@/store/modules/GroupStore'
const groupStore = grStore()

const OpCode = ref(0)
const OpTitle = ref('')
const OpHint = ref('')
const OpTextFieldLabel = ref('')
const OpTextFieldString = ref('')
const OpLoading = ref(false)
const Overlay = ref(false)
const OpSnackBar = ref(false)
const OpSnackBarHint = ref('')
const OpUseTextField = ref(true)
const OpUseSelect = ref(false)
const OpSelectLabel = ref('')
const OpSelectItem = ref(Array())
const OpSelectValue = ref(Array())

const router = useRouter(); // 获取路由实例
const isloading = ref(true)
const HideSelect = ref(true)

const getAuthority = (admin: number, IsMember: boolean) => {
    let res = ''
    if (IsMember) res += '成员 '
    if (admin == 1) res += '通知发布者 '
    else if (admin == 2) res += '管理员 '
    else if (admin == 3) res += '超级管理员 '
    if (!IsMember && admin == 0) res += '未知'
    return res
}

const getType = (type: number) => {
    if (type == 0) return '行政班'
    else if (type == 1) return '教学班'
    else return '学生组织'
}

const CurGroup = ref(0)
const Expanel = ref(['info'])
const WindowTitle = ref('')

interface subGroup {
    FatherGroupID: number;
    GroupID: number;
    Name: string;
}
const subgroupList = Array<subGroup>()

interface SelectGroupItem { title: string; value: number; subtitle: string; }
const SelectItem = Array<SelectGroupItem>()
const SelectedItem = ref(Array<number>())

interface groupPathName { [propname: number]: string; }
let groupPath: groupPathName = {}

let GroupDetail: DetailedGroupItem = {
    GroupID: 0,
    GroupName: "undefined",
    Type: 0,
    Admin: 0,
    IsMember: false,
    Members: [],
    Admins: [],
    FatherGroup: []
}

const GroupFullReload = () => {
    isloading.value = true
    HideSelect.value = true
    WindowTitle.value = '组织信息'
    subgroupList.length = 0
    SelectItem.length = 0
    groupPath = {}
    Promise.all([getSubGroupList(CurGroup.value), getGroupByID(CurGroup.value)]).then((results) => {
        GroupDetail = results[1]
        subgroupList.push({ 'FatherGroupID': 0, 'GroupID': GroupDetail.GroupID, 'Name': GroupDetail.GroupName })
        results[0].forEach((item) => {
            subgroupList.push({ 'FatherGroupID': item.FatherGroupID, 'GroupID': item.GroupID, 'Name': item.Name })
        });

        subgroupList.forEach((item) => {
            groupPath[item.GroupID] = item.FatherGroupID == 0 ? item.Name : groupPath[item.FatherGroupID] + '/' + item.Name
            SelectItem.push({ 'title': item.Name, 'value': item.GroupID, 'subtitle': groupPath[item.GroupID] })
        });
        isloading.value = false
        HideSelect.value = false
    })
}

const GroupReload = () => {
    isloading.value = true
    WindowTitle.value = '组织信息'
    getGroupByID(CurGroup.value).then((result) => {
        GroupDetail = result
        isloading.value = false
        HideSelect.value = false
    })
}

CurGroup.value = parseInt(router.currentRoute.value.params.id.toString())
GroupFullReload()
SelectedItem.value.push(CurGroup.value)

watch(SelectedItem, (newValue) => {
    if (newValue.length == 0) return
    const NewValue = parseInt(newValue.toString());
    if (CurGroup.value == NewValue) return
    else {
        isloading.value = true
        CurGroup.value = parseInt(newValue.toString())
        getGroupByID(CurGroup.value).then((result) => {
            GroupDetail = result
            Expanel.value = ['info']
            isloading.value = false
        })
    }
})

const OpTextFieldHint = computed(() => {
    const uid = parseInt(OpTextFieldString.value)
    if (Number.isNaN(uid) || uid < 0) return 'ID必须是正整数'
    if (OpCode.value != 1 && OpCode.value != 2) return ''
    let isMember = false, Admin = 0
    let uname = ''
    GroupDetail.Members.forEach((item) => {
        if (item.UserID == uid) isMember = true, uname = item.Name
    })
    GroupDetail.Admins.forEach((item) => {
        if (item.UserID == uid) Admin = item.type, uname = item.Name
    })
    if (uname != '') return '用户名:' + uname + '  用户身份：' + getAuthority(Admin, isMember)
    else return '用户身份：' + getAuthority(Admin, isMember)
})


const AddMember = () => {
    OpUseTextField.value = true
    OpUseSelect.value = false
    OpCode.value = 0
    OpTitle.value = '添加成员'
    OpHint.value = '请输入要添加的成员的UID'
    OpTextFieldLabel.value = 'UID'
    OpTextFieldString.value = ''
    OpLoading.value = false
    Overlay.value = true
}

const DeleteMember = () => {
    OpUseTextField.value = true
    OpUseSelect.value = false
    OpCode.value = 1
    OpTitle.value = '删除成员'
    OpHint.value = '请输入要删除的成员的UID'
    OpTextFieldLabel.value = 'UID'
    OpTextFieldString.value = ''
    OpLoading.value = false
    Overlay.value = true
}

const AddAuthority = () => {
    OpUseTextField.value = true
    OpUseSelect.value = true
    OpSelectLabel.value = "请选择赋予该用户的权限"
    OpSelectItem.value = ['移除管理员权限', '通知发布者', '管理员', '超级管理员']
    OpCode.value = 2
    OpTitle.value = '修改管理员权限'
    OpHint.value = '请输入要修改的用户的UID'
    OpTextFieldLabel.value = 'UID'
    OpTextFieldString.value = ''
    OpLoading.value = false
    Overlay.value = true
}

const DeleteGroup = () => {
    OpUseTextField.value = false
    OpUseSelect.value = false
    OpCode.value = 3
    OpTitle.value = '删除组织'
    OpHint.value = '确定要删除当前组织及其子组织吗？'
    OpLoading.value = false
    Overlay.value = true
}

const ModifyFatherGroup = () => {
    OpUseTextField.value = true
    OpUseSelect.value = false
    OpCode.value = 4
    OpTitle.value = '修改上下级关系'
    OpHint.value = GroupDetail.FatherGroup.length > 1 ? '当前上级组织为：' + GroupDetail.FatherGroup[1].GroupName : '当前无上级组织'
    OpTextFieldLabel.value = '请输入新的上级组织的ID'
    OpTextFieldString.value = ''
    OpLoading.value = false
    Overlay.value = true
}

const DeleteFatherGroup = () => {
    OpUseTextField.value = false
    OpUseSelect.value = false
    OpCode.value = 5
    OpTitle.value = '删除当前上下级关系'
    OpHint.value = '确认要删除当前组织的上下级关系吗?'
    OpLoading.value = false
    Overlay.value = true
}

const OpFail = (hint: string) => {
    OpSnackBarHint.value = hint
    OpSnackBar.value = true
    OpLoading.value = false
}

const OpSuccess = (hint: string, quit?: number) => {
    OpSnackBarHint.value = hint
    OpSnackBar.value = true
    OpLoading.value = false
    Overlay.value = !Overlay.value
    if (quit == 1)
    {
        groupStore.upToDate = false
        router.push('/Group')
    } 
    else if (quit == 2) {
        CurGroup.value = parseInt(router.currentRoute.value.params.id.toString())
        groupStore.upToDate = false
        GroupFullReload()
    }
    else GroupReload()
}

const OpConfirm = () => {
    OpLoading.value = true
    if (OpCode.value == 0) {
        const uid = parseInt(OpTextFieldString.value);
        if (Number.isNaN(uid) || uid < 0)
            return OpFail('请输入正确的UID')
        else modifyMember(CurGroup.value, uid, 0).then((result) => {
            if (result) return OpSuccess('操作成功!')
            else return OpFail('操作失败!')
        })
    }
    else if (OpCode.value == 1) {
        const uid = parseInt(OpTextFieldString.value);
        if (Number.isNaN(uid) || uid < 0)
            return OpFail('请输入正确的UID')
        else modifyMember(CurGroup.value, uid, 1).then((result) => {
            if (result) return OpSuccess('操作成功!')
            else return OpFail('操作失败!')
        })
    }
    else if (OpCode.value == 2) {
        const uid = parseInt(OpTextFieldString.value);
        if (Number.isNaN(uid) || uid < 0)
            return OpFail('请输入正确的UID')
        else modifyAdmin(CurGroup.value, uid, OpSelectValue.value.toString()).then((result) => {
            if (result) return OpSuccess('操作成功!')
            else return OpFail('操作失败!')
        })
    }
    else if (OpCode.value == 3) {
        deleteCurGroup(CurGroup.value).then((result) => {
            if (result) return OpSuccess('操作成功!', 1)
            else return OpFail('操作失败!')
        })
    }
    else if (OpCode.value == 4) {
        const gid = parseInt(OpTextFieldString.value);
        if (Number.isNaN(gid) || gid < 0)
            return OpFail('请输入正确的UID')
        else modifyFatherGroup(CurGroup.value, gid).then((result) => {
            if (result) return OpSuccess('操作成功!', 2)
            else return OpFail('操作失败!')
        })
    }
    else if (OpCode.value == 5) {
        modifyFatherGroup(CurGroup.value, 0).then((result) => {
            if (result) return OpSuccess('操作成功!', 2)
            else return OpFail('操作失败!')
        })
    }
}

</script>
<template>
    <!-- 顶部导航栏 -->
    <v-app-bar density="compact" color="teal-lighten-3">
        <v-btn icon="mdi-chevron-left" @click="router.push('/Group')">
        </v-btn>
        <v-app-bar-title>{{ WindowTitle }}</v-app-bar-title>
    </v-app-bar>
    <v-container>
        <v-select label="选择当前查看的组织" v-if="!HideSelect" class="mt-2" :items="SelectItem" v-model="SelectedItem"
            :readonly="isloading">
            <template v-slot:item="{ item, props }">
                <v-list-item v-bind="props">
                    <v-list-item-subtitle>{{ item.raw.subtitle }}</v-list-item-subtitle>
                </v-list-item>
            </template>
        </v-select>
    </v-container>
    <v-container v-if="!isloading" style="margin-top: -30px;">
        <v-expansion-panels v-model="Expanel" multiple>
            <v-expansion-panel title="组织信息" value="info">
                <v-expansion-panel-text>
                    <div class="text-h6">{{ GroupDetail.GroupName }}</div>
                    <div class="text-subtitle-1">{{ "ID：" + GroupDetail.GroupID }}</div>
                    <div class="text-subtitle-1">{{ "组织类型：" + getType(GroupDetail.Type) }}</div>
                    <div class="text-subtitle-1">{{ "权限：" + getAuthority(GroupDetail.Admin, GroupDetail.IsMember) }}</div>
                </v-expansion-panel-text>
            </v-expansion-panel>
            <v-expansion-panel title="上级组织" value="superior">
                <v-expansion-panel-text>
                    <v-container>
                        <v-timeline side="end">
                            <v-timeline-item v-for="(item, i) in GroupDetail.FatherGroup" :key="i">
                                <v-card>
                                    <v-card-title>{{ item.GroupName }}</v-card-title>
                                    <v-card-text>
                                        {{ "ID：" + item.GroupID }}
                                    </v-card-text>
                                </v-card>
                            </v-timeline-item>
                        </v-timeline>
                    </v-container>
                </v-expansion-panel-text>
            </v-expansion-panel>
            <v-expansion-panel title="成员列表" value="member">
                <v-expansion-panel-text>
                    <div v-if="GroupDetail.Members.length == 0" class="text-h6" style="text-align: center;">本组织无直属成员</div>
                    <v-list v-if="GroupDetail.Members.length != 0" class="MemberList">
                        <v-list-item v-for="(item, i) in GroupDetail.Members" :key="i" prepend-icon="mdi-account">
                            <v-list-item-title>{{ item.Name }}</v-list-item-title>
                            <v-list-item-subtitle>{{ "UID：" + item.UserID }}</v-list-item-subtitle>
                        </v-list-item>
                    </v-list>
                </v-expansion-panel-text>
            </v-expansion-panel>
            <v-expansion-panel title="直属管理员列表" value="admin">
                <v-expansion-panel-text>
                    <div v-if="GroupDetail.Admins.length == 0" class="text-h6" style="text-align: center;">本组织无直属管理员</div>
                    <v-list v-if="GroupDetail.Admins.length != 0" class="MemberList">
                        <v-list-item v-for="(item, i) in GroupDetail.Admins" :key="i" prepend-icon="mdi-account">
                            <v-list-item-title>{{ item.Name }}</v-list-item-title>
                            <v-list-item-subtitle>{{ "UID：" + item.UserID + ' | 类型：' +
                                getAuthority(item.type, false) }}</v-list-item-subtitle>
                        </v-list-item>
                    </v-list>
                </v-expansion-panel-text>
            </v-expansion-panel>
            <v-expansion-panel title="管理选项" value="manage" v-if="GroupDetail.Admin > 1">
                <v-expansion-panel-text>
                    <v-list>
                        <v-list-item>
                            <v-list-item-title>成员操作</v-list-item-title>
                            <v-item-group class="AuthorityOpPanel">
                                <v-chip @click="AddMember()">添加成员</v-chip>
                                <v-chip @click="DeleteMember()">删除成员</v-chip>
                            </v-item-group>
                        </v-list-item>
                        <v-divider />
                        <v-list-item v-if="GroupDetail.Admin > 2">
                            <v-list-item-title>管理员操作</v-list-item-title>
                            <v-item-group class="AuthorityOpPanel">
                                <v-chip @click="AddAuthority()">添加/修改/删除管理员权限</v-chip>
                            </v-item-group>
                        </v-list-item>
                        <v-divider />
                        <v-list-item v-if="GroupDetail.Admin > 2">
                            <v-list-item-title>上下级组织关系操作</v-list-item-title>
                            <v-item-group class="AuthorityOpPanel">
                                <v-chip @click="ModifyFatherGroup()">修改上级组织</v-chip>
                                <v-chip @click="DeleteFatherGroup()">删除上下级关系</v-chip>
                            </v-item-group>
                        </v-list-item>
                        <v-divider />
                        <v-list-item v-if="GroupDetail.Admin > 2">
                            <v-list-item-title>删除组织</v-list-item-title>
                            <v-item-group class="AuthorityOpPanel">
                                <v-chip color="red" @click="DeleteGroup()">删除组织</v-chip>
                            </v-item-group>
                        </v-list-item>
                    </v-list>
                </v-expansion-panel-text>
            </v-expansion-panel>
        </v-expansion-panels>
    </v-container>

    <v-container v-if="Overlay" class="OpCard">
        <v-overlay v-model="Overlay" activator="parent" location-strategy="connected" scroll-strategy="block">
            <v-card>
                <v-card-title>
                    {{ OpTitle }}
                </v-card-title>
                <v-card-subtitle>
                    {{ OpHint }}
                </v-card-subtitle>
                <v-card-subtitle v-if="OpCode == 4 || OpCode == 5" class="mt-1">
                    请注意，当前操作可能让本组织脱离您的管理！
                </v-card-subtitle>
                <v-card-text v-if="OpUseTextField">
                    <v-text-field :label="OpTextFieldLabel" :hint="OpTextFieldHint" v-model="OpTextFieldString" persistent-hint
                        :rules="[value => (parseInt(value) >= 0) || 'ID必须是正整数']"></v-text-field>
                    <v-select class="mt-3" v-if="OpUseSelect" :label="OpSelectLabel" :items="OpSelectItem"
                        v-model="OpSelectValue"></v-select>
                </v-card-text>
                <v-card-actions>
                    <v-spacer />
                    <v-btn @click="OpConfirm()" :loading="OpLoading">确定</v-btn>
                    <v-btn @click="Overlay = !Overlay">取消</v-btn>
                </v-card-actions>
            </v-card>
        </v-overlay>
    </v-container>

    <v-snackbar v-model="OpSnackBar" timeout="1000">
        {{ OpSnackBarHint }}
        <template v-slot:actions>
            <v-btn color="pink" variant="text" @click="OpSnackBar = false">关闭</v-btn>
        </template>
    </v-snackbar>

    <!-- 加载进度条 -->
    <v-progress-circular v-if="isloading" indeterminate class="groupDetailCircular"></v-progress-circular>
</template>
<style>
.groupDetailCircular {
    position: fixed;
    left: 50%;
    top: 50%;
}

.AuthorityOpPanel {
    margin-top: 5px;
    margin-bottom: 5px;
    display: flex;
    gap: 10px;
}

.OpCard {
    z-index: 3;
    position: fixed;
    left: 15%;
    width: 70%;
    top: 30%;
}

.MemberList {
    margin-left: -15px;
    margin-right: -15px;
}
</style>