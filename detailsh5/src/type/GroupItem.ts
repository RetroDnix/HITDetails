interface GroupItem{
    GroupID: number;
    GroupName: string;
    Type: number;
    IsMember: boolean;
    Admin: number;
}

export interface DetailedGroupItem{
    GroupID: number;
    GroupName: string;
    Type: number;
    Admin: number;
    IsMember: boolean;
    Members: any[];
    Admins: any[];
    FatherGroup: GroupItem[];
}

export default GroupItem;