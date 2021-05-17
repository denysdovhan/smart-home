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

![Home](https://user-images.githubusercontent.com/3459374/115125884-d37c8100-9fd3-11eb-92c9-74253af26bc6.png){: loading=lazy }

## Living Room

This dashboard controls the living room.

- **Lights** section controls all smart lights in this room.
- **Media** displays the information about my media players (Apple TV, Samsung TV, PS4, Google Nest Mini).
- **Condition** shows the current conditions in this room (temperature, humidity, motion) and controls the air purifier via [`purifier-card`](https://github.com/denysdovhan/purifier-card).

![Living Room](https://user-images.githubusercontent.com/3459374/115125905-f60e9a00-9fd3-11eb-8797-4b0302c12aae.png){: loading=lazy }

## Bedroom

This dashboard is for Bedroom related devices.

- **Lights** section controls all smart lights in this room.
- **Media** controls Google Home Mini smart speaker.
- **Condition** shows the current conditions in this room (temperature, humidity, motion) and controls the air humidifier via [mini-humidifier](https://github.com/artem-sedykh/mini-humidifier).

![Bedroom](https://user-images.githubusercontent.com/3459374/115125917-19394980-9fd4-11eb-8e64-799900c4faef.png){: loading=lazy }

## Balcony

This dashboard is for the Balcony. I use the Balcony as my workplace.

- **Lights** section controls all smart lights in this room.
- **Media** displays the information about my Spotify player.

![Balcony](https://user-images.githubusercontent.com/3459374/115125936-3706ae80-9fd4-11eb-922e-e2d9e4d75517.png){: loading=lazy }

## Vacuum

This dashboard is for controlling a vacuum cleaner robot.

- **Vacuum card** for controlling a vacuum cleaner and scrips for quick access to the vacuum, which is hidden under the bed. I developed my own [`vacuum-card`](https://github.com/denysdovhan/vacuum-card) for vacuum management.
- **A map** for displaying the current position of the vacuum in my home. The map is blurred. I use [`lovelace-xiaomi-vacuum-map-car`](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) for displaying a live map, though `vacuum-card` is also capable of displaying live maps.

![Vacuum](https://user-images.githubusercontent.com/3459374/115125949-50a7f600-9fd4-11eb-96b5-6df3343c9396.png){: loading=lazy }

## Car

This dashboard lets me control my Toyota vehicle.

- **Alarm controls** let my arm/disarm my smart alarm, start/stop the engine, trigger horn.
- **History map** display the 24-hour path history of the vehicle.
- **States** are displaying the sensor states of the hood, doors, trunk, engine and interior temperature, connection quality.

<!-- prettier-ignore -->
!!! info
    You may see that most of the controls and sensors are unavailable on the screenshots. That's because I keep my car in the underground parking, where the GSM connection is poor.

    Though, there's no need to worry, since the parking is secured with many security systems.

![Car](https://user-images.githubusercontent.com/3459374/115125975-71704b80-9fd4-11eb-93ab-60a6fa830c66.png){: loading=lazy }

## Cameras

This dashboard lets me watch the live streams from Kyiv (where I live) and from Chernivtsi (where I've grown up). Unfortunately, there is a very small number of publicly accessible live cameras in Kyiv. Most of them are unstable and have very poor quality.

![Cameras](https://user-images.githubusercontent.com/3459374/115126127-92856c00-9fd5-11eb-93a3-0c7621cd2d53.png){: loading=lazy }

## Space

This dashboard displays information about International Space Station flying over my home location. It's just interesting to catch ISS flying on the sky.

![Space](https://user-images.githubusercontent.com/3459374/118517248-b86e6f80-b73f-11eb-8f7f-519166aeaeaf.png)

## System

This dashboard lets me overview the state of my smart home SystemHealthRegistration

- **Internet and System** section displays the Internet speed, ping, and connected devices. Below there are a group of sensor for CPU, RAM, Swap and Disk usage of my Raspberry Pi.
- **Adguard Home** let me monitor and control the DNS ad-blocking rates.
- **Zigbee Bridge** allows toggling pairing mode.

![System](https://user-images.githubusercontent.com/3459374/115126227-32db9080-9fd6-11eb-9e47-725c0649261c.png){: loading=lazy }
