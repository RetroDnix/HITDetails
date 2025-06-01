#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
预约会议
https://open.welink.huaweicloud.com/docs/#/990hh0/ka0vzc/i2vnm3?type=internal
@author: wecode@huawei.com
"""
import copy

from welink.api.base import RestApi
from welink.api.conference import Conference


class MeetingV1CreateconferenceRequest(RestApi):
    """预约会议"""

    def __init__(self, url):
        super(MeetingV1CreateconferenceRequest, self).__init__(url)
        self.__body_params = Conference()
        self.__rest_method = "POST"
        self.__valid_path = ("/api/meeting/v1/createconference",)
        self.__params = super(
            MeetingV1CreateconferenceRequest, self
        ).get_params()
        self.__user_id_key = "userId"
        self.__unnull_keys = (self.__user_id_key,)

    @property
    def body(self):
        return self.__body_params

    @property
    def user_id(self):
        """
        用户帐号，如zhangsan@xxx
        """
        return self.__params.get(self.__user_id_key)

    @user_id.setter
    def user_id(self, value):
        self.__params[self.__user_id_key] = str(value)

    @property
    def conference_type(self):
        """
        0 : 普通会议（默认）；
        1 : 周期会议，此时cycleParams必须填写。
        """
        return self.__body_params.conference_type

    @conference_type.setter
    def conference_type(self, value):
        self.__body_params.conference_type = value

    @conference_type.deleter
    def conference_type(self):
        del self.__body_params.conference_type

    @property
    def start_time(self):
        """
会议开始时间。采用UTC时间。会议本地的开始时间要通过startTime和timeZoneID计算得到。\
比如startTime为UTC 2020-03-20 02:00, timeZoneID为56，对应东八区，\
则本地会议开始时间为东八区的2020-03-20 10:00。\
预定创建会议时，如果没有指定开始时间，或填空串，则表示会议马上开始。\
格式：YYYY-MM-DD HH:MM
        """
        return self.__body_params.start_time

    @start_time.setter
    def start_time(self, value):
        self.__body_params.start_time = value

    @start_time.deleter
    def start_time(self):
        del self.__body_params.start_time

    @property
    def length(self):
        """会议持续时长。单位分钟，最长1440，最短15，默认为30。"""
        return self.__body_params.length

    @length.setter
    def length(self, value):
        self.__body_params.length = value

    @length.deleter
    def length(self):
        del self.__body_params.length

    @property
    def subject(self):
        """会议主题。长度限制为128个字符。"""
        return self.__body_params.subject

    @subject.setter
    def subject(self, value):
        self.__body_params.subject = value

    @subject.deleter
    def subject(self):
        del self.__body_params.subject

    @property
    def media_types(self):
        """
会议的媒体类型。由1个或多个枚举String组成，多个枚举时，每个枚举值之间通过”,”逗号分隔，\
枚举值如下：
“Voice”：语音
“Video”：标清视频
“HDVideo”：高清视频（与Video互斥，如果同时选择Video、HDVideo，则系统默认选择Video）
“Telepresence”：智真\
(与HDVideo、Video互斥，如果同时选择，系统使用Telepresence)。（预留字段）
“Data”：多媒体（AS会根据系统配置决定是否自动添加Data）
        """
        return self.__body_params.media_types

    @media_types.setter
    def media_types(self, value):
        self.__body_params.media_types = value

    @property
    def is_auto_record(self):
        """
会议是否自动启动录制，在录播类型为:录播、直播+录播时有效。1 :true：自动启动录制；0 :false：不自动启动录制。（默认）
        """
        return self.__body_params.is_auto_record

    @is_auto_record.setter
    def is_auto_record(self, value):
        self.__body_params.is_auto_record = value

    @is_auto_record.deleter
    def is_auto_record(self):
        del self.__body_params.is_auto_record

    @property
    def encrypt_mode(self):
        """
        会议媒体加密模式。0 : auto：自适应加密；1 : must：强制加密；2 : 不出现：不加密
        """
        return self.__body_params.encrypt_mode

    @encrypt_mode.setter
    def encrypt_mode(self, value):
        self.__body_params.encrypt_mode = value

    @encrypt_mode.deleter
    def encrypt_mode(self):
        del self.__body_params.encrypt_mode

    @property
    def language(self):
        """
