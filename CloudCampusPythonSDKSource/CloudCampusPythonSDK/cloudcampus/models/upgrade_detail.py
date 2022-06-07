# coding: utf-8

"""
    设备升级

    · 查询设备文件 · 创建站点升级 · 查询站点升级 · 查询设备升级 · 取消设备升级 · 删除站点升级 · 重新升级设备 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpgradeDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'device_id': 'str',
        'device_name': 'str',
        'esn': 'str',
        'device_status': 'int',
        'device_model': 'str',
        'device_type': 'str',
        'site_name': 'str',
        'pkg_ver': 'str',
        'pkg_percent': 'int',
        'pkg_up_status': 'int',
        'pat_ver': 'str',
        'pat_percent': 'int',
        'pat_up_status': 'int',
        'failure_cause': 'str',
        'reboot_time': 'int',
        'download_time': 'int'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'device_name': 'deviceName',
        'esn': 'esn',
        'device_status': 'deviceStatus',
        'device_model': 'deviceModel',
        'device_type': 'deviceType',
        'site_name': 'siteName',
        'pkg_ver': 'pkgVer',
        'pkg_percent': 'pkgPercent',
        'pkg_up_status': 'pkgUpStatus',
        'pat_ver': 'patVer',
        'pat_percent': 'patPercent',
        'pat_up_status': 'patUpStatus',
        'failure_cause': 'failureCause',
        'reboot_time': 'rebootTime',
        'download_time': 'downloadTime'
    }

    def __init__(self, device_id=None, device_name=None, esn=None, device_status=None, device_model=None, device_type=None, site_name=None, pkg_ver=None, pkg_percent=None, pkg_up_status=None, pat_ver=None, pat_percent=None, pat_up_status=None, failure_cause=None, reboot_time=None, download_time=None):
        """
        UpgradeDetail - a model defined in Swagger
        """

        self._device_id = None
        self._device_name = None
        self._esn = None
        self._device_status = None
        self._device_model = None
        self._device_type = None
        self._site_name = None
        self._pkg_ver = None
        self._pkg_percent = None
        self._pkg_up_status = None
        self._pat_ver = None
        self._pat_percent = None
        self._pat_up_status = None
        self._failure_cause = None
        self._reboot_time = None
        self._download_time = None

        if device_id is not None:
          self.device_id = device_id
        if device_name is not None:
          self.device_name = device_name
        if esn is not None:
          self.esn = esn
        if device_status is not None:
          self.device_status = device_status
        if device_model is not None:
          self.device_model = device_model
        if device_type is not None:
          self.device_type = device_type
        if site_name is not None:
          self.site_name = site_name
        if pkg_ver is not None:
          self.pkg_ver = pkg_ver
        if pkg_percent is not None:
          self.pkg_percent = pkg_percent
        if pkg_up_status is not None:
          self.pkg_up_status = pkg_up_status
        if pat_ver is not None:
          self.pat_ver = pat_ver
        if pat_percent is not None:
          self.pat_percent = pat_percent
        if pat_up_status is not None:
          self.pat_up_status = pat_up_status
        if failure_cause is not None:
          self.failure_cause = failure_cause
        if reboot_time is not None:
          self.reboot_time = reboot_time
        if download_time is not None:
          self.download_time = download_time

    @property
    def device_id(self):
        """
        Gets the device_id of this UpgradeDetail.
        设备ID。

        :return: The device_id of this UpgradeDetail.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this UpgradeDetail.
        设备ID。

        :param device_id: The device_id of this UpgradeDetail.
        :type: str
        """

        self._device_id = device_id

    @property
    def device_name(self):
        """
        Gets the device_name of this UpgradeDetail.
        设备名称。

        :return: The device_name of this UpgradeDetail.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """
        Sets the device_name of this UpgradeDetail.
        设备名称。

        :param device_name: The device_name of this UpgradeDetail.
        :type: str
        """
        if device_name is not None and len(device_name) > 256:
            raise ValueError("Invalid value for `device_name`, length must be less than or equal to `256`")
        if device_name is not None and len(device_name) < 0:
            raise ValueError("Invalid value for `device_name`, length must be greater than or equal to `0`")

        self._device_name = device_name

    @property
    def esn(self):
        """
        Gets the esn of this UpgradeDetail.
        设备ESN。

        :return: The esn of this UpgradeDetail.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """
        Sets the esn of this UpgradeDetail.
        设备ESN。

        :param esn: The esn of this UpgradeDetail.
        :type: str
        """
        if esn is not None and len(esn) > 256:
            raise ValueError("Invalid value for `esn`, length must be less than or equal to `256`")
        if esn is not None and len(esn) < 0:
            raise ValueError("Invalid value for `esn`, length must be greater than or equal to `0`")

        self._esn = esn

    @property
    def device_status(self):
        """
        Gets the device_status of this UpgradeDetail.
        设备状态。 0：正常 1：告警 3：离线 4：未注册 

        :return: The device_status of this UpgradeDetail.
        :rtype: int
        """
        return self._device_status

    @device_status.setter
    def device_status(self, device_status):
        """
        Sets the device_status of this UpgradeDetail.
        设备状态。 0：正常 1：告警 3：离线 4：未注册 

        :param device_status: The device_status of this UpgradeDetail.
        :type: int
        """
        if device_status is not None and device_status > 10:
            raise ValueError("Invalid value for `device_status`, must be a value less than or equal to `10`")
        if device_status is not None and device_status < 0:
            raise ValueError("Invalid value for `device_status`, must be a value greater than or equal to `0`")

        self._device_status = device_status

    @property
    def device_model(self):
        """
        Gets the device_model of this UpgradeDetail.
        设备款型。

        :return: The device_model of this UpgradeDetail.
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """
        Sets the device_model of this UpgradeDetail.
        设备款型。

        :param device_model: The device_model of this UpgradeDetail.
        :type: str
        """
        if device_model is not None and len(device_model) > 256:
            raise ValueError("Invalid value for `device_model`, length must be less than or equal to `256`")
        if device_model is not None and len(device_model) < 0:
            raise ValueError("Invalid value for `device_model`, length must be greater than or equal to `0`")

        self._device_model = device_model

    @property
    def device_type(self):
        """
        Gets the device_type of this UpgradeDetail.
        设备类型，取值为AP，AR，LSW，FW其中之一。

        :return: The device_type of this UpgradeDetail.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """
        Sets the device_type of this UpgradeDetail.
        设备类型，取值为AP，AR，LSW，FW其中之一。

        :param device_type: The device_type of this UpgradeDetail.
        :type: str
        """
        if device_type is not None and len(device_type) > 256:
            raise ValueError("Invalid value for `device_type`, length must be less than or equal to `256`")
        if device_type is not None and len(device_type) < 0:
            raise ValueError("Invalid value for `device_type`, length must be greater than or equal to `0`")

        self._device_type = device_type

    @property
    def site_name(self):
        """
        Gets the site_name of this UpgradeDetail.
        站点名称。

        :return: The site_name of this UpgradeDetail.
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """
        Sets the site_name of this UpgradeDetail.
        站点名称。

        :param site_name: The site_name of this UpgradeDetail.
        :type: str
        """
        if site_name is not None and len(site_name) > 256:
            raise ValueError("Invalid value for `site_name`, length must be less than or equal to `256`")
        if site_name is not None and len(site_name) < 0:
            raise ValueError("Invalid value for `site_name`, length must be greater than or equal to `0`")

        self._site_name = site_name

    @property
    def pkg_ver(self):
        """
        Gets the pkg_ver of this UpgradeDetail.
        软件包版本。

        :return: The pkg_ver of this UpgradeDetail.
        :rtype: str
        """
        return self._pkg_ver

    @pkg_ver.setter
    def pkg_ver(self, pkg_ver):
        """
        Sets the pkg_ver of this UpgradeDetail.
        软件包版本。

        :param pkg_ver: The pkg_ver of this UpgradeDetail.
        :type: str
        """
        if pkg_ver is not None and len(pkg_ver) > 256:
            raise ValueError("Invalid value for `pkg_ver`, length must be less than or equal to `256`")
        if pkg_ver is not None and len(pkg_ver) < 0:
            raise ValueError("Invalid value for `pkg_ver`, length must be greater than or equal to `0`")

        self._pkg_ver = pkg_ver

    @property
    def pkg_percent(self):
        """
        Gets the pkg_percent of this UpgradeDetail.
        软件包下载进度。

        :return: The pkg_percent of this UpgradeDetail.
        :rtype: int
        """
        return self._pkg_percent

    @pkg_percent.setter
    def pkg_percent(self, pkg_percent):
        """
        Sets the pkg_percent of this UpgradeDetail.
        软件包下载进度。

        :param pkg_percent: The pkg_percent of this UpgradeDetail.
        :type: int
        """
        if pkg_percent is not None and pkg_percent > 100:
            raise ValueError("Invalid value for `pkg_percent`, must be a value less than or equal to `100`")
        if pkg_percent is not None and pkg_percent < 0:
            raise ValueError("Invalid value for `pkg_percent`, must be a value greater than or equal to `0`")

        self._pkg_percent = pkg_percent

    @property
    def pkg_up_status(self):
        """
        Gets the pkg_up_status of this UpgradeDetail.
        大包升级状态。 0：已创建升级任务，未升级 1：正在下载 2：已下载 5：升级完成 6：无需升级 8：升级失败 9：等待重启上线 10：正在激活大包 11：激活完成 16：取消升级成功 17：取消升级失败 18：下载停止 

        :return: The pkg_up_status of this UpgradeDetail.
        :rtype: int
        """
        return self._pkg_up_status

    @pkg_up_status.setter
    def pkg_up_status(self, pkg_up_status):
        """
        Sets the pkg_up_status of this UpgradeDetail.
        大包升级状态。 0：已创建升级任务，未升级 1：正在下载 2：已下载 5：升级完成 6：无需升级 8：升级失败 9：等待重启上线 10：正在激活大包 11：激活完成 16：取消升级成功 17：取消升级失败 18：下载停止 

        :param pkg_up_status: The pkg_up_status of this UpgradeDetail.
        :type: int
        """
        if pkg_up_status is not None and pkg_up_status > 20:
            raise ValueError("Invalid value for `pkg_up_status`, must be a value less than or equal to `20`")
        if pkg_up_status is not None and pkg_up_status < 0:
            raise ValueError("Invalid value for `pkg_up_status`, must be a value greater than or equal to `0`")

        self._pkg_up_status = pkg_up_status

    @property
    def pat_ver(self):
        """
        Gets the pat_ver of this UpgradeDetail.
        补丁版本。

        :return: The pat_ver of this UpgradeDetail.
        :rtype: str
        """
        return self._pat_ver

    @pat_ver.setter
    def pat_ver(self, pat_ver):
        """
        Sets the pat_ver of this UpgradeDetail.
        补丁版本。

        :param pat_ver: The pat_ver of this UpgradeDetail.
        :type: str
        """
        if pat_ver is not None and len(pat_ver) > 256:
            raise ValueError("Invalid value for `pat_ver`, length must be less than or equal to `256`")
        if pat_ver is not None and len(pat_ver) < 0:
            raise ValueError("Invalid value for `pat_ver`, length must be greater than or equal to `0`")

        self._pat_ver = pat_ver

    @property
    def pat_percent(self):
        """
        Gets the pat_percent of this UpgradeDetail.
        补丁下载进度。

        :return: The pat_percent of this UpgradeDetail.
        :rtype: int
        """
        return self._pat_percent

    @pat_percent.setter
    def pat_percent(self, pat_percent):
        """
        Sets the pat_percent of this UpgradeDetail.
        补丁下载进度。

        :param pat_percent: The pat_percent of this UpgradeDetail.
        :type: int
        """
        if pat_percent is not None and pat_percent > 100:
            raise ValueError("Invalid value for `pat_percent`, must be a value less than or equal to `100`")
        if pat_percent is not None and pat_percent < 0:
            raise ValueError("Invalid value for `pat_percent`, must be a value greater than or equal to `0`")

        self._pat_percent = pat_percent

    @property
    def pat_up_status(self):
        """
        Gets the pat_up_status of this UpgradeDetail.
        补丁升级状态。 0：已创建升级任务，未升级 1：正在下载 2：已下载 5：升级完成 6：无需升级 8：升级失败 9：等待重启上线 12：正在补丁操作 13：补丁操作完成 16：取消升级成功 17：取消升级失败 18：下载停止 

        :return: The pat_up_status of this UpgradeDetail.
        :rtype: int
        """
        return self._pat_up_status

    @pat_up_status.setter
    def pat_up_status(self, pat_up_status):
        """
        Sets the pat_up_status of this UpgradeDetail.
        补丁升级状态。 0：已创建升级任务，未升级 1：正在下载 2：已下载 5：升级完成 6：无需升级 8：升级失败 9：等待重启上线 12：正在补丁操作 13：补丁操作完成 16：取消升级成功 17：取消升级失败 18：下载停止 

        :param pat_up_status: The pat_up_status of this UpgradeDetail.
        :type: int
        """
        if pat_up_status is not None and pat_up_status > 20:
            raise ValueError("Invalid value for `pat_up_status`, must be a value less than or equal to `20`")
        if pat_up_status is not None and pat_up_status < 0:
            raise ValueError("Invalid value for `pat_up_status`, must be a value greater than or equal to `0`")

        self._pat_up_status = pat_up_status

    @property
    def failure_cause(self):
        """
        Gets the failure_cause of this UpgradeDetail.
        失败原因。

        :return: The failure_cause of this UpgradeDetail.
        :rtype: str
        """
        return self._failure_cause

    @failure_cause.setter
    def failure_cause(self, failure_cause):
        """
        Sets the failure_cause of this UpgradeDetail.
        失败原因。

        :param failure_cause: The failure_cause of this UpgradeDetail.
        :type: str
        """
        if failure_cause is not None and len(failure_cause) > 256:
            raise ValueError("Invalid value for `failure_cause`, length must be less than or equal to `256`")
        if failure_cause is not None and len(failure_cause) < 0:
            raise ValueError("Invalid value for `failure_cause`, length must be greater than or equal to `0`")

        self._failure_cause = failure_cause

    @property
    def reboot_time(self):
        """
        Gets the reboot_time of this UpgradeDetail.
        重启时间。UTC时间。

        :return: The reboot_time of this UpgradeDetail.
        :rtype: int
        """
        return self._reboot_time

    @reboot_time.setter
    def reboot_time(self, reboot_time):
        """
        Sets the reboot_time of this UpgradeDetail.
        重启时间。UTC时间。

        :param reboot_time: The reboot_time of this UpgradeDetail.
        :type: int
        """
        if reboot_time is not None and reboot_time > 4102416000:
            raise ValueError("Invalid value for `reboot_time`, must be a value less than or equal to `4102416000`")
        if reboot_time is not None and reboot_time < 0:
            raise ValueError("Invalid value for `reboot_time`, must be a value greater than or equal to `0`")

        self._reboot_time = reboot_time

    @property
    def download_time(self):
        """
        Gets the download_time of this UpgradeDetail.
        下载时间。UTC时间。

        :return: The download_time of this UpgradeDetail.
        :rtype: int
        """
        return self._download_time

    @download_time.setter
    def download_time(self, download_time):
        """
        Sets the download_time of this UpgradeDetail.
        下载时间。UTC时间。

        :param download_time: The download_time of this UpgradeDetail.
        :type: int
        """
        if download_time is not None and download_time > 4102416000:
            raise ValueError("Invalid value for `download_time`, must be a value less than or equal to `4102416000`")
        if download_time is not None and download_time < 0:
            raise ValueError("Invalid value for `download_time`, must be a value greater than or equal to `0`")

        self._download_time = download_time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UpgradeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other