# Installed Addons

I'm trying keep all of the tools that manage my home automation as part of Home Assistant setup. Here are my installed addons:

### [Mosquitto Addon](https://github.com/home-assistant/addons/tree/master/mosquitto)

[Eclipse Mosquitto](https://mosquitto.org/) is lightweight and is suitable for use on all devices from low power single board computers to full servers.

In my case, this is an MQTT broker (basically, a man in the middle) between [Home Assistant MQTT integration](https://www.home-assistant.io/integrations/mqtt/) and [Zigbee2MQTT](#zigbee2mqtt) container. This is necessary to incorporate my Zigbee devices into my smart home.

### [zigbee2mqtt Addon](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt/tree/master/zigbee2mqtt)

[zigbee2mqtt](https://www.zigbee2mqtt.io/) is a addon for connecting Zigbee devices without proprietary Zigbee bridges. It bridges events and allows controlling Zigbee devices via MQTT.

In my case, it bridges my Zigbee devices to Home Assistant via sniffer. You can read more about it in the [Hardware section](../../hardware).

### ESPHome Addon

[ESPHome](https://esphome.io/) is a system to control ESP8266/ESP32 devices by simple and powerful configuration files and control them remotely through Home Automation systems.

I use ESPHome for connecting and controlling my Midea AC remotely.

### [AirCast Addon](https://github.com/hassio-addons/addon-aircast)

It is a simple addon to make UPnP/Sonos & Chromecast devices available via AirPlay.
