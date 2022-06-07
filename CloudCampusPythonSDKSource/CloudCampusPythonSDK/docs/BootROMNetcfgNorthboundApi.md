# swagger_client.BootROMNetcfgNorthboundApi

All URIs are relative to *https://localhost/controller/campus/v1/networkservice/networkconfig/net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_init_boot_rom**](BootROMNetcfgNorthboundApi.md#config_init_boot_rom) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/bootrom | 配置租户BootROM密码
[**update_site_boot_rom_config**](BootROMNetcfgNorthboundApi.md#update_site_boot_rom_config) | **PUT** /controller/campus/v1/networkservice/networkconfig/net/bootrom/sites/{siteId}/bootrom | 配置站点BootROM密码


# **config_init_boot_rom**
> BootRomResponse config_init_boot_rom(body)

配置租户BootROM密码

## 典型场景 ##    提供配置租户BootROM密码的接口。 ## 接口功能 ##    配置租户设备BootROM密码。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.BootROMNetcfgNorthboundApi()
body = cloudcampus.BootRomDto() # BootRomDto | 配置租户BootROM密码。

try: 
    # 配置租户BootROM密码
    api_response = api_instance.config_init_boot_rom(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootROMNetcfgNorthboundApi->config_init_boot_rom: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BootRomDto**](BootRomDto.md)| 配置租户BootROM密码。 | 

### Return type

[**BootRomResponse**](BootRomResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_boot_rom_config**
> BootRomResponse update_site_boot_rom_config(site_id, boot_rom_dto)

配置站点BootROM密码

## 典型场景 ##    提供配置站点下BootROM密码的接口。 ## 接口功能 ##    配置站点下设备BootROM密码。 ## 接口约束 ##    只有租户管理员获取token并建立会话后才能调用该接口。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.BootROMNetcfgNorthboundApi()
site_id = 'fbb684c8-0d37-496f-bafa-4b06d5151e2e' # str | 站点标识，UUID格式。
boot_rom_dto = cloudcampus.BootRomDto() # BootRomDto | 配置的设备BootROM密码。

try: 
    # 配置站点BootROM密码
    api_response = api_instance.update_site_boot_rom_config(site_id, boot_rom_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootROMNetcfgNorthboundApi->update_site_boot_rom_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点标识，UUID格式。 | 
 **boot_rom_dto** | [**BootRomDto**](BootRomDto.md)| 配置的设备BootROM密码。 | 

### Return type

[**BootRomResponse**](BootRomResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

