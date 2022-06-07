# swagger_client.SysconfigServiceApi

All URIs are relative to *https://localhost/controller/campus/v3/configresource*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_radio_country_channel**](SysconfigServiceApi.md#get_radio_country_channel) | **GET** /controller/campus/v3/configresource/channels | 查询射频管理国家码


# **get_radio_country_channel**
> RadioCountryChannelResult get_radio_country_channel()

查询射频管理国家码

## 典型场景 ##  查询射频管理国家码。 ## 接口功能 ##  查询射频管理国家码。 ## 接口约束 ##  该接口权限点位于“云管理>开放接口>国家码信道”。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.SysconfigServiceApi()

try: 
    # 查询射频管理国家码
    api_response = api_instance.get_radio_country_channel()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SysconfigServiceApi->get_radio_country_channel: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RadioCountryChannelResult**](RadioCountryChannelResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

