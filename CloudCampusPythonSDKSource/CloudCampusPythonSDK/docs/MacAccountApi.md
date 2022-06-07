# swagger_client.MacAccountApi

All URIs are relative to *https://localhost/controller/campus/v1/accountservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mac_account**](MacAccountApi.md#create_mac_account) | **POST** /controller/campus/v1/accountservice/mac | 创建mac账号
[**delete_mac_account**](MacAccountApi.md#delete_mac_account) | **POST** /controller/campus/v1/accountservice/mac/action/batch-delete | 删除mac帐号
[**get_mac_account_list**](MacAccountApi.md#get_mac_account_list) | **GET** /controller/campus/v1/accountservice/mac | 查询mac帐号
[**update_mac_account**](MacAccountApi.md#update_mac_account) | **PUT** /controller/campus/v1/accountservice/mac/{id} | 修改mac帐号


# **create_mac_account**
> DataMacDto create_mac_account(body)

创建mac账号

## 典型场景 ##    创建mac帐号。 ## 接口功能 ##    创建mac帐号。 ## 接口约束 ##    该接口支持北向操作管理员访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.MacAccountApi()
body = cloudcampus.MacInputDto() # MacInputDto | mac账号信息。

try: 
    # 创建mac账号
    api_response = api_instance.create_mac_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MacAccountApi->create_mac_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MacInputDto**](MacInputDto.md)| mac账号信息。 | 

### Return type

[**DataMacDto**](DataMacDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mac_account**
> DeleteMacsOutput delete_mac_account(body)

删除mac帐号

## 典型场景 ##    删除mac帐号。 ## 接口功能 ##    批量删除mac帐号。 ## 接口约束 ##    该接口支持北向操作管理员访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.MacAccountApi()
body = cloudcampus.Ids() # Ids | 待删除的mac帐号列表。

try: 
    # 删除mac帐号
    api_response = api_instance.delete_mac_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MacAccountApi->delete_mac_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ids**](Ids.md)| 待删除的mac帐号列表。 | 

### Return type

[**DeleteMacsOutput**](DeleteMacsOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mac_account_list**
> MacDataList get_mac_account_list(page_index=page_index, page_size=page_size, search_name=search_name, id=id)

查询mac帐号

## 典型场景 ##    查询mac帐号。 ## 接口功能 ##    查询mac帐号。 ## 接口约束 ##    1、该接口支持北向操作管理员访问，必须在用户会话建立后使用。    2、pageSize默认按照1000进行分页。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.MacAccountApi()
page_index = 1 # int | 页面索引。 (optional)
page_size = 20 # int | 页面大小。 (optional)
search_name = 'mac' # str | 名称搜索关键词。该字段支持模糊查询。 (optional)
id = 'a91e1696-02a2-4a68-bad4-aa639359c8cf' # str | mac帐号ID，UUID格式。 (optional)

try: 
    # 查询mac帐号
    api_response = api_instance.get_mac_account_list(page_index=page_index, page_size=page_size, search_name=search_name, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MacAccountApi->get_mac_account_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_index** | **int**| 页面索引。 | [optional] 
 **page_size** | **int**| 页面大小。 | [optional] 
 **search_name** | **str**| 名称搜索关键词。该字段支持模糊查询。 | [optional] 
 **id** | **str**| mac帐号ID，UUID格式。 | [optional] 

### Return type

[**MacDataList**](MacDataList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mac_account**
> DataMacDto update_mac_account(id, body)

修改mac帐号

## 典型场景 ##    修改mac帐号。 ## 接口功能 ##    修改mac帐号。 ## 接口约束 ##    1、该接口支持北向操作管理员访问，必须在用户会话建立后使用。    2、该接口为全量修改接口，按照最新的入参进行全量覆盖。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.MacAccountApi()
id = 'a91e1696-02a2-4a68-bad4-aa639359c8cf' # str | mac帐号ID，UUID格式。
body = cloudcampus.MacInputDto() # MacInputDto | 修改mac帐号信息。

try: 
    # 修改mac帐号
    api_response = api_instance.update_mac_account(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MacAccountApi->update_mac_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| mac帐号ID，UUID格式。 | 
 **body** | [**MacInputDto**](MacInputDto.md)| 修改mac帐号信息。 | 

### Return type

[**DataMacDto**](DataMacDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

