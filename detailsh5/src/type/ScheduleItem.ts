// Schedule类型，承载Type 3,4的消息
interface ScheduleItem {
    ScheduleID: number;
    Title: string;
    Body: string;
    Location: string;
    Type: number;
    StartTime: Date;
    FinishTime: Date;
    Stars: number;
    Created: boolean;
    Tags: TagItem[];
}

export interface TagItem{
    title: string;
    value: number;
}

export default ScheduleItem;