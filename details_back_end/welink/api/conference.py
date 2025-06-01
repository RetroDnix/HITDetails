#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
会议基本信息模块
Create on 2020-04-09
@author wecode@huawei.com
"""
import copy

from welink.api import constants, exceptions, utils
from welink.api.base import ParametersList


class RestAttendeeDTO(object):
    """
预定会议时，指定的与会者列表。该与会者列表可以用于发送会议通知、会议提醒、会议开始时候进行自动邀请。
    """

    def __init__(self):
        self.__account_id_key = "accountId"
        self.__name_key = "name"
        self.__role_key = "role"
        self.__phone_key = "phone"
        self.__phone2_key = "phone2"
        self.__phone3_key = "phone3"
        self.__email_key = "email"
        self.__sms_key = "sms"
        self.__is_auto_invite_key = "isAutoInvite"
        self.__type_key = "type"
        self.__address_key = "address"
        self.__dept_name_key = "deptName"
        self.__data = dict()
        self.__valid_check_map = {
            self.__role_key: (constants.ROLE_LIST, constants.ROLE_TRANS),
            self.__is_auto_invite_key: (
                constants.IS_AUTO_INVITE_LIST,
                constants.IS_AUTO_INVITE_TRANS,
            ),
            self.__type_key: (
                constants.CONFERENCE_USER_TYPE_LIST,
                constants.CONFERENCE_USER_TYPE_TRANS,
            ),
        }

    def valid_check(self, key, value):
        """
        参数有效性检查
        :param key: string 需要检查的字段名称
        :param value: 需要检查的字段参数值
        """
        pass

    @property
    def account_id(self):
        """
        与会者账号，即用户的userId
        """
        return self.__data.get(self.__phone_key)

    @account_id.setter
    def account_id(self, value):
        self.__data[self.__account_id_key] = str(value)

    @account_id.deleter
    def account_id(self):
        if self.__account_id_key in self.__data:
            del self.__data[self.__account_id_key]

    @property
    def name(self):
        """
        与会者名称或昵称，长度限制为96个字符。
        """
        return self.__data.get(self.__name_key)

    @name.setter
    def name(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_NAME_LENGTH, value, self.__name_key
        )
        self.__data[self.__name_key] = value

    @name.deleter
    def name(self):
        if self.__name_key in self.__data:
            del self.__data[self.__name_key]

    @property
    def role(self):
        """
        会议中的角色。1：会议主席；0：普通与会者（默认）；2：单向会场（预留字段）
        """
        return self.__data[self.__role_key]

    @role.setter
    def role(self, value):
        value = utils.integer_check(
            value, self.__role_key, class_name=self.__class__.__name__
        )
        self.valid_check(self.__role_key, value)
        self.__data[self.__role_key] = value

    @role.deleter
    def role(self):
        if self.__role_key in self.__data:
            del self.__data[self.__role_key]

    @property
    def phone(self):
        """
号码（可支持SIP、TEL号码格式）。\
最大不超过127个字符。当type为telepresence时，且设备为三屏智真，则该字段填写中屏号码。（三屏智真为预留字段）
        """
        return self.__data.get(self.__phone_key)

    @phone.setter
    def phone(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_PHONE_LENGTH, value, self.__phone_key
        )
        self.__data[self.__phone_key] = value

    @property
    def phone2(self):
        """
取值类型同phone。当type为telepresence时，且设备为三屏智真，则该字段填写左屏号码。（三屏智真为预留字段）
        """
        return self.__data.get(self.__phone2_key)

    @phone2.setter
    def phone2(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_PHONE_LENGTH, value, self.__phone2_key
        )

    @phone2.deleter
    def phone2(self):
        if self.__phone2_key in self.__data:
            del self.__data[self.__phone2_key]

    @property
    def phone3(self):
        """
取值类型同phone。当type为telepresence时，且设备为三屏智真，则该字段填写右屏号码。（三屏智真为预留字段）
        """
        return self.__data.get(self.__phone3_key)

    @phone3.setter
    def phone3(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_PHONE_LENGTH, value, self.__phone3_key
        )
        self.__data[self.__phone3_key] = value

    @phone3.deleter
    def phone3(self):
        if self.__phone3_key in self.__data:
            del self.__data[self.__phone3_key]

    @property
    def email(self):
        """
        邮件地址。最大不超过255个字符。
        """
        return self.__data.get(self.__email_key)

    @email.setter
    def email(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_EMAIL_LENGTH, value, self.__email_key
        )
        self.__data[self.__email_key] = value

    @email.deleter
    def email(self):
        if self.__email_key in self.__data:
            del self.__data[self.__email_key]

    @property
    def sms(self):
        """
        短信通知的手机号码。最大不超过32个字符。
        """
        return self.__data.get(self.__sms_key)

    @sms.setter
    def sms(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_SMS_NUMBER_LENGTH, value, self.__sms_key
        )
        self.__data[self.__sms_key] = value

    @sms.deleter
    def sms(self):
        if self.__sms_key in self.__data:
            del self.__data[self.__sms_key]

    @property
    def is_auto_invite(self):
        """
        会议开始时是否自动邀请该与会者。0：不自动邀请；1：自动邀请（默认）
        """
        return self.__data.get(self.__is_auto_invite_key)

    @is_auto_invite.setter
    def is_auto_invite(self, value):
        value = utils.integer_check(
            value,
            self.__is_auto_invite_key,
            class_name=self.__class__.__name__,
        )
        self.valid_check(self.__is_auto_invite_key, value)
        self.__data[self.__is_auto_invite_key] = value

    @is_auto_invite.deleter
    def is_auto_invite(self):
        if self.__is_auto_invite_key in self.__data:
            del self.__data[self.__is_auto_invite_key]

    @property
    def type(self):
        """
默认值由会议AS定义，号码类型枚举值如下：
“normal”：语音、高清、标清与会者地址（默认），软终端用户。
“telepresence”：智真与会者地址类型，单屏、三屏智真均属此类。（三屏智真为预留字段）
“terminal”：会议室或硬终端。
“outside”：外部与会人。
“anonymous”：匿名入会。
“mobile”：软终端用户手机。
“telephone”：软终端用户固定电话，暂不使用。
        """
        return self.__data.get(self.__type_key)

    @type.setter
    def type(self, value):
        value = str(value)
        self.valid_check(self.__type_key, value)
        self.__data[self.__type_key] = value

    @type.deleter
    def type(self):
        if self.__type_key in self.__data:
            del self.__data[self.__type_key]

    @property
    def address(self):
        """
        终端所在会议室信息。
        """
        return self.__data.get(self.__address_key)

    @address.setter
    def address(self, value):
        self.__data[self.__address_key] = value

    @address.deleter
    def address(self):
        if self.__address_key in self.__data:
            del self.__data[self.__address_key]

    @property
    def dept_name(self):
        """
        组织名称。最大不超过128个字符。
        """
        return self.__data.get(self.__dept_name_key)

    @dept_name.setter
    def dept_name(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_DEPT_NAME_LENGTH, value, self.__dept_name_key
        )
        self.__data[self.__dept_name_key] = value

    @dept_name.deleter
    def dept_name(self):
        if self.__dept_name_key in self.__data:
            del self.__data[self.__dept_name_key]

    def get_data(self):
        """
        以dict形式获取与会者实例的内容
        :return: dict 与会者实例的内容
        """
        return copy.deepcopy(self.__data)

    def unnull_check(self):
        """
        必填字段校验，检查与会者实例中的必填字段是否设置完成
        """
        for k in self.__unnull_keys:
            if k not in self.__data:
                raise exceptions.ParameterException(
                    "The attribute [%s] of %s cannot be empty"
                    % (k, self.__class__.__name__)
                )


class RestConfConfigDTO(object):
    """
    会议其他配置信息，用于其他会议配置参数。后续新增的会议配置参数都在该结构中定义。
    """

    def __init__(self):
        self.__is_guest_free_pwd_key = "isGuestFreePwd"
        self.__is_send_notify_key = "isSendNotify"
        self.__is_send_sms_key = "isSendSms"
        self.__data = dict()
        self.__valid_check_map = {
            self.__is_guest_free_pwd_key: (
                constants.IS_GUEST_FREE_PWD_LIST,
                constants.IS_GUEST_FREE_PWD_TRANS,
            ),
            self.__is_send_notify_key: (
                constants.IS_SEND_NOTIFY_LIST,
                constants.IS_SEND_NOTIFY_TRANS,
            ),
            self.__is_send_sms_key: (
                constants.IS_SEND_SMS_LIST,
                constants.IS_SEND_SMS_TRANS,
            ),
        }
        self.__unnull_keys = tuple()

    def valid_check(self, key, value):
        """
        参数有效性检查
        :param key: string 需要检查的字段名称
        :param value: 需要检查的字段参数值
        """
        if key in self.__valid_check_map:
            utils.attribute_valid_check(
                self.__valid_check_map[key][0],
                value,
                key,
                self.__class__.__name__,
                self.__valid_check_map[key][1],
            )

    @property
    def is_guest_free_pwd(self):
        """
        来宾是否免密。
        True：免密
        False：不免密
        默认值由会议模板决定，适用于随机id会议。
        """
        return self.__data.get(self.__is_guest_free_pwd_key)

    @is_guest_free_pwd.setter
    def is_guest_free_pwd(self, value):
        self.valid_check(self.__is_guest_free_pwd_key, value)
        self.__data[self.__is_guest_free_pwd_key] = value

    @is_guest_free_pwd.deleter
    def is_guest_free_pwd(self):
        if self.__is_guest_free_pwd_key in self.__data:
            del self.__data[self.__is_guest_free_pwd_key]

    @property
    def is_send_notify(self):
        """
        是否需要发送会议邮件通知。
        True：需要
        False：不需要
        默认值由会议模板决定。
        """
        return self.__data.get(self.__is_send_notify_key)

    @is_send_notify.setter
    def is_send_notify(self, value):
        self.valid_check(self.__is_send_notify_key, value)
        self.__data[self.__is_send_notify_key] = value

    @is_send_notify.deleter
    def is_send_notify(self):
        if self.__is_send_notify_key in self.__data:
            del self.__data[self.__is_send_notify_key]

    @property
    def is_send_sms(self):
        """
        是否需要发送会议通知。
        True：需要
        False：不需要
        默认值由会议模板决定。
        """
        return self.__data.get(self.__is_send_sms_key)

    @is_send_sms.setter
    def is_send_sms(self, value):
        self.valid_check(self.__is_send_sms_key, value)
        self.__data[self.__is_send_sms_key] = value

    @is_send_sms.deleter
    def is_send_sms(self):
        if self.__is_send_sms_key in self.__data:
            del self.__data[self.__is_send_sms_key]

    def get_data(self):
        """
        以dict形式获取会议配置实例的内容
        :return: dict 会议配置实例的内容
        """
        return copy.deepcopy(self.__data)

    def unnull_check(self):
        """
        必填字段校验，检查会议配置实例中的必填字段是否设置完成
        """
        for k in self.__unnull_keys:
            if k not in self.__data:
                raise exceptions.ParameterException(
                    "The attribute [%s] of %s cannot be empty"
                    % (k, self.__class__.__name__)
                )


class Conference(object):
    """
    会议详情对象
    """

    def __init__(self):
        self.conference_type_key = "conferenceType"
        self.start_time_key = "startTime"
        self.length_key = "length"
        self.subject_key = "subject"
        self.group_uri_key = "groupuri"
        self.media_types_key = "mediaTypes"
        self.attendees_key = "attendees"
        self.is_auto_record_key = "isAutoRecord"
        self.encrypt_mode_key = "encryptMode"
        self.language_key = "language"
        self.time_zone_id_key = "timeZoneID"
        self.record_type_key = "recordType"
        self.live_address_key = "liveAddress"
        self.aux_address_key = "auxAddress"
        self.record_aux_stream_key = "recordAuxStream"
        self.conf_config_info_key = "confConfigInfo"
        self.vmr_flag_key = "vmrFlag"
        self.vmr_id_key = "vmrID"
        self.attendees = ParametersList()
        self.attendees.item_class_obj = RestAttendeeDTO
        self.attendees.attr_name = self.attendees_key
        self.date_time_format = "%Y-%m-%d %H:%M"
        self.valid_check_map = {
            self.conference_type_key: (
                constants.CONFERENCE_TYPE_LIST,
                constants.CONFERENCE_TYPE_TRANS,
            ),
            self.media_types_key: (
                constants.CONFERENCE_MEDIA_TYPE_LIST,
                constants.CONFERENCE_MEDIA_TYPE_TRANS,
            ),
            self.is_auto_record_key: (
                constants.IS_AUTO_RECORD_LIST,
                constants.IS_AUTO_RECORD_TRANS,
            ),
            self.encrypt_mode_key: (
                constants.ENCRYPT_MODE_LIST,
                constants.ENCRYPT_MODE_TRANS,
            ),
            self.language_key: (
                constants.CONFERENCE_LANGUAGE_LIST,
                constants.CONFERENCE_LANGUAGE_TRANS,
            ),
            self.record_type_key: (
                constants.RECORD_TYPE_LIST,
                constants.RECORD_TYPE_TRANS,
            ),
            self.record_aux_stream_key: (
                constants.RECORD_AUX_STREAM_LIST,
                constants.RECORD_AUX_STREAM_TRANS,
            ),
            self.vmr_flag_key: (
                constants.VMR_FLAG_LIST,
                constants.VMR_FLAG_TRANS,
            ),
        }
        self.data = dict()
        self.unnull_keys = (self.media_types_key,)

    def valid_check(self, key, value):
        """
        参数有效性检查
        :param key: string 需要检查的字段名称
        :param value: 需要检查的字段参数值
        """
        pass

    @property
    def conference_type(self):
        """
        0 : 普通会议（默认）；
        1 : 周期会议，此时cycleParams必须填写。
        """
        return self.data.get(self.conference_type_key)

    @conference_type.setter
    def conference_type(self, value):
        value = utils.integer_check(
            value, self.conference_type_key, self.__class__.__name__
        )
        self.valid_check(self.conference_type_key, value)
        self.data[self.conference_type_key] = value

    @conference_type.deleter
    def conference_type(self):
        if self.conference_type_key in self.data:
            del self.data[self.conference_type_key]

    @property
    def start_time(self):
        """
会议开始时间。采用UTC时间。 会议本地的开始时间要通过startTime和timeZoneID计算得到。\
比如startTime为UTC 2020-03-20 02:00, timeZoneID为56，对应东八区，\
则本地会议开始时间为东八区的2020-03-20 10:00。\
预定创建会议时，如果没有指定开始时间，或填空串，则表示会议马上开始。格式：YYYY-MM-DD HH:MM
        """
        return self.data.get(self.start_time_key)

    @start_time.setter
    def start_time(self, value):
        new_time = utils.datetime_format_check(
            value, self.date_time_format, self.start_time_key
        )
        self.data[self.start_time_key] = new_time.strftime(
            self.date_time_format
        )

    @start_time.deleter
    def start_time(self):
        if self.start_time_key in self.data:
            del self.data[self.start_time_key]

    @property
    def length(self):
        """
        会议持续时长。单位分钟，最长1440，最短15，默认为30。
        """
        return self.data.get(self.length_key)

    @length.setter
    def length(self, value):
        value = utils.integer_check(
            value, self.length_key, self.__class__.__name__
        )
        utils.attribute_bounds_check(
            value,
            constants.MIN_CONFERENCE_LENGTH,
            constants.MAX_CONFERENCE_LENGTH,
            self.__class__.__name__,
            self.length_key,
        )
        self.data[self.length_key] = value

    @length.deleter
    def length(self):
        if self.length_key in self.data:
            del self.data[self.length_key]

    @property
    def subject(self):
        """会议主题。长度限制为128个字符。"""
        return self.data.get(self.subject_key)

    @subject.setter
    def subject(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_CONFERENCE_SUBJECT_LENGTH, value, self.subject_key
        )
        self.data[self.subject_key] = value

    @subject.deleter
    def subject(self):
        if self.subject in self.data:
            del self.data[self.subject]

    @property
    def groupuri(self):
        """
软终端创建即时会议时在当前字段带临时群组ID，由服务器在邀请其他与会者时在或者conference-info头域中携带。长度限制为31个字符。
        """
        return self.data.get(self.group_uri_key)

    @groupuri.setter
    def groupuri(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_CONFERENCE_GROUP_ID_LENGTH, value, self.group_uri_key,
        )
        self.data[self.group_uri_key] = value

    @groupuri.deleter
    def groupuri(self):
        if self.group_uri_key in self.data:
            del self.group_uri_key

    @property
    def media_types(self):
        """
        会议的媒体类型。由1个或多个枚举String组成，多个枚举时，每个枚举值之间通过”,”逗号分隔，枚举值如下：
        “Voice”：语音
        “Video”：标清视频
        “HDVideo”：高清视频（与Video互斥，如果同时选择Video、HDVideo，则系统默认选择Video）
        “Telepresence”：智真(与HDVideo、Video互斥，如果同时选择，系统使用Telepresence)。（预留字段）
        “Data”：多媒体（AS会根据系统配置决定是否自动添加Data）
        """
        return self.data[self.media_types_key]

    @media_types.setter
    def media_types(self, value):
        value = str(value)
        for m_type in value.split(","):
            self.valid_check(self.media_types_key, m_type)
        self.data[self.media_types_key] = value

    @property
    def is_auto_record(self):
        """
        会议是否自动启动录制，在录播类型为:录播、直播+录播时有效。1 :true：自动启动录制；0 :false：不自动启动录制。（默认）
        """
        return self.data.get(self.is_auto_record_key)

    @is_auto_record.setter
    def is_auto_record(self, value):
        value = utils.integer_check(
            value, self.is_auto_record_key, self.__class__.__name__
        )
        self.data[self.is_auto_record_key] = value

    @is_auto_record.deleter
    def is_auto_record(self):
        if self.is_auto_record_key in self.data:
            del self.data[self.is_auto_record_key]

    @property
    def encrypt_mode(self):
        """
        会议媒体加密模式。0 : auto：自适应加密；1 : must：强制加密；2 : 不出现：不加密
        """
        return self.data.get(self.encrypt_mode_key)

    @encrypt_mode.setter
    def encrypt_mode(self, value):
        value = utils.integer_check(
            value, self.encrypt_mode_key, class_name=self.__class__.__name__
        )
        self.valid_check(self.encrypt_mode_key, value)
        self.data[self.encrypt_mode_key] = value

    @encrypt_mode.deleter
    def encrypt_mode(self):
        if self.encrypt_mode_key in self.data:
            del self.data[self.encrypt_mode_key]

    @property
    def language(self):
        """
会议的默认语言，默认值由会议AS定义，MediaX是“zh-CN”，对于系统支持的语言，按照RFC3066规范传递。zh-CN：简体中文；en-US：美国英文
        """
        return self.data.get(self.language_key)

    @language.setter
    def language(self, value):
        value = str(value)
        self.valid_check(self.language_key, value)
        self.data[self.language_key] = value

    @language.deleter
    def language(self):
        if self.language_key in self.data:
            del self.data[self.language_key]

    @property
    def time_zone_id(self):
        """
        开始时间的时区信息。时区信息参考时区映射关系
        """
        return self.data.get(self.time_zone_id_key)

    @time_zone_id.setter
    def time_zone_id(self, value):
        value = str(value)
        self.valid_check(self.time_zone_id_key, value)
        self.data[self.time_zone_id_key] = value

    @time_zone_id.deleter
    def time_zone_id(self):
        if self.time_zone_id_key in self.data:
            del self.data[self.time_zone_id_key]

    @property
    def record_type(self):
        """
        录播类型。0: 禁用；1: 直播；2: 录播；3: 直播+录播
        """
        return self.data.get(self.record_type_key)

    @record_type.setter
    def record_type(self, value):
        value = utils.integer_check(
            value, self.record_type_key, self.__class__.__name__
        )
        self.valid_check(self.record_type_key, value)
        self.data[self.record_type_key] = value

    @record_type.deleter
    def record_type(self):
        if self.record_type_key in self.data:
            del self.data[self.record_type_key]

    @property
    def live_address(self):
        """
        主流直播地址。最大不超过255个字符。在录播类型为 :直播、直播+录播时有效。
        """
        return self.data.get(self.live_address_key)

    @live_address.setter
    def live_address(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_LIVE_ADDRESS_LENGTH, value, self.live_address_key
        )
        self.data[self.live_address_key] = value

    @live_address.deleter
    def live_address(self):
        if self.live_address_key in self.data:
            del self.data[self.live_address_key]

    @property
    def aux_address(self):
        """
        辅流直播地址。最大不超过255个字符。在录播类型为: 直播、直播+录播时有效。
        """
        return self.data.get(self.aux_address_key)

    @aux_address.setter
    def aux_address(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_AUX_ADDRESS_LENGTH, value, self.aux_address_key
        )
        self.data[self.aux_address_key] = value

    @aux_address.deleter
    def aux_address(self):
        if self.aux_address_key in self.data:
            del self.data[self.aux_address_key]

    @property
    def record_aux_stream(self):
        """
        是否录制辅流。在录播类型为:录播、直播+录播时有效。0：否；1：是
        """
        return self.data.get(self.record_aux_stream_key)

    @record_aux_stream.setter
    def record_aux_stream(self, value):
        value = utils.integer_check(
            value, self.record_aux_stream_key, self.__class__.__name__
        )
        self.valid_check(self.record_aux_stream_key, value)
        self.data[self.record_aux_stream_key] = value

    @record_aux_stream.deleter
    def record_aux_stream(self):
        if self.record_aux_stream_key in self.data:
            del self.data[self.record_aux_stream_key]

    @property
    def vmr_flag(self):
        """
        是否使用VMR召开预约会议。0：不使用VMR；1：使用VMR
        """
        return self.data.get(self.vmr_flag_key)

    @vmr_flag.setter
    def vmr_flag(self, value):
        value = utils.integer_check(
            value, self.vmr_flag_key, class_name=self.__class__.__name__
        )
        self.valid_check(self.vmr_flag_key, value)
        self.data[self.vmr_flag_key] = value

    @vmr_flag.deleter
    def vmr_flag(self):
        if self.vmr_flag_key in self.data:
            del self.data[self.vmr_flag_key]

    @property
    def vmr_id(self):
        """
用于识别用户开会时绑定的VMR会议室。不为空，则用ID查询VMR信息；为空，则查用户所有VMR，如果有个人VMR，用个人；没有，取最小VMRID
        """
        return self.data.get(self.vmr_id_key)

    @vmr_id.setter
    def vmr_id(self, value):
        value = str(value)
        self.data[self.vmr_id_key] = value

    @vmr_id.deleter
    def vmr_id(self):
        if self.vmr_id_key in self.data:
            del self.data[self.vmr_id_key]

    @property
    def conf_config_info(self):
        """
        会议其他配置信息，用于其他会议配置参数。后续新增的会议配置参数都在该结构中定义。
        """
        return RestConfConfigDTO

    @conf_config_info.setter
    def conf_config_info(self, value):
        utils.type_check(value, RestConfConfigDTO)
        self.data[self.conf_config_info_key] = value.get_data()

    def unnull_check(self):
        """
        必填字段校验，检查会议详情实例的必填字段是否设置完成
        """
        for key in self.unnull_keys:
            if key not in self.data:
                raise exceptions.ParameterException(
                    "The attribute [%s] of %s cannot be empty"
                    % (key, self.__class__.__name__)
                )

    def get_data(self):
        """
        以map形式获取会议详情实例的内容
        :return: dict 会议详情实例的内容
        """
        data = copy.deepcopy(self.data)
        attendees_data = self.attendees.get_data()
        if attendees_data:
            data[self.attendees_key] = attendees_data
        return data


class ConferenceListQuery(object):
    """会议列表查询参数对象"""

    def __init__(self):
        self.user_id_key = "userId"
        self.page_index_key = "pageIndex"
        self.page_size_key = "pageSize"
        self.query_all_key = "queryAll"
        self.status_key = "status"
        self.condition_key = "condition"
        self.query_conf_mode_key = "queryConfMode"
        self.sort_type_key = "sortType"
        self.valid_check_map = {
            self.status_key: (
                constants.CONFERENCE_LIST_STATUS_LIST,
                constants.CONFERENCE_LIST_STATUS_TRANS,
            ),
            self.query_conf_mode_key: (
                constants.CONFERENCE_LIST_CONF_MODE_LIST,
                constants.CONFERENCE_LIST_CONF_MODE_TRANS,
            ),
            self.sort_type_key: (
                constants.CONFERENCE_LIST_SORT_LIST,
                constants.CONFERENCE_LIST_SORT_TRANS,
            ),
        }
        self.unnull_keys = (
            self.page_index_key,
            self.page_size_key,
            self.query_all_key,
            self.status_key,
        )
        self.data = dict()

    def valid_check(self, key, value):
        """
        参数有效性检查
        :param key: string 需要检查的字段名称
        :param value: 需要检查的字段参数值
        """
        if key in self.valid_check_map:
            utils.attribute_valid_check(
                self.valid_check_map[key][0],
                value,
                key,
                self.__class__.__name__,
                self.valid_check_map[key][1],
            )

    @property
    def user_id(self):
        """待查询的会议预定者的帐号。"""
        return self.data.get(self.user_id_key)

    @user_id.setter
    def user_id(self, value):
        self.data[self.user_id_key] = value

    @user_id.deleter
    def user_id(self):
        if self.user_id_key in self.data:
            del self.data[self.user_id_key]

    @property
    def page_index(self):
        """指定返回的页面索引。该值必须大于0，默认为1。"""
        return self.data.get(self.page_index_key)

    @page_index.setter
    def page_index(self, value):
        value = utils.integer_check(
            value, self.page_index_key, class_name=self.__class__.__name__
        )
        utils.check_page(value, self.page_index_key, "header")
        self.data[self.page_index_key] = value

    @property
    def page_size(self):
        """
        指定返回的记录数。
        默认值由会议AS定义，默认是20，最大500条
        """
        return self.data.get(self.page_size_key)

    @page_size.setter
    def page_size(self, value):
        value = utils.integer_check(
            value, self.page_size_key, class_name=self.__class__.__name__
        )
        utils.records_count_check(
            constants.MAX_CONFERENCE_LIST_LENGTH, value, self.page_size_key
        )
        self.data[self.page_size_key] = value

    @property
    def query_all(self):
        """
