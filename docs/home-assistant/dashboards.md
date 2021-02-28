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

![Home](https://user-images.githubusercontent.com/3459374/109427050-3ea8ce80-79f9-11eb-886b-e2ba715244ec.png)

## Living Room

This dashboard controls the living room.

- **Lights** section controls all smart lights in this room.
- **Media** displays the information about my media players (Apple TV, Samsung TV, PS4, Google Nest Mini).
- **Condition** shows the current conditions in this room (temperature, humidity, motion) and controls the air purifier via [`purifier-card`](https://github.com/denysdovhan/purifier-card).

![Living Room](https://user-images.githubusercontent.com/3459374/109427048-3ea8ce80-79f9-11eb-8d19-45e9c31217e9.png)

## Bedroom

This dashboard is for Bedroom related devices.

- **Lights** section controls all smart lights in this room.
- **Media** controls Google Home Mini smart speaker.
- **Condition** shows the current conditions in this room (temperature, humidity, motion) and controls the air humidifier via [mini-humidifier](https://github.com/artem-sedykh/mini-humidifier).

![Bedroom](https://user-images.githubusercontent.com/3459374/109427047-3e103800-79f9-11eb-9066-78ed53425e1d.png)

## Balcony

This dashboard is for the Balcony. I use the Balcony as my workplace.

- **Lights** section controls all smart lights in this room.
- **Media** displays the information about my Spotify player.

![Balcony](https://user-images.githubusercontent.com/3459374/109427046-3e103800-79f9-11eb-9c38-165b78c2d82b.png)

## Vacuum

This dashboard is for controlling a vacuum cleaner robot.

- **Vacuum card** for controlling a vacuum cleaner and scrips for quick access to the vacuum, which is hidden under the bed. I developed my own [`vacuum-card`](https://github.com/denysdovhan/vacuum-card) for vacuum management.
- **A map** for displaying the current position of the vacuum in my home. The map is blurred. I use [`lovelace-xiaomi-vacuum-map-car`](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) for displaying a live map, though `vacuum-card` is also capable of displaying live maps.

![Vacuum](https://user-images.githubusercontent.com/3459374/109428681-cd6d1980-7a00-11eb-9b1a-b1a760a1dbb6.png)

## Car

This dashboard let me control my Toyota vehicle.

- **Alarm controls** let me arm/disarm my smart alarm, start/stop the engine, trigger horn.
- **History map** display the 24-hour path history of the vehicle.
- **States** are displaying the sensor states of the hood, doors, trunk, engine and interior temperature, connection quality.

<!-- prettier-ignore -->
!!! info
    You may see that most of the controls and sensors are unavailable on the screenshots. That's because I keep my car in the underground parking, where GSP connection is poor.

    Though, there's no need to worry, since the parking is secured with many security systems.

![Car](https://user-images.githubusercontent.com/3459374/109427044-3cdf0b00-79f9-11eb-8bf3-354bd8fbed7a.png)

## Cameras

This dashboard let me watch the live streams from Kyiv (where I live) and from Chernivtsi (where I've grown up). Unfortunately, there are very small number publicly accessible live cameras in Kyiv. Most of them are unstable and with very poor quality.

![Cameras](https://user-images.githubusercontent.com/3459374/109427043-3b154780-79f9-11eb-9cc8-43f0647c753c.png)

## System

This dashboard let me overview the state of my smart home SystemHealthRegistration

- **Internet and System** section displays the Internet speed, ping and connected devices. Below there are a group of sensor for CPU, RAM, Swap and Disk usage of my Raspberry Pi.
- **Adguard Home** let me monitor and control the DNS ad blocking rates.
- **Zigbee Bridge** allows to toggle pairing mode.

![System](https://user-images.githubusercontent.com/3459374/109427040-381a5700-79f9-11eb-9dfa-f7e2d24f7981.png)
