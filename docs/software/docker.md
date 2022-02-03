# Docker Containers

Main `docker-compose` file lives alongside Home Assistant configuration in a config folder.

## Portainer CE

![Portainer CE](https://user-images.githubusercontent.com/3459374/115123723-ffddd080-9fc6-11eb-8f26-e11f48ef185e.png)

[Portainer](https://documentation.portainer.io) is a lightweight management UI that allows easy Docker management.

I use it for restarting, stoping, killing docker containers. I can check logs, ports, statistics. This is my primary tool, that replaces Home Assistant Supervisor.

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

## Samba

[Samba Docker container](https://github.com/dperson/samba) allows me to share folders from my machine as Samba volumes. I use it to expose my home config folder (`smart-home`) and my media vault (`media`).

## AdGuard Home

![AdGuard Home](https://user-images.githubusercontent.com/3459374/115125413-8b0f9400-9fd0-11eb-8ae1-a0773c9af151.png)

[AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) is a powerful network-wide ads & trackers blocking DNS server.

Once it's set up, it'll cover **all** home devices, so there's no need to install any client-side software for that.

You can read more about it in a [section about Ad-Blocking](../ad-blocking).

## Plex

![Plex](https://user-images.githubusercontent.com/3459374/115125503-2acd2200-9fd1-11eb-8c99-3c839e639a98.png)

[Plex Media Server](https://www.plex.tv/media-server-downloads/#plex-media-server) organizes video, music, and photos from personal media libraries and streams them to smart TVs, streaming boxes, and mobile devices.

Basically, this is a self-hosted Netflix. Plex helps me expose and manage media files from the [hard drive wired to Raspberry Pi](../../hardware#media-volume). It finds localized metadata for my media: descriptions, reviews, posters, and soundtracks.

Media is downloaded via [Transmission](#transmission).

## Transmission

![Transmission](https://user-images.githubusercontent.com/3459374/115125563-ac24b480-9fd1-11eb-84f6-0767b70ee4a0.png)

[Transmission](https://transmissionbt.com/) is a popular BitTorrent client. It can be hosted as a Docker container — that's exactly what I did.

I use it for downloading media to [my hard drive](../../hardware#media-volume).

## Bitwarden

![Bitwarden](https://user-images.githubusercontent.com/3459374/116572155-642c5880-a914-11eb-964c-1db0c962a5ef.png)

[Bitwarden](https://bitwarden.com/) is an open-source password manager that can be self-hosted. I'm using [Vaultwarden](https://github.com/dani-garcia/vaultwarden), which is an unofficial Bitwarden client written in Rust. Vaultwarden is especially useful for low powerful machines, like Raspberry Pi.
