# Custom Extensions

Home Assistant has a lot of integrations, but sometimes it's not enough. Fortunately, Home Assistant provides a way to add external integrations.

Below you will find integrations and Lovelace cards [developed by me](#developed-by-me) and [by other smart-home enthusiasts](#third-party).

I use [HACS](//hacs.xyz) for managing my third-party integrations and cards.

## Developed by Me

Sometimes even extensions provided by HACS are not enough, so I had to develop some extensions by myself.

### Lovelace Cards

#### [`vacuum-card`](https://github.com/denysdovhan/vacuum-card)

By default, Home Assistant does not provide any card for controlling vacuum cleaners. This card displays the state and allows you to control your robot.

![vacuum-card](https://user-images.githubusercontent.com/3459374/81119202-fa60b500-8f32-11ea-9b23-325efa93d7ab.gif){: loading=lazy, width=50% }

#### [`purifier-card`](https://github.com/denysdovhan/purifier-card)

As for vacuums, Home Assistant doesn't provide any card for controlling air purifiers either. This card displays the state and allows to control your air purifier.

![purifier-card](https://user-images.githubusercontent.com/3459374/94728037-48ee7000-0368-11eb-8637-c8bbc5ffaf99.gif){: loading=lazy, width=50% }

## Third party

Here's a list of extensions developed by other developers.

### Lovelace Cards

- [`mini-media-player`](https://github.com/kalkih/mini-media-player) — The default one looks not so elegant and has way fewer options to display.
- [`mini-graph-card`](https://github.com/kalkih/mini-graph-card) — This one has a ton of different options. The killer feature for me: the ability to animate and display multiple graphs.
- [`mini-humidifier`](https://github.com/artem-sedykh/mini-humidifier) — Simple and minimalistic. Default humidifier card allows displaying humidifiers only from `humidifier` domain, whereas my humidifier is available under `fan` domain. I don't actually like this card and plan to make my own to match the design of vacuum and purifier cards.
- [`lovelace-xiaomi-vacuum-map-card`](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) — This card enables you to specify a target or start a zoned cleanup using a live or static map, just like in Xiaomi Home app. Additionally you can define a list of zones and choose the ones to be cleaned.
- [`state-switch`](https://github.com/thomasloven/lovelace-state-switch) — This card is like a usual conditional card, but allows to make conditions based on the current user. I used this only to display appropriate Spotify player in Lovelace.
- [`bar-card`](https://github.com/custom-cards/bar-card) — This card is design to display progress bars.
- [`transmission-card`](https://github.com/amaximus/transmission-card) — This card is for displaying controls over Transmission torrent client.

### Integrations

- [HACS (Home Assistant Community Store)](//hacs.xyz) — A store for easier management of `custom_components`.
- [Xiaomi Cloud Map Extractor](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor) — This custom integration provides a way to present a live view of a map for a Xiaomi (and Roborock) vacuums.
- [Adaptive Lighting](https://github.com/basnijholt/adaptive-lighting) — Adaptive Lighting slowly synchronizes your color-changing lights with the regular naturally occurring color temperature of the sky throughout the day. This gives your environment a more natural feel, with cooler hues during the midday and warmer tints near twilight and dawn. Built-in `flux` integration is very limited and bold.
- [Car Wash](https://github.com/Limych/ha-car_wash) — This component checks the weather forecast for several days in advance and concludes whether it is worth washing the car now.
- [Snowtire](https://github.com/Limych/ha-snowtire) — This component checks the weather forecast for several days in advance and concludes whether it is time to change car tires from summer to winter and vice versa.
- [Powercalc](https://github.com/bramstroker/homeassistant-powercalc) — This component calculates estimated power consumption of lights and other appliances. This allows to make use of Energy dashboard even when you don't have smart electricity meters.
- [Presence Simulation](https://github.com/slashback100/presence_simulation) — This component looks for history of devices and simulates the history with a random shift. Very useful to simulate presence at home when we are away.
