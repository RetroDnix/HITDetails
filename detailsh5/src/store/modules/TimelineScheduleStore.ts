import { ref } from "vue";
import { defineStore } from "pinia";
import { axiosInstance } from "@/utils/Axios";
import ScheduleItem, { TagItem } from "@/type/ScheduleItem";
import upperBound from "@/utils/UpperBound";
import qs from 'qs';
interface fliterParm {
    SortByTime: boolean;
    Page: number;
    [propname: string]: any;
}

export const addScheduleData = (data: any, list: Array<ScheduleItem>, HasTag?: boolean) => {
    data.forEach((s: any) => {
        list.push({
            ScheduleID: parseInt(s.ScheduleID),
            Title: s.Title,
            Body: s.Body,
            Location: s.Location,
            Type: s.Type,
            StartTime: s.DeadLine == undefined ? new Date(s.StartTime * 1000) : new Date(s.DeadLine * 1000),
            FinishTime: new Date(s.FinishTime * 1000),
            Stars: s.Stars,
            Created: s.Created,
            Tags: HasTag ? getTags(s.Tags) : [],
        });
    });
}

export const getTags = (data: any) => {
    const tags: TagItem[] = [];
    data.forEach((s: any) => {
        tags.push({
            title: s.TagName,
            value: s.TagID,
        });
    });
    return tags;
}

const tlineStore = defineStore('ScheduleStore', {
    state: () => {
        return {
            tagList: new Array<TagItem>(),
            scheduleList: new Array<ScheduleItem>(),
            upToDate: ref(false),
            isloading: false,
            noMore: false,
            curPage: 0,
            curPos: 0,
            windowscroll: 0,
            fliterType: 0,
            fliterStars: 0,
            fliterStartTime: 0,
            fliterFinishTime: 0,
            fliterTags: Array<string>(),
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
            this.windowscroll = 0
            this.isloading = true
            this.scheduleList = []
            this.tagList = []
            let flag = true
            const params: fliterParm = {
                SortByTime: true,
                Page: 1,
                HasTag: true,
            };
            try {
                const response = await axiosInstance.get("/tags/get_tags");
                if (response.data.Tags != undefined)
                    response.data.Tags.forEach((s: any) => {
                        this.tagList.push({
                            title: s.TagName,
                            value: s.TagID,
                        });
                    });
            }
            catch (error) {
                console.log(error);
            }
            if (this.fliterType != 0) params.Type = this.fliterType;
            if (this.fliterStars != 0) params.Stars = this.fliterStars;
            if (this.fliterStartTime != 0) params.StartTime = this.fliterStartTime / 1000;
            if (this.fliterFinishTime != 0) params.DeadLine = this.fliterFinishTime / 1000 + 86400;
            if (this.fliterTags.length != 0) params.Tags = this.fliterTags;
            try {
                do {
                    const response = await axiosInstance.get("/schedule", {
                        params: params,
                        paramsSerializer: function (params) {return qs.stringify(params, { arrayFormat: 'repeat' })}
                    })
                    if (response.data.Schedules != undefined) {
                        addScheduleData(response.data.Schedules, this.scheduleList, true)
                        params.Page++
                    }
                    else flag = false
                } while (flag)
                this.curPos = upperBound(this.scheduleList, new Date().getTime()) - 1
            }
            catch (error) {
                console.log(error);
            }
            this.isloading = false;
            this.upToDate = true;
        },
        // async applyUpdate() {
        //     if (this.upToDate) return;
        //     if (this.noMore) return;
        //     if (!this.isloading) {
        //         this.isloading = true
        //         const curLength = this.scheduleList.length;
        //         const currentDate = new Date();
        //         const startTime = new Date();
        //         startTime.setDate(currentDate.getDate() - 1);
        //         try {
        //             const response = await axiosInstance.get("/schedule?HasTag=True", { params: { StartTime: startTime.getTime() / 1000, SortByTime: true, Maxnum: 5, Page: this.curPage + 1 } });
        //             console.log(response.data);
        //             if (response.data.Schedules != undefined)
        //                 response.data.Schedules.forEach((s: any) => {
        //                     this.scheduleList.push({
        //                         ScheduleID: parseInt(s.ScheduleID),
        //                         Title: s.Title,
        //                         Body: s.Body,
        //                         Location: s.Location,
        //                         Type: s.Type,
        //                         StartTime: s.DeadLine == undefined ? new Date(s.StartTime * 1000) : new Date(s.DeadLine * 1000),
        //                         FinishTime: new Date(s.FinishTime * 1000),
        //                         Stars: s.Stars,
        //                         Created: s.Created,
        //                         Tags: getTags(s.Tags),
        //                     });
        //                 });

        //         }
        //         catch (error) {
        //             console.log(error);
        //         }
        //         if (this.scheduleList.length > curLength)
        //             this.curPage++;
        //         else this.noMore = true;
        //         this.isloading = false;
        //         this.upToDate = true;
        //     }
        // }
    }
});

export default tlineStore;