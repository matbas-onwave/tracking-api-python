import time
import lb_tracking_api
from lb_tracking_api.rest import ApiException
from pprint import pprint

USERNAME = ''
PASSWORD = ''

# create an instance of the API class
client=lb_tracking_api.ApiClient()
user_api = lb_tracking_api.UserApi(client)
# Login to get auth token
token = user_api.user_login({"username": USERNAME, "password": PASSWORD})
user_id = token.user_id
client.set_default_header(header_name="Authorization", header_value=token.id)
device_api = lb_tracking_api.DeviceApi(client)
#
try:

    filter = '{"where": {"lastConnection": { "gt": "2019-01-01" } } }' # str | Filter defining fields and include - must be a JSON-encoded string, optional
    devices_on_account_with_recent_connections = user_api.user_prototype_get_devices(user_id, filter=filter)
    for device in devices_on_account_with_recent_connections:
        last_point = device_api.device_prototype_get_points(device.id, filter='{"limit":1, "order":"timestamp DESC", "where": {"location":{"neq":null}}}')[0]
        print("Last point for device %s was at address %s @ %s" % (device.name, last_point.address, last_point.timestamp))
except ApiException as e:
    print("Exception when calling DeviceApi->device_find_by_id: %s\n" % e)

