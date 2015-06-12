# SmartThings IoT Integration Pack

This integration pack allows you to integrate with SmartThings. Works
by setting up an API to your device via SmartApp. Subscribing to events
requires an MQTT bridge setup.

The adapter is modeled heavily after [David Janes's SmartThings/MQTT](https://github.com/dpjanes/iotdb-smartthings)
and the [SmartTiles](http://www.smarttiles.click) to setup an API that can be
called via StackStorm actions located within this pack.

## Configuration

* `api_token` - API token to access SmartThings SmartApp
* `api_endpoint` - HTTP endpoint for SmartThings SmartApp

## Actions

* `disengage_lock`  - Disengage (lock) a device that can be locked
* `engage_lock`     - Engage (lock) a device that can be locked
* `find_id_by_name` - Lookup a specific device ID based on its name/type
* `get_device_info` - Get information on a specific device
* `list_devices`    - List devices of a specific type from SmartThings
* `set_mode`        - Set current temperature.
* `set_temperature` - Set current temperature.
* `toggle_lock`     - Toggle a lock
* `toggle_switch`   - Toggle a switch
* `turn_off_switch` - Turn off a light
* `turn_on_switch`  - Turn on a switch

## Installing SmartThings SmartApp

This integration requires a Groovy SmartApp installed in your acount. See
the file located at `etc/smartthings-adapter.groovy`.

* Log into SmartThings
  * https://graph.api.smartthings.com/
* Create a new SmartApp
  * Click on "+ New SmartApp"
  * ... eh... write something else.