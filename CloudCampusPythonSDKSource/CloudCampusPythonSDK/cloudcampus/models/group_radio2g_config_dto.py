# coding: utf-8

"""
    AP站点模板射频配置

    AP站点模板射频配置第三方接口说明。 

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GroupRadio2gConfigDto(object):
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
        'dca2g_channel_set': 'str',
        'radio2g_base_rate': 'str',
        'radio2g_support_rate': 'str',
        'tpc2g_max_tx_pwr': 'int',
        'tpc2g_min_tx_pwr': 'int',
        'tpc2g_coverage_threshold': 'int',
        'radio2_dot4_guard_interval_mode': 'str'
    }

    attribute_map = {
        'dca2g_channel_set': 'dca2gChannelSet',
        'radio2g_base_rate': 'radio2gBaseRate',
        'radio2g_support_rate': 'radio2gSupportRate',
        'tpc2g_max_tx_pwr': 'tpc2gMaxTxPwr',
        'tpc2g_min_tx_pwr': 'tpc2gMinTxPwr',
        'tpc2g_coverage_threshold': 'tpc2gCoverageThreshold',
        'radio2_dot4_guard_interval_mode': 'radio2Dot4GuardIntervalMode'
    }

    def __init__(self, dca2g_channel_set=None, radio2g_base_rate=None, radio2g_support_rate=None, tpc2g_max_tx_pwr=None, tpc2g_min_tx_pwr=None, tpc2g_coverage_threshold=None, radio2_dot4_guard_interval_mode=None):
        """
        GroupRadio2gConfigDto - a model defined in Swagger
        """

        self._dca2g_channel_set = None
        self._radio2g_base_rate = None
        self._radio2g_support_rate = None
        self._tpc2g_max_tx_pwr = None
        self._tpc2g_min_tx_pwr = None
        self._tpc2g_coverage_threshold = None
        self._radio2_dot4_guard_interval_mode = None

        if dca2g_channel_set is not None:
          self.dca2g_channel_set = dca2g_channel_set
        if radio2g_base_rate is not None:
          self.radio2g_base_rate = radio2g_base_rate
        if radio2g_support_rate is not None:
          self.radio2g_support_rate = radio2g_support_rate
        if tpc2g_max_tx_pwr is not None:
          self.tpc2g_max_tx_pwr = tpc2g_max_tx_pwr
        if tpc2g_min_tx_pwr is not None:
          self.tpc2g_min_tx_pwr = tpc2g_min_tx_pwr
        if tpc2g_coverage_threshold is not None:
          self.tpc2g_coverage_threshold = tpc2g_coverage_threshold
        if radio2_dot4_guard_interval_mode is not None:
          self.radio2_dot4_guard_interval_mode = radio2_dot4_guard_interval_mode

    @property
    def dca2g_channel_set(self):
        """
        Gets the dca2g_channel_set of this GroupRadio2gConfigDto.
        2.4G调优信道集。可选\"1，6，11\"和\"1，5，9，13\"两种信道集。

        :return: The dca2g_channel_set of this GroupRadio2gConfigDto.
        :rtype: str
        """
        return self._dca2g_channel_set

    @dca2g_channel_set.setter
    def dca2g_channel_set(self, dca2g_channel_set):
        """
        Sets the dca2g_channel_set of this GroupRadio2gConfigDto.
        2.4G调优信道集。可选\"1，6，11\"和\"1，5，9，13\"两种信道集。

        :param dca2g_channel_set: The dca2g_channel_set of this GroupRadio2gConfigDto.
        :type: str
        """

        self._dca2g_channel_set = dca2g_channel_set

    @property
    def radio2g_base_rate(self):
        """
        Gets the radio2g_base_rate of this GroupRadio2gConfigDto.
        2.4基础速率。支持的速率有1，2，5.5，6，9，11，12，18，24，36，48，54。单位（Mbps）。至少选择一项。

        :return: The radio2g_base_rate of this GroupRadio2gConfigDto.
        :rtype: str
        """
        return self._radio2g_base_rate

    @radio2g_base_rate.setter
    def radio2g_base_rate(self, radio2g_base_rate):
        """
        Sets the radio2g_base_rate of this GroupRadio2gConfigDto.
        2.4基础速率。支持的速率有1，2，5.5，6，9，11，12，18，24，36，48，54。单位（Mbps）。至少选择一项。

        :param radio2g_base_rate: The radio2g_base_rate of this GroupRadio2gConfigDto.
        :type: str
        """

        self._radio2g_base_rate = radio2g_base_rate

    @property
    def radio2g_support_rate(self):
        """
        Gets the radio2g_support_rate of this GroupRadio2gConfigDto.
        2.4G支持速率。支持的速率有1，2，5.5，6，9，11，12，18，24，36，48，54。单位（Mbps）。至少选择一项。

        :return: The radio2g_support_rate of this GroupRadio2gConfigDto.
        :rtype: str
        """
        return self._radio2g_support_rate

    @radio2g_support_rate.setter
    def radio2g_support_rate(self, radio2g_support_rate):
        """
        Sets the radio2g_support_rate of this GroupRadio2gConfigDto.
        2.4G支持速率。支持的速率有1，2，5.5，6，9，11，12，18，24，36，48，54。单位（Mbps）。至少选择一项。

        :param radio2g_support_rate: The radio2g_support_rate of this GroupRadio2gConfigDto.
        :type: str
        """

        self._radio2g_support_rate = radio2g_support_rate

    @property
    def tpc2g_max_tx_pwr(self):
        """
        Gets the tpc2g_max_tx_pwr of this GroupRadio2gConfigDto.
        2.4G的TPC上限。取值范围为1到127之间的整数。单位（dBm）。

        :return: The tpc2g_max_tx_pwr of this GroupRadio2gConfigDto.
        :rtype: int
        """
        return self._tpc2g_max_tx_pwr

    @tpc2g_max_tx_pwr.setter
    def tpc2g_max_tx_pwr(self, tpc2g_max_tx_pwr):
        """
        Sets the tpc2g_max_tx_pwr of this GroupRadio2gConfigDto.
        2.4G的TPC上限。取值范围为1到127之间的整数。单位（dBm）。

        :param tpc2g_max_tx_pwr: The tpc2g_max_tx_pwr of this GroupRadio2gConfigDto.
        :type: int
        """
        if tpc2g_max_tx_pwr is not None and tpc2g_max_tx_pwr > 127:
            raise ValueError("Invalid value for `tpc2g_max_tx_pwr`, must be a value less than or equal to `127`")
        if tpc2g_max_tx_pwr is not None and tpc2g_max_tx_pwr < 1:
            raise ValueError("Invalid value for `tpc2g_max_tx_pwr`, must be a value greater than or equal to `1`")

        self._tpc2g_max_tx_pwr = tpc2g_max_tx_pwr

    @property
    def tpc2g_min_tx_pwr(self):
        """
        Gets the tpc2g_min_tx_pwr of this GroupRadio2gConfigDto.
        2.4G的TPC上限。取值范围为1到127之间的整数。单位（dBm）。

        :return: The tpc2g_min_tx_pwr of this GroupRadio2gConfigDto.
        :rtype: int
        """
        return self._tpc2g_min_tx_pwr

    @tpc2g_min_tx_pwr.setter
    def tpc2g_min_tx_pwr(self, tpc2g_min_tx_pwr):
        """
        Sets the tpc2g_min_tx_pwr of this GroupRadio2gConfigDto.
        2.4G的TPC上限。取值范围为1到127之间的整数。单位（dBm）。

        :param tpc2g_min_tx_pwr: The tpc2g_min_tx_pwr of this GroupRadio2gConfigDto.
        :type: int
        """
        if tpc2g_min_tx_pwr is not None and tpc2g_min_tx_pwr > 127:
            raise ValueError("Invalid value for `tpc2g_min_tx_pwr`, must be a value less than or equal to `127`")
        if tpc2g_min_tx_pwr is not None and tpc2g_min_tx_pwr < 1:
            raise ValueError("Invalid value for `tpc2g_min_tx_pwr`, must be a value greater than or equal to `1`")

        self._tpc2g_min_tx_pwr = tpc2g_min_tx_pwr

    @property
    def tpc2g_coverage_threshold(self):
        """
        Gets the tpc2g_coverage_threshold of this GroupRadio2gConfigDto.
        2.4G的TPC阈值。取值范围为-85到-35之间的整数。

        :return: The tpc2g_coverage_threshold of this GroupRadio2gConfigDto.
        :rtype: int
        """
        return self._tpc2g_coverage_threshold

    @tpc2g_coverage_threshold.setter
    def tpc2g_coverage_threshold(self, tpc2g_coverage_threshold):
        """
        Sets the tpc2g_coverage_threshold of this GroupRadio2gConfigDto.
        2.4G的TPC阈值。取值范围为-85到-35之间的整数。

        :param tpc2g_coverage_threshold: The tpc2g_coverage_threshold of this GroupRadio2gConfigDto.
        :type: int
        """
        if tpc2g_coverage_threshold is not None and tpc2g_coverage_threshold > -35:
            raise ValueError("Invalid value for `tpc2g_coverage_threshold`, must be a value less than or equal to `-35`")
        if tpc2g_coverage_threshold is not None and tpc2g_coverage_threshold < -85:
            raise ValueError("Invalid value for `tpc2g_coverage_threshold`, must be a value greater than or equal to `-85`")

        self._tpc2g_coverage_threshold = tpc2g_coverage_threshold

    @property
    def radio2_dot4_guard_interval_mode(self):
        """
        Gets the radio2_dot4_guard_interval_mode of this GroupRadio2gConfigDto.
        2.4G射频间隔（GI）模式，可填default（默认）、short（短间隔）或normal（普通间隔）。普通间隔的时间为800ns，在802.11n和802.11ac标准中允许使用短间隔，为400ns，可以提高802.11n和802.11ac的传输率。

        :return: The radio2_dot4_guard_interval_mode of this GroupRadio2gConfigDto.
        :rtype: str
        """
        return self._radio2_dot4_guard_interval_mode

    @radio2_dot4_guard_interval_mode.setter
    def radio2_dot4_guard_interval_mode(self, radio2_dot4_guard_interval_mode):
        """
        Sets the radio2_dot4_guard_interval_mode of this GroupRadio2gConfigDto.
        2.4G射频间隔（GI）模式，可填default（默认）、short（短间隔）或normal（普通间隔）。普通间隔的时间为800ns，在802.11n和802.11ac标准中允许使用短间隔，为400ns，可以提高802.11n和802.11ac的传输率。

        :param radio2_dot4_guard_interval_mode: The radio2_dot4_guard_interval_mode of this GroupRadio2gConfigDto.
        :type: str
        """

        self._radio2_dot4_guard_interval_mode = radio2_dot4_guard_interval_mode

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
        if not isinstance(other, GroupRadio2gConfigDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other