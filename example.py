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

    filter = '{"where": {"lastConnection": { "gt": "2020-04-14" } }, "limit":10, "order":"lastConnection DESC" }' # str | Filter defining fields and include - must be a JSON-encoded string, optional
    devices_on_account_with_recent_connections = user_api.user_prototype_get_devices(user_id, filter=filter)
    for device in devices_on_account_with_recent_connections:
        last_points = device_api.device_prototype_get_points(device.id, filter='{"limit":1, "order":"timestamp DESC", "where": {"location":{"neq":null}}}')
        if len(last_points) > 0:
            last_point = last_points[0]
        else:
            print('No data for device %s' % device.name)
            continue	
            
        print("Last point for device %s was at address %s @ %s" % (device.name, last_point.address, last_point.timestamp))
        
        # Get associated sensor / ble data for this point
        bleData = device_api.device_prototype_nearby_devices(id=device.id, correlation_id = last_point.correlation_id)
        #pprint(bleData)
        if len(bleData) > 0:
            for nearby_device in bleData:
                #pprint(nearby_device['device'])
                print("Associated bluetooth data for %s: %s " % (nearby_device['device']['name'], ', '.join(nearby_device['readings'].keys())))
                #pprint(nearby_device['readings']);
                try:
                    ble_name = nearby_device['readings']['ble_seen']['value']['name']
                    print("Ble device name = %s" % (ble_name))
                except:
                    pass
                
        #sensor_readings = device_api.device_prototype_get_readings(device.id, filter='{"limit": 100, "order":"timestamp DESC", "where": {"timestamp": { "gt": "2019-08-01" }}}') # optionally specify where.type = "temp"
        #for reading in sensor_readings:
         #   print("Device %s sensor: type %s @ %s value %s, meta %s" % (device.name, reading.type, reading.timestamp, reading.value, reading.meta))

        # Change device settings
        # device_api.device_prototype_update_config(device.id, data={"interval":3600, "sleepInterval": 3600, "reset":0}) # change update intervals to 1h and force device reset
except ApiException as e:
    print("Exception when calling DeviceApi->device_find_by_id: %s\n" % e)

