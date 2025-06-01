import { axiosInstance } from "@/utils/Axios";
import ScheduleItem from "@/type/ScheduleItem";
import MessageItem from "@/type/MessageItem";
import { DetailedGroupItem } from "@/type/GroupItem";
import { addScheduleData, getTags } from "@/store/modules/TimelineScheduleStore"
// 获取Schedule信息
export const getScheduleByID = async (SID: number) => {
    let res: ScheduleItem = {
        ScheduleID: 0,
        Title: 'undefined',
        Body: 'undefined',
        Location: 'undefined',
        Type: 3,
        StartTime: new Date(),
        FinishTime: new Date(),
        Stars: 0,
        Created: false,
        Tags: [],
    }
    try {
        const response = await axiosInstance.get("/schedule", { params: { ScheduleID: SID, HasTag: true } });
        //console.log(SID);
        if (response.data.Schedules != undefined)
            response.data.Schedules.forEach((s: any) => {
                res = ({
                    ScheduleID: parseInt(s.ScheduleID),
                    Title: s.Title,
                    Body: s.Body,
                    Location: s.Location,
                    Type: s.Type,
                    StartTime: s.DeadLine == undefined ? new Date(s.StartTime * 1000) : new Date(s.DeadLine * 1000),
                    FinishTime: new Date(s.FinishTime * 1000),
                    Stars: s.Stars,
                    Created: false,
                    Tags: getTags(s.Tags)
                });
            });
    }
    catch (error) {
        console.log(error);
    }
    return res
}

// 获取Message信息
export const getMessageByID = async (MID?: number) => {
    let res: MessageItem = {
        MessageID: 0,
        Title: 'undefined',
        Body: 'undefined',
        Type: 1,
        Stars: 0,
        Sender: 'undefined',
        SendTime: new Date(),
        HaveRead: false,
        Schedules: [],
        Tags: [],
        Images: '',
        OriginGroupName: 'undefined',
        OriginGroupID: 0
    }
    try {
        const response = await axiosInstance.get("/message", { params: { MessageID: MID } });
        //console.log(SID);
        if (response.data.Messages != undefined)
            response.data.Messages.forEach((s: any) => {
                const scheduleList: ScheduleItem[] = [];
                addScheduleData(s.Schedules, scheduleList)
                res = ({
                    MessageID: parseInt(s.MessageID),
                    Title: s.Title,
                    Body: s.Body,
                    Sender: s.Sender,
                    Type: s.Type,
                    SendTime: new Date(s.Time * 1000),
                    Stars: s.Stars,
                    HaveRead: s.HaveRead == 'false' ? false : true,
                    Schedules: scheduleList,
                    Tags: JSON.parse(s.Tags),
                    Images: s.Images,
                    OriginGroupName: s.OriGroupName,
                    OriginGroupID: s.OriGroupID
                });
            });
    }
    catch (error) {
        console.log(error);
    }
    return res
}

export const getGroupByID = async (GID: number) => {
    const res: DetailedGroupItem = {
        GroupID: 0,
        GroupName: 'undefined',
        Type: 1,
        Admin: 0,
        IsMember: false,
        Members: [],
        Admins: [],
        FatherGroup: []
    }
    try {
        const response = await axiosInstance.get("/groupClassic", { params: { GroupID: GID } });
        res.GroupID = response.data.GroupID;
        res.GroupName = response.data.GroupName;
        res.Type = response.data.Type;
        res.Admin = response.data.Authority;
        res.IsMember = response.data.IsMember;
        res.FatherGroup = response.data.FatherGroup;
        const response2 = await axiosInstance.get("/group/members", { params: { GroupID: GID } });
        res.Members = response2.data.members;
        const response3 = await axiosInstance.get("/group/admins", { params: { GroupID: GID } });
        res.Admins = response3.data.admins;
        //console.log(res)
    }
    catch (error) {
        console.log(error);
    }
    return res
}

export const getSubGroupList = async (GID: number) => {
    let res = Array<any>()
    try {
        const response = await axiosInstance.get("/getSubGroupClassic", { params: { GroupID: GID } });
        res = response.data.Groups
    }
    catch (error) {
        console.log(error);
    }
    return res
}

export const getToken = async (UserName: string , PassWord: string) => {
    const params = new URLSearchParams();
    params.append('username', UserName);
    params.append('password', PassWord);
    try {
        const response = await axiosInstance.post("/login", params);
        if (response.status == 200)
        {
            console.log(response.data);
            return response.data.access_token;
        }
        else return 'failed';
    }
    catch (error) {
        console.log(error);
        return 'failed';
    }
}

export const getSysToken = async (Uid: string) => {
    const params = new URLSearchParams();
    params.append('WeLinkUID', Uid);
    try {
        const response = await axiosInstance.post("/Welinklogin", params);
        if (response.status == 200)
        {
            console.log(response.data);
            return response.data.access_token;
        }
        else if(response.status == 204) return 'null';
        else return 'failed';
    }
    catch (error) {
        console.log(error);
        return 'failed';
    }
}