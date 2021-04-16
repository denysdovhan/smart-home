# Hardware

This is the list of the hardware that is present in my smart home.

## Home Server

The heart of my smart home is a home server based on [Raspberry Pi 4 Model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) with 4GB of RAM onboard. It's a small, affordable, but nonetheless a very capable device. It's held within an [aluminum alloy case](https://www.aliexpress.com/item/4000039821460.html?spm=a2g0s.9042311.0.0.27424c4dyqD1Vd) I bought on AliExpress. The aluminum case itself helps to disperse heat. Additionally, it came with a heat sink set and a tiny cooling fan.

As storage, I use a [SanDisk Extreme Pro MicroSD A2 V30 64GB](https://www.amazon.com/SanDisk-Extreme-UHS-I-128GB-Adapter/dp/B07G3H5RBT). This card is fast and reliable in handling small I/O operations.

<!-- prettier-ignore -->
!!! info
    Home Assistant team [recommands](https://www.home-assistant.io/installation/raspberrypi#suggested-hardware) to use [Application Class 2](https://www.sdcard.org/developers/overview/application/index.html) as they handle small I/O much more consistently than cards not optimized to host applications. A 32 GB or bigger card is recommended.

I use official [Raspberry Pi 15.3W USB-C Power Supply](https://www.raspberrypi.org/products/type-c-power-supply/) for powering my smart home server. It is important to get enough power for Raspberry Pi to work properly. Home Assistant requires at least 3A power and this power supply cable handles it just right.

=== "Home Server Hardware"

    Here's a photo of my home server hardware, right after I received it:

    ![My home server hardware](https://user-images.githubusercontent.com/3459374/108915547-b3fd5380-7635-11eb-8b3f-2826d6d2bc54.jpeg)

=== "Alluminium Case Assembling"

    A photo of the aluminum case when I was assembling it:

    ![An aluminum case for my Raspberry Pi](https://user-images.githubusercontent.com/3459374/108916909-9cbf6580-7637-11eb-844e-a701bc01dec7.jpeg)

=== "Assembled and Connected"

    Here's a whole kit assembled and connected to power:

    ![A whole kit assembled and connected to power](https://user-images.githubusercontent.com/3459374/108917386-50c0f080-7638-11eb-9ae2-7bfc379b04d7.jpeg)

## WiFi Network

You're going to have a lot of devices in your network when you have a smart home. It's critical to choose a good router to handle multiple devices and heavy traffic.

### Wireless Router

The second most important thing in my smart home is a WiFi router.

I've spent a lot of time choosing _the right router_. My main requirements for the router were:

- **Dual-band: 2.4GHz and 5GHz** — Primarily, I use two networks in my home: 2.4GHz for smart devices and 5GHz for personal devices like phones and laptops. 5GHz uses shorter radio waves, and that provides faster speeds.
- [**MU-MIMO**](https://en.wikipedia.org/wiki/Multi-user_MIMO) — This is a technology that enables simultaneous communication to multiple devices, improving overall speed and enabling network multitasking. It is critical when you have lots of connected devices and want each of them to work with the highest speed.
- [**802.11ac**](https://en.wikipedia.org/wiki/IEEE_802.11ac-2013) — this is a so-called WiFi5 standard. It allows increased speeds and improved scalability. I have a gigabyte connection at my home and wanted to benefit from it.

I chose [ASUS RT-AC1750U](https://www.asus.com/Networking-IoT-Servers/WiFi-Routers/ASUS-WiFi-Routers/RT-AC1750U/) router for my home. It matches every condition above and has nice additional features. Also, I've noticed that routers by ASUS are quite respected among other smart-home enthusiasts.

I'm happy with my decision so far. This router gives the constant 600-900 Mbit/s speed, which is enough to download a 10GB file in less than 2 minutes.

Previously, I've also tried Xiaomi Router and wasn't happy about it. Xiaomi Router has UI in Chines and worked unreliably overall.

Here are my current ASUS and former Xiaomi routers:

![My current ASUS and former Xiaomi routers](https://user-images.githubusercontent.com/3459374/109073645-56cdd480-76ff-11eb-86ac-0f659381becf.jpeg)

### Devices

Below you will find a list of my devices connected to the local network. Most of them, except for Apple TV, have static IP addresses.

| Device                                       | IP                 | HA Integration                |
| -------------------------------------------- | :----------------- | ----------------------------- |
| [Apple TV 4K][apple-tv]                      | `192.168.50.x`\*   | [Apple TV][ha-apple-tv]       |
| [Koogeek P1EU Smart Plug][koogeek-p1]        | `192.168.50.9`     | [HomeKit Controller][homekit] |
| [Koogeek P1EU Smart Plug][koogeek-p1]        | `192.168.50.10`    | [HomeKit Controller][homekit] |
| [Koogeek P1EU Smart Plug][koogeek-p1]        | `192.168.50.11`    | [HomeKit Controller][homekit] |
| [Samsung 55" Q67R 4K Smart QLED TV][tv]      | `192.168.50.93`    | [ha-samsungtv-tizen]\*\*      |
| [Raspberry Pi][pi]                           | `192.168.50.113`\* | –                             |
| [Yeelight LED Bulb 1S (Color)][yeelight-1s]  | `192.168.50.128`   | [Yeelight][yeelight]          |
| [Yeelight LED Bulb 1S (Color)][yeelight-1s]  | `192.168.50.129`   | [Yeelight][yeelight]          |
| [Xiaomi Bulb White and Color][yeelight-bulb] | `192.168.50.130`   | [Yeelight][yeelight]          |
| [Xiaomi Desk Lamp Pro][desk-lamp]            | `192.168.50.131`   | [Yeelight][yeelight]          |
| [PlayStation 4 Pro][ps4]                     | `192.168.50.185`\* | [Sony PlayStation 4][ha-ps4]  |
| [Roborock S5 Max][roborock]                  | `192.168.50.186`   | [Xiaomi Miio][xiaomi-miio]    |
| [Deerma Humidifier (mjjsq)][humidifier]      | `192.168.50.187`   | [xiaomi_airpurifier]\*\*      |
| [Xiaomi Air Purifier 3H][air-purifier]       | `192.168.50.188`   | [Xiaomi Miio][xiaomi-miio]    |
| [Google Home Mini][google-home-mini]         | `192.168.50.220`   | [Google Cast][cast]           |
| [Google Nest Mini][google-nest-mini]         | `192.168.50.221`   | [Google Cast][cast]           |

\* — means the device is connected via Ethernet instead of WiFi to ensure a more reliable connection.

\*\* — means the device is integrated via custom integration.

<!-- Devices -->

[apple-tv]: https://www.apple.com/apple-tv-4k/
[koogeek-p1]: https://www.koogeek.com/p-p1eu.html
[tv]: https://www.samsung.com/ua/tvs/qled-tv/q67r-55-inch-qled-4k-smart-tv-qe55q67rauxua/
[pi]: https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
[yeelight-1s]: https://www.yeelight.com/en_US/product/lemon2-color
[yeelight-bulb]: https://www.aliexpress.com/item/1005001870039407.html
[desk-lamp]: https://www.aliexpress.com/item/33045143366.html
[ps4]: https://www.playstation.com/en-us/ps4/ps4-pro/
[roborock]: https://us.roborock.com/pages/roborock-s5-max
[humidifier]: https://www.aliexpress.com/item/4000056420604.html
[air-purifier]: https://www.mi.com/global/mi-air-purifier-3H
[google-home-mini]: https://store.google.com/us/product/google_home_mini_first_gen
[google-nest-mini]: https://store.google.com/us/product/google_nest_mini

<!-- Integrations -->

[homekit]: https://www.home-assistant.io/integrations/homekit_controller/
[yeelight]: https://www.home-assistant.io/integrations/yeelight/
[ha-ps4]: https://www.home-assistant.io/integrations/ps4/
[cast]: https://www.home-assistant.io/integrations/cast/
[xiaomi-miio]: https://www.home-assistant.io/integrations/xiaomi_miio/
[xiaomi_airpurifier]: https://github.com/syssi/xiaomi_airpurifier
[ha-apple-tv]: https://www.home-assistant.io/integrations/apple_tv/
[ha-samsungtv-tizen]: https://github.com/jaruba/ha-samsungtv-tizen

## Zigbee Network

My Zigbee devices are connected to Home Assistant via [CC2531 Sniffer Board](https://www.aliexpress.com/item/4000059514865.html) as a coordinator. Devices are controlled by Home Assistant via: [zigbee2mqtt](https://www.zigbee2mqtt.io/) + [Mosquitto](https://mosquitto.org/) + [MQTT Integration](https://www.home-assistant.io/integrations/mqtt/).

<!-- prettier-ignore -->
!!! tip
    I connected my coordinator to the Raspberry Pi through a USB extension cable to avoid interference and improve the connection.
    This approach is suggested by [zigbee2mqtt documentation](https://www.zigbee2mqtt.io/information/FAQ.html#interview-fails).

I used to use Aqara Hub, but it switched to the current approach because of its compatibility. The current approach allows binding together [nearly every possible Zigbee device](https://www.zigbee2mqtt.io/information/supported_devices.html).

### Devices

| Device                                      | Quantity | Notes                                            |
| :------------------------------------------ | :------: | :----------------------------------------------- |
| [Aqara Smart LED Bulb 9W][aqara-bulb]       |    5     | Ceiling and Main lights                          |
| [Aqara Motion Sensor][aqara-motion]         |    2     | Detecting motions in both rooms                  |
| [Aqara Magic Cube Controller][aqara-cube]   |    1     | Controlling lights, scenes and modes             |
| [Aqara Conditions Sensor][aqara-conditions] |    1     | Internal temperature, humidity and pressure data |
| [Aqara Contact Sensor][aqara-contact]       |    1     | Detection front door opening                     |
| [MiJia Conditions Sensor][mija-conditions]  |    1     | Internal temperature and humidity data           |

<!-- Devices -->

[aqara-bulb]: https://www.aliexpress.com/item/33005500098.html
[aqara-motion]: https://www.aliexpress.com/item/32975225751.html
[aqara-cube]: https://www.aliexpress.com/item/32986728343.html
[aqara-conditions]: https://www.aliexpress.com/item/32990414707.html
[aqara-contact]: https://www.aliexpress.com/item/32991903307.html
[mija-conditions]: https://www.aliexpress.com/item/32870614227.html

## Other Devices

Another important device is a smart car alarm. I used [StarLine AS96 BT GSM GPS](https://starline-sales.eu/Car-Alarms/starline-as96-bt-gsm-gps) which is easily integrated with Home Assistant via built-in [StarLine integration](https://www.home-assistant.io/integrations/starline/).

This alarm allows to start/stop the engine, arm/disarm the alarm, trigger horn remotely via Home Assistant. Primarily, I use this for tracking down my car and checking interior temperature right from Home Assistant.
