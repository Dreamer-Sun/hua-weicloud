# coding: utf-8

"""
    网络设备管理

    提供北向查询网络设备服务。 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .acl_dto_detail import AclDtoDetail
from .acl_dto_in_response import AclDtoInResponse
from .add_portal_page_rule_input_dto import AddPortalPageRuleInputDto
from .add_template_dto import AddTemplateDto
from .add_usergroup_input_dto import AddUsergroupInputDto
from .add_usergroup_output_dto import AddUsergroupOutputDto
from .add_usergroup_out_data import AddUsergroupOutData
from .add_user_input_dto import AddUserInputDto
from .add_user_output_data import AddUserOutputData
from .add_user_output_dto import AddUserOutputDto
from .aplocation_dto import AplocationDto
from .application_info_detail import ApplicationInfoDetail
from .application_info_resp import ApplicationInfoResp
from .appsk_dto import AppskDto
from .ap_device_radio_api_dto import ApDeviceRadioApiDto
from .ap_device_radio_responses_dto import ApDeviceRadioResponsesDto
from .ap_device_radio_result_api_dto import ApDeviceRadioResultApiDto
from .ap_dhcp_config_api_dto import ApDhcpConfigApiDto
from .ap_dhcp_config_responses_dto import ApDhcpConfigResponsesDto
from .ap_extra_service_dto import ApExtraServiceDto
from .ap_extra_service_input_dto import ApExtraServiceInputDto
from .ap_extra_service_response_dto import ApExtraServiceResponseDto
from .ar_staticroute_delete_dto import ArStaticrouteDeleteDto
from .ar_staticroute_delete_response_dto import ArStaticrouteDeleteResponseDto
from .ar_staticroute_delete_response_fail_dto import ArStaticrouteDeleteResponseFailDto
from .ar_staticroute_info_dto import ArStaticrouteInfoDto
from .ar_staticroute_response_dto import ArStaticrouteResponseDto
from .aspf_config_dto import AspfConfigDto
from .aspf_config_resp_dto import AspfConfigRespDto
from .authentication_log_detail_output_dto import AuthenticationLogDetailOutputDto
from .authentication_log_output_dto import AuthenticationLogOutputDto
from .authen_profile_delete_dto import AuthenProfileDeleteDto
from .authen_profile_delete_failed_result_dto import AuthenProfileDeleteFailedResultDto
from .authen_profile_delete_resp_dto import AuthenProfileDeleteRespDto
from .authen_profile_delete_success_result_dto import AuthenProfileDeleteSuccessResultDto
from .authen_profile_dto import AuthenProfileDto
from .authen_profile_query_result_dto import AuthenProfileQueryResultDto
from .authen_resp_dto import AuthenRespDto
from .authorization_output_dto import AuthorizationOutputDto
from .authorization_output_dto_data import AuthorizationOutputDtoData
from .auth_content_dto import AuthContentDto
from .auth_delete_fail_result import AuthDeleteFailResult
from .available_version import AvailableVersion
from .base_response_dto import BaseResponseDto
from .batch_get_dto import BatchGetDto
from .batch_modify_devices import BatchModifyDevices
from .batch_modify_device_bean import BatchModifyDeviceBean
from .batch_modify_device_dto import BatchModifyDeviceDto
from .batch_modify_device_fail_bean import BatchModifyDeviceFailBean
from .batch_modify_device_fail_data_bean import BatchModifyDeviceFailDataBean
from .batch_modify_device_success_bean import BatchModifyDeviceSuccessBean
from .binding_site_list_dto import BindingSiteListDto
from .boards_info_output_dto import BoardsInfoOutputDto
from .board_config_dto import BoardConfigDto
from .board_delete_dto import BoardDeleteDto
from .board_delete_response_dto import BoardDeleteResponseDto
from .board_info import BoardInfo
from .board_info_dto import BoardInfoDto
from .boot_rom_dto import BootRomDto
from .boot_rom_response import BootRomResponse
from .building_dto import BuildingDto
from .card_operation_output_dto import CardOperationOutputDto
from .cis_response_dto import CisResponseDto
from .common_authorization_output_dto import CommonAuthorizationOutputDto
from .common_dto import CommonDto
from .common_output_dto import CommonOutputDto
from .common_portal_page_rule_output_dto import CommonPortalPageRuleOutputDto
from .common_response_bean import CommonResponseBean
from .common_response_body import CommonResponseBody
from .common_time_flow_config_dto import CommonTimeFlowConfigDto
from .common_usergroup_output_dto import CommonUsergroupOutputDto
from .common_user_output_dto import CommonUserOutputDto
from .config_policy_response import ConfigPolicyResponse
from .config_response_dto import ConfigResponseDto
from .config_save_dto import ConfigSaveDto
from .config_save_item import ConfigSaveItem
from .config_save_result import ConfigSaveResult
from .config_ssid_response import ConfigSsidResponse
from .config_state_result import ConfigStateResult
from .config_upgrade_policy_dto import ConfigUpgradePolicyDto
from .config_upgrade_policy_list_dto import ConfigUpgradePolicyListDto
from .count import Count
from .create_device_bean import CreateDeviceBean
from .create_device_dto import CreateDeviceDto
from .create_device_fail_bean import CreateDeviceFailBean
from .create_device_fail_data_bean import CreateDeviceFailDataBean
from .create_device_success_bean import CreateDeviceSuccessBean
from .create_local_user_info_requst import CreateLocalUserInfoRequst
from .create_local_user_info_response import CreateLocalUserInfoResponse
from .create_radius_temp_dto import CreateRadiusTempDto
from .create_radius_temp_response_dto import CreateRadiusTempResponseDto
from .create_site_dto import CreateSiteDto
from .create_site_dto_data import CreateSiteDtoData
from .create_site_fail import CreateSiteFail
from .create_site_fail_data import CreateSiteFailData
from .create_site_out import CreateSiteOut
from .create_site_success import CreateSiteSuccess
from .create_site_temp_dto import CreateSiteTempDto
from .create_site_temp_response_dto import CreateSiteTempResponseDto
from .create_stack_dto import CreateStackDto
from .create_stack_dto_data import CreateStackDtoData
from .create_stack_fail import CreateStackFail
from .create_stack_out_dto import CreateStackOutDto
from .create_stack_success import CreateStackSuccess
from .create_tacacs_tmpl_info_dto import CreateTacacsTmplInfoDto
from .create_tacacs_tmpl_response import CreateTacacsTmplResponse
from .create_tenant_common_dto import CreateTenantCommonDto
from .create_tenant_dto import CreateTenantDto
from .create_tenant_response_dto import CreateTenantResponseDto
from .create_tenant_result_dto import CreateTenantResultDto
from .cut_portal_online_user_input_dto import CutPortalOnlineUserInputDto
from .cut_portal_online_user_output_dto import CutPortalOnlineUserOutputDto
from .cut_portal_online_user_result_dto import CutPortalOnlineUserResultDto
from .cut_user_data import CutUserData
from .cut_user_input_dto import CutUserInputDto
from .cut_user_output_dto import CutUserOutputDto
from .data_list_dto import DataListDto
from .data_mac_dto import DataMacDto
from .data_object_json import DataObjectJson
from .data_upload_dto import DataUploadDto
from .day_content_dto import DayContentDto
from .delete_acl_ret import DeleteAclRet
from .delete_auth_response import DeleteAuthResponse
from .delete_device_bean import DeleteDeviceBean
from .delete_device_dto import DeleteDeviceDto
from .delete_device_fail_bean import DeleteDeviceFailBean
from .delete_fail_dto import DeleteFailDto
from .delete_fw_nat_info_dto import DeleteFwNatInfoDto
from .delete_fw_static_route_info_dto import DeleteFwStaticRouteInfoDto
from .delete_local_user_info_response import DeleteLocalUserInfoResponse
from .delete_macs_output import DeleteMacsOutput
from .delete_portal_page_rule_input_dto import DeletePortalPageRuleInputDto
from .delete_portal_page_rule_output_dto import DeletePortalPageRuleOutputDto
from .delete_radius_temp_dto import DeleteRadiusTempDto
from .delete_radius_temp_response_dto import DeleteRadiusTempResponseDto
from .delete_radius_temp_response_dto_fail import DeleteRadiusTempResponseDtoFail
from .delete_response_dto import DeleteResponseDto
from .delete_response_fail_dto import DeleteResponseFailDto
from .delete_site_dto import DeleteSiteDto
from .delete_site_fail import DeleteSiteFail
from .delete_site_out import DeleteSiteOut
from .delete_site_temp_dto import DeleteSiteTempDto
from .delete_site_temp_response_dto import DeleteSiteTempResponseDto
from .delete_site_temp_response_dto_fail import DeleteSiteTempResponseDtoFail
from .delete_ssid_response import DeleteSsidResponse
from .delete_stp_protection_fail import DeleteStpProtectionFail
from .delete_stp_protection_request_dto import DeleteStpProtectionRequestDto
from .delete_stp_protection_response_dto import DeleteStpProtectionResponseDto
from .delete_tacacs_tmpl_responses import DeleteTacacsTmplResponses
from .delete_tacacs_tmpl_responses_fail import DeleteTacacsTmplResponsesFail
from .delete_tacacs_tmpl_reuest import DeleteTacacsTmplReuest
from .delete_template_dto import DeleteTemplateDto
from .delete_time_flow_config_output_dto import DeleteTimeFlowConfigOutputDto
from .delete_time_flow_fail_info import DeleteTimeFlowFailInfo
from .delete_usergroup_output_dto import DeleteUsergroupOutputDto
from .delete_user_group_fail import DeleteUserGroupFail
from .delete_user_input_dto import DeleteUserInputDto
from .delete_user_output_dto import DeleteUserOutputDto
from .del_mstp_region import DelMstpRegion
from .del_mstp_region_instance import DelMstpRegionInstance
from .del_region_instance_device import DelRegionInstanceDevice
from .del_stp_dto import DelStpDto
from .del_user_output_data import DelUserOutputData
from .device import Device
from .device_ar_staticroute_info_dto import DeviceArStaticrouteInfoDto
from .device_base_info import DeviceBaseInfo
from .device_bean import DeviceBean
from .device_count_trend import DeviceCountTrend
from .device_count_trend_resp import DeviceCountTrendResp
from .device_detail_list_res import DeviceDetailListRes
from .device_fw_nat_info_dto import DeviceFwNatInfoDto
from .device_fw_static_route_info_dto import DeviceFwStaticRouteInfoDto
from .device_group_tag import DeviceGroupTag
from .device_group_tag_resp import DeviceGroupTagResp
from .device_info import DeviceInfo
from .device_location_info import DeviceLocationInfo
from .device_log_info import DeviceLogInfo
from .device_model import DeviceModel
from .device_model_entity import DeviceModelEntity
from .device_model_entity_list import DeviceModelEntityList
from .device_performance import DevicePerformance
from .device_performance_resp import DevicePerformanceResp
from .device_radio_config_responses_dto import DeviceRadioConfigResponsesDto
from .device_radio_entity_api_dto import DeviceRadioEntityApiDto
from .device_response_bean import DeviceResponseBean
from .device_station_statistic_info import DeviceStationStatisticInfo
from .device_station_statistic_resp import DeviceStationStatisticResp
from .device_statistic_info import DeviceStatisticInfo
from .device_traffic_statistic_resp import DeviceTrafficStatisticResp
from .domain_name_dto import DomainNameDto
from .domain_name_response_dto import DomainNameResponseDto
from .download_policy_dto import DownloadPolicyDto
from .edit_tacacs_config_response import EditTacacsConfigResponse
from .edit_tacacs_tmpl_response import EditTacacsTmplResponse
from .entry_of_id2_name import EntryOfId2Name
from .ethernet_card_dto import EthernetCardDto
from .ethernet_card_output_dto import EthernetCardOutputDto
from .eth_trunk_dto import EthTrunkDto
from .eth_trunk_interfaces_dto import EthTrunkInterfacesDto
from .eth_trunk_response_dto import EthTrunkResponseDto
from .failed_operation import FailedOperation
from .failed_operation_dto import FailedOperationDto
from .failed_oper_dto import FailedOperDto
from .fail_bean import FailBean
from .fail_list_dto import FailListDto
from .fan_info_dto import FanInfoDto
from .feature_item_state_dto import FeatureItemStateDto
from .feature_state_dto import FeatureStateDto
from .file_info_model import FileInfoModel
from .fit_ap_info import FitApInfo
from .floor_details import FloorDetails
from .floor_dto import FloorDto
from .floor_location_details import FloorLocationDetails
from .flow_distr_model import FlowDistrModel
from .flow_distr_resp import FlowDistrResp
from .frame_res_data import FrameResData
from .frame_res_response import FrameResResponse
from .fw_failed_operation_dto import FwFailedOperationDto
from .fw_nat_delete_dto import FwNatDeleteDto
from .fw_nat_delete_response_dto import FwNatDeleteResponseDto
from .fw_nat_delete_response_fail_dto import FwNatDeleteResponseFailDto
from .fw_nat_info_dto import FwNatInfoDto
from .fw_nat_response_dto import FwNatResponseDto
from .fw_route_info import FwRouteInfo
from .fw_static_route_delete_dto import FwStaticRouteDeleteDto
from .fw_static_route_delete_response_dto import FwStaticRouteDeleteResponseDto
from .fw_static_route_delete_response_fail_dto import FwStaticRouteDeleteResponseFailDto
from .fw_static_route_info_dto import FwStaticRouteInfoDto
from .fw_static_route_response_dto import FwStaticRouteResponseDto
from .get_ar_staticroute_response_dto import GetArStaticrouteResponseDto
from .get_board_response_dto import GetBoardResponseDto
from .get_fan_info_output_dto import GetFanInfoOutputDto
from .get_fw_nat_response_dto import GetFwNatResponseDto
from .get_fw_static_route_response_dto import GetFwStaticRouteResponseDto
from .get_local_user_infos_response import GetLocalUserInfosResponse
from .get_poe_power_state_resp import GetPoePowerStateResp
from .get_policy_response import GetPolicyResponse
from .get_portal_page_rule_output_dto import GetPortalPageRuleOutputDto
from .get_power_info_output_dto import GetPowerInfoOutputDto
from .get_radius_temp_response_dto import GetRadiusTempResponseDto
from .get_reboot_status_resp import GetRebootStatusResp
from .get_reset_reason_output_dto import GetResetReasonOutputDto
from .get_response_dto import GetResponseDto
from .get_site_list_dto import GetSiteListDto
from .get_site_temp_dto import GetSiteTempDto
from .get_site_temp_response_dto import GetSiteTempResponseDto
from .get_stp_protection_response_dto import GetStpProtectionResponseDto
from .get_system_power_info_output_dto import GetSystemPowerInfoOutputDto
from .get_tacacs_config_response import GetTacacsConfigResponse
from .get_tacacs_tmpl_response import GetTacacsTmplResponse
from .get_usergroups_output_dto import GetUsergroupsOutputDto
from .group_radio2g_config_dto import GroupRadio2gConfigDto
from .group_radio5g_config_dto import GroupRadio5gConfigDto
from .group_radio_config_api_dto import GroupRadioConfigApiDto
from .group_radio_config_responses_dto import GroupRadioConfigResponsesDto
from .group_radio_config_result_api_dto import GroupRadioConfigResultApiDto
from .ids import Ids
from .import_active_code_dto import ImportActiveCodeDto
from .import_active_code_out import ImportActiveCodeOut
from .import_active_code_out_data import ImportActiveCodeOutData
from .incre_mstp_region import IncreMstpRegion
from .incre_mstp_region_instance import IncreMstpRegionInstance
from .incre_region_instance_device import IncreRegionInstanceDevice
from .incre_stp_dto import IncreStpDto
from .inform_message import InformMessage
from .init_local_user_info_requst import InitLocalUserInfoRequst
from .init_local_user_info_response import InitLocalUserInfoResponse
from .interdiction_dto import InterdictionDTO
from .interfaces_info_output_dto import InterfacesInfoOutputDto
from .interface_info_dto import InterfaceInfoDto
from .iot_card_config_dto import IotCardConfigDto
from .iot_card_dto import IotCardDto
from .iot_card_operation_dto import IotCardOperationDto
from .iot_cmd_result_info import IotCmdResultInfo
from .iot_server1_dto import IotServer1Dto
from .io_t_config_dto import IoTConfigDto
from .io_t_config_response_dto import IoTConfigResponseDto
from .io_t_dto import IoTDto
from .io_t_response_dto import IoTResponseDto
from .ip_binding_mac_config_api_dto import IpBindingMacConfigApiDto
from .isolation_dto import IsolationDTO
from .it_change_message import ItChangeMessage
from .it_query_resonse import ItQueryResonse
from .lacp_lag_info_result_dto import LacpLagInfoResultDto
from .lacp_lag_info_result_dto_data import LacpLagInfoResultDtoData
from .link_data_model import LinkDataModel
from .link_info_bo import LinkInfoBo
from .link_model_for_web_notify import LinkModelForWebNotify
from .local_user_security_info_dto import LocalUserSecurityInfoDto
from .located_device_details import LocatedDeviceDetails
from .located_device_info import LocatedDeviceInfo
from .lsw_auth_config import LswAuthConfig
from .lsw_auth_config_core import LswAuthConfigCore
from .lsw_auth_config_profile import LswAuthConfigProfile
from .lsw_auth_config_profile_core import LswAuthConfigProfileCore
from .lsw_auth_config_response import LswAuthConfigResponse
from .lsw_auth_delete_dto import LswAuthDeleteDto
from .lsw_device_info import LswDeviceInfo
from .lsw_eth_port_dto import LSWEthPortDto
from .lsw_eth_trunk_port_dto import LSWEthTrunkPortDto
from .lsw_eth_trunk_port_resp_dto import LSWEthTrunkPortRespDto
from .lsw_get_eth_port_dto import LSWGetEthPortDto
from .lsw_get_eth_trunk_port_dto import LSWGetEthTrunkPortDto
from .lsw_get_port_dto import LSWGetPortDto
from .lsw_global_vlan_all_resp_dto import LswGlobalVlanAllRespDto
from .lsw_global_vlan_del_resp_dto import LswGlobalVlanDelRespDto
from .lsw_global_vlan_dto import LswGlobalVlanDto
from .lsw_global_vlan_failed_operation import LswGlobalVlanFailedOperation
from .lsw_global_vlan_response_dto import LswGlobalVlanResponseDto
from .lsw_global_vlan_update_dto import LswGlobalVlanUpdateDto
from .lsw_interface_info import LswInterfaceInfo
from .lsw_port_dto import LSWPortDto
from .lsw_stp_protection_get_dto import LSWStpProtectionGetDto
from .mac_data_list import MacDataList
from .mac_input_dto import MacInputDto
from .mac_output_dto import MacOutputDto
from .mgmt_vlan_dto import MgmtVlanDto
from .mgmt_vlan_response_dto import MgmtVlanResponseDto
from .modify_device_bean import ModifyDeviceBean
from .modify_device_data_bean import ModifyDeviceDataBean
from .modify_device_dto import ModifyDeviceDto
from .mstp_region import MstpRegion
from .mstp_region_instance import MstpRegionInstance
from .nat_session_log_config_param import NatSessionLogConfigParam
from .nat_session_log_config_result import NatSessionLogConfigResult
from .neighbors_info_dto import NeighborsInfoDto
from .neighbors_info_result_dto import NeighborsInfoResultDto
from .neighbors_info_result_dto_data import NeighborsInfoResultDtoData
from .network_traffic import NetworkTraffic
from .network_traffic_resp import NetworkTrafficResp
from .ne_detail_info import NeDetailInfo
from .ne_list_open_api_response import NeListOpenApiResponse
from .north_response import NorthResponse
from .north_rest_response import NorthRestResponse
from .open_ap_iot_command_in import OpenApIotCommandIn
from .open_ap_iot_command_out import OpenApIotCommandOut
from .ot_point_res_data import OTPointResData
from .ot_point_res_response import OTPointResResponse
from .period_reboot_device_resp import PeriodRebootDeviceResp
from .ping_diagnose_dto import PingDiagnoseDto
from .ping_reply_response import PingReplyResponse
from .ping_reply_result import PingReplyResult
from .ping_reply_result_ping_reply import PingReplyResultPingReply
from .ping_reply_single import PingReplySingle
from .ping_task_diagnose import PingTaskDiagnose
from .ping_task_response import PingTaskResponse
from .pkg import Pkg
from .poe_power_state_data import PoePowerStateData
from .policy_config import PolicyConfig
from .policy_config_res import PolicyConfigRes
from .policy_content_dto import PolicyContentDto
from .policy_device_cancel_input_list import PolicyDeviceCancelInputList
from .policy_hits_dto import PolicyHitsDTO
from .policy_hits_list_builder import PolicyHitsListBuilder
from .policy_site_cancel_input_list import PolicySiteCancelInputList
from .policy_site_input import PolicySiteInput
from .portal_content import PortalContent
from .portal_content_dto import PortalContentDto
from .portal_online_user_info_dto import PortalOnlineUserInfoDto
from .portal_page_rule_output_data import PortalPageRuleOutputData
from .port_res_data import PortResData
from .port_res_response import PortResResponse
from .power_info_dto import PowerInfoDto
from .power_supply_dto import PowerSupplyDto
from .power_supply_output_dto import PowerSupplyOutputDto
from .ppsk_base_dto import PPSKBaseDto
from .ppsk_delete_response_dto import PpskDeleteResponseDto
from .ppsk_get_response_dto import PpskGetResponseDto
from .ppsk_info_dto import PPSKInfoDto
from .ppsk_post_or_put_response_dto import PpskPostOrPutResponseDto
from .ppsk_post_request_dto import PPSKPostRequestDto
from .ppsk_put_request_dto import PPSKPutRequestDto
from .ppsk_response_dto import PPSKResponseDto
from .prohibited_attribute import ProhibitedAttribute
from .put_response_dto import PutResponseDto
from .put_response_fail_dto import PutResponseFailDto
from .query_acl_ret import QueryAclRet
from .query_buildings_response import QueryBuildingsResponse
from .query_cmd_result_out import QueryCmdResultOut
from .query_device_location_info_response import QueryDeviceLocationInfoResponse
from .query_floors_response import QueryFloorsResponse
from .query_floor_details_response import QueryFloorDetailsResponse
from .query_floor_location_details_response import QueryFloorLocationDetailsResponse
from .query_hits_response_dto import QueryHitsResponseDTO
from .query_link_list_param import QueryLinkListParam
from .query_located_device_details_response import QueryLocatedDeviceDetailsResponse
from .query_portal_online_user_info_output_dto import QueryPortalOnlineUserInfoOutputDto
from .query_response import QueryResponse
from .query_response_data import QueryResponseData
from .query_sites_out import QuerySitesOut
from .query_sites_out_data import QuerySitesOutData
from .query_ssid_response import QuerySsidResponse
from .query_status_response_dto import QueryStatusResponseDTO
from .radio_country_channel_dto import RadioCountryChannelDto
from .radio_country_channel_result import RadioCountryChannelResult
from .radius_content_dto import RadiusContentDto
from .radius_temp_dto import RadiusTempDto
from .radius_temp_dto_called_station_id import RadiusTempDtoCalledStationId
from .radius_temp_dto_master_account_server import RadiusTempDtoMasterAccountServer
from .radius_temp_dto_master_auth_server import RadiusTempDtoMasterAuthServer
from .radius_temp_dto_prohibit_attribute import RadiusTempDtoProhibitAttribute
from .radius_temp_dto_realtime_accounting import RadiusTempDtoRealtimeAccounting
from .radius_temp_dto_slave_account_server import RadiusTempDtoSlaveAccountServer
from .radius_temp_dto_slave_auth_server import RadiusTempDtoSlaveAuthServer
from .radius_temp_response_dto import RadiusTempResponseDto
from .rate_limit_content_dto import RateLimitContentDto
from .reboot_status_data import RebootStatusData
from .region_instance_device import RegionInstanceDevice
from .registry_info import RegistryInfo
from .replace_device_dto import ReplaceDeviceDto
from .replace_original_device_dto import ReplaceOriginalDeviceDto
from .reriod_reboot_device_param import ReriodRebootDeviceParam
from .reset_board_output_dto import ResetBoardOutputDto
from .reset_chassis_output_dto import ResetChassisOutputDto
from .reset_device_failed_dto import ResetDeviceFailedDto
from .reset_device_request import ResetDeviceRequest
from .reset_device_response import ResetDeviceResponse
from .reset_device_result import ResetDeviceResult
from .reset_device_success_dto import ResetDeviceSuccessDto
from .reset_reason_dto import ResetReasonDto
from .response import Response
from .response_base_dto import ResponseBaseDto
from .response_dto import ResponseDto
from .restart_policy_dto import RestartPolicyDto
from .reupgrade_request_body import ReupgradeRequestBody
from .route_info import RouteInfo
from .rule_list import RuleList
from .security_policy_config_dto import SecurityPolicyConfigDto
from .security_url_filter_dto import SecurityUrlFilterDto
from .service_list_info_dto import ServiceListInfoDto
from .site_ap_info import SiteApInfo
from .site_health_output import SiteHealthOutput
from .site_health_output_dto import SiteHealthOutputDto
from .site_list_dto import SiteListDto
from .site_station_statistic_info import SiteStationStatisticInfo
from .site_station_statistic_resp import SiteStationStatisticResp
from .site_template_and_site_list_response_dto import SiteTemplateAndSiteListResponseDto
from .site_template_and_site_list_response_dto_fail import SiteTemplateAndSiteListResponseDtoFail
from .site_template_auth_content_dto import SiteTemplateAuthContentDto
from .site_template_config_ssid_response import SiteTemplateConfigSsidResponse
from .site_template_delete_ssid_response import SiteTemplateDeleteSsidResponse
from .site_template_group_radio_dto import SiteTemplateGroupRadioDto
from .site_template_group_radio_response_dto import SiteTemplateGroupRadioResponseDto
from .site_template_policy_content_dto import SiteTemplatePolicyContentDto
from .site_template_portal_content_dto import SiteTemplatePortalContentDto
from .site_template_query_ssid_response import SiteTemplateQuerySsidResponse
from .site_template_radius_content_dto import SiteTemplateRadiusContentDto
from .site_template_rate_limit_content_dto import SiteTemplateRateLimitContentDto
from .site_template_security_policy_config_dto import SiteTemplateSecurityPolicyConfigDto
from .site_template_security_url_filter_dto import SiteTemplateSecurityUrlFilterDto
from .site_template_snmp_dto import SiteTemplateSnmpDto
from .site_template_snmp_response_dto import SiteTemplateSnmpResponseDto
from .site_template_ssid_config_dto import SiteTemplateSsidConfigDto
from .site_template_ssid_config_out import SiteTemplateSsidConfigOut
from .site_template_ssid_delete_dto import SiteTemplateSsidDeleteDto
from .site_template_ssid_delete_fail_result import SiteTemplateSsidDeleteFailResult
from .site_template_vlan_dto import SiteTemplateVlanDto
from .site_temp_dto import SiteTempDto
from .site_temp_response_dto import SiteTempResponseDto
from .slot_res_data import SlotResData
from .slot_res_response import SlotResResponse
from .ssh_first_enable_dto import SSHFirstEnableDto
from .ssh_first_enable_response_dto import SSHFirstEnableResponseDto
from .ssid_config_dto import SsidConfigDto
from .ssid_config_out import SsidConfigOut
from .ssid_delete_dto import SsidDeleteDto
from .ssid_delete_fail_result import SsidDeleteFailResult
from .stack_member_input import StackMemberInput
from .stack_member_output import StackMemberOutput
from .state_response_dto import StateResponseDto
from .station_data_resp import StationDataResp
from .station_info import StationInfo
from .stp_dto import StpDto
from .stp_protection_dto import StpProtectionDto
from .stp_protection_fail_dto import StpProtectionFailDto
from .stp_protection_out_dto import StpProtectionOutDto
from .stp_protection_request_dto import StpProtectionRequestDto
from .stp_protection_response_dto import StpProtectionResponseDto
from .stp_protection_view_dto import StpProtectionViewDto
from .stp_response_dto import StpResponseDto
from .subscribe_response import SubscribeResponse
from .sub_slot_res_data import SubSlotResData
from .sub_slot_res_response import SubSlotResResponse
from .success_bean import SuccessBean
from .switchover_output_dto import SwitchoverOutputDto
from .system_power_info_dto import SystemPowerInfoDto
from .tacacs_server_info import TacacsServerInfo
from .tacacs_tmpl_common_info_dto import TacacsTmplCommonInfoDto
from .tacacs_tmpl_info_dto import TacacsTmplInfoDto
from .tag_dto import TagDto
from .target_hosts_dto import TargetHostsDto
from .template_result_dto import TemplateResultDto
from .tenancy_config_api_dto import TenancyConfigApiDto
from .tenant_common_dto import TenantCommonDto
from .tenant_data import TenantData
from .tenant_list_dto import TenantListDto
from .third_user_info_data import ThirdUserInfoData
from .timezone_dto import TimezoneDto
from .timezone_resp_dto import TimezoneRespDto
from .time_config_dto import TimeConfigDto
from .time_config_resp_dto import TimeConfigRespDto
from .time_flow_configs_output_dto import TimeFlowConfigsOutputDto
from .time_flow_config_common import TimeFlowConfigCommon
from .time_flow_config_delete_dto import TimeFlowConfigDeleteDto
from .time_flow_config_output_dto import TimeFlowConfigOutputDto
from .time_flow_st_detail_infos_output_dto import TimeFlowStDetailInfosOutputDto
from .time_flow_st_infos_output_dto import TimeFlowStInfosOutputDto
from .time_info import TimeInfo
from .time_template_dto import TimeTemplateDto
from .token_dto import TokenDto
from .token_dto_wrapper import TokenDtoWrapper
from .top_nssid_traffic_dto import TopNSSIDTrafficDto
from .top_nssid_traffic_list_dto import TopNSSIDTrafficListDto
from .trace_diagnose_dto import TraceDiagnoseDto
from .trace_hop_diagnose import TraceHopDiagnose
from .trace_hop_diagnose_trace_probe_list import TraceHopDiagnoseTraceProbeList
from .trace_probe_diagnose import TraceProbeDiagnose
from .trace_reply_response import TraceReplyResponse
from .trace_reply_result import TraceReplyResult
from .trace_reply_result_trace_hop_list import TraceReplyResultTraceHopList
from .trace_task_diagnose import TraceTaskDiagnose
from .trace_task_response import TraceTaskResponse
from .traffic_statistic_data_resp import TrafficStatisticDataResp
from .traffic_statistic_info import TrafficStatisticInfo
from .upadate_acl_dto import UpadateAclDto
from .update_acl_ret import UpdateAclRet
from .update_local_user_info_requst import UpdateLocalUserInfoRequst
from .update_local_user_info_response import UpdateLocalUserInfoResponse
from .update_portal_page_rule_input_dto import UpdatePortalPageRuleInputDto
from .update_radius_temp_dto import UpdateRadiusTempDto
from .update_radius_temp_response_dto import UpdateRadiusTempResponseDto
from .update_sites_dto import UpdateSitesDto
from .update_sites_out import UpdateSitesOut
from .update_sites_out_data import UpdateSitesOutData
from .update_site_temp_dto import UpdateSiteTempDto
from .update_site_temp_response_dto import UpdateSiteTempResponseDto
from .update_tacacs_tmpl_info_dto import UpdateTacacsTmplInfoDto
from .update_usergroup_input_dto import UpdateUsergroupInputDto
from .upgrade_detail import UpgradeDetail
from .upgrade_policydetail import UpgradePolicydetail
from .upgrade_policy_dto import UpgradePolicyDto
from .up_path import UpPath
from .usergroup_output_dto import UsergroupOutputDto
from .user_authorization_input_dto import UserAuthorizationInputDto
from .user_auth_input_dto import UserAuthInputDto
from .user_auth_output_dto import UserAuthOutputDto
from .user_auth_output_dto_data import UserAuthOutputDtoData
from .user_common_info import UserCommonInfo
from .user_dto import UserDto
from .user_infos_dto import UserInfosDto
from .user_logout_input_dto import UserLogoutInputDto
from .vlan_dto import VlanDto
from .wac_fit_ap_dto import WACFitApDto
from .wac_fit_ap_response_dto import WACFitApResponseDto
from .wac_fit_query_response_dto import WACFitQueryResponseDto
