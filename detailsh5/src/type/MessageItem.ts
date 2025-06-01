import ScheduleItem from "@/type/ScheduleItem";

// Message类型，承载Type 1,2 的消息
interface MessageItem {
    MessageID: number;
    SendTime:Date;
    Sender:string;
    Title: string;
    Body: string;
    Schedules:ScheduleItem[];
    Type: number;
    Stars: number;
    HaveRead:boolean;
    Tags:string[];
    Images: string;
    OriginGroupName:string;
    OriginGroupID:number;
    // Receiver: string;
    // Receive_self:boolean;
}

export interface GroupSelectItem{
    title: string;
    value: number;
}

export default MessageItem;