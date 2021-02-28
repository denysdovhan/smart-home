# Dashboards

Below you're going to find my dashboards. I use those to display information and control accessories in my smart home.

<!-- prettier-ignore -->
!!! warning
    I constantly update my smart home setup and tweaking UI to match my needs. Please, beware that the look of these dashboards on screenshots might differ from how they actually look right now.

    Please, [visit the repo](https://github.com/denysdovhan/smart-home/) to see the current state of these dashboards.

I use [`mini-media-player`](https://github.com/kalkih/mini-media-player) card for the media players and [`mini-graph-card`](https://github.com/kalkih/mini-graph-card) for the graphs.

## Home

This dashboard displays the information about my home in general.

- **Scene** controls of the scenes are located at the beginning of the dashboard to be accessible on the phone right away.
- **Room buttons** navigate to the room dashboards on the press, and turn off all lights in the room on hold.
- **Media** block helps to control my smart speakers and Spotify.
- **Conditions** contain information about the weather, indoor temperature, humidity, and pressure, UV-index outdoors, and AQI indoor as well as outdoor (from the nearby AQI station).
- **Status** display the information about our location, phone battery, and travel history for the last hours.

![Home](https://user-images.githubusercontent.com/3459374/109431538-d0233b00-7a0f-11eb-952e-957d60b806bb.png)

## Living Room

This dashboard controls the living room.

- **Lights** section controls all smart lights in this room.
- **Media** displays the information about my media players (Apple TV, Samsung TV, PS4, Google Nest Mini).
- **Condition** shows the current conditions in this room (temperature, humidity, motion) and controls the air purifier via [`purifier-card`](https://github.com/denysdovhan/purifier-card).

![Living Room](https://user-images.githubusercontent.com/3459374/109431589-0fea2280-7a10-11eb-877d-70e1d2a4a9a0.png)

## Bedroom

This dashboard is for Bedroom related devices.

- **Lights** section controls all smart lights in this room.
- **Media** controls Google Home Mini smart speaker.
- **Condition** shows the current conditions in this room (temperature, humidity, motion) and controls the air humidifier via [mini-humidifier](https://github.com/artem-sedykh/mini-humidifier).

![Bedroom](https://user-images.githubusercontent.com/3459374/109431649-458f0b80-7a10-11eb-94b7-85647766bd70.png)

## Balcony

This dashboard is for the Balcony. I use the Balcony as my workplace.

- **Lights** section controls all smart lights in this room.
- **Media** displays the information about my Spotify player.

![Balcony](https://user-images.githubusercontent.com/3459374/109431705-8b4bd400-7a10-11eb-8f65-5d71896192a6.png)

## Vacuum

This dashboard is for controlling a vacuum cleaner robot.

- **Vacuum card** for controlling a vacuum cleaner and scrips for quick access to the vacuum, which is hidden under the bed. I developed my own [`vacuum-card`](https://github.com/denysdovhan/vacuum-card) for vacuum management.
- **A map** for displaying the current position of the vacuum in my home. The map is blurred. I use [`lovelace-xiaomi-vacuum-map-car`](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) for displaying a live map, though `vacuum-card` is also capable of displaying live maps.

![Vacuum](https://user-images.githubusercontent.com/3459374/109431769-d9f96e00-7a10-11eb-8ea5-04d1d0a79521.png)

## Car

This dashboard lets me control my Toyota vehicle.

- **Alarm controls** let my arm/disarm my smart alarm, start/stop the engine, trigger horn.
- **History map** display the 24-hour path history of the vehicle.
- **States** are displaying the sensor states of the hood, doors, trunk, engine and interior temperature, connection quality.

<!-- prettier-ignore -->
!!! info
    You may see that most of the controls and sensors are unavailable on the screenshots. That's because I keep my car in the underground parking, where the GSM connection is poor.

    Though, there's no need to worry, since the parking is secured with many security systems.

![Car](https://user-images.githubusercontent.com/3459374/109431845-2b096200-7a11-11eb-91d5-eaafee886d9f.png)

## Cameras

This dashboard lets me watch the live streams from Kyiv (where I live) and from Chernivtsi (where I've grown up). Unfortunately, there is a very small number of publicly accessible live cameras in Kyiv. Most of them are unstable and have very poor quality.

![Cameras](https://user-images.githubusercontent.com/3459374/109431888-5a1fd380-7a11-11eb-986f-cf6ae935764d.png)

## System

This dashboard lets me overview the state of my smart home SystemHealthRegistration

- **Internet and System** section displays the Internet speed, ping, and connected devices. Below there are a group of sensor for CPU, RAM, Swap and Disk usage of my Raspberry Pi.
- **Adguard Home** let me monitor and control the DNS ad-blocking rates.
- **Zigbee Bridge** allows toggling pairing mode.

![System](https://user-images.githubusercontent.com/3459374/109431914-80457380-7a11-11eb-8318-dcb596e39922.png)
