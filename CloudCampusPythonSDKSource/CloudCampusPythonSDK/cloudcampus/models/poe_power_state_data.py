# coding: utf-8

"""
    PoE电源状态查询

    查询设备PoE电源状态。 

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PoePowerStateData(object):
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
        'interface_id': 'str',
        'interface_name': 'str',
        'port_legacy': 'bool',
        'port_enable': 'bool',
        'port_power': 'bool',
        'port_status': 'str',
        'port_class': 'int',
        'port_ref': 'int',
        'port_priority': 'str',
        'port_max': 'int',
        'port_current_mw': 'int',
        'port_peak': 'int',
        'port_average': 'int',
        'port_current_ma': 'float',
        'port_voltage': 'float'
    }

    attribute_map = {
        'interface_id': 'interfaceId',
        'interface_name': 'interfaceName',
        'port_legacy': 'portLegacy',
        'port_enable': 'portEnable',
        'port_power': 'portPower',
        'port_status': 'portStatus',
        'port_class': 'portClass',
        'port_ref': 'portRef',
        'port_priority': 'portPriority',
        'port_max': 'portMax',
        'port_current_mw': 'portCurrentMW',
        'port_peak': 'portPeak',
        'port_average': 'portAverage',
        'port_current_ma': 'portCurrentMA',
        'port_voltage': 'portVoltage'
    }

    def __init__(self, interface_id=None, interface_name=None, port_legacy=None, port_enable=None, port_power=None, port_status=None, port_class=None, port_ref=None, port_priority=None, port_max=None, port_current_mw=None, port_peak=None, port_average=None, port_current_ma=None, port_voltage=None):
        """
        PoePowerStateData - a model defined in Swagger
        """

        self._interface_id = None
        self._interface_name = None
        self._port_legacy = None
        self._port_enable = None
        self._port_power = None
        self._port_status = None
        self._port_class = None
        self._port_ref = None
        self._port_priority = None
        self._port_max = None
        self._port_current_mw = None
        self._port_peak = None
        self._port_average = None
        self._port_current_ma = None
        self._port_voltage = None

        if interface_id is not None:
          self.interface_id = interface_id
        if interface_name is not None:
          self.interface_name = interface_name
        if port_legacy is not None:
          self.port_legacy = port_legacy
        if port_enable is not None:
          self.port_enable = port_enable
        if port_power is not None:
          self.port_power = port_power
        if port_status is not None:
          self.port_status = port_status
        if port_class is not None:
          self.port_class = port_class
        if port_ref is not None:
          self.port_ref = port_ref
        if port_priority is not None:
          self.port_priority = port_priority
        if port_max is not None:
          self.port_max = port_max
        if port_current_mw is not None:
          self.port_current_mw = port_current_mw
        if port_peak is not None:
          self.port_peak = port_peak
        if port_average is not None:
          self.port_average = port_average
        if port_current_ma is not None:
          self.port_current_ma = port_current_ma
        if port_voltage is not None:
          self.port_voltage = port_voltage

    @property
    def interface_id(self):
        """
        Gets the interface_id of this PoePowerStateData.
        接口ID，UUID格式。

        :return: The interface_id of this PoePowerStateData.
        :rtype: str
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """
        Sets the interface_id of this PoePowerStateData.
        接口ID，UUID格式。

        :param interface_id: The interface_id of this PoePowerStateData.
        :type: str
        """

        self._interface_id = interface_id

    @property
    def interface_name(self):
        """
        Gets the interface_name of this PoePowerStateData.
        接口名。

        :return: The interface_name of this PoePowerStateData.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """
        Sets the interface_name of this PoePowerStateData.
        接口名。

        :param interface_name: The interface_name of this PoePowerStateData.
        :type: str
        """

        self._interface_name = interface_name

    @property
    def port_legacy(self):
        """
        Gets the port_legacy of this PoePowerStateData.
        接口是否使能兼容性检测功能(true，false)。

        :return: The port_legacy of this PoePowerStateData.
        :rtype: bool
        """
        return self._port_legacy

    @port_legacy.setter
    def port_legacy(self, port_legacy):
        """
        Sets the port_legacy of this PoePowerStateData.
        接口是否使能兼容性检测功能(true，false)。

        :param port_legacy: The port_legacy of this PoePowerStateData.
        :type: bool
        """

        self._port_legacy = port_legacy

    @property
    def port_enable(self):
        """
        Gets the port_enable of this PoePowerStateData.
        接口是否使能PoE供电功能(true，false)。

        :return: The port_enable of this PoePowerStateData.
        :rtype: bool
        """
        return self._port_enable

    @port_enable.setter
    def port_enable(self, port_enable):
        """
        Sets the port_enable of this PoePowerStateData.
        接口是否使能PoE供电功能(true，false)。

        :param port_enable: The port_enable of this PoePowerStateData.
        :type: bool
        """

        self._port_enable = port_enable

    @property
    def port_power(self):
        """
        Gets the port_power of this PoePowerStateData.
        接口是否供电(true，false)。

        :return: The port_power of this PoePowerStateData.
        :rtype: bool
        """
        return self._port_power

    @port_power.setter
    def port_power(self, port_power):
        """
        Sets the port_power of this PoePowerStateData.
        接口是否供电(true，false)。

        :param port_power: The port_power of this PoePowerStateData.
        :type: bool
        """

        self._port_power = port_power

    @property
    def port_status(self):
        """
        Gets the port_status of this PoePowerStateData.
        接口的供电状态：Test mode(测试状态)、Detecting(检测状态)、Disabled(接口PoE功能未使能状态)、Chip fault(芯片故障状态)、Power-deny(参考功率大于接口最大输出功率)、Classification overcurrent(分级过流)、Unknown class(未知分级)、Power overcurrent(接口过流)、Power-on failed(上电失败)、Power-ready(接口供电就绪)、Powering(正在上电)、Powered(上电结束)、Over loaded(功率过载)、Time-range power-off(接口处于下电时间段)、Unstable voltage(接口电压不稳定)。

        :return: The port_status of this PoePowerStateData.
        :rtype: str
        """
        return self._port_status

    @port_status.setter
    def port_status(self, port_status):
        """
        Sets the port_status of this PoePowerStateData.
        接口的供电状态：Test mode(测试状态)、Detecting(检测状态)、Disabled(接口PoE功能未使能状态)、Chip fault(芯片故障状态)、Power-deny(参考功率大于接口最大输出功率)、Classification overcurrent(分级过流)、Unknown class(未知分级)、Power overcurrent(接口过流)、Power-on failed(上电失败)、Power-ready(接口供电就绪)、Powering(正在上电)、Powered(上电结束)、Over loaded(功率过载)、Time-range power-off(接口处于下电时间段)、Unstable voltage(接口电压不稳定)。

        :param port_status: The port_status of this PoePowerStateData.
        :type: str
        """

        self._port_status = port_status

    @property
    def port_class(self):
        """
        Gets the port_class of this PoePowerStateData.
        接口接入设备PD的分级，系统自动根据PD设备的最大功率给PD分类，分为0～4级。

        :return: The port_class of this PoePowerStateData.
        :rtype: int
        """
        return self._port_class

    @port_class.setter
    def port_class(self, port_class):
        """
        Sets the port_class of this PoePowerStateData.
        接口接入设备PD的分级，系统自动根据PD设备的最大功率给PD分类，分为0～4级。

        :param port_class: The port_class of this PoePowerStateData.
        :type: int
        """

        self._port_class = port_class

    @property
    def port_ref(self):
        """
        Gets the port_ref of this PoePowerStateData.
        接口的参考功率（系统会自动识别PD设备的最大功率，并给PD设备归类，定义各类别的参考功率。PD类型和参考功率的对应关系为：0-参考功率为15400mW。1-参考功率为4000mW。2-参考功率为7000mW。3-参考功率为15400mW。4-参考功率为30000mW。）。

        :return: The port_ref of this PoePowerStateData.
        :rtype: int
        """
        return self._port_ref

    @port_ref.setter
    def port_ref(self, port_ref):
        """
        Sets the port_ref of this PoePowerStateData.
        接口的参考功率（系统会自动识别PD设备的最大功率，并给PD设备归类，定义各类别的参考功率。PD类型和参考功率的对应关系为：0-参考功率为15400mW。1-参考功率为4000mW。2-参考功率为7000mW。3-参考功率为15400mW。4-参考功率为30000mW。）。

        :param port_ref: The port_ref of this PoePowerStateData.
        :type: int
        """

        self._port_ref = port_ref

    @property
    def port_priority(self):
        """
        Gets the port_priority of this PoePowerStateData.
        接口供电的优先级，有三种取值：Critical-最高的优先级，High-次高的优先级，Low-最低的优先级。

        :return: The port_priority of this PoePowerStateData.
        :rtype: str
        """
        return self._port_priority

    @port_priority.setter
    def port_priority(self, port_priority):
        """
        Sets the port_priority of this PoePowerStateData.
        接口供电的优先级，有三种取值：Critical-最高的优先级，High-次高的优先级，Low-最低的优先级。

        :param port_priority: The port_priority of this PoePowerStateData.
        :type: str
        """

        self._port_priority = port_priority

    @property
    def port_max(self):
        """
        Gets the port_max of this PoePowerStateData.
        接口最大输出功率，如果最大输出功率为15400mW，说明此设备支持802.3af标准；如果最大输出功率为30000mW，说明此设备支持802.3at标准。

        :return: The port_max of this PoePowerStateData.
        :rtype: int
        """
        return self._port_max

    @port_max.setter
    def port_max(self, port_max):
        """
        Sets the port_max of this PoePowerStateData.
        接口最大输出功率，如果最大输出功率为15400mW，说明此设备支持802.3af标准；如果最大输出功率为30000mW，说明此设备支持802.3at标准。

        :param port_max: The port_max of this PoePowerStateData.
        :type: int
        """

        self._port_max = port_max

    @property
    def port_current_mw(self):
        """
        Gets the port_current_mw of this PoePowerStateData.
        接口当前的输出功率。

        :return: The port_current_mw of this PoePowerStateData.
        :rtype: int
        """
        return self._port_current_mw

    @port_current_mw.setter
    def port_current_mw(self, port_current_mw):
        """
        Sets the port_current_mw of this PoePowerStateData.
        接口当前的输出功率。

        :param port_current_mw: The port_current_mw of this PoePowerStateData.
        :type: int
        """

        self._port_current_mw = port_current_mw

    @property
    def port_peak(self):
        """
        Gets the port_peak of this PoePowerStateData.
        接口的峰值输出功率。

        :return: The port_peak of this PoePowerStateData.
        :rtype: int
        """
        return self._port_peak

    @port_peak.setter
    def port_peak(self, port_peak):
        """
        Sets the port_peak of this PoePowerStateData.
        接口的峰值输出功率。

        :param port_peak: The port_peak of this PoePowerStateData.
        :type: int
        """

        self._port_peak = port_peak

    @property
    def port_average(self):
        """
        Gets the port_average of this PoePowerStateData.
        接口的平均输出功率。

        :return: The port_average of this PoePowerStateData.
        :rtype: int
        """
        return self._port_average

    @port_average.setter
    def port_average(self, port_average):
        """
        Sets the port_average of this PoePowerStateData.
        接口的平均输出功率。

        :param port_average: The port_average of this PoePowerStateData.
        :type: int
        """

        self._port_average = port_average

    @property
    def port_current_ma(self):
        """
        Gets the port_current_ma of this PoePowerStateData.
        接口的输出电流。

        :return: The port_current_ma of this PoePowerStateData.
        :rtype: float
        """
        return self._port_current_ma

    @port_current_ma.setter
    def port_current_ma(self, port_current_ma):
        """
        Sets the port_current_ma of this PoePowerStateData.
        接口的输出电流。

        :param port_current_ma: The port_current_ma of this PoePowerStateData.
        :type: float
        """

        self._port_current_ma = port_current_ma

    @property
    def port_voltage(self):
        """
        Gets the port_voltage of this PoePowerStateData.
        接口的输出电压。

        :return: The port_voltage of this PoePowerStateData.
        :rtype: float
        """
        return self._port_voltage

    @port_voltage.setter
    def port_voltage(self, port_voltage):
        """
        Sets the port_voltage of this PoePowerStateData.
        接口的输出电压。

        :param port_voltage: The port_voltage of this PoePowerStateData.
        :type: float
        """

        self._port_voltage = port_voltage

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
        if not isinstance(other, PoePowerStateData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other