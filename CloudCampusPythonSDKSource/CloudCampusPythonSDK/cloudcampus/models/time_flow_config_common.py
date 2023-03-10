# coding: utf-8

"""
    上网时长流量策略

    上网时长流量策略编辑查询开放API。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TimeFlowConfigCommon(object):
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
        'time_flow_name': 'str',
        'site_id': 'str',
        'enable_traffic_limit_mode': 'bool',
        'traffic_limit_mode': 'int',
        'traffic_limit': 'float',
        'enable_duration_limit_mode': 'bool',
        'duration_limit_mode': 'int',
        'duration_limit': 'float',
        'is_re_count': 'bool',
        'is_anonymous': 'bool',
        'user_group_ids': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'time_flow_name': 'timeFlowName',
        'site_id': 'siteId',
        'enable_traffic_limit_mode': 'enableTrafficLimitMode',
        'traffic_limit_mode': 'trafficLimitMode',
        'traffic_limit': 'trafficLimit',
        'enable_duration_limit_mode': 'enableDurationLimitMode',
        'duration_limit_mode': 'durationLimitMode',
        'duration_limit': 'durationLimit',
        'is_re_count': 'isReCount',
        'is_anonymous': 'isAnonymous',
        'user_group_ids': 'userGroupIds',
        'description': 'description'
    }

    def __init__(self, time_flow_name=None, site_id=None, enable_traffic_limit_mode=None, traffic_limit_mode=None, traffic_limit=None, enable_duration_limit_mode=None, duration_limit_mode=None, duration_limit=None, is_re_count=None, is_anonymous=False, user_group_ids=None, description=None):
        """
        TimeFlowConfigCommon - a model defined in Swagger
        """

        self._time_flow_name = None
        self._site_id = None
        self._enable_traffic_limit_mode = None
        self._traffic_limit_mode = None
        self._traffic_limit = None
        self._enable_duration_limit_mode = None
        self._duration_limit_mode = None
        self._duration_limit = None
        self._is_re_count = None
        self._is_anonymous = None
        self._user_group_ids = None
        self._description = None

        if time_flow_name is not None:
          self.time_flow_name = time_flow_name
        if site_id is not None:
          self.site_id = site_id
        if enable_traffic_limit_mode is not None:
          self.enable_traffic_limit_mode = enable_traffic_limit_mode
        if traffic_limit_mode is not None:
          self.traffic_limit_mode = traffic_limit_mode
        if traffic_limit is not None:
          self.traffic_limit = traffic_limit
        if enable_duration_limit_mode is not None:
          self.enable_duration_limit_mode = enable_duration_limit_mode
        if duration_limit_mode is not None:
          self.duration_limit_mode = duration_limit_mode
        if duration_limit is not None:
          self.duration_limit = duration_limit
        if is_re_count is not None:
          self.is_re_count = is_re_count
        if is_anonymous is not None:
          self.is_anonymous = is_anonymous
        if user_group_ids is not None:
          self.user_group_ids = user_group_ids
        if description is not None:
          self.description = description

    @property
    def time_flow_name(self):
        """
        Gets the time_flow_name of this TimeFlowConfigCommon.
        计费策略名。

        :return: The time_flow_name of this TimeFlowConfigCommon.
        :rtype: str
        """
        return self._time_flow_name

    @time_flow_name.setter
    def time_flow_name(self, time_flow_name):
        """
        Sets the time_flow_name of this TimeFlowConfigCommon.
        计费策略名。

        :param time_flow_name: The time_flow_name of this TimeFlowConfigCommon.
        :type: str
        """
        if time_flow_name is not None and len(time_flow_name) > 32:
            raise ValueError("Invalid value for `time_flow_name`, length must be less than or equal to `32`")
        if time_flow_name is not None and len(time_flow_name) < 1:
            raise ValueError("Invalid value for `time_flow_name`, length must be greater than or equal to `1`")

        self._time_flow_name = time_flow_name

    @property
    def site_id(self):
        """
        Gets the site_id of this TimeFlowConfigCommon.
        站点ID，UUID格式。

        :return: The site_id of this TimeFlowConfigCommon.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """
        Sets the site_id of this TimeFlowConfigCommon.
        站点ID，UUID格式。

        :param site_id: The site_id of this TimeFlowConfigCommon.
        :type: str
        """

        self._site_id = site_id

    @property
    def enable_traffic_limit_mode(self):
        """
        Gets the enable_traffic_limit_mode of this TimeFlowConfigCommon.
        启用流量控制。

        :return: The enable_traffic_limit_mode of this TimeFlowConfigCommon.
        :rtype: bool
        """
        return self._enable_traffic_limit_mode

    @enable_traffic_limit_mode.setter
    def enable_traffic_limit_mode(self, enable_traffic_limit_mode):
        """
        Sets the enable_traffic_limit_mode of this TimeFlowConfigCommon.
        启用流量控制。

        :param enable_traffic_limit_mode: The enable_traffic_limit_mode of this TimeFlowConfigCommon.
        :type: bool
        """

        self._enable_traffic_limit_mode = enable_traffic_limit_mode

    @property
    def traffic_limit_mode(self):
        """
        Gets the traffic_limit_mode of this TimeFlowConfigCommon.
        流量限制方式（1---每天，2---每月，3---每周，4---每年），启用流量控制后必填。

        :return: The traffic_limit_mode of this TimeFlowConfigCommon.
        :rtype: int
        """
        return self._traffic_limit_mode

    @traffic_limit_mode.setter
    def traffic_limit_mode(self, traffic_limit_mode):
        """
        Sets the traffic_limit_mode of this TimeFlowConfigCommon.
        流量限制方式（1---每天，2---每月，3---每周，4---每年），启用流量控制后必填。

        :param traffic_limit_mode: The traffic_limit_mode of this TimeFlowConfigCommon.
        :type: int
        """

        self._traffic_limit_mode = traffic_limit_mode

    @property
    def traffic_limit(self):
        """
        Gets the traffic_limit of this TimeFlowConfigCommon.
        流量限制值（兆），启用流量控制后必填。

        :return: The traffic_limit of this TimeFlowConfigCommon.
        :rtype: float
        """
        return self._traffic_limit

    @traffic_limit.setter
    def traffic_limit(self, traffic_limit):
        """
        Sets the traffic_limit of this TimeFlowConfigCommon.
        流量限制值（兆），启用流量控制后必填。

        :param traffic_limit: The traffic_limit of this TimeFlowConfigCommon.
        :type: float
        """
        if traffic_limit is not None and traffic_limit > 999999999:
            raise ValueError("Invalid value for `traffic_limit`, must be a value less than or equal to `999999999`")
        if traffic_limit is not None and traffic_limit < 1:
            raise ValueError("Invalid value for `traffic_limit`, must be a value greater than or equal to `1`")

        self._traffic_limit = traffic_limit

    @property
    def enable_duration_limit_mode(self):
        """
        Gets the enable_duration_limit_mode of this TimeFlowConfigCommon.
        启用时长控制。

        :return: The enable_duration_limit_mode of this TimeFlowConfigCommon.
        :rtype: bool
        """
        return self._enable_duration_limit_mode

    @enable_duration_limit_mode.setter
    def enable_duration_limit_mode(self, enable_duration_limit_mode):
        """
        Sets the enable_duration_limit_mode of this TimeFlowConfigCommon.
        启用时长控制。

        :param enable_duration_limit_mode: The enable_duration_limit_mode of this TimeFlowConfigCommon.
        :type: bool
        """

        self._enable_duration_limit_mode = enable_duration_limit_mode

    @property
    def duration_limit_mode(self):
        """
        Gets the duration_limit_mode of this TimeFlowConfigCommon.
        时长限制方式（1---每天，2---每月，3---每周，4---每年），启用时长控制后必填。

        :return: The duration_limit_mode of this TimeFlowConfigCommon.
        :rtype: int
        """
        return self._duration_limit_mode

    @duration_limit_mode.setter
    def duration_limit_mode(self, duration_limit_mode):
        """
        Sets the duration_limit_mode of this TimeFlowConfigCommon.
        时长限制方式（1---每天，2---每月，3---每周，4---每年），启用时长控制后必填。

        :param duration_limit_mode: The duration_limit_mode of this TimeFlowConfigCommon.
        :type: int
        """

        self._duration_limit_mode = duration_limit_mode

    @property
    def duration_limit(self):
        """
        Gets the duration_limit of this TimeFlowConfigCommon.
        时长限制值（分钟），启用时长控制后必填。

        :return: The duration_limit of this TimeFlowConfigCommon.
        :rtype: float
        """
        return self._duration_limit

    @duration_limit.setter
    def duration_limit(self, duration_limit):
        """
        Sets the duration_limit of this TimeFlowConfigCommon.
        时长限制值（分钟），启用时长控制后必填。

        :param duration_limit: The duration_limit of this TimeFlowConfigCommon.
        :type: float
        """
        if duration_limit is not None and duration_limit > 8432640:
            raise ValueError("Invalid value for `duration_limit`, must be a value less than or equal to `8432640`")
        if duration_limit is not None and duration_limit < 5:
            raise ValueError("Invalid value for `duration_limit`, must be a value greater than or equal to `5`")

        self._duration_limit = duration_limit

    @property
    def is_re_count(self):
        """
        Gets the is_re_count of this TimeFlowConfigCommon.
        重认证后流量和时长清零并重新计算。

        :return: The is_re_count of this TimeFlowConfigCommon.
        :rtype: bool
        """
        return self._is_re_count

    @is_re_count.setter
    def is_re_count(self, is_re_count):
        """
        Sets the is_re_count of this TimeFlowConfigCommon.
        重认证后流量和时长清零并重新计算。

        :param is_re_count: The is_re_count of this TimeFlowConfigCommon.
        :type: bool
        """

        self._is_re_count = is_re_count

    @property
    def is_anonymous(self):
        """
        Gets the is_anonymous of this TimeFlowConfigCommon.
        策略适用于匿名账号。

        :return: The is_anonymous of this TimeFlowConfigCommon.
        :rtype: bool
        """
        return self._is_anonymous

    @is_anonymous.setter
    def is_anonymous(self, is_anonymous):
        """
        Sets the is_anonymous of this TimeFlowConfigCommon.
        策略适用于匿名账号。

        :param is_anonymous: The is_anonymous of this TimeFlowConfigCommon.
        :type: bool
        """

        self._is_anonymous = is_anonymous

    @property
    def user_group_ids(self):
        """
        Gets the user_group_ids of this TimeFlowConfigCommon.
        用户组ID列表。

        :return: The user_group_ids of this TimeFlowConfigCommon.
        :rtype: list[str]
        """
        return self._user_group_ids

    @user_group_ids.setter
    def user_group_ids(self, user_group_ids):
        """
        Sets the user_group_ids of this TimeFlowConfigCommon.
        用户组ID列表。

        :param user_group_ids: The user_group_ids of this TimeFlowConfigCommon.
        :type: list[str]
        """

        self._user_group_ids = user_group_ids

    @property
    def description(self):
        """
        Gets the description of this TimeFlowConfigCommon.
        计费策略描述。

        :return: The description of this TimeFlowConfigCommon.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TimeFlowConfigCommon.
        计费策略描述。

        :param description: The description of this TimeFlowConfigCommon.
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

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
        if not isinstance(other, TimeFlowConfigCommon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
