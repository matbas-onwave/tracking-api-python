# SensorReading

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Timestamp for the reading | 
**created** | **datetime** | Timestamp for the writing to db | 
**type** | **str** | Sensor type: &#39;ultra&#39; (fill level), &#39;temp&#39; (temperature), ... | 
**value** | **object** | JSON value | 
**rssi** | **float** | RSSI if from secondary wireless device | [optional] 
**meta** | **object** | JSON metadata | [optional] 
**related_id** | **float** | LoraId of another (ie for signal strength) | [optional] 
**correlation_id** | **str** | Internal use - correlation identifier | [optional] 
**id** | **float** |  | [optional] 
**gateway_id** | **float** |  | [optional] 
**device_id** | **float** |  | [optional] 
**sensor_device_id** | **str** |  | [optional] 
**datapoint_id** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


