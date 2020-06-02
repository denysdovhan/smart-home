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
  - Zibee pairing
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
