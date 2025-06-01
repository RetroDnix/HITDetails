import { ref } from "vue";
import { defineStore } from "pinia";
import { axiosInstance } from "@/utils/Axios";
import MessageItem,{ GroupSelectItem } from '@/type/MessageItem';
import ScheduleItem from "@/type/ScheduleItem";
import { addScheduleData } from "@/store/modules/TimelineScheduleStore"

interface fliterParm {
    SortByTime: boolean;
    Page: number;
    [propname: string]: any;
}

const addMessageData = (data: any, list: Array<MessageItem>) => {
    data.forEach((s: any) => {
        const scheduleList = new Array<ScheduleItem>();
        if (s.Schedules != undefined)
            addScheduleData(s.Schedules, scheduleList);        
        let taglist = JSON.parse(s.Tags);
        if(taglist == null) taglist = new Array<string>();
        list.push({
            MessageID: parseInt(s.MessageID),
            Title: s.Title,
            Body: s.Body,
            Sender: s.Sender,
            Type: s.Type,
            SendTime: new Date(s.Time * 1000),
            Stars: s.Stars,
            HaveRead: s.HaveRead,
            Schedules: scheduleList,
            Tags: taglist,
            Images: s.Images,
            OriginGroupName: s.OriGroupName,
            OriginGroupID: s.OriGroupID
        });
    });
}

const mesStore = defineStore('MessageStore', {
    state: () => {
        return {
            messageList: new Array<MessageItem>(),
            GroupSelectList: new Array<GroupSelectItem>(),
            upToDate: ref(false),
            isloading: false,
            windowscroll: 0,
            fliterType: 0,
            fliterStars: 0,
            fliterOrigin: 0,
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
            this.messageList = []
            let flag = true
            const params: fliterParm = {
                SortByTime: true,
                Page: 1,
            };
            if (this.fliterType != 0) params.Type = this.fliterType;
            if (this.fliterStars != 0) params.Stars = this.fliterStars;
            if (this.fliterOrigin != 0) params.Group = this.fliterOrigin;
            else delete params.Group;
            if (this.fliterType == 0 && this.fliterStars == 0 && this.fliterOrigin == 0)
            {
                this.GroupSelectList = []
                this.GroupSelectList.push({title:'全部',value:0})
            }
            //console.log(params);
            try {
                do {
                    const response = await axiosInstance.get("/message", { params: params });
                    if (response.data.Messages != undefined) {
                        addMessageData(response.data.Messages, this.messageList)
                        if(this.fliterType == 0 && this.fliterStars == 0 && this.fliterOrigin == 0)
                        {
                            this.messageList.forEach((s: MessageItem) => {
                                if(!this.GroupSelectList.some(item => item.title === s.OriginGroupName && item.value === s.OriginGroupID))
                                    this.GroupSelectList.push({
                                        title: s.OriginGroupName,
                                        value: s.OriginGroupID
                                    })
                            })
                        }
                        params.Page++
                    }
                    else flag = false
                } while (flag)
            }
            catch (error) {
                console.log(error);
            }
            this.isloading = false;
            this.upToDate = true;
        },
    }
});

export default mesStore;