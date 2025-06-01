#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
api模块预加载
Created on 2020-03-02
@author: wecode@huawei.com
"""
from welink.api.rest.AiserviceV1OcrBusinessCardRequest import (
    AiserviceV1OcrBusinessCardRequest,
)

from welink.api.rest.AiserviceV1OcrAutoClassificationRequest import (
    AiserviceV1OcrAutoClassificationRequest,
)

from welink.api.rest.AiserviceV1OcrGeneralTableRequest import (
    AiserviceV1OcrGeneralTableRequest,
)

from welink.api.rest.AiserviceV1OcrIdCardRequest import (
    AiserviceV1OcrIdCardRequest,
)

from welink.api.rest.AiserviceV1OcrWebImageRequest import (
    AiserviceV1OcrWebImageRequest,
)


from welink.api.rest.AiserviceV1SisShortAudioRequest import (
    AiserviceV1SisShortAudioRequest,
)

from welink.api.rest.AiserviceV1SisTtsRequest import AiserviceV1SisTtsRequest
from welink.api.rest.AiserviceV1SisAudioAssessmentRequest import (
    AiserviceV1SisAudioAssessmentRequest,
)


from welink.api.rest.AiserviceV2FrsFaceCompareRequest import (
    AiserviceV2FrsFaceCompareRequest,
)

from welink.api.rest.AiserviceV2FrsFaceDetectRequest import (
    AiserviceV2FrsFaceDetectRequest,
)


from welink.api.rest.AiserviceV1ModerationTextRequest import (
    AiserviceV1ModerationTextRequest,
)

from welink.api.rest.AiserviceV1ModerationImageRequest import (
    AiserviceV1ModerationImageRequest,
)


from welink.api.rest.AiserviceV1NlpNerRequest import AiserviceV1NlpNerRequest
from welink.api.rest.AiserviceV1NlpSegmentRequest import (
    AiserviceV1NlpSegmentRequest,
)

from welink.api.rest.AiserviceV1NlpSentenceEmbeddingRequest import (
    AiserviceV1NlpSentenceEmbeddingRequest,
)

from welink.api.rest.AiserviceV1NlpSemanticParserRequest import (
    AiserviceV1NlpSemanticParserRequest,
)

from welink.api.rest.AiserviceV1NlpSummarizationRequest import (
    AiserviceV1NlpSummarizationRequest,
)

from welink.api.rest.AiserviceV1NlpTextSimilarityRequest import (
    AiserviceV1NlpTextSimilarityRequest,
)

from welink.api.rest.AiserviceV1NlpSentimentRequest import (
    AiserviceV1NlpSentimentRequest,
)


from welink.api.rest.AiserviceV1TranslateDetectRequest import (
    AiserviceV1TranslateDetectRequest,
)

from welink.api.rest.AiserviceV1TranslateSupportedRequest import (
    AiserviceV1TranslateSupportedRequest,
)

from welink.api.rest.AiserviceV1TranslateTranslateRequest import (
    AiserviceV1TranslateTranslateRequest,
)


from welink.api.rest.AttendanceV2RecordsRequest import (
    AttendanceV2RecordsRequest,
)

from welink.api.rest.AuthV2TicketsRequest import AuthV2TicketsRequest
from welink.api.rest.AuthV2UseridRequest import AuthV2UseridRequest
from welink.api.rest.ContactV1DepartmentParentRequest import (
    ContactV1DepartmentParentRequest,
)

from welink.api.rest.ContactV1DepartmentsRequest import (
    ContactV1DepartmentsRequest,
)

from welink.api.rest.ContactV1UserParentRequest import (
    ContactV1UserParentRequest,
)

from welink.api.rest.ContactV1UsersAccountsRequest import (
    ContactV1UsersAccountsRequest,
)

from welink.api.rest.ContactV1UserMobilenumberRequest import (
    ContactV1UserMobilenumberRequest,
)

from welink.api.rest.ContactV2UsersBulkRequest import ContactV2UsersBulkRequest
from welink.api.rest.ContactV1UsersBulkRequest import ContactV1UsersBulkRequest
from welink.api.rest.ContactV2UsersUpdateRequest import (
    ContactV2UsersUpdateRequest,
)

from welink.api.rest.ContactV2DepartmentsUpdateRequest import (
    ContactV2DepartmentsUpdateRequest,
)

from welink.api.rest.ContactV3UserPermissionUsersRequest import (
    ContactV3UserPermissionUsersRequest,
)

from welink.api.rest.ContactV1UsersEmailRequest import (
    ContactV1UsersEmailRequest,
)

from welink.api.rest.ContactV1UsersRequest import ContactV1UsersRequest
from welink.api.rest.ContactV3UsersRequest import ContactV3UsersRequest
from welink.api.rest.ContactV1UsersSimpleRequest import (
    ContactV1UsersSimpleRequest,
)

from welink.api.rest.ContactV3UsersSimpleRequest import (
    ContactV3UsersSimpleRequest,
)

from welink.api.rest.ContactV1UsersStatusRequest import (
    ContactV1UsersStatusRequest,
)

from welink.api.rest.ContactV1UserUsersRequest import ContactV1UserUsersRequest
from welink.api.rest.ContactV2DepartmentsBulkRequest import (
    ContactV2DepartmentsBulkRequest,
)

from welink.api.rest.ContactV2DepartmentsListRequest import (
    ContactV2DepartmentsListRequest,
)

from welink.api.rest.ContactV2DepartmentsStatusRequest import (
    ContactV2DepartmentsStatusRequest,
)

from welink.api.rest.ContactV2UserUseridRequest import (
    ContactV2UserUseridRequest,
)

from welink.api.rest.ContactV2UserUsersRequest import ContactV2UserUsersRequest
from welink.api.rest.ContactV3DepartmentsListRequest import (
    ContactV3DepartmentsListRequest,
)


from welink.api.rest.ContactV1RolegroupCreateRequest import (
    ContactV1RolegroupCreateRequest,
)

from welink.api.rest.ContactV1RolegroupUpdateRequest import (
    ContactV1RolegroupUpdateRequest,
)

from welink.api.rest.ContactV1RolegroupDetailRequest import (
    ContactV1RolegroupDetailRequest,
)

from welink.api.rest.ContactV1RolegroupListRequest import (
    ContactV1RolegroupListRequest,
)

from welink.api.rest.ContactV1RolegroupDeleteRequest import (
    ContactV1RolegroupDeleteRequest,
)

from welink.api.rest.ContactV1RoleCreateRequest import (
    ContactV1RoleCreateRequest,
)

from welink.api.rest.ContactV1RoleUpdateRequest import (
    ContactV1RoleUpdateRequest,
)

from welink.api.rest.ContactV1RoleDeleteRequest import (
    ContactV1RoleDeleteRequest,
)

from welink.api.rest.ContactV1RoleDetailRequest import (
    ContactV1RoleDetailRequest,
)

from welink.api.rest.ContactV1RoleSimplelistRequest import (
    ContactV1RoleSimplelistRequest,
)


from welink.api.rest.KnowledgeV1ArticlesAddRequest import (
    KnowledgeV1ArticlesAddRequest,
)

from welink.api.rest.KnowledgeV1ArticlesUpdateRequest import (
    KnowledgeV1ArticlesUpdateRequest,
)

from welink.api.rest.KnowledgeV2ArticlesAddRequest import (
    KnowledgeV2ArticlesAddRequest,
)

from welink.api.rest.KnowledgeV2ArticlesUpdateRequest import (
    KnowledgeV2ArticlesUpdateRequest,
)


from welink.api.rest.MeetingV1CreateconferenceRequest import (
    MeetingV1CreateconferenceRequest,
)

from welink.api.rest.MeetingV1DeleteconferenceRequest import (
    MeetingV1DeleteconferenceRequest,
)

from welink.api.rest.MeetingV1QueryconferencedetailRequest import (
    MeetingV1QueryconferencedetailRequest,
)

from welink.api.rest.MeetingV1QueryconferencesRequest import (
    MeetingV1QueryconferencesRequest,
)

from welink.api.rest.MeetingV1QueryhistoryconferencedetailRequest import (
    MeetingV1QueryhistoryconferencedetailRequest,
)

from welink.api.rest.MeetingV1QueryhistoryconferencesRequest import (
    MeetingV1QueryhistoryconferencesRequest,
)

from welink.api.rest.MeetingV1UpdateconferenceRequest import (
    MeetingV1UpdateconferenceRequest,
)

from welink.api.rest.MessagesV3SendRequest import MessagesV3SendRequest
from welink.api.rest.TenantV1TenantsRequest import TenantV1TenantsRequest
from welink.api.rest.TodoV1AddtaskRequest import TodoV1AddtaskRequest
from welink.api.rest.TodoV1UpdatetaskRequest import TodoV1UpdatetaskRequest
from welink.api.rest.TodoV1DeltaskRequest import TodoV1DeltaskRequest
from welink.api.rest.TodoV2UpdatetaskRequest import TodoV2UpdatetaskRequest
from welink.api.rest.TodoV2AddtaskRequest import TodoV2AddtaskRequest
from welink.api.rest.WelinkIMV1GroupServiceGroupCreateGroupRequest import (
    WelinkIMV1GroupServiceGroupCreateGroupRequest,
)

from welink.api.rest.WelinkIMV1GroupServiceGroupDisbandGroupRequest import (
    WelinkIMV1GroupServiceGroupDisbandGroupRequest,
)

from welink.api.rest.WelinkIMV1GroupServiceGroupTransferGroupOwnerRequest import (
    WelinkIMV1GroupServiceGroupTransferGroupOwnerRequest,
)

from welink.api.rest.WelinkIMV1GroupServiceGroupMemberAddGroupMemberRequest import (
    WelinkIMV1GroupServiceGroupMemberAddGroupMemberRequest,
)

from welink.api.rest.WelinkIMV1GroupServiceGroupModifyGroupNameRequest import (
    WelinkIMV1GroupServiceGroupModifyGroupNameRequest,
)

from welink.api.rest.WelinkIMV1GroupServiceGroupMemberRemoveGroupMemberRequest import (
    WelinkIMV1GroupServiceGroupMemberRemoveGroupMemberRequest,
)

from welink.api.rest.WelinkIMV1GroupServiceGroupModifyGroupCapacityRequest import (
    WelinkIMV1GroupServiceGroupModifyGroupCapacityRequest,
)


from welink.api.rest.WelinkIMV1ImServiceChatGroupChatRequest import (
    WelinkIMV1ImServiceChatGroupChatRequest,
)

from welink.api.rest.WeopenV1IsadminRequest import WeopenV1IsadminRequest

from welink.api.rest.CalendarV1MeetingsAddRequest import (
    CalendarV1MeetingsAddRequest,
)

from welink.api.rest.CalendarV1MeetingsUpdateRequest import (
    CalendarV1MeetingsUpdateRequest,
)

from welink.api.rest.CalendarV1MeetingsDeleteRequest import (
    CalendarV1MeetingsDeleteRequest,
)

from welink.api.rest.CalendarV1EventsUpdateRequest import (
    CalendarV1EventsUpdateRequest,
)

from welink.api.rest.CalendarV1EventsAddRequest import (
    CalendarV1EventsAddRequest,
)

from welink.api.rest.CalendarV1EventsDeleteRequest import (
    CalendarV1EventsDeleteRequest,
)

from welink.api.rest.ContactV1UserDetailRequest import (
    ContactV1UserDetailRequest,
)

from welink.api.rest.ContactV1UserSimplelistRequest import (
    ContactV1UserSimplelistRequest,
)


from welink.api.callback.CallBackV1 import CallBackV1

from welink.api.rest.LivecastV1RoomsAudienceRequest import (
    LivecastV1RoomsAudienceRequest,
)

from welink.api.rest.LivecastV1RoomsDetailRequest import (
    LivecastV1RoomsDetailRequest,
)

from welink.api.rest.LivecastV1RoomsListRequest import (
    LivecastV1RoomsListRequest,
)

from welink.api.rest.LivecastV1VideosAudienceRequest import (
    LivecastV1VideosAudienceRequest,
)

from welink.api.rest.LivecastV1VideosRequest import LivecastV1VideosRequest

from welink.api.rest.ApproveV1UserHealthRequest import (
    ApproveV1UserHealthRequest,
)


from welink.api.rest.SearchV1IndexesBulkAddRequest import (
    SearchV1IndexesBulkAddRequest,
)

from welink.api.rest.SearchV1IndexesBulkEditRequest import (
    SearchV1IndexesBulkEditRequest,
)

from welink.api.rest.SearchV1IndexesBulkDelRequest import (
    SearchV1IndexesBulkDelRequest,
)

from welink.api.rest.SearchV1IndexesSearchRequest import (
    SearchV1IndexesSearchRequest,
)


from welink.api.rest.WeopenV1UserscopeRequest import WeopenV1UserscopeRequest

from welink.api.rest.ContactV1UserCreateRequest import (
    ContactV1UserCreateRequest,
)

from welink.api.rest.WelinkIMV1GroupServiceGroupModifyGroupCapacityRequest import (
    WelinkIMV1GroupServiceGroupModifyGroupCapacityRequest,
)


from welink.api.rest.KnowledgeV1ArticlesDeleteRequest import (
    KnowledgeV1ArticlesDeleteRequest,
)


from welink.api.rest.ContactV1UserDeleteRequest import (
    ContactV1UserDeleteRequest,
)

from welink.api.rest.ContactV1UserListRequest import ContactV1UserListRequest

from welink.api.rest.ContactV1DepartmentCreateRequest import (
    ContactV1DepartmentCreateRequest,
)

from welink.api.rest.ContactV1DepartmentUpdateRequest import (
    ContactV1DepartmentUpdateRequest,
)

from welink.api.rest.ContactV1DepartmentDetailRequest import (
    ContactV1DepartmentDetailRequest,
)

from welink.api.rest.ContactV1DepartmentListRequest import (
    ContactV1DepartmentListRequest,
)

from welink.api.rest.ContactV1UserBatchCreateRequest import (
    ContactV1UserBatchCreateRequest,
)

from welink.api.rest.ContactV1UserBatchUpdateRequest import (
    ContactV1UserBatchUpdateRequest,
)

from welink.api.rest.ContactV1UserBatchUpdatemobileRequest import (
    ContactV1UserBatchUpdatemobileRequest,
)

from welink.api.rest.ContactV1UserBatchUpdatecorpuidRequest import (
    ContactV1UserBatchUpdatecorpuidRequest,
)

from welink.api.rest.ContactV1UserBatchDeleteRequest import (
    ContactV1UserBatchDeleteRequest,
)

from welink.api.rest.ContactV1DepartmentBatchCreateRequest import (
    ContactV1DepartmentBatchCreateRequest,
)

from welink.api.rest.ContactV1DepartmentBatchUpdateRequest import (
    ContactV1DepartmentBatchUpdateRequest,
)

from welink.api.rest.ContactV1DepartmentBatchUpdatecorpdeptRequest import (
    ContactV1DepartmentBatchUpdatecorpdeptRequest,
)

from welink.api.rest.ContactV1DepartmentBatchDeleteRequest import (
    ContactV1DepartmentBatchDeleteRequest,
)

from welink.api.rest.ContactV1BatchResultRequest import (
    ContactV1BatchResultRequest,
)

from welink.api.rest.ContactV1DepartmentDeleteRequest import (
    ContactV1DepartmentDeleteRequest,
)

from welink.api.rest.ContactV2DepartmentParentRequest import (
    ContactV2DepartmentParentRequest,
)

from welink.api.rest.ContactV1UserUpdateRequest import (
    ContactV1UserUpdateRequest,
)

from welink.api.rest.ContactV2UserListRequest import ContactV2UserListRequest

from welink.api.rest.ContactV2UserDetailRequest import (
    ContactV2UserDetailRequest,
)

from welink.api.rest.ContactV2DepartmentListRequest import (
    ContactV2DepartmentListRequest,
)

from welink.api.rest.ContactV2DepartmentDetailRequest import (
    ContactV2DepartmentDetailRequest,
)

from welink.api.rest.ContactV2DepartmentBatchUpdateRequest import (
    ContactV2DepartmentBatchUpdateRequest,
)

from welink.api.rest.ContactV2DepartmentBatchCreateRequest import (
    ContactV2DepartmentBatchCreateRequest,
)

from welink.api.rest.ContactV1RolegroupSimplelistRequest import (
    ContactV1RolegroupSimplelistRequest,
)

from welink.api.rest.MessagesV1CardCommonRequest import (
    MessagesV1CardCommonRequest,
)

from welink.api.rest.MessagesV1CardWecodeRequest import (
    MessagesV1CardWecodeRequest,
)

from welink.api.rest.KnowledgeV1CategoryListRequest import (
    KnowledgeV1CategoryListRequest,
)

from welink.api.rest.KnowledgeV1ComponentListRequest import (
    KnowledgeV1ComponentListRequest,
)

from welink.api.rest.KnowledgeV1ArticleListRequest import (
    KnowledgeV1ArticleListRequest,
)

from welink.api.rest.WeopenWecodeListRequest import WeopenWecodeListRequest

from welink.api.rest.WeopenWecodeDetailRequest import WeopenWecodeDetailRequest

from welink.api.rest.WeopenWecodeUpdateRequest import WeopenWecodeUpdateRequest

from welink.api.rest.ContactV1UserBatchSyncRequest import (
    ContactV1UserBatchSyncRequest,
)

from welink.api.rest.AthenaserviceV1ContextawarePushRequest import (
    AthenaserviceV1ContextawarePushRequest,
)

from welink.api.rest.MessagesV2CardCommonRequest import (
    MessagesV2CardCommonRequest,
)

from welink.api.rest.MessagesV1UpdateRequest import MessagesV1UpdateRequest

from welink.api.rest.MessagesV1RecallRequest import MessagesV1RecallRequest

from welink.api.rest.WeopenFormListRequest import WeopenFormListRequest

from welink.api.rest.WeopenFormDataRequest import WeopenFormDataRequest

from welink.api.rest.WeopenFormScopeDetailRequest import (
    WeopenFormScopeDetailRequest,
)

from welink.api.rest.WeopenFormScopeRequest import WeopenFormScopeRequest

from welink.api.rest.AttendanceV3RecordsRequest import (
    AttendanceV3RecordsRequest,
)

from welink.api.rest.AttendanceV1GroupListRequest import (
    AttendanceV1GroupListRequest,
)

from welink.api.rest.AttendanceV1GroupSettingsRequest import (
    AttendanceV1GroupSettingsRequest,
)

from welink.api.rest.AttendanceV1ScheduleSettingCreateRequest import (
    AttendanceV1ScheduleSettingCreateRequest,
)

from welink.api.rest.AttendanceV1ScheduleSettingUpdateRequest import (
    AttendanceV1ScheduleSettingUpdateRequest,
)

from welink.api.rest.AttendanceV1ScheduleSettingDeleteRequest import (
    AttendanceV1ScheduleSettingDeleteRequest,
)

from welink.api.rest.AttendanceV1GroupSettingsRulesRequest import (
    AttendanceV1GroupSettingsRulesRequest,
)

from welink.api.rest.TodoV3AddtaskRequest import TodoV3AddtaskRequest

from welink.api.rest.LivecastV1RoomsCreateRequest import (
    LivecastV1RoomsCreateRequest,
)

from welink.api.rest.LivecastV1RoomsUpdateRequest import (
    LivecastV1RoomsUpdateRequest,
)

from welink.api.rest.AdmincenterV1UserDomainScopeRequest import (
    AdmincenterV1UserDomainScopeRequest,
)

from welink.api.rest.AttendanceV1ScheduleSettingListRequest import (
    AttendanceV1ScheduleSettingListRequest,
)
