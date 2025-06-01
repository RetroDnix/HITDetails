import ScheduleItem from "@/type/ScheduleItem";

export const getItemTime = (item:ScheduleItem) => {
    return item.StartTime.getTime()
}

const upperBound = (arr:Array<ScheduleItem>, target:number) => {
    let l = 0, r = arr.length;
    while (l < r) {
        const mid = Math.floor((l + r) / 2);
        const midValue = getItemTime(arr[mid]);
        if (midValue < target) 
            l = mid + 1;
        else
            r = mid;
    }
    return l;
}

export default upperBound;