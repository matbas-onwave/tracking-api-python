# lb_tracking_api.UserApi

All URIs are relative to *https://cp.remotethings.co.uk/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_login**](UserApi.md#user_login) | **POST** /users/login | Login a user with username/email and password.
[**user_prototype_create_geofences**](UserApi.md#user_prototype_create_geofences) | **POST** /users/{id}/geofences | Creates a new instance in geofences of this model.
[**user_prototype_delete_geofences**](UserApi.md#user_prototype_delete_geofences) | **DELETE** /users/{id}/geofences | Deletes all geofences of this model.
[**user_prototype_destroy_by_id_geofences**](UserApi.md#user_prototype_destroy_by_id_geofences) | **DELETE** /users/{id}/geofences/{fk} | Delete a related item by id for geofences.
[**user_prototype_find_by_id_geofences**](UserApi.md#user_prototype_find_by_id_geofences) | **GET** /users/{id}/geofences/{fk} | Find a related item by id for geofences.
[**user_prototype_get_devices**](UserApi.md#user_prototype_get_devices) | **GET** /users/{id}/devices | Queries devices of user.
[**user_prototype_get_geofences**](UserApi.md#user_prototype_get_geofences) | **GET** /users/{id}/geofences | Queries geofences of user.
[**user_prototype_get_mqtt_credentials**](UserApi.md#user_prototype_get_mqtt_credentials) | **GET** /users/{id}/getMqttCredentials | 
[**user_prototype_update_by_id_geofences**](UserApi.md#user_prototype_update_by_id_geofences) | **PUT** /users/{id}/geofences/{fk} | Update a related item by id for geofences.


# **user_login**
> AccessToken user_login(credentials, include=include)

Login a user with username/email and password.

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.UserApi()
credentials = lb_tracking_api.Credentials() # Credentials | Body (JSON)
include = 'include_example' # str | Related objects to include in the response. See the description of return value for more details. (optional)

try:
    # Login a user with username/email and password.
    api_response = api_instance.user_login(credentials, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**Credentials**](Credentials.md)| Body (JSON) | 
 **include** | **str**| Related objects to include in the response. See the description of return value for more details. | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_prototype_create_geofences**
> Geofence user_prototype_create_geofences(id, data=data)

Creates a new instance in geofences of this model.

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.UserApi()
id = 'id_example' # str | user id
data = lb_tracking_api.Geofence() # Geofence | Body (JSON) (optional)

try:
    # Creates a new instance in geofences of this model.
    api_response = api_instance.user_prototype_create_geofences(id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_prototype_create_geofences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user id | 
 **data** | [**Geofence**](Geofence.md)| Body (JSON) | [optional] 

### Return type

[**Geofence**](Geofence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_prototype_delete_geofences**
> user_prototype_delete_geofences(id)

Deletes all geofences of this model.

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.UserApi()
id = 'id_example' # str | user id

try:
    # Deletes all geofences of this model.
    api_instance.user_prototype_delete_geofences(id)
except ApiException as e:
    print("Exception when calling UserApi->user_prototype_delete_geofences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_prototype_destroy_by_id_geofences**
> user_prototype_destroy_by_id_geofences(id, fk)

Delete a related item by id for geofences.

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.UserApi()
id = 'id_example' # str | user id
fk = 8.14 # float | Foreign key for geofences

try:
    # Delete a related item by id for geofences.
    api_instance.user_prototype_destroy_by_id_geofences(id, fk)
except ApiException as e:
    print("Exception when calling UserApi->user_prototype_destroy_by_id_geofences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user id | 
 **fk** | **float**| Foreign key for geofences | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_prototype_find_by_id_geofences**
> Geofence user_prototype_find_by_id_geofences(id, fk)

Find a related item by id for geofences.

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.UserApi()
id = 'id_example' # str | user id
fk = 8.14 # float | Foreign key for geofences

try:
    # Find a related item by id for geofences.
    api_response = api_instance.user_prototype_find_by_id_geofences(id, fk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_prototype_find_by_id_geofences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user id | 
 **fk** | **float**| Foreign key for geofences | 

### Return type

[**Geofence**](Geofence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_prototype_get_devices**
> list[Device] user_prototype_get_devices(id, filter=filter)

Queries devices of user.

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.UserApi()
id = 'id_example' # str | user id
filter = 'filter_example' # str | JSON Filter object (optional)

try:
    # Queries devices of user.
    api_response = api_instance.user_prototype_get_devices(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_prototype_get_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user id | 
 **filter** | **str**| JSON Filter object | [optional] 

### Return type

[**list[Device]**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_prototype_get_geofences**
> list[Geofence] user_prototype_get_geofences(id, filter=filter)

Queries geofences of user.

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.UserApi()
id = 'id_example' # str | user id
filter = 'filter_example' # str | JSON Filter object (optional)

try:
    # Queries geofences of user.
    api_response = api_instance.user_prototype_get_geofences(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_prototype_get_geofences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user id | 
 **filter** | **str**| JSON Filter object | [optional] 

### Return type

[**list[Geofence]**](Geofence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_prototype_get_mqtt_credentials**
> InlineResponse200 user_prototype_get_mqtt_credentials(id)



### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.UserApi()
id = 'id_example' # str | user id

try:
    api_response = api_instance.user_prototype_get_mqtt_credentials(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_prototype_get_mqtt_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user id | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_prototype_update_by_id_geofences**
> Geofence user_prototype_update_by_id_geofences(id, fk, data=data)

Update a related item by id for geofences.

### Example
```python
from __future__ import print_function
import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lb_tracking_api.UserApi()
id = 'id_example' # str | user id
fk = 8.14 # float | Foreign key for geofences
data = lb_tracking_api.Geofence() # Geofence | Body (JSON) (optional)

try:
    # Update a related item by id for geofences.
    api_response = api_instance.user_prototype_update_by_id_geofences(id, fk, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_prototype_update_by_id_geofences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| user id | 
 **fk** | **float**| Foreign key for geofences | 
 **data** | [**Geofence**](Geofence.md)| Body (JSON) | [optional] 

### Return type

[**Geofence**](Geofence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

