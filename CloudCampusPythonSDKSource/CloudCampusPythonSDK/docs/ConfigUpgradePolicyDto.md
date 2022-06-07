# ConfigUpgradePolicyDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | **str** | 站点标识，UUID格式。 | 
**upgrade_regularly** | **bool** | 策略是否为周期升级。当upgradeRegularly为true时，upgradeImmediately必须为false；当upgradeRegularly为false时，upgradeImmediately必须为true。 | 
**upgrade_immediately** | **bool** | 策略是否为立即升级。当upgradeImmediately为true时，upgradeRegularly必须为false;当upgradeImmediately为false时，upgradeRegularly必须为true。 | 
**upgrade_day** | **str** | 策略为周期升级时，周几升级。当upgradeRegularly为true时，upgradeDay生效且必填。 | [optional] 
**upgrade_time** | **str** | 策略为周期升级时，升级的时间点。当upgradeRegularly为true时，upgradeTime生效且必填。 | [optional] 
**signature_database_types** | **list[str]** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


