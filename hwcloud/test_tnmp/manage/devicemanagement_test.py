# 测试设备管理


from tnmp.manage.devicemanagement import *

if __name__ == '__main__':
    # pageIndex = 1
    # pageSize = 10
    # GetDeviceInfo(pageIndex, pageSize)
    # body = {
    #     "devices": [
    #         {
    #             "esn": "",
    #             "name": "测试设备",
    #             "siteId": "84a5eb1d-0985-4c9a-b747-f7572f0e2fe5",
    #             "description": "AP1",
    #             "resourceId": "",
    #             "deviceModel": "AP2050DN",
    #             "systemIp": "",
    #             "tags": [],
    #             "ztpConfirm": 'true',
    #             "role": [
    #                 "AP"
    #             ]
    #         }
    #     ]
    # }
    # CreateDevice(body_params=body)
    body = {
    "deviceIds": [
        "a98e621e-dc4b-48e3-8932-e83ed668eb91"
    ],
    "reset": "false"
}
    DeleteDevice(body)
