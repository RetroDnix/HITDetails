// 这个库是为了进行时间的格式化显示

export const parseTime = (TimeString: string) => {
    // 将形如 yy/mm/dd hh:mm 的字符串转换为 Date 
    if (TimeString == undefined) return new Date(0)
    //console.log(TimeString)
    const TimeS = TimeString.split(' ')
    if (TimeS[0] == undefined) return new Date(0)
    if (TimeS[1] == undefined) return new Date(0)
    const DateArray = TimeS[0].split('/')
    let TimeArray
    if (TimeS[1].toString().indexOf('：') == -1)
        TimeArray = TimeS[1].split(':')
    else TimeArray = TimeS[1].split('：')
    const result = new Date()
    result.setHours(0, 0, 0, 0)
    const YY = parseInt(DateArray[0]), MM = parseInt(DateArray[1]), DD = parseInt(DateArray[2]), hh = parseInt(TimeArray[0]), mm = parseInt(TimeArray[1])
    if (!Number.isNaN(YY)) result.setFullYear(YY < 2000 ? YY + 2000 : YY)
    if (!Number.isNaN(MM)) result.setMonth(MM - 1)
    if (!Number.isNaN(DD)) result.setDate(DD)
    if (!Number.isNaN(hh)) result.setHours(hh)
    if (!Number.isNaN(mm)) result.setMinutes(mm)
    return result
}


export const hintDateChinese = (timestamp: number) => {
	if (timestamp == 0) return ''
	const date = new Date(timestamp)
	return `${date.getFullYear()}年${date.getMonth() + 1}月${date.getDate()}日 (${WeekDay[date.getDay()]})`
}

export const toDateChinese = (date: Date) => {
	return `${date.getMonth() + 1}月${date.getDate()}日`
}

export const toDateChineseSlim = (date: Date) => {
	return `${date.getFullYear()%2000}/${date.getMonth() + 1}/${date.getDate()}`
}

export const toDateTimeChinese = (date: Date,datef?: Date) => {
    //格式化Date对象为"YYYY年MM月DD日 HH:MM"的字符串
    const hours1 = date.getHours().toString().padStart(2, '0'); // 填充小时
    const minutes1 = date.getMinutes().toString().padStart(2, '0'); // 填充分钟
    if(datef!=undefined){
        // 判断两个date是否是同一天
        const hours2 = datef.getHours().toString().padStart(2, '0');
        const minutes2 = datef.getMinutes().toString().padStart(2, '0');
        if(date.getDate()==datef.getDate()&&date.getMonth()==datef.getMonth()&&date.getFullYear()==datef.getFullYear())
            return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + "日 " + hours1 + ":" + minutes1 + ' - ' + hours2 + ":" + minutes2
        else
        {
            // 判断两个date相差的天数
            const days = Math.floor((datef.getTime()-date.getTime())/(24*3600*1000))
            return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + "日 " + hours1 + ":" + minutes1 + ' - (+' + days + ')' + hours2 + ":" + minutes2
        }
    }
    else return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + "日 " + hours1 + ":" + minutes1
}


export const toDateTimeChineseSlim = (date: Date,datef?: Date) => {
    //格式化Date对象为"YYYY年MM月DD日 HH:MM"的字符串
    const hours1 = date.getHours().toString().padStart(2, '0'); // 填充小时
    const minutes1 = date.getMinutes().toString().padStart(2, '0'); // 填充分钟
    if(datef!=undefined){
        // 判断两个date是否是同一天
        const hours2 = datef.getHours().toString().padStart(2, '0');
        const minutes2 = datef.getMinutes().toString().padStart(2, '0');
        if(date.getDate()==datef.getDate()&&date.getMonth()==datef.getMonth()&&date.getFullYear()==datef.getFullYear())
        return date.getFullYear()%2000 + "/" + (date.getMonth() + 1) + "/" + date.getDate() + "/ " + hours1 + ":" + minutes1 + ' - ' + hours2 + ":" + minutes2
    else
    {
        // 判断两个date相差的天数
        const days = Math.floor((datef.getTime()-date.getTime())/(24*3600*1000))
        return date.getFullYear()%2000 + "/" + (date.getMonth() + 1) + "/" + date.getDate() + "/ " + hours1 + ":" + minutes1 + ' - (+' + days + ')' + hours2 + ":" + minutes2
    }
}
else return date.getFullYear()%2000 + "/" + (date.getMonth() + 1) + "/" + date.getDate() + "/ " + hours1 + ":" + minutes1
}

const WeekDay = ['星期日','星期一','星期二','星期三','星期四','星期五','星期六']
export const toDateTimeChineseWeekDay = (date: Date,datef?: Date) => {
    //格式化Date对象为"YYYY年MM月DD日 HH:MM"的字符串
    const hours1 = date.getHours().toString().padStart(2, '0'); // 填充小时
    const minutes1 = date.getMinutes().toString().padStart(2, '0'); // 填充分钟
    if(datef!=undefined){
        // 判断两个date是否是同一天
        const hours2 = datef.getHours().toString().padStart(2, '0');
        const minutes2 = datef.getMinutes().toString().padStart(2, '0');
        if(date.getDate()==datef.getDate()&&date.getMonth()==datef.getMonth()&&date.getFullYear()==datef.getFullYear())
        return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + "日 " + hours1 + ":" + minutes1 + ' - ' + hours2 + ":" + minutes2 + ' (' + WeekDay[date.getDay()] + ')'
        else
        {
            // 判断两个date相差的天数
            const days = Math.floor((datef.getTime()-date.getTime())/(24*3600*1000))
            return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + "日 " + hours1 + ":" + minutes1 + ' - (+' + days + ')' + hours2 + ":" + minutes2 + ' (' + WeekDay[date.getDay()] + ')'
        }
    }
    else return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + "日 " + hours1 + ":" + minutes1 + ' (' + WeekDay[date.getDay()] + ')'
}