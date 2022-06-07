# StationInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_time** | **int** | 用户接入的格林威治时间，单位：秒。 | [optional] 
**access_type** | **int** | 接入类型，0---有线接入，1---无线接入。 | [optional] 
**account** | **str** | 用户名称。 | [optional] 
**device_name** | **str** | 关联设备的名称。 | [optional] 
**auth_type** | **str** | 接入设备认证方式。 | [optional] 
**channel** | **int** | 无线信道。 | [optional] 
**cumulative_traffic** | **int** | 累计上下行流量，单位：字节。 | [optional] 
**downward_speed** | **int** | 下行速率，单位：bps，最后一个统计周期内的平均值，统计周期为5分钟。 | [optional] 
**dual_frequency** | **int** | 双频能力，0-支持2.4G、1-支持5G。 | [optional] 
**frequency_band** | **int** | 关联频段，1-2.4G、2-5G。 | [optional] 
**host_name** | **str** | 终端设备名称。 | [optional] 
**mode** | **int** | 模式，0-802.11b、1-802.11g、2-802.11n、3-802.11a、4-802.11ac。 | [optional] 
**online_status** | **int** | 在线状态，1---在线、2---离线。 | [optional] 
**online_time** | **int** | 在线时长，单位：秒。 | [optional] 
**package_loss_rate** | **int** | 丢包率（上报周期内），单位：百分比。 | [optional] 
**port_index** | **int** | 接入端口索引，不推荐使用。 | [optional] 
**retrans_rate** | **int** | 重传率（上报周期内），单位：百分比。 | [optional] 
**rssi** | **int** | 信号强度，单位：dBm。 | [optional] 
**send_package_speed** | **int** | 实际发包速率（协商速率），单位：bps。 | [optional] 
**signal_noise_ratio** | **int** | 信噪比（上报周期内），单位：dB。 | [optional] 
**ssid** | **str** | SSID名称。 | [optional] 
**sticky_tags** | **int** | 粘性标记，0---no、1---yes，粘性终端标记含义：信号低、速率低且不漫游的终端。 | [optional] 
**terminal_ip** | **str** | 终端IP。 | [optional] 
**terminal_mac** | **str** | 终端MAC。 | [optional] 
**upward_speed** | **int** | 上行速率，单位：bps，最后一个统计周期内的平均值，统计周期为5分钟。 | [optional] 
**vlan** | **int** | 接入VLAN。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