会议的默认语言，默认值由会议AS定义，MediaX是“zh-CN”，对于系统支持的语言，按照RFC3066规范传递。zh-CN：简体中文；en-US：美国英文
        """
        return self.__body_params.language

    @language.setter
    def language(self, value):
        self.__body_params.language = value

    @language.deleter
    def language(self):
        del self.__body_params.language

    @property
    def time_zone_i_d(self):
        """
        开始时间的时区信息。时区信息参考时区映射关系
        """
        return self.__body_params.time_zone_id

    @time_zone_i_d.setter
    def time_zone_i_d(self, value):
        self.__body_params.time_zone_id = value

    @time_zone_i_d.deleter
    def time_zone_i_d(self):
        del self.__body_params.time_zone_id

    @property
    def record_type(self):
        """录播类型。0: 禁用；1: 直播；2: 录播；3: 直播+录播"""
        return self.__body_params.record_type

    @record_type.setter
    def record_type(self, value):
        self.__body_params.record_type = value

    @record_type.deleter
    def record_type(self):
        del self.__body_params.record_type

    @property
    def live_address(self):
        """
        主流直播地址。最大不超过255个字符。在录播类型为 :直播、直播+录播时有效。
        """
        return self.__body_params.live_address

    @live_address.setter
    def live_address(self, value):
        self.__body_params.live_address = value

    @live_address.deleter
    def live_address(self):
        del self.__body_params.live_address

    @property
    def aux_address(self):
        """
        辅流直播地址。最大不超过255个字符。在录播类型为: 直播、直播+录播时有效。
        """
        return self.aux_address

    @aux_address.setter
    def aux_address(self, value):
        self.__body_params.aux_address = value

    @aux_address.deleter
    def aux_address(self):
        del self.__body_params.aux_address

    @property
    def record_aux_stream(self):
        """
        是否录制辅流。在录播类型为:录播、直播+录播时有效。0：否；1：是
        """
        return self.__body_params.record_aux_stream

    @record_aux_stream.setter
    def record_aux_stream(self, value):
        self.__body_params.record_aux_stream = value

    @record_aux_stream.deleter
    def record_aux_stream(self):
        del self.__body_params.record_aux_stream

    @property
    def conf_config_info(self):
        """
        会议其他配置信息，用于其他会议配置参数。后续新增的会议配置参数都在该结构中定义。
        """
        return self.__body_params.conf_config_info

    @conf_config_info.setter
    def conf_config_info(self, value):
        self.__body_params.conf_config_info = value

    @property
    def vmr_flag(self):
        """是否使用VMR召开预约会议。0：不使用VMR；1：使用VMR"""
        return self.__body_params.vmr_flag

    @vmr_flag.setter
    def vmr_flag(self, value):
        self.__body_params.vmr_flag = value

    @vmr_flag.deleter
    def vmr_flag(self):
        del self.__body_params.vmr_flag

    @property
    def vmr_i_d(self):
        """
用于识别用户开会时绑定的VMR会议室。不为空，则用ID查询VMR信息；为空，则查用户所有VMR，如果有个人VMR，用个人；没有，取最小VMRID
        """
        return self.__body_params.vmr_id

    @vmr_i_d.setter
    def vmr_i_d(self, value):
        self.__body_params.vmr_id = value

    @vmr_i_d.deleter
    def vmr_i_d(self):
        del self.__body_params.vmr_id

    @property
    def attendees(self):
        """
预定会议时，指定的与会者列表。该与会者列表可以用于发送会议通知、会议提醒、会议开始时候进行自动邀请。请参考RestAttendeeDTO。
        """
        return self.__body_params.attendees.item_class_obj

    def get_attendees_by_index(self, index):
        """
        根据索引获取指定位置的与会者信息
        :param index: int 索引
        :return: dict 获取到的与会者信息
        """
        return self.__body_params.attendees.get_param_by_index(index)

    def add_attendees(self, value):
        """
        在请求实例中添加新的与会者信息对象
        :param value: RestAttendeeDTO 需要添加的新的与会者信息对象
        """
        self.__body_params.attendees.add_param(value)

    def set_attendees(self, attendee, index):
        """
        根据索引修改指定位置的与会者信息对象
        :param attendee: RestAttendeeDTO 需要修改的新的与会者信息
        :param index: int 索引
        """
        self.__body_params.attendees.set_param_by_index(attendee, index)

    def del_attendees(self, index):
        """
        根据索引删除指定位置的与会者信息
        :param index: int 索引
        """
        self.__body_params.attendees.del_param_by_index(index)

    def get_body_params(self):
        return self.__body_params.get_data()

    def get_rest_method(self):
        return self.__rest_method

    def check_bodies(self):
        self.__body_params.unnull_check()

    def get_valid_path(self):
        return self.__valid_path

    def get_params(self):
        return copy.deepcopy(self.__params)

    def get_unnull_keys(self):
        return self.__unnull_keys
