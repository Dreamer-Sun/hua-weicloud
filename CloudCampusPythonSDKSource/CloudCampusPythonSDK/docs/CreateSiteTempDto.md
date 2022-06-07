# CreateSiteTempDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 站点模板名称（不支持包括特殊字符&#39; , : \&quot;  ^ / &lt; &gt; &#x3D; &amp; % # ? + ! ）几项。 | 
**types** | **list[str]** | 站点模板类型列表，可为AP，LSW，FW。 | 
**custom** | **bool** | 是否定制特性。 | [optional] [default to False]
**config_identifies** | **list[str]** | \&quot;当custom为true时必填且不能为空，支持定制的特性，和站点模板类型有对应关系（所有站点模板类型都支持定制通用配置特性：   snmp -- SNMP、   clientdata -- 运维配置(O&amp;M Parameters)、   bootrom -- BootROM、   time -- NTP时间(NTP Time)、   initloginuser -- 本地用户(Local User)； AP站点模板类型单独支持定制特性：   apssid -- AP SSID、   groupradio -- 射频(Radio)； FW站点模板类型单独支持定制特性：   fwtrafficpolicy -- 流量策略(Traffic Policy)、   fwsecureauth -- 认证(Authentication)、   fwssid -- FW SSID、   fwsecuritypolicy -- 安全策略(Security Policy)； LSW站点模板类型无单独支持的定制特性）。\&quot;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


