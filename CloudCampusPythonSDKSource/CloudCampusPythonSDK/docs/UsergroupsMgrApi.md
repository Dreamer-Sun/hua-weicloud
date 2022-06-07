# swagger_client.UsergroupsMgrApi

All URIs are relative to *https://localhost/controller/campus/v1/accountservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_usergroup**](UsergroupsMgrApi.md#add_usergroup) | **POST** /controller/campus/v1/accountservice/usergroups | 新增用户组
[**del_usergroups**](UsergroupsMgrApi.md#del_usergroups) | **DELETE** /controller/campus/v1/accountservice/usergroups/{id} | 删除用户组
[**get_usergroups**](UsergroupsMgrApi.md#get_usergroups) | **GET** /controller/campus/v1/accountservice/usergroups | 查询用户组
[**update_usergroup**](UsergroupsMgrApi.md#update_usergroup) | **PUT** /controller/campus/v1/accountservice/usergroups/{id} | 修改用户组


# **add_usergroup**
> AddUsergroupOutputDto add_usergroup(body)

新增用户组

## 典型场景 ##  提供新增用户组北向接口。 ## 接口功能 ##  新增用户组 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。 

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UsergroupsMgrApi()
body = cloudcampus.AddUsergroupInputDto() # AddUsergroupInputDto | 用户组结构。

try: 
    # 新增用户组
    api_response = api_instance.add_usergroup(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupsMgrApi->add_usergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddUsergroupInputDto**](AddUsergroupInputDto.md)| 用户组结构。 | 

### Return type

[**AddUsergroupOutputDto**](AddUsergroupOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_usergroups**
> DeleteUsergroupOutputDto del_usergroups(id)

删除用户组

## 典型场景 ##  提供删除用户组北向接口。 ## 接口功能 ##  删除指定的用户组 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UsergroupsMgrApi()
id = 'a91e1696-02a2-4a68-bad4-aa639359c8cf' # str | 用户组ID，UUID格式。

try: 
    # 删除用户组
    api_response = api_instance.del_usergroups(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupsMgrApi->del_usergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 用户组ID，UUID格式。 | 

### Return type

[**DeleteUsergroupOutputDto**](DeleteUsergroupOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usergroups**
> GetUsergroupsOutputDto get_usergroups(user_group_id=user_group_id, user_group_name=user_group_name, is_contain_sub_group=is_contain_sub_group, page_index=page_index, page_size=page_size, sort=sort)

查询用户组

## 典型场景 ##  提供查询用户组北向接口。 ## 接口功能 ##  查询用户组 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UsergroupsMgrApi()
user_group_id = 'a91e1696-02a2-4a68-bad4-aa639359c8cf' # str | 用户组ID，UUID格式。 (optional)
user_group_name = 'user' # str | 用户组名，支持模糊查询。 (optional)
is_contain_sub_group = false # bool | 是否包含子用户组，该变量需要和userGroupId一起使用，主要用于查询指定用户组下子部门（只包含当前指定用户组下一层子用户组，更下层的不包含）。 (optional)
page_index = 1 # int | 页面索引。 (optional)
page_size = 40 # int | 页面大小。 (optional)
sort = 'userGroupName' # str | 排序字段仅支持‘userGroupName’ +表示升序，-表示降序，默认用升序。 (optional)

try: 
    # 查询用户组
    api_response = api_instance.get_usergroups(user_group_id=user_group_id, user_group_name=user_group_name, is_contain_sub_group=is_contain_sub_group, page_index=page_index, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupsMgrApi->get_usergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| 用户组ID，UUID格式。 | [optional] 
 **user_group_name** | **str**| 用户组名，支持模糊查询。 | [optional] 
 **is_contain_sub_group** | **bool**| 是否包含子用户组，该变量需要和userGroupId一起使用，主要用于查询指定用户组下子部门（只包含当前指定用户组下一层子用户组，更下层的不包含）。 | [optional] 
 **page_index** | **int**| 页面索引。 | [optional] 
 **page_size** | **int**| 页面大小。 | [optional] 
 **sort** | **str**| 排序字段仅支持‘userGroupName’ +表示升序，-表示降序，默认用升序。 | [optional] 

### Return type

[**GetUsergroupsOutputDto**](GetUsergroupsOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usergroup**
> CommonUsergroupOutputDto update_usergroup(id, body)

修改用户组

## 典型场景 ##  提供修改用户组北向接口。 ## 接口功能 ##  修改指定的用户组 ## 接口约束 ##  该接口支持北向管理员访问，必须在用户会话建立后使用。  

### Example 
```python
from __future__ import print_function
import time
import cloudcampus
from cloudcampus.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudcampus.UsergroupsMgrApi()
id = 'a91e1696-02a2-4a68-bad4-aa639359c8cf' # str | 用户组ID，UUID格式。
body = cloudcampus.UpdateUsergroupInputDto() # UpdateUsergroupInputDto | 用户组结构。

try: 
    # 修改用户组
    api_response = api_instance.update_usergroup(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsergroupsMgrApi->update_usergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 用户组ID，UUID格式。 | 
 **body** | [**UpdateUsergroupInputDto**](UpdateUsergroupInputDto.md)| 用户组结构。 | 

### Return type

[**CommonUsergroupOutputDto**](CommonUsergroupOutputDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

