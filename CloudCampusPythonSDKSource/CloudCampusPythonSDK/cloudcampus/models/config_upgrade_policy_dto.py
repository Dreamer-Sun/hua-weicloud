# coding: utf-8

"""
    防火墙特征库升级

    防火墙特征库升级接口 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConfigUpgradePolicyDto(object):
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
        'upgrade_regularly': 'bool',
        'upgrade_immediately': 'bool',
        'upgrade_day': 'str',
        'upgrade_time': 'str',
        'signature_database_types': 'list[str]'
    }

    attribute_map = {
        'site_id': 'siteId',
        'upgrade_regularly': 'upgradeRegularly',
        'upgrade_immediately': 'upgradeImmediately',
        'upgrade_day': 'upgradeDay',
        'upgrade_time': 'upgradeTime',
        'signature_database_types': 'signatureDatabaseTypes'
    }

    def __init__(self, site_id=None, upgrade_regularly=None, upgrade_immediately=None, upgrade_day=None, upgrade_time=None, signature_database_types=None):
        """
        ConfigUpgradePolicyDto - a model defined in Swagger
        """

        self._site_id = None
        self._upgrade_regularly = None
        self._upgrade_immediately = None
        self._upgrade_day = None
        self._upgrade_time = None
        self._signature_database_types = None

        if site_id is not None:
          self.site_id = site_id
        if upgrade_regularly is not None:
          self.upgrade_regularly = upgrade_regularly
        if upgrade_immediately is not None:
          self.upgrade_immediately = upgrade_immediately
        if upgrade_day is not None:
          self.upgrade_day = upgrade_day
        if upgrade_time is not None:
          self.upgrade_time = upgrade_time
        if signature_database_types is not None:
          self.signature_database_types = signature_database_types

    @property
    def site_id(self):
        """
        Gets the site_id of this ConfigUpgradePolicyDto.
        站点标识，UUID格式。

        :return: The site_id of this ConfigUpgradePolicyDto.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """
        Sets the site_id of this ConfigUpgradePolicyDto.
        站点标识，UUID格式。

        :param site_id: The site_id of this ConfigUpgradePolicyDto.
        :type: str
        """
        if site_id is not None and len(site_id) > 36:
            raise ValueError("Invalid value for `site_id`, length must be less than or equal to `36`")
        if site_id is not None and len(site_id) < 36:
            raise ValueError("Invalid value for `site_id`, length must be greater than or equal to `36`")

        self._site_id = site_id

    @property
    def upgrade_regularly(self):
        """
        Gets the upgrade_regularly of this ConfigUpgradePolicyDto.
        策略是否为周期升级。当upgradeRegularly为true时，upgradeImmediately必须为false；当upgradeRegularly为false时，upgradeImmediately必须为true。

        :return: The upgrade_regularly of this ConfigUpgradePolicyDto.
        :rtype: bool
        """
        return self._upgrade_regularly

    @upgrade_regularly.setter
    def upgrade_regularly(self, upgrade_regularly):
        """
        Sets the upgrade_regularly of this ConfigUpgradePolicyDto.
        策略是否为周期升级。当upgradeRegularly为true时，upgradeImmediately必须为false；当upgradeRegularly为false时，upgradeImmediately必须为true。

        :param upgrade_regularly: The upgrade_regularly of this ConfigUpgradePolicyDto.
        :type: bool
        """

        self._upgrade_regularly = upgrade_regularly

    @property
    def upgrade_immediately(self):
        """
        Gets the upgrade_immediately of this ConfigUpgradePolicyDto.
        策略是否为立即升级。当upgradeImmediately为true时，upgradeRegularly必须为false;当upgradeImmediately为false时，upgradeRegularly必须为true。

        :return: The upgrade_immediately of this ConfigUpgradePolicyDto.
        :rtype: bool
        """
        return self._upgrade_immediately

    @upgrade_immediately.setter
    def upgrade_immediately(self, upgrade_immediately):
        """
        Sets the upgrade_immediately of this ConfigUpgradePolicyDto.
        策略是否为立即升级。当upgradeImmediately为true时，upgradeRegularly必须为false;当upgradeImmediately为false时，upgradeRegularly必须为true。

        :param upgrade_immediately: The upgrade_immediately of this ConfigUpgradePolicyDto.
        :type: bool
        """

        self._upgrade_immediately = upgrade_immediately

    @property
    def upgrade_day(self):
        """
        Gets the upgrade_day of this ConfigUpgradePolicyDto.
        策略为周期升级时，周几升级。当upgradeRegularly为true时，upgradeDay生效且必填。

        :return: The upgrade_day of this ConfigUpgradePolicyDto.
        :rtype: str
        """
        return self._upgrade_day

    @upgrade_day.setter
    def upgrade_day(self, upgrade_day):
        """
        Sets the upgrade_day of this ConfigUpgradePolicyDto.
        策略为周期升级时，周几升级。当upgradeRegularly为true时，upgradeDay生效且必填。

        :param upgrade_day: The upgrade_day of this ConfigUpgradePolicyDto.
        :type: str
        """

        self._upgrade_day = upgrade_day

    @property
    def upgrade_time(self):
        """
        Gets the upgrade_time of this ConfigUpgradePolicyDto.
        策略为周期升级时，升级的时间点。当upgradeRegularly为true时，upgradeTime生效且必填。

        :return: The upgrade_time of this ConfigUpgradePolicyDto.
        :rtype: str
        """
        return self._upgrade_time

    @upgrade_time.setter
    def upgrade_time(self, upgrade_time):
        """
        Sets the upgrade_time of this ConfigUpgradePolicyDto.
        策略为周期升级时，升级的时间点。当upgradeRegularly为true时，upgradeTime生效且必填。

        :param upgrade_time: The upgrade_time of this ConfigUpgradePolicyDto.
        :type: str
        """
        if upgrade_time is not None and len(upgrade_time) > 5:
            raise ValueError("Invalid value for `upgrade_time`, length must be less than or equal to `5`")
        if upgrade_time is not None and len(upgrade_time) < 5:
            raise ValueError("Invalid value for `upgrade_time`, length must be greater than or equal to `5`")

        self._upgrade_time = upgrade_time

    @property
    def signature_database_types(self):
        """
        Gets the signature_database_types of this ConfigUpgradePolicyDto.

        :return: The signature_database_types of this ConfigUpgradePolicyDto.
        :rtype: list[str]
        """
        return self._signature_database_types

    @signature_database_types.setter
    def signature_database_types(self, signature_database_types):
        """
        Sets the signature_database_types of this ConfigUpgradePolicyDto.

        :param signature_database_types: The signature_database_types of this ConfigUpgradePolicyDto.
        :type: list[str]
        """
        allowed_values = ["ip-reputation", "antivirus", "intrusion-prevention", "file-reputation", "cnc", "application"]
        if not set(signature_database_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `signature_database_types` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(signature_database_types)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._signature_database_types = signature_database_types

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
        if not isinstance(other, ConfigUpgradePolicyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
