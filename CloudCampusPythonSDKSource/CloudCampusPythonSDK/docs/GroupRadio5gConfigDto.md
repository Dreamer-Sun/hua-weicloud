# GroupRadio5gConfigDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dca_bandwidth** | **str** | 5G调优频宽，只能为20mhz，40mhz，80mhz其中一种。 | [optional] 
**dca5g_channel_set** | **str** | 5G调优信道集。当5G调优频宽为20MHz时，支持的信道有36，40，44，48，52，56，60，64，149，153，157，161，165； 当5G调优信道为40MHz或80MHz时，支持的信道有36，40，44，48，52，56，60，64，149，153，157，161。 为了确保校准结果，请选择至少三个选项。若可选信道少于三个，则此国家不支持配置此调优频宽。 | [optional] 
**radio5g_base_rate** | **str** | 5G基础速率。支持的速率有6，9，12，18，24，36，48，54。单位（Mbps）。至少选择一项。 | [optional] 
**radio5g_support_rate** | **str** | 5G支持速率。支持的速率有6，9，12，18，24，36，48，54。单位（Mbps）。至少选择一项。 | [optional] 
**tpc5g_max_tx_pwr** | **int** | 5G的TPC上限。取值范围为1到127之间的整数。单位（dBm）。 | [optional] 
**tpc5g_min_tx_pwr** | **int** | 5G的TPC下限。取值范围为1到127之间的整数。单位（dBm）。 | [optional] 
**tpc5g_coverage_threshold** | **int** | 5G的TPC阈值。取值范围为-85到-35之间的整数。 | [optional] 
**radio5_guard_interval_mode** | **str** | 5G射频间隔（GI）模式，可填default（默认）、short（短间隔）或normal（普通间隔）。普通间隔的时间为800ns，在802.11n和802.11ac标准中允许使用短间隔，为400ns，可以提高802.11n和802.11ac的传输率。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


