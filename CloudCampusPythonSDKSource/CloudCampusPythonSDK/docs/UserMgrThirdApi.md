# swagger_client.UserMgrThirdApi

All URIs are relative to *https://localhost/controller/campus/v1/accountservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_third**](UserMgrThirdApi.md#add_user_third) | **POST** /controller/campus/v1/accountservice/users | 新增用户信息
[**delete_user_third**](UserMgrThirdApi.md#delete_user_third) | **POST** /controller/campus/v1/accountservice/users/batch-delete | 删除指定用户
[**get_user_third**](UserMgrThirdApi.md#get_user_third) | **GET** /controller/campus/v1/accountservice/users | 查询内置用户信息
[**update_user_third**](UserMgrThirdApi.md#update_user_third) | **PUT** /controller/campus/v1/accountservice/users/{id} | 修改用户信息


# **add_user_third**
> AddUserOutputDto add_user_third(body)

新增用户信息

## 典型场景 ##  提供新增用户北向接口。 ## 接口功能 ##  新增用户 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UserMgrThirdApi()
body = cloudcampus.AddUserInputDto() # AddUserInputDto | 用户结构。

try: 
    # 新增用户信息
    api_response = api_instance.add_user_third(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserMgrThirdApi->add_user_third: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddUserInputDto**](AddUserInputDto.md)| 用户结构。 | 

### Return type

[**AddUserOutputDto**](AddUserOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_third**
> DeleteUserOutputDto delete_user_third(body)

删除指定用户

## 典型场景 ##  提供删除用户北向接口。 ## 接口功能 ##  删除指定的用户 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UserMgrThirdApi()
body = cloudcampus.DeleteUserInputDto() # DeleteUserInputDto | 删除条件，用户ID。

try: 
    # 删除指定用户
    api_response = api_instance.delete_user_third(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserMgrThirdApi->delete_user_third: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteUserInputDto**](DeleteUserInputDto.md)| 删除条件，用户ID。 | 

### Return type

[**DeleteUserOutputDto**](DeleteUserOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_third**
> DataListDto get_user_third(user_group_id=user_group_id, user_name=user_name, email=email, is_contain_sub_group=is_contain_sub_group, page_index=page_index, page_size=page_size, sort_key=sort_key, sort_dir=sort_dir)

查询内置用户信息

## 典型场景 ##  提供通过用户组ID、用户帐号等查询内置用户信息。 ## 接口功能 ##  通过用户组ID、用户帐号等查询内置用户信息。 ## 接口约束 ##  该接口支持北向操作管理员管理访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UserMgrThirdApi()
user_group_id = '51cdcbe3-5e14-492b-ab27-86950b661d19' # str | 用户组ID。 (optional)
user_name = 'user' # str | 用户名称，支持模糊查询。 (optional)
email = 'aaa@huawei.com' # str | 用户邮箱。 (optional)
is_contain_sub_group = 'false' # str | 是否包含子用户组。 (optional)
page_index = 1 # int | 页面索引。 (optional)
page_size = 40 # int | 页面大小。 (optional)
sort_key = '' # str | 排序字段，默认是userName。 (optional)
sort_dir = '' # str | 升降序字段，支持ASC和DESC，默认是DESC。 (optional)

try: 
    # 查询内置用户信息
    api_response = api_instance.get_user_third(user_group_id=user_group_id, user_name=user_name, email=email, is_contain_sub_group=is_contain_sub_group, page_index=page_index, page_size=page_size, sort_key=sort_key, sort_dir=sort_dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserMgrThirdApi->get_user_third: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| 用户组ID。 | [optional] 
 **user_name** | **str**| 用户名称，支持模糊查询。 | [optional] 
 **email** | **str**| 用户邮箱。 | [optional] 
 **is_contain_sub_group** | **str**| 是否包含子用户组。 | [optional] 
 **page_index** | **int**| 页面索引。 | [optional] 
 **page_size** | **int**| 页面大小。 | [optional] 
 **sort_key** | **str**| 排序字段，默认是userName。 | [optional] 
 **sort_dir** | **str**| 升降序字段，支持ASC和DESC，默认是DESC。 | [optional] 

### Return type

[**DataListDto**](DataListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_third**
> CommonUserOutputDto update_user_third(id, body)

修改用户信息

## 典型场景 ##  提供修改用户北向接口。 ## 接口功能 ##  修改指定的用户 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UserMgrThirdApi()
id = '51cdcbe3-5e14-492b-ab27-86950b661d19' # str | 用户ID。
body = cloudcampus.UserCommonInfo() # UserCommonInfo | 用户信息。

try: 
    # 修改用户信息
    api_response = api_instance.update_user_third(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserMgrThirdApi->update_user_third: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 用户ID。 | 
 **body** | [**UserCommonInfo**](UserCommonInfo.md)| 用户信息。 | 

### Return type

[**CommonUserOutputDto**](CommonUserOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

