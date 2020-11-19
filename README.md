# Home Assistant Config [![Build Status][travis-img]][travis-ci]

> 🏠 My smart home setup based on Home Assistant

What is included:

- Home Assistant
- HomeKit
- Google Assistant
- Yeelight
- MQTT + zigbee2mqtt
- Roborock Vacuum
- HACS
  - Samsung TV Tizen
  - Apple TV Beta
  - Custom Vacuum card
- Travis CI
- Automation
  - Zigbee pairing
  - Day/Night theme auto switch
  - Notification for new Home Assistant releases
  - Notification when torrent finished
- Local AdGuard DNS

## Rooms

```json
[
  [
    16, // Living Room
    "350001002902"
  ],
  [
    17, // Bedroom
    "350001004993"
  ],
  [
    18, // Corridor
    "350001010484"
  ],
  [
    19, // Bathroom
    "350001010483"
  ],
  [
    20, // Kitchen
    "350001010672"
  ]
]
```

Bin location: `[24500, 24500]`.

## IP Addresses

| IP |  MAC | Device |
|:--:| ------ | --- |
| `192.168.50.1` | `A8:5E:45:44:26:68` | Asus Router |
| `192.168.50.9` | `A0:9D:C1:B5:13:0F` | Koogeek P1 |
| `192.168.50.10` | `A0:9D:C1:B5:0D:FE` | Koogeek P1 |
| `192.168.50.93` | `B8:BC:5B:B5:08:F2` | Samsung Tizen TV |
| `192.168.50.113` | `DC:A6:32:30:37:AD` | Home Assistant |
| `192.168.50.128` | `5C:E5:0C:2A:5B:EB` | Yeelight Color Bulb 1S |
| `192.168.50.129` | `44:23:7C:DB:99:95` | Yeelight Color Bulb 1S |
| `192.168.50.130` | `04:CF:8C:92:29:A4` | Yeelight Color Bulb 1 |
| `192.168.50.131` | `64:90:C1:A0:C1:05` | Xiaomi Desk Lamp Pro |
| `192.168.50.220` | `38:8B:59:2F:B6:75` | Google Home Mini |
| `192.168.50.185` | `2C:CC:44:92:CF:A4` | PlayStation 4 Pro |
| `192.168.50.186` | `64:90:C1:18:8B:79` | Roborock S5 Max |
| `192.168.50.187` | `44:23:7C:B0:AB:BB` | Deerma Humidifier |
| `192.168.50.188` | `44:23:7C:D8:72:56` | Xiaomi Air Purifier 3H |

## Tracking

* Home Assistant app for following the location
* iCloud for a more precise following (updates more often)
* ASUS Router for detecting when people arrive or leave home immediately

## Ad Blocking List

* https://adaway.org/hosts.txt
* https://www.malwaredomainlist.com/hostslist/hosts.txt
* NoTracking List https://github.com/notracking/hosts-blocklists
* YouTube Ads https://github.com/kboghdady/youTube_ads_4_pi-hole
* AdGuard Base Filter https://filters.adtidy.org/extension/chromium/filters/2.txt
* AdGuard Annoyances Filter https://filters.adtidy.org/extension/chromium/filters/14.txt
* AdGuard Russian Ad Filter https://filters.adtidy.org/extension/chromium/filters/1.txt
* AdGuard Mobile Ads Filter https://filters.adtidy.org/extension/chromium/filters/11.txt
* AdGuard Safari Filter https://filters.adtidy.org/extension/chromium/filters/11.txt

## Guides

* [How I set up room-cleaning automation with Google Home, Home-Assistant and Xiaomi vacuum cleaner](
https://hackernoon.com/how-i-set-up-room-cleaning-automation-with-google-home-home-assistant-and-xiaomi-vacuum-cleaner-9149e0267e6d)

<!-- References -->

[travis-ci]: https://travis-ci.org/denysdovhan/home-assistant-config
[travis-img]: https://img.shields.io/travis/denysdovhan/home-assistant-config.svg?style=flat-square
