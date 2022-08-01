# Docker Containers

## Portainer CE

![Portainer CE](https://user-images.githubusercontent.com/3459374/115123723-ffddd080-9fc6-11eb-8f26-e11f48ef185e.png)

[Portainer](https://documentation.portainer.io) is a lightweight management UI that allows easy Docker management.

I use it for restarting, stoping, killing docker containers. I can check logs, ports, statistics. This is my primary tool, that replaces Home Assistant Supervisor.

## Home Assistant

![Home Assistant](https://user-images.githubusercontent.com/3459374/115124968-f86df580-9fcd-11eb-813a-9d3dcf573a69.png)

[Home Assistant](https://www.home-assistant.io) is an open-source home automation platform that puts local control and privacy first. This is the heart of my smart home.

Home Assistant powers my home automation binds my devices together, passes them to Google Home and HomeKit, etc.

You can read more about it in [Home Assistant section](../../home-assistant/introduction/) of this documentation.

## Mosquitto

[Eclipse Mosquitto](https://mosquitto.org/) is lightweight and is suitable for use on all devices from low power single board computers to full servers.

In my case, this is an MQTT broker (basically, a man in the middle) between [Home Assistant MQTT integration](https://www.home-assistant.io/integrations/mqtt/) and [Zigbee2MQTT](#zigbee2mqtt) container. This is necessary to incorporate my Zigbee devices into my smart home.

## zigbee2mqtt

![zigbee2mqtt](https://user-images.githubusercontent.com/3459374/115125014-2fdca200-9fce-11eb-9d85-db97c2dc8a13.png)

[zigbee2mqtt](https://www.zigbee2mqtt.io/) is a container for connecting Zigbee devices without proprietary Zigbee bridges. It bridges events and allows controlling Zigbee devices via MQTT.

In my case, it bridges my Zigbee devices to Home Assistant via CC2531 sniffer. You can read more about it in the [Hardware section](../../hardware).

## ESPHome

![ESPHome](https://user-images.githubusercontent.com/3459374/134775986-076a68af-7fff-4251-8e38-36072302f1bb.png)

[ESPHome](https://esphome.io/) is a system to control ESP8266/ESP32 devices by simple and powerful configuration files and control them remotely through Home Automation systems.

I use ESPHome for connecting and controlling my Midea AC remotely.

## Duplicati

![Duplicati](https://user-images.githubusercontent.com/3459374/115125056-6e725c80-9fce-11eb-813b-07f3e5441f7b.png)

[Duplicati](https://www.duplicati.com) is a backup software to store encrypted backups online. It works standard protocols like FTP or SSH and cloud services.

I use Duplicati as a replacement for [Supervisor's Snapshots](https://www.home-assistant.io/common-tasks/os/#snapshots). It allows to schedule incremental backups, encrypt them, upload to cloud services (Google Drive, Dropbox). Additionally, it gives an ability to restore granularly (only specified files or folders).

## MariaDB

[MariaDB](https://mariadb.com) is a high-performing open-source relational database, forked from MySQL.

Long story short, it's a fast, light, and backward compatible with MySQL database solution. I use it as a SQL database for my smart home. This is used by [Nginx Proxy Manager](#nginx-proxy-manager) and [Umami](#umami).

## Adminer

![Adminer](https://user-images.githubusercontent.com/3459374/115125143-f8222a00-9fce-11eb-8a32-c261b9b1a5b8.png)

[Adminer](https://www.adminer.org) (formerly phpMinAdmin) is a full-featured database management tool written in PHP.

It's a dead-simple UI for my [MariaDB database](#mariadb).

## Nginx Proxy Manager

![Nginx Proxy Manager](https://user-images.githubusercontent.com/3459374/115125358-44219e80-9fd0-11eb-8a72-27383603d546.png)

[Nginx Proxy Manager](https://nginxproxymanager.com) is a Docker container for managing Nginx proxy hosts with a simple, powerful interface.

This allows me to easily expose services from my local network to the internet. It automatically requests, invalidates, and renews SSL certificates from [Let's Encrypt](https://letsencrypt.org/).

## AirConnect

[AirConnect](https://github.com/philippe44/AirConnect) is a simple tool to make UPnP/Sonos & Chromecast devices available via AirPlay.

## Samba

[Samba Docker container](https://github.com/dperson/samba) allows me to share folders from my machine as Samba volumes. I use it to expose my home config folder (`smart-home`) and my media vault (`media`).

## AdGuard Home

![AdGuard Home](https://user-images.githubusercontent.com/3459374/115125413-8b0f9400-9fd0-11eb-8ae1-a0773c9af151.png)

[AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) is a powerful network-wide ads & trackers blocking DNS server.

Once it's set up, it'll cover **all** home devices, so there's no need to install any client-side software for that.

You can read more about it in a [section about Ad-Blocking](../ad-blocking).

<!-- TODO: Add reference -->

## Plex

![Plex](https://user-images.githubusercontent.com/3459374/115125503-2acd2200-9fd1-11eb-8c99-3c839e639a98.png)

[Plex Media Server](https://www.plex.tv/media-server-downloads/#plex-media-server) organizes video, music, and photos from personal media libraries and streams them to smart TVs, streaming boxes, and mobile devices.

Basically, this is a self-hosted Netflix. Plex helps me expose and manage media files from the [hard drive wired to Raspberry Pi](../../hardware#media-volume). It finds localized metadata for my media: descriptions, reviews, posters, and soundtracks.

Media is downloaded via [Transmission](#transmission).

## Transmission

![Transmission](https://user-images.githubusercontent.com/3459374/115125563-ac24b480-9fd1-11eb-84f6-0767b70ee4a0.png)

[Transmission](https://transmissionbt.com/) is a popular BitTorrent client. It can be hosted as a Docker container — that's exactly what I did.

I use it for downloading media to [my hard drive](../../hardware#media-volume).

## Umami

![Umami](https://user-images.githubusercontent.com/3459374/115125705-9f549080-9fd2-11eb-9d68-5b6443f4bff8.png)

[Umami](https://umami.is/) is self-hosted analytics for my websites. Simple although completely fits my needs.

<!-- prettier-ignore -->
!!! note
    Official images [does not support ARM architectures](https://github.com/mikecao/umami/issues/593). I've made my own Dockerfile that builds an image right on my Raspberry Pi.

## Bitwarden

![Bitwarden](https://user-images.githubusercontent.com/3459374/116572155-642c5880-a914-11eb-964c-1db0c962a5ef.png)

[Bitwarden](https://bitwarden.com/) is an open-source password manager that can be self-hosted. I'm using [Vaultwarden](https://github.com/dani-garcia/vaultwarden), which is an unofficial Bitwarden client written in Rust. Vaultwarden is especially useful for low powerful machines, like Raspberry Pi.
