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
- Automation
  - Zigbee pairing
  - Notification for new Home Assistant releases
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

## Tracking

- Home Assistant app for following the location
- iCloud for a more precise following (updates more often)
- ASUS Router for detecting when people arrive or leave home immediately

## Ad Blocking List

- https://adaway.org/hosts.txt
- https://www.malwaredomainlist.com/hostslist/hosts.txt
- NoTracking List https://github.com/notracking/hosts-blocklists
- YouTube Ads https://github.com/kboghdady/youTube_ads_4_pi-hole
- AdGuard Base Filter https://filters.adtidy.org/extension/chromium/filters/2.txt
- AdGuard Annoyances Filter https://filters.adtidy.org/extension/chromium/filters/14.txt
- AdGuard Russian Ad Filter https://filters.adtidy.org/extension/chromium/filters/1.txt
- AdGuard Mobile Ads Filter https://filters.adtidy.org/extension/chromium/filters/11.txt
- AdGuard Safari Filter https://filters.adtidy.org/extension/chromium/filters/11.txt
