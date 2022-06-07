# UpPath

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_model** | **str** | 设备款型。 | 
**target_software_id** | **str** | 目标软件版本ID。从/version这个接口的返回的pkgList获取。targetSoftwareId和targetPatchId至少填一个。 | [optional] 
**target_patch_id** | **str** | 目标补丁ID。从/version这个接口的返回的pkgPatchMap获取。targetSoftwareId和targetPatchId至少填一个。 | [optional] 
**is_uninstall** | **int** | 是否卸载旧补丁。 1：是 0：否  | [optional] 
**status** | **int** | 升级状态。查询站点升级计划和详情时返回。 0：未创建升级任务 1：无需升级 2：升级成功 3：升级失败 4：下载完成 5：升级中 创建多站点升级计划时无需填写。  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