指定是否查询企业下所有用户的会议记录。如果登录帐号不是企业管理员，则该字段无效。如果该字段为true，则userId字段无效。默认为False。
        """
        return self.data.get(self.query_all_key)

    @query_all.setter
    def query_all(self, value):
        utils.type_check(value, bool)
        self.data[self.query_all_key] = value

    @property
    def status(self):
        """
        0: 查询待召开的和已召开的（默认）
        1：查询待召开的
        2：查询正在召开的
        """
        return self.data.get(self.status_key)

    @status.setter
    def status(self, value):
        value = utils.integer_check(
            value, self.status_key, class_name=self.__class__.__name__
        )
        self.valid_check(self.status_key, value)
        self.data[self.status_key] = value

    @property
    def condition(self):
        """查询用来当作关键词的字符串。长度限制为1~128个字符。"""
        return self.data.get(self.condition_key)

    @condition.deleter
    def condition(self):
        if self.condition_key in self.data:
            del self.data[self.condition_key]

    @condition.setter
    def condition(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_CONFERENCE_CONDITION_LENGTH,
            value,
            self.condition_key,
        )
        self.data[self.condition_key] = value

    @property
    def query_conf_mode(self):
        """
        ADAY：一天
        AWEEK：一周
        AMONTH：一个月
        ALL：查询所有
        """
        return self.data.get(self.query_conf_mode_key)

    @query_conf_mode.setter
    def query_conf_mode(self, value):
        value = str(value)
        self.valid_check(self.query_conf_mode_key, value)
        self.data[self.query_conf_mode_key] = value

    @query_conf_mode.deleter
    def query_conf_mode(self):
        if self.query_conf_mode_key in self.data:
            del self.data[self.query_conf_mode_key]

    @property
    def sort_type(self):
        """
        ASC_StartTIME：按会议开始时间升序排序
        DSC_StartTIME：按会议开始时间降序排序
        ASC_RecordTYPE：按会议是否有录播文件排序，之后默认按照会议开始时间升序排序
        DSC_RecordTYPE：按会议是否有录播文件排序，之后默认按照会议开始时间降序排序
        """
        return self.data.get(self.sort_type_key)

    @sort_type.setter
    def sort_type(self, value):
        value = str(value)
        self.valid_check(self.sort_type_key, value)
        self.data[self.sort_type_key] = value

    @sort_type.deleter
    def sort_type(self):
        if self.sort_type_key in self.data:
            del self.data[self.sort_type_key]

    def unnull_check(self):
        """
        必填字段校验，检查会议列表查询参数实例的必填字段是否设置完成
        """
        for key in self.unnull_keys:
            if key not in self.data:
                raise exceptions.ParameterException(
                    "The attribute [%s] of %s cannot be empty"
                    % (key, self.__class__.__name__)
                )

    def get_data(self):
        """
        以map形式获取会议列表查询参数实例的内容
        :return: dict 会议列表查询参数实例的内容
        """
        return copy.deepcopy(self.data)


class ConferenceDetailQuery(object):
    """会议详情查询参数对象"""

    def __init__(self):
        self.conference_id_key = "conferenceid"
        self.page_index_key = "pageIndex"
        self.page_size_key = "pageSize"
        self.condition_key = "condition"
        self.user_id_key = "userId"
        self.type_key = "userId"
        self.query_type_key = "queryType"
        self.valid_check_map = {
            self.type_key: (
                constants.CONFERENCE_INFO_TYPE_LIST,
                constants.CONFERENCE_INFO_TYPE_TRANS,
            ),
            self.query_type_key: (
                constants.CONFERENCE_INFO_QUERY_TYPE_LIST,
                constants.CONFERENCE_INFO_QUERY_TYPE_TRANS,
            ),
        }
        self.unnull_keys = (self.conference_id_key,)
        self.data = dict()

    def valid_check(self, key, value):
        """
        参数有效性检查
        :param key: string 需要检查的字段名称
        :param value: 需要检查的字段参数值
        """
        pass

    @property
    def conference_id(self):
        """会议标识"""
        return self.data.get(self.conference_id_key)

    @conference_id.setter
    def conference_id(self, value):
        self.data[self.conference_id_key] = str(value)

    @property
    def page_index(self):
        """指定返回的与会者列表的页面索引。该值必须大于0，默认为1。"""
        return self.data.get(self.page_index_key)

    @page_index.setter
    def page_index(self, value):
        value = utils.integer_check(
            value, self.page_index_key, class_name=self.__class__.__name__
        )
        self.data[self.page_index_key] = value

    @page_index.deleter
    def page_index(self):
        if self.page_index_key in self.data:
            del self.data[self.page_index_key]

    @property
    def page_size(self):
        """指定返回的与会者记录数，默认值由会议AS定义，内置会议和MediaX默认是20"""
        return self.data.get(self.page_size_key)

    @page_size.setter
    def page_size(self, value):
        value = utils.integer_check(
            value, self.page_size_key, self.__class__.__name__
        )
        self.data[self.page_size_key] = value

    @page_size.deleter
    def page_size(self):
        if self.page_size_key in self.data:
            del self.data[self.page_size_key]

    @property
    def condition(self):
        """查询用来当做关键词的字符串，范围限定为1~128个字符。"""
        return self.data.get(self.condition_key)

    @condition.setter
    def condition(self, value):
        value = str(value)
        utils.bytes_length_check(
            constants.MAX_CONFERENCE_CONDITION_LENGTH,
            value,
            self.condition_key,
        )
        self.data[self.condition_key] = value

    @condition.deleter
    def condition(self):
        if self.condition_key in self.data:
            del self.data[self.condition_key]

    @property
    def user_id(self):
        """用户帐号"""
        return self.data.get(self.user_id_key)

    @user_id.deleter
    def user_id(self):
        del self.data[self.user_id_key]

    @user_id.setter
    def user_id(self, value):
        self.data[self.user_id_key] = str(value)

    @property
    def type(self):
        """
        0：不区分终端和与会人。
        1：分页查询区分终端和与会人，结果合并返回。
        2：单独查询终端和与会人，结果单独返回。
        默认值为“0”。
        """
        return self.data.get(self.type_key)

    @type.setter
    def type(self, value):
        value = utils.integer_check(
            value, self.type_key, class_name=self.__class__.__name__
        )
        self.valid_check(self.type_key, value)
        self.data[self.type_key] = value

    @type.deleter
    def type(self):
        if self.type_key in self.data:
            del self.data[self.type_key]

    @property
    def query_type(self):
        """
        当“type”为“2”时，该字段有效。
        0：查询与会人。
        1：查询终端。
        """
        return self.data.get(self.query_type_key)

    @query_type.setter
    def query_type(self, value):
        value = utils.integer_check(
            value, self.query_type_key, class_name=self.__class__.__name__
        )
        self.valid_check(self.query_type_key, value)
        self.data[self.query_type_key] = value

    @query_type.deleter
    def query_type(self):
        if self.query_type_key in self.data:
            del self.data[self.query_type_key]

    def unnull_check(self):
        """
        必填字段校验，检查会议详情查询参数实例的必填字段是否设置完成
        """
        for key in self.unnull_keys:
            if key not in self.data:
                raise exceptions.ParameterException(
                    "The attribute [%s] of %s cannot be empty"
                    % (key, self.__class__.__name__)
                )

    def get_data(self):
        """
        以map形式获取会议详情查询参数实例的内容
        :return: dict 会议详情查询参数实例的内容
        """
        return copy.deepcopy(self.data)


class HistoryConferenceListQuery(ConferenceListQuery):
    """历史会议列表查询参数对象"""

    def __init__(self):
        super(HistoryConferenceListQuery, self).__init__()
        self.start_date_key = "startDate"
        self.end_date_key = "endDate"
        self.unnull_keys = (
            self.page_index_key,
            self.page_size_key,
            self.query_all_key,
            self.status_key,
            self.start_date_key,
            self.end_date_key,
            self.sort_type_key,
        )

    @property
    def start_date(self):
        """查询的起始日期毫秒数"""
        return self.data.get(self.start_date_key)

    @start_date.setter
    def start_date(self, value):
        value = utils.integer_check(
            value, self.start_date_key, class_name=self.__class__.__name__
        )
        self.data[self.start_date_key] = value

    @start_date.deleter
    def start_date(self):
        if self.start_date_key in self.data:
            del self.data[self.start_date_key]

    @property
    def end_date(self):
        """查询的截止日期毫秒数"""
        return self.data.get(self.end_date_key)

    @end_date.setter
    def end_date(self, value):
        value = utils.integer_check(
            value, self.end_date_key, class_name=self.__class__.__name__
        )
        self.data[self.end_date_key] = value

    @end_date.deleter
    def end_date(self):
        if self.end_date_key in self.data:
            del self.data[self.end_date_key]


class HistoryConferenceDetailQuery(ConferenceDetailQuery):
    """历史会议详情查询参数对象"""

    def __init__(self):
        super(HistoryConferenceDetailQuery, self).__init__()
        self.conf_uuid_key = "confuuid"
        self.unnull_keys = (
            self.conf_uuid_key,
            self.page_index_key,
            self.page_size_key,
        )

    @property
    def conf_uuid(self):
        """会议uuid"""
        return self.data.get(self.conf_uuid_key)

    @conf_uuid.setter
    def conf_uuid(self, value):
        self.data[self.conf_uuid_key] = value

    @conf_uuid.deleter
    def conf_uuid(self):
        if self.conf_uuid_key in self.data:
            del self.data[self.conf_uuid_key]
