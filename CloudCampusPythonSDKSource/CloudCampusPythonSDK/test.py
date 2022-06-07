#!/usr/bin/python
import sys

from cloudcampus.api_client import ApiClient
from cloudcampus.configuration import Configuration
from cloudcampus.apis.site_manager_api import SiteManagerApi
from cloudcampus.apis.user_mgr_third_api import UserMgrThirdApi


def main():
    # 环境参数
    tenantName = 'campus@north.com'
    tenantPwd = 'jkq0kI03g@'
    host = '139.9.213.72'
    port = '18002'

    # 初始化apiClient
    # 自动设置token
    config = Configuration(host, port, tenantName, tenantPwd)
    api_client = ApiClient(config)

    # # 手动设置token
    # config = Configuration(host, port)
    # api_client = ApiClient(config)
    # api_client.isAutoSetToken = False
    # api_client.token_id = 'x-byerfy46nsoag6jy3uk48484fxtitg9j4b04o6tjhdakg4s73wlddjjypfekdh06vyfuobc6ek7wju3u5i5faqby5giptfpd7svxfwunob7znzsbqrmmoa7vdik4069g'

    # 初始化api
    siteManagerApi = SiteManagerApi(api_client)
    # 参数
    pageIndex = 0
    pageSize = 10
    # 调用api
    model1 = siteManagerApi.query_sites(page_index=pageIndex, page_size=pageSize)
    print(model1)


    userMgrThirdApi = UserMgrThirdApi(api_client)
    userName = '~anonymous'
    model2 = userMgrThirdApi.get_user_third(user_name=userName)
    print(model2)

    # 调用结束，删除token
    api_client.deleteToken()
    pass


if __name__ == "__main__":
    sys.exit(main())
