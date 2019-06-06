# lb_tracking_api.DeviceApi

All URIs are relative to *https://cp.remotethings.co.uk/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_find_by_id**](DeviceApi.md#device_find_by_id) | **GET** /devices/{id} | Find a model instance by {{id}} from the data source.
[**device_prototype_create_notification_triggers**](DeviceApi.md#device_prototype_create_notification_triggers) | **POST** /devices/{id}/notificationTriggers | Create alert/notification trigger for device
[**device_prototype_delete_notification_triggers**](DeviceApi.md#device_prototype_delete_notification_triggers) | **DELETE** /devices/{id}/notificationTriggers | Remove all alert/notification trigger for device
[**device_prototype_destroy_by_id_points**](DeviceApi.md#device_prototype_destroy_by_id_points) | **DELETE** /devices/{id}/points/{fk} | Delete a specific point for a device
[**device_prototype_find_by_id_points**](DeviceApi.md#device_prototype_find_by_id_points) | **GET** /devices/{id}/points/{fk} | Retrieve a specific point for a device
[**device_prototype_find_by_id_readings**](DeviceApi.md#device_prototype_find_by_id_readings) | **GET** /devices/{id}/readings/{fk} | Retrieve a specific reading for a device
[**device_prototype_flight_mode**](DeviceApi.md#device_prototype_flight_mode) | **GET** /devices/{id}/flightMode | 
[**device_prototype_get_config**](DeviceApi.md#device_prototype_get_config) | **GET** /devices/{id}/config | Retrieve configuration for a device
[**device_prototype_get_notification_triggers**](DeviceApi.md#device_prototype_get_notification_triggers) | **GET** /devices/{id}/notificationTriggers | Get alerts for device
[**device_prototype_get_points**](DeviceApi.md#device_prototype_get_points) | **GET** /devices/{id}/points | Retrieve points for a device
[**device_prototype_get_readings**](DeviceApi.md#device_prototype_get_readings) | **GET** /devices/{id}/readings | Retrieve readings for a device
[**device_prototype_get_safe_zone**](DeviceApi.md#device_prototype_get_safe_zone) | **GET** /devices/{id}/getSafeZone | Get safe-zone for device
[**device_prototype_set_safe_zone**](DeviceApi.md#device_prototype_set_safe_zone) | **POST** /devices/{id}/setSafeZone | Update safe-zone for device
[**device_prototype_sleep**](DeviceApi.md#device_prototype_sleep) | **GET** /devices/{id}/sleep | Send sleep instruction to device
[**device_prototype_update_config**](DeviceApi.md#device_prototype_update_config) | **PUT** /devices/{id}/config | Update configuration for a device
[**device_prototype_wake_up**](DeviceApi.md#device_prototype_wake_up) | **GET** /devices/{id}/wakeUp | Send wake instruction to device


# **device_find_by_id**
> Device device_find_by_id(id, filter=filter)

Find a model instance by {{id}} from the data source.

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 'id_example' # str | Model id
filter = 'filter_example' # str | Filter defining fields and include - must be a JSON-encoded string ({\"something\":\"value\"}) (optional)

try:
    # Find a model instance by {{id}} from the data source.
    api_response = api_instance.device_find_by_id(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_find_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model id | 
 **filter** | **str**| Filter defining fields and include - must be a JSON-encoded string ({\&quot;something\&quot;:\&quot;value\&quot;}) | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_create_notification_triggers**
> NotificationTrigger device_prototype_create_notification_triggers(id, data=data)

Create alert/notification trigger for device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
data = lb_tracking_api.NotificationTrigger() # NotificationTrigger | Body (JSON) (optional)

try:
    # Create alert/notification trigger for device
    api_response = api_instance.device_prototype_create_notification_triggers(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_create_notification_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **data** | [**NotificationTrigger**](NotificationTrigger.md)| Body (JSON) | [optional] 

### Return type

[**NotificationTrigger**](NotificationTrigger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_delete_notification_triggers**
> device_prototype_delete_notification_triggers(id)

Remove all alert/notification trigger for device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id

try:
    # Remove all alert/notification trigger for device
    api_instance.device_prototype_delete_notification_triggers(id)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_delete_notification_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_destroy_by_id_points**
> device_prototype_destroy_by_id_points(id, fk)

Delete a specific point for a device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
fk = 8.14 # float | Foreign key for points

try:
    # Delete a specific point for a device
    api_instance.device_prototype_destroy_by_id_points(id, fk)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_destroy_by_id_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **fk** | **float**| Foreign key for points | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_find_by_id_points**
> Datapoint device_prototype_find_by_id_points(id, fk)

Retrieve a specific point for a device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
fk = 8.14 # float | Foreign key for points

try:
    # Retrieve a specific point for a device
    api_response = api_instance.device_prototype_find_by_id_points(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_find_by_id_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **fk** | **float**| Foreign key for points | 

### Return type

[**Datapoint**](Datapoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_find_by_id_readings**
> SensorReading device_prototype_find_by_id_readings(id, fk)

Retrieve a specific reading for a device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
fk = 8.14 # float | Foreign key for readings

try:
    # Retrieve a specific reading for a device
    api_response = api_instance.device_prototype_find_by_id_readings(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_find_by_id_readings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **fk** | **float**| Foreign key for readings | 

### Return type

[**SensorReading**](SensorReading.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_flight_mode**
> object device_prototype_flight_mode(id, duration)



### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
duration = 8.14 # float | How long to go into flightMode, in minutes

try:
    api_response = api_instance.device_prototype_flight_mode(id, duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_flight_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **duration** | **float**| How long to go into flightMode, in minutes | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_get_config**
> DeviceConfig device_prototype_get_config(id, refresh=refresh)

Retrieve configuration for a device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
refresh = true # bool | unused (optional)

try:
    # Retrieve configuration for a device
    api_response = api_instance.device_prototype_get_config(id, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **refresh** | **bool**| unused | [optional] 

### Return type

[**DeviceConfig**](DeviceConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_get_notification_triggers**
> list[NotificationTrigger] device_prototype_get_notification_triggers(id, filter=filter)

Get alerts for device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
filter = 'filter_example' # str | JSON Filter object (optional)

try:
    # Get alerts for device
    api_response = api_instance.device_prototype_get_notification_triggers(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_get_notification_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **filter** | **str**| JSON Filter object | [optional] 

### Return type

[**list[NotificationTrigger]**](NotificationTrigger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_get_points**
> list[Datapoint] device_prototype_get_points(id, filter=filter)

Retrieve points for a device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
filter = 'filter_example' # str | JSON Filter object (optional)

try:
    # Retrieve points for a device
    api_response = api_instance.device_prototype_get_points(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_get_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **filter** | **str**| JSON Filter object | [optional] 

### Return type

[**list[Datapoint]**](Datapoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_get_readings**
> list[SensorReading] device_prototype_get_readings(id, filter=filter)

Retrieve readings for a device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
filter = 'filter_example' # str | JSON Filter object (optional)

try:
    # Retrieve readings for a device
    api_response = api_instance.device_prototype_get_readings(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_get_readings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **filter** | **str**| JSON Filter object | [optional] 

### Return type

[**list[SensorReading]**](SensorReading.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_get_safe_zone**
> Geofence device_prototype_get_safe_zone(id)

Get safe-zone for device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id

try:
    # Get safe-zone for device
    api_response = api_instance.device_prototype_get_safe_zone(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_get_safe_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 

### Return type

[**Geofence**](Geofence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_set_safe_zone**
> Geofence device_prototype_set_safe_zone(id, data)

Update safe-zone for device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
data = [lb_tracking_api.GeoPoint()] # list[GeoPoint] | Array of {lat:x,lng:y} points denoting the vertices of the safe-zone

try:
    # Update safe-zone for device
    api_response = api_instance.device_prototype_set_safe_zone(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_set_safe_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **data** | [**list[GeoPoint]**](GeoPoint.md)| Array of {lat:x,lng:y} points denoting the vertices of the safe-zone | 

### Return type

[**Geofence**](Geofence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_sleep**
> object device_prototype_sleep(id, duration=duration)

Send sleep instruction to device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
duration = 8.14 # float |  (optional)

try:
    # Send sleep instruction to device
    api_response = api_instance.device_prototype_sleep(id, duration=duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_sleep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **duration** | **float**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_update_config**
> DeviceConfig device_prototype_update_config(id, data=data)

Update configuration for a device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
data = lb_tracking_api.DeviceConfig() # DeviceConfig | Body (JSON) (optional)

try:
    # Update configuration for a device
    api_response = api_instance.device_prototype_update_config(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_update_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **data** | [**DeviceConfig**](DeviceConfig.md)| Body (JSON) | [optional] 

### Return type

[**DeviceConfig**](DeviceConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_prototype_wake_up**
> object device_prototype_wake_up(id, duration=duration)

Send wake instruction to device

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.DeviceApi()
id = 8.14 # float | device id
duration = 8.14 # float |  (optional)

try:
    # Send wake instruction to device
    api_response = api_instance.device_prototype_wake_up(id, duration=duration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_prototype_wake_up: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| device id | 
 **duration** | **float**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

