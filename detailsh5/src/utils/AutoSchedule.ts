import OpenAI from "openai";
import { zodTextFormat } from "openai/helpers/zod";
import { z } from "zod";

const openai = new OpenAI({
  apiKey: "<OPENAI_API_KEY>",
  baseURL: "<OPENAI_API_BASE_URL>",
  dangerouslyAllowBrowser: true
});

const Schedule = z.object({
    ScheTitle: z.string(),
    ScheLocation: z.string(),
    ScheisDDL: z.boolean(),
    ScheStartTime: z.string(),
    ScheFinishTime: z.string(),
    ScheBody: z.string(),
});

const ScheduleList = z.array(Schedule);

export const getAppendix = async (notice: string) => {
    const response = await openai.chat.completions.create({
        model: "gpt-4.1",
        messages: [
            { role: "system", content: "从以下通知中提取其包含的日程为一个Json对象，通知可能包含多个日程，此时你应该返回一个Json对象列表。你应该始终仅返回一个纯json字符串，不包括“```”等markdown格式符。对于键的解释为：\nScheTitle：日程标题\nScheLocation：日程地点\nScheisDDL：日程是否只有一个截止时间（否则日程有开始和结束时间）\nScheStartTime：如果ScheisDDL=true，这项为日程的截止时间；否则，这项为日程的开始时间\nScheFinishTime：如果ScheisDDL=true，这项无意义（设置为20/01/01 00:00）；否则，这项为日程的结束时间\nScheBody：日程的正文（介绍）\n时间的统一格式为：yy/mm/dd hh:mm" },
            {
            role: "user",
            content: notice,
            },
        ],
    });
    return response.choices[0].message.content;
}