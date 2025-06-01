import { axiosInstance } from "@/utils/Axios";
import ScheduleItem from "@/type/ScheduleItem";
import { PostImage } from "@/utils/ImageUploader";

export const updateScheduleByID = async (data: ScheduleItem) => {
    const params = new URLSearchParams();
    params.append('ScheduleID', data.ScheduleID.toString());
    params.append('Title', data.Title);
    params.append('Body', data.Body);
    params.append('StartTime', Math.floor(data.StartTime.getTime() / 1000).toString());
    params.append('FinishTime', Math.floor(data.FinishTime.getTime() / 1000).toString());
    params.append('Type', data.Type.toString());
    params.append('Location', data.Location);
    params.append('Stars', data.Stars.toString());
    try {
        await axiosInstance.put("/schedule", params);
    }
    catch (error) {
        console.log(error);
    }
}

export const deleteScheduleByID = async (SID: number) => {
    try {
        await axiosInstance.delete("/schedule", { params: { ScheduleID: SID } });
    }
    catch (error) {
        console.log(error);
    }
}

export const postSchedule = async (data: ScheduleItem) => {
    const params = new URLSearchParams();
    params.append('Title', data.Title);
    params.append('Body', data.Body);
    params.append('StartTime', Math.floor(data.StartTime.getTime() / 1000).toString());
    params.append('FinishTime', Math.floor(data.FinishTime.getTime() / 1000).toString());
    params.append('Type', data.Type.toString());
    params.append('Location', data.Location);
    params.append('Stars', data.Stars.toString());
    params.append('Self', 'True');
    try {
        await axiosInstance.post("/schedule", params);
    }
    catch (error) {
        console.log(error);
    }
}

export const markMessageRead = async (MID: number) => {
    const params = new URLSearchParams();
    params.append('MessageID', MID.toString());
    try {
        const response = await axiosInstance.post("/messageConfirm", params);
        if (response.status == 204) return true;
        else return false;
    }
    catch (error) {
        console.log(error);
        return false;
    }
}

export const deleteMessageByID = async (MID: number) => {
    try {
        const response = await axiosInstance.delete("/messageConfirm", { params: { MessageID: MID } });
        if (response.status == 204) return true;
        else return false;
    }
    catch (error) {
        console.log(error);
        return false;
    }
}

export const addToSchedule = async (SID: number, MID: number, Stars: number) => {
    try {
        const params = new URLSearchParams();
        params.append('ScheduleID', SID.toString());
        params.append('MessageID', MID.toString());
        if (Stars != 0) params.append('Stars', Stars.toString());
        const response = await axiosInstance.patch("/schedule", params);
        if (response.status == 200) return response.data.message.ScheduleID;
        else return -1;
    }
    catch (error) {
        console.log(error);
        return -1;
    }
}

export const modifyMember = async (GID: number, UID: number, Type: number) => {
    try {
        const params = new URLSearchParams();
        params.append('UserID', UID.toString());
        params.append('GroupID', GID.toString());
        params.append('Type', Type.toString());
        const response = await axiosInstance.post("/group/modify_member", params);
        if (response.status == 204 || response.status == 202) return true;
        else return false;
    }
    catch (error) {
        console.log(error);
        return false;
    }
}

export const modifyAdmin = async (GID: number, UID: number, Role: string) => {
    try {
        const params = new URLSearchParams();
        params.append('UserID', UID.toString());
        params.append('GroupID', GID.toString());
        if (Role == "移除管理员权限") params.append('Role', 'Member');
        else if (Role == '通知发布者') params.append('Role', 'Assistant');
        else if (Role == '管理员') params.append('Role', 'Administrator');
        else if (Role == '超级管理员') params.append('Role', 'Owner');
        else return false;
        console.log(params)
        const response = await axiosInstance.post("/group/modify_permissions", params);
        if (response.status == 204) return true;
        else return false;
    }
    catch (error) {
        console.log(error);
        return false;
    }
}

export const deleteCurGroup = async (GID: number) => {
    try {
        const response = await axiosInstance.delete("/group/delete_group", { params: { GroupID: GID } });
        if (response.status == 204) return true;
        else return false;
    }
    catch (error) {
        console.log(error);
        return false;
    }
}

export const modifyFatherGroup = async (GID: number, FatherGroup: number) => {
    try {
        const params = new URLSearchParams();
        params.append('GroupID', GID.toString())
        if (FatherGroup != 0)
            params.append('FatherGroupID', FatherGroup.toString());
        const response = await axiosInstance.post("/group/modify_superior_group", params);
        if (response.status == 204) return true;
        else return false;
    }
    catch (error) {
        console.log(error);
        return false;
    }
}

export const addTag = async (TagName: string) => {
    try {
        const params = new URLSearchParams();
        params.append('TagName', TagName);
        const response = await axiosInstance.post("/tags/create_tag", params);
        if (response.status == 201)
            return response.data.TagID;
        else return -1;
    }
    catch (error) {
        console.log(error);
        return -1;
    }
}

export const updateTag = async (TagID: number, SID: number, type: number) => {
    try {
        const params = new URLSearchParams();
        params.append('TagID', TagID.toString());
        params.append('ScheduleID', SID.toString());
        const response = await axiosInstance.post(type == 1 ? '/tags/remove_tag_from_schedule' : "/tags/add_tag_to_schedule", params);
        if (response.status == 204)
            return true;
        else return false;
    }
    catch (error) {
        console.log(error);
        return false;
    }
}

export const CreateScheduleFlip = async (data: ScheduleItem) => {
    const params = new URLSearchParams();
    params.append('Title', data.Title);
    params.append('Body', data.Body);
    params.append('StartTime', Math.floor(data.StartTime.getTime() / 1000).toString());
    if (data.FinishTime.getTime() != 0) params.append('FinishTime', Math.floor(data.FinishTime.getTime() / 1000).toString());
    params.append('Type', data.Type.toString());
    params.append('Location', data.Location);
    params.append('Stars', data.Stars.toString());
    params.append('Self', 'False');
    try {
        const response = await axiosInstance.post("/schedule", params);
        //console.log(response)
        if (response.status != 201) return -1
        else return response.data.ScheduleID;
    }
    catch (error) {
        console.log(error);
        return -1
    }
}



export const postMessage = async (OriginGroup: number, TargetGroup: number[], PostMethod: number[], Title: string, Sender: string, Body: string, Tag: string, Stars: number, Schedules: number[], ImageSourceList: any[]) => {
    let ImageURL = ''
    const promises = ImageSourceList.map(imageSource => PostImage(imageSource));
    try {
        const results = await Promise.all(promises);
        results.forEach((item) => { ImageURL += item + ';' })
    } catch (error) {
        return false
    }

    const params = new URLSearchParams();
    params.append('Images', ImageURL)
    params.append('OriginGroup', OriginGroup.toString())
    params.append('Title', Title);
    params.append('Body', Body);
    params.append('Sender', Sender);
    params.append('Type', '1');
    params.append('Stars', Stars.toString());

    Schedules.forEach((item) => {
        params.append('Schedules', item.toString());
    })

    const list = Tag.split(',');
    params.append('Tags', JSON.stringify(list));

    if (PostMethod.find((item) => item == 1))
        TargetGroup.forEach((item) => {
            params.append('ToGroupBoardCast', item.toString());
        })
    if (PostMethod.find((item) => item == 2))
        TargetGroup.forEach((item) => {
            params.append('ToGroupThrough', item.toString());
        })
    if (PostMethod.find((item) => item == 1) == undefined && PostMethod.find((item) => item == 2) == undefined)
        TargetGroup.forEach((item) => {
            params.append('ToGroupSingle', item.toString());
        })


    try {
        const response = await axiosInstance.post("/message", params);
        if (response.status == 201) return true
        else return false
    }
    catch (error) {
        console.log(error);
        return false
    }
}

export const createGroup = async (GroupName: string) => {
    try {
        const params = new URLSearchParams();
        params.append('GroupName', GroupName);
        const response = await axiosInstance.post("/group/create_group", params);
        if (response.status == 202)
            return true
        else return false;
    }
    catch (error) {
        console.log(error);
        return false;
    }
}

export const deleteTag = async (TagID: number) => {
    try {
        const response = await axiosInstance.delete("/tags/delete_tag", { params: { TagID: TagID } });
        if (response.status == 204)
            return true
        else return false;
    }
    catch (error) {
        console.log(error);
        return false;
    }
}

export const bindToken = async (WelinkUID: string, UserName: string, PassWord: string) => {
    try {
        const params = new URLSearchParams();
        params.append('WeLinkUID', WelinkUID);
        params.append('username', UserName);
        params.append('password', PassWord);
        const response = await axiosInstance.post("/WeLinkBind", params);
        if (response.status == 200)
        {
            console.log(response.data);
            return response.data.access_token;
        }
        else if (response.status == 204)
            return 'bindtwice';
        else return 'failed';
    }
    catch (error) {
        console.log(error);
        return 'failed';
    }
}
