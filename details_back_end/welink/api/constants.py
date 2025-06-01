#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
定义宏变量
Create on 2020-02-29
@auuthor wecode@huawei.com
"""

# 支持的URL协议清单
PROTOCOLS = ("https", "http")

# 通用的请求头
REQUEST_HEADERS = {
    "Accept-Charset": "UTF-8",
    "Content-Type": "application/json",
}

# 支持的REST方法清单
REST_METHODS = ("GET", "POST", "PUT", "DELETE")

# access_token在消息头中的KEY
TOKEN_KEY_IN_HEADER = "x-wlk-Authorization"

# 返回信息中的关键字
RES_CODE_KEY = "code"
RES_MSG_KEY = "message"
RES_APP_HOST_KEY = "Application-Host"
RES_SERVICE_HOST_KEY = "Location-Host"

# 用户性别属性清单(男，女)
SEX_LIST = ("M", "F")
SEX_TRANS = ("male", "female")

# 用户是否开户属性清单(是，否)
IS_OPEN_ACCOUNT_LIST = ("1", "0")
IS_OPEN_ACCOUNT_TRANS = ("yes", "no")

# 是否有效属性清单(是，否)
IS_VALID_LIST = ("1", "0")
IS_VALID_TRANS = ("yes", "no")

# 是否隐藏手机号码属性清单(是，否)
IS_HIDE_MOBILE_NUMBER_LIST = ("1", "0")
IS_HIDE_MOBILE_NUMBER_TRANS = ("yes", "no")

# 人员在部门内排序界限
MIN_ORDER_IN_DEPT = 1
MAX_ORDER_IN_DEPT = 9999

# 部门排序界限
MIN_DEPT_ORDER = 1
MAX_DEPT_ORDER = 999

# 是否递归查询部门信息(是，否)
RECURSIVE_FLAG_LIST = ("1", "0")
RECURSIVE_FLAG_TRANS = ("yes", "no")

# 查询子部门当前页字段取值界限
MIN_OFFSET = 1

# 部门人员列表单页数据量取值界限
MIN_PAGE_SIZE = 1
MAX_PAGE_SIZE = 50

# 单次查询子部门数据量取值界限
MIN_LIMIT = 1
MAX_LIMIT = 100

# 部门visibleRange属性清单
VISIBLE_RANGE_LIST = ("1", "2", "3")
VISIBLE_RANGE_TRANS = ("全部可见", "尽自己可见", "当前部门和子部门可见")

# 部门级别界限
MIN_DEPT_LEVEL = 1

# 单次查询用户userId数据量界限
MAX_USER_ID_RECORDS_COUNT = 50

# 单次同步用户数据量界限
MAX_USERS_SYNC_COUNT = 10

# 单次同步部门数据量界限
MAX_DEPTS_SYNC_COUNT = 10

# 公众号消息推送用户数界限
MAX_USER_NUMBER_TO_BE_PUSHED_MSG = 1000

# 考勤打卡记录查询用户数量界限
MAX_USER_NUMBER_TO_QUERY_ATTENDANCE_RECORDS = 50

# 查询的考勤打卡数据量界限
MAX_ATTENDANCE_RECORDS_LIMIT = 100
MIN_ATTENDANCE_RECORDS_LIMIT = 1

# 查询考勤打卡记录的时间跨度界限(SECONDS)
MAX_INTERVAL_BETWEEN_START_AND_END_WORKDAYS = 24 * 60 * 60

# 公众号消息同步类型清单
MSG_RANGE_LIST = (0,)
MSG_RANGE_TRANS = ("push by user",)

# 公众号消息字节长度限制
MAX_LENGTH_OF_MSG_TITLE = 128

# 公众号消息正文字节长度限制
MAX_LENGTH_OFMSG_CONTENT = 512

# 公众号消息显示配置清单
MSG_DISPLAY_MODE_LIST = (0, 1)
MSG_DISPLAY_MODE_TRANS = ("支持手机链接和PC链接", "仅移动端显示")

# cmd特殊字符清单
CMD_SPECIAL_CHAR_LIST = ("^", "<", ">", "|", "&")

# 文章自定义来源正则表达式
SOURCE_NAME_RE = r"[\dA-Za-z_]+"

# 文章自定义来源最大长度
MAX_SOURCE_NAME_LENGTH = 50

# 文章来源ID最大长度
MAX_SOURCE_ID_LENGTH = 50

# 文章来源id正则表达式
SOURCE_ID_RE = r"[\dA-Za-z_]+"

# 文章类型清单
ARTICLE_CONTENT_TYPE_LIST = (0, 1)
ARTICLE_CONTENT_TYPE_TRANS = ("链接型", "内容型")

# 文章模块清单
ARTICLE_MODULE_TYPE_LIST = ("bulletins",)
ARTICLE_MODULE_TYPE_TRANS = ("信息发布文章",)

# 文章语言清单
ARTICLE_LANG_LIST = (0, 1)
ARTICLE_LANG_TRANS = ("中文", "英文")

# 文章是否推荐标记清单
IS_RECOMMENDED_LIST = (0, 1)
IS_RECOMMENDED_TRANS = ("否", "是")

# 文章是否置顶标记清单
IS_TOPPED_LIST = (0, 1)
IS_TOPPED_TRANS = ("否", "是")

# 文章条目模板清单
REC_DATA_STYLE_LIST = (1, 2, 3, 4, 5, 6, 7, 8, 9)
REC_DATA_STYLE_TRANS = (
    "左文右图",
    "大图卡",
    "视频（大）",
    "视频（小）",
    "直播",
    "音频",
    "博客",
    "问答",
    "文档式",
)

# 会议角色清单
ROLE_LIST = (0, 1, 2)
ROLE_TRANS = ("普通与会者", "会议主席", "单向会场")

# 与会者名称长度界限
MAX_NAME_LENGTH = 96

# 会议角色号码长度界限
MAX_PHONE_LENGTH = 127

# 邮箱地址长度界限
MAX_EMAIL_LENGTH = 255

# 短信通知的手机号码长度界限
MAX_SMS_NUMBER_LENGTH = 32

# 会议开始时是否自动邀请与会者标记清单
IS_AUTO_INVITE_LIST = (0, 1)
IS_AUTO_INVITE_TRANS = ("不自动邀请", "自动邀请")

# 会议角色类型清单
CONFERENCE_USER_TYPE_LIST = (
    "normal",
    "telepresence",
    "terminal",
    "outside",
    "anonymous",
    "mobile",
    "telephone",
)
CONFERENCE_USER_TYPE_TRANS = (
    "语音、高清、标清与会者地址（默认），软终端用户",
    "智真与会者地址类型，单屏、三屏智真均属此类(三屏智真为预留字段)",
    "会议室或硬终端",
    "外部与会人",
    "匿名入会",
    "软终端用户手机",
    "软终端用户固定电话，暂不使用",
)

# 组织名称长度界限
MAX_DEPT_NAME_LENGTH = 128

# 时区映射关系取值范围
TIME_ZONE_LIST = range(1, 78)

# 会议类型清单
CONFERENCE_TYPE_LIST = (0, 1)
CONFERENCE_TYPE_TRANS = ("普通会议", "周期会议")

# 会议时长取值界限
MIN_CONFERENCE_LENGTH = 15
MAX_CONFERENCE_LENGTH = 1440

# 会议主题长度限制
MAX_CONFERENCE_SUBJECT_LENGTH = 128

# 会议临时群组ID长度界限
MAX_CONFERENCE_GROUP_ID_LENGTH = 31

# 会议的媒体类型清单
CONFERENCE_MEDIA_TYPE_LIST = (
    "Voice",
    "Video",
    "HDVideo",
    "Telepresence",
    "Data",
)
CONFERENCE_MEDIA_TYPE_TRANS = (
    "语音",
    "标清视频",
    "高清视频（与Video互斥，如果同时选择Video、HDVideo，则系统默认选择Video）",
    "智真(与HDVideo、Video互斥，如果同时选择，系统使用Telepresence)。（预留字段）",
    "多媒体（AS会根据系统配置决定是否自动添加Data）",
)

# 是否自动启动录制标记清单
IS_AUTO_RECORD_LIST = (0, 1)
IS_AUTO_RECORD_TRANS = ("不自动启动录制", "自动启动录制")

# 会议媒体加密模式
ENCRYPT_MODE_LIST = (0, 1, 2)
ENCRYPT_MODE_TRANS = ("自适应加密", "强制加密", "不加密")

# 会议语言类型清单
CONFERENCE_LANGUAGE_LIST = ("zh-CN", "en-US")
CONFERENCE_LANGUAGE_TRANS = ("简体中文", "美国英文")

# 会议录播类型
RECORD_TYPE_LIST = (0, 1, 2, 3)
RECORD_TYPE_TRANS = ("禁用", "直播", "录播", "直播+录播")

# 是否录制辅流标记清单
RECORD_AUX_STREAM_LIST = (0, 1)
RECORD_AUX_STREAM_TRANS = ("否", "是")

# 是否使用VMR召开预约会议标记清单
VMR_FLAG_LIST = (0, 1)
VMR_FLAG_TRANS = ("不使用VMR", "使用VMR")

# 主流直播地址长度限制
MAX_LIVE_ADDRESS_LENGTH = 255

# 辅流直播地址长度限制
MAX_AUX_ADDRESS_LENGTH = 255

# 来宾是否免密标记清单
IS_GUEST_FREE_PWD_LIST = (True, False)
IS_GUEST_FREE_PWD_TRANS = ("免密", "不免密")

# 是否需要发送会议邮件通知标记清单。
IS_SEND_NOTIFY_LIST = (True, False)
IS_SEND_NOTIFY_TRANS = ("需要", "不需要")

# 是否需要发送会议通知标记清单。
IS_SEND_SMS_LIST = (True, False)
IS_SEND_SMS_TRANS = ("需要", "不需要")

# 会议列表单页数据量界限
MAX_CONFERENCE_LIST_LENGTH = 500

# 查询会议列表的状态过滤参数清单
CONFERENCE_LIST_STATUS_LIST = (0, 1, 2)
CONFERENCE_LIST_STATUS_TRANS = ("查询待召开的和已召开的（默认）", "查询待召开的", "查询正在召开的")

# 会议关键字长度限制
MAX_CONFERENCE_CONDITION_LENGTH = 128

# 查询会议列表的时间段过滤参数清单
CONFERENCE_LIST_CONF_MODE_LIST = ("ADAY", "AWEEK", "AMONTH", "ALL")
CONFERENCE_LIST_CONF_MODE_TRANS = ("一天", "一周", "一个月", "查询所有")

# 查询会议列表的排序参数清单
CONFERENCE_LIST_SORT_LIST = (
    "ASC_StartTIME",
    "DSC_StartTIME",
    "ASC_RecordTYPE",
    "DSC_RecordTYPE",
)
CONFERENCE_LIST_SORT_TRANS = (
    "按会议开始时间升序排序",
    "按会议开始时间降序排序",
    "按会议是否有录播文件排序，之后默认按照会议开始时间升序排序",
    "按会议是否有录播文件排序，之后默认按照会议开始时间降序排序",
)

# 会议详情查询类型清单
CONFERENCE_INFO_TYPE_LIST = (0, 1, 2)
CONFERENCE_INFO_TYPE_TRANS = (
    "不区分终端和与会人。",
    "分页查询区分终端和与会人，结果合并返回。",
    "单独查询终端和与会人，结果单独返回。",
)

# 会议详情查询子类型清单(当“type”为“2”时，该字段有效。)
CONFERENCE_INFO_QUERY_TYPE_LIST = (0, 1)
CONFERENCE_INFO_QUERY_TYPE_TRANS = ("查询与会人。", "查询终端。")
