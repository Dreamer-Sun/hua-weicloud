# NatSessionLogConfigParam

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nat_session_log_enable** | **bool** | Nat日志上报使能开关。当natSessionLogEnable为true时，logInterval，binaryNatSessionLogEnable生效。 | [optional] 
**log_interval** | **int** | Nat日志上报时间间隔，单位：s，默认30s。 | [optional] 
**binary_nat_session_log_enable** | **bool** | 二进制格式的日志上报开关。当binaryNatSessionLogEnable为true时，binaryLogHostAddress，binaryLogHostPort，binaryLogSrcPort生效。当binaryNatSessionLogEnable为false时，Nat日志上报的格式为文本。 | [optional] 
**binary_log_host_address** | **str** | 二进制上报日志目标服务器IP地址。 | [optional] 
**binary_log_host_port** | **int** | 二进制上报日志目标服务器端口号，范围为：1-65535。 | [optional] 
**binary_log_src_port** | **int** | 二进制上报日志设备源端口号，范围为：10240-55534。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


