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


class UpgradePolicyDto(object):
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
        'site_id': 'str',
        'download_policy_dto': 'DownloadPolicyDto',
        'restart_policy_dto': 'RestartPolicyDto',
        'up_path': 'list[UpPath]'
    }

    attribute_map = {
        'site_id': 'siteId',
        'download_policy_dto': 'downloadPolicyDto',
        'restart_policy_dto': 'restartPolicyDto',
        'up_path': 'upPath'
    }

    def __init__(self, site_id=None, download_policy_dto=None, restart_policy_dto=None, up_path=None):
        """
        UpgradePolicyDto - a model defined in Swagger
        """

        self._site_id = None
        self._download_policy_dto = None
        self._restart_policy_dto = None
        self._up_path = None

        if site_id is not None:
          self.site_id = site_id
        if download_policy_dto is not None:
          self.download_policy_dto = download_policy_dto
        if restart_policy_dto is not None:
          self.restart_policy_dto = restart_policy_dto
        if up_path is not None:
          self.up_path = up_path

    @property
    def site_id(self):
        """
        Gets the site_id of this UpgradePolicyDto.
        站点ID。

        :return: The site_id of this UpgradePolicyDto.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """
        Sets the site_id of this UpgradePolicyDto.
        站点ID。

        :param site_id: The site_id of this UpgradePolicyDto.
        :type: str
        """

        self._site_id = site_id

    @property
    def download_policy_dto(self):
        """
        Gets the download_policy_dto of this UpgradePolicyDto.

        :return: The download_policy_dto of this UpgradePolicyDto.
        :rtype: DownloadPolicyDto
        """
        return self._download_policy_dto

    @download_policy_dto.setter
    def download_policy_dto(self, download_policy_dto):
        """
        Sets the download_policy_dto of this UpgradePolicyDto.

        :param download_policy_dto: The download_policy_dto of this UpgradePolicyDto.
        :type: DownloadPolicyDto
        """

        self._download_policy_dto = download_policy_dto

    @property
    def restart_policy_dto(self):
        """
        Gets the restart_policy_dto of this UpgradePolicyDto.

        :return: The restart_policy_dto of this UpgradePolicyDto.
        :rtype: RestartPolicyDto
        """
        return self._restart_policy_dto

    @restart_policy_dto.setter
    def restart_policy_dto(self, restart_policy_dto):
        """
        Sets the restart_policy_dto of this UpgradePolicyDto.

        :param restart_policy_dto: The restart_policy_dto of this UpgradePolicyDto.
        :type: RestartPolicyDto
        """

        self._restart_policy_dto = restart_policy_dto

    @property
    def up_path(self):
        """
        Gets the up_path of this UpgradePolicyDto.
        升级路径。

        :return: The up_path of this UpgradePolicyDto.
        :rtype: list[UpPath]
        """
        return self._up_path

    @up_path.setter
    def up_path(self, up_path):
        """
        Sets the up_path of this UpgradePolicyDto.
        升级路径。

        :param up_path: The up_path of this UpgradePolicyDto.
        :type: list[UpPath]
        """

        self._up_path = up_path

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
        if not isinstance(other, UpgradePolicyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other