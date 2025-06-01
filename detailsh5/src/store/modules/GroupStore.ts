import { ref } from "vue";
import { defineStore } from "pinia";
import { axiosInstance } from "@/utils/Axios";
import GroupItem from "@/type/GroupItem";
import { GroupSelectItem } from "@/type/MessageItem";

export const addGroupData = (data: any, list: Array<GroupItem>) => {
    data.forEach((s: any) => {
        list.push({
            GroupID: parseInt(s.GroupID),
            GroupName: s.Name,
            Type: s.Type,
            IsMember: s.IsMember,
            Admin: s.Authority,
        });
    });
}

const grStore = defineStore('groupStore', {
    state: () => {
        return {
            groupList: new Array<GroupItem>(),
            authoredGroupList: new Array<GroupSelectItem>(),
            upToDate: ref(false),
            isloading: false,
            windowscroll: 0,
        }
    },
    actions: {
        setUpdate(): void {
            if (!this.isloading) {
                this.upToDate = false;
            }
        },
        async reloadAll() {
            if (this.isloading) return
            if (this.upToDate) return
            this.isloading = true
            this.groupList = []
            this.authoredGroupList = []
            try {
                const response1 = await axiosInstance.get("/user/get_group");
                if (response1.data.Groups != undefined)
                    addGroupData(response1.data.Groups, this.groupList)
                const response2 = await axiosInstance.get("user/managed_group");
                    response2.data.Groups.forEach((s: any) => {
                            this.authoredGroupList.push({
                                title: s.Name,
                                value: s.GroupID,
                            });
                    });
                
            }
            catch (error) {
                console.log(error);
            }
            this.isloading = false;
            this.upToDate = true;
        },
    }
})

export default grStore;