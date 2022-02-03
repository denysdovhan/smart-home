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

![Home](https://user-images.githubusercontent.com/3459374/152371766-1d2a1e17-34d3-4fe6-9e6d-aded02f14de1.png){: loading=lazy }

## Living Room

This dashboard controls the living room.

- **Lights** section controls all smart lights in this room.
- **Media** displays the information about my media players (Apple TV, Samsung TV, PS4, Google Nest Mini).
- **Condition** shows the current conditions in this room (climate, temperature, humidity, motion) and controls the air purifier via [`purifier-card`](https://github.com/denysdovhan/purifier-card).

![Living Room](https://user-images.githubusercontent.com/3459374/152372151-be201bd1-cef9-4ce5-a59d-fd1b534934dc.png){: loading=lazy }

## Bedroom

This dashboard is for Bedroom related devices.

- **Lights** section controls all smart lights in this room.
- **Media** controls Google Home Mini smart speaker.
- **Condition** shows the current conditions in this room (temperature, humidity, motion) and controls the air humidifier via [mini-humidifier](https://github.com/artem-sedykh/mini-humidifier).

![Bedroom](https://user-images.githubusercontent.com/3459374/152372530-703121d2-2a96-4acc-a664-65109447ab93.png){: loading=lazy }

## Balcony

This dashboard is for the Balcony. I use the Balcony as my workplace.

- **Lights** section controls all smart lights in this room.
- **Media** displays the information about my Spotify player.

![Balcony](https://user-images.githubusercontent.com/3459374/152372756-a14bbc12-cd40-4549-b93b-6205d8356ce9.png){: loading=lazy }

## Vacuum

This dashboard is for controlling a vacuum cleaner robot.

- **Vacuum card** for controlling a vacuum cleaner and scrips for quick access to the vacuum, which is hidden under the bed. I developed my own [`vacuum-card`](https://github.com/denysdovhan/vacuum-card) for vacuum management.
- **A map** for displaying the current position of the vacuum in my home. The map is blurred. I use [`lovelace-xiaomi-vacuum-map-car`](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) for displaying a live map, though `vacuum-card` is also capable of displaying live maps.

![Vacuum](https://user-images.githubusercontent.com/3459374/152373217-a5ebc40c-3d62-4575-8cbc-736ca1641c8c.png){: loading=lazy }

## Car

This dashboard lets me control my Toyota vehicle.

- **Alarm controls** let my arm/disarm my smart alarm, start/stop the engine, trigger horn.
- **History map** display the 24-hour path history of the vehicle.
- **States** are displaying the sensor states of the hood, doors, trunk, engine and interior temperature, connection quality.

<!-- prettier-ignore -->
!!! info
    You may see that most of the controls and sensors are unavailable on the screenshots. That's because I keep my car in the underground parking, where the GSM connection is poor.

    Though, there's no need to worry, since the parking is secured with many security systems.

![Car](https://user-images.githubusercontent.com/3459374/152373434-9334d8a3-f715-4ea1-8e09-6d9038473bbe.png){: loading=lazy }

## City

![City](https://user-images.githubusercontent.com/3459374/152373679-5555a14a-8a1d-4015-8a71-e9d821cf30cb.png)

This dashboard is created for monitoring city conditions.

- **Air Quality** displays AQI in my neighbourhood and Kyiv average, PM2.5 concentration indoor/outdoor and AQI map.
- **Traffic** displays realtime traffic map, congestion and traveltime to/from city center.

## Observation

This dashboard displays status of my plants, position of the sun, etc.

![Observation](https://user-images.githubusercontent.com/3459374/152374474-e6e0c9f4-949d-4471-8820-e5e6cf59a928.png){: loading=lazy }

## Cameras

This dashboard lets me watch the live streams from Kyiv (where I live) and from Chernivtsi (where I've grown up). Unfortunately, there is a very small number of publicly accessible live cameras in Kyiv. Most of them are unstable and have very poor quality.

![Cameras](https://user-images.githubusercontent.com/3459374/115126127-92856c00-9fd5-11eb-93a3-0c7621cd2d53.png){: loading=lazy }

## System

This dashboard lets me overview the state of my smart home SystemHealthRegistration

- **Internet and System** section displays the Internet speed, ping, and connected devices. Below there are a group of sensor for CPU, RAM, Swap and Disk usage of my Raspberry Pi.
- **Adguard Home** let me monitor the DNS ad-blocking rates.

![System](https://user-images.githubusercontent.com/3459374/152374825-4e564a75-7c8d-4001-b71a-00dcd5291e73.png){: loading=lazy }
