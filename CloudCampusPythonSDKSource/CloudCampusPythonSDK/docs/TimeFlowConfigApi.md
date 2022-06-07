# swagger_client.TimeFlowConfigApi

All URIs are relative to *https://localhost/controller/campus/v1/authconfigservice/accessconfig*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_time_flow_config**](TimeFlowConfigApi.md#add_time_flow_config) | **POST** /controller/campus/v1/authconfigservice/accessconfig/timeflowconfig | 新增计费策略
[**del_time_flow_config**](TimeFlowConfigApi.md#del_time_flow_config) | **POST** /controller/campus/v1/authconfigservice/accessconfig/timeflowconfig/batch-delete | 删除计费策略
[**get_time_flow_config**](TimeFlowConfigApi.md#get_time_flow_config) | **GET** /controller/campus/v1/authconfigservice/accessconfig/timeflowconfig | 查询计费策略
[**modify_time_flow_config**](TimeFlowConfigApi.md#modify_time_flow_config) | **PUT** /controller/campus/v1/authconfigservice/accessconfig/timeflowconfig/{id} | 修改计费策略


# **add_time_flow_config**
> TimeFlowConfigsOutputDto add_time_flow_config(body)

新增计费策略

## 操作场景 ##  提供新增计费策略北向接口。 ## 接口功能 ##  为指定的租户的站点新增计费策略。 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeFlowConfigApi()
body = cloudcampus.TimeFlowConfigCommon() # TimeFlowConfigCommon | 计费信息。

try: 
    # 新增计费策略
    api_response = api_instance.add_time_flow_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeFlowConfigApi->add_time_flow_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeFlowConfigCommon**](TimeFlowConfigCommon.md)| 计费信息。 | 

### Return type

[**TimeFlowConfigsOutputDto**](TimeFlowConfigsOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_time_flow_config**
> DeleteTimeFlowConfigOutputDto del_time_flow_config(body)

删除计费策略

## 操作场景 ##  提供删除计费策略北向接口。 ## 接口功能 ##  为指定的租户的站点删除计费策略。 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeFlowConfigApi()
body = cloudcampus.TimeFlowConfigDeleteDto() # TimeFlowConfigDeleteDto | 删除条件，策略ID列表。

try: 
    # 删除计费策略
    api_response = api_instance.del_time_flow_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeFlowConfigApi->del_time_flow_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeFlowConfigDeleteDto**](TimeFlowConfigDeleteDto.md)| 删除条件，策略ID列表。 | 

### Return type

[**DeleteTimeFlowConfigOutputDto**](DeleteTimeFlowConfigOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_flow_config**
> TimeFlowConfigsOutputDto get_time_flow_config(site_id, id=id, time_flow_name=time_flow_name)

查询计费策略

## 操作场景 ##  提供查询计费策略北向接口。 ## 接口功能 ##  查询计费策略。 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeFlowConfigApi()
site_id = '75f8ed0f-810a-4ff5-8e64-67c81312d01c' # str | 站点ID，UUID格式。
id = '75f8ed0f810a4ff58e6467c81312d01c' # str | 计费策略ID，UUID格式。 (optional)
time_flow_name = 'policy' # str | 计费策略名称，模糊查询。 (optional)

try: 
    # 查询计费策略
    api_response = api_instance.get_time_flow_config(site_id, id=id, time_flow_name=time_flow_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeFlowConfigApi->get_time_flow_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| 站点ID，UUID格式。 | 
 **id** | **str**| 计费策略ID，UUID格式。 | [optional] 
 **time_flow_name** | **str**| 计费策略名称，模糊查询。 | [optional] 

### Return type

[**TimeFlowConfigsOutputDto**](TimeFlowConfigsOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_time_flow_config**
> CommonTimeFlowConfigDto modify_time_flow_config(id, body)

修改计费策略

## 操作场景 ##  提供修改计费策略北向接口。 ## 接口功能 ##  为指定的租户的站点修改计费策略。 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.TimeFlowConfigApi()
id = '75f8ed0f810a4ff58e6467c81312d01c' # str | 修改条件，计费策略ID。
body = cloudcampus.TimeFlowConfigCommon() # TimeFlowConfigCommon | 修改内容。

try: 
    # 修改计费策略
    api_response = api_instance.modify_time_flow_config(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeFlowConfigApi->modify_time_flow_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 修改条件，计费策略ID。 | 
 **body** | [**TimeFlowConfigCommon**](TimeFlowConfigCommon.md)| 修改内容。 | 

### Return type

[**CommonTimeFlowConfigDto**](CommonTimeFlowConfigDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

