# Docker Containers

## Portainer CE

![Portainer CE](https://user-images.githubusercontent.com/3459374/115123723-ffddd080-9fc6-11eb-8f26-e11f48ef185e.png)

[Portainer](https://documentation.portainer.io) is a lightweight management UI that allows easy Docker management.

I use it for restarting, stoping, killing docker containers. I can check logs, ports, statistics. This is my primary tool, that replaces Home Assistant Supervisor.

## Pi-hole

![Pi-hole](https://user-images.githubusercontent.com/3459374/182233051-71f35e28-ac2e-4541-905d-abff4c09e132.png)

[Pi-hole](https://pi-hole.net) is a powerful network-wide ads & trackers blocking DNS server.

Once it's set up, it'll cover **all** home devices, so there's no need to install any client-side software for that.

You can read more about it in a [section about Ad-Blocking](../ad-blocking).

<!-- prettier-ignore -->
!!! note
    Previously, I used AdGuard Home to blocks advertisements. AdGuard is a company founded and developed by Russians. After Russian invasion in Ukraine I decied to move away from AdGuard.

## Plex

![Plex](https://user-images.githubusercontent.com/3459374/115125503-2acd2200-9fd1-11eb-8c99-3c839e639a98.png)

[Plex Media Server](https://www.plex.tv/media-server-downloads/#plex-media-server) organizes video, music, and photos from personal media libraries and streams them to smart TVs, streaming boxes, and mobile devices.

Basically, this is a self-hosted Netflix. Plex helps me expose and manage media files from the [hard drive wired to Raspberry Pi](../../hardware#media-volume). It finds localized metadata for my media: descriptions, reviews, posters, and soundtracks.

Media is downloaded via [Transmission](#transmission).

## Transmission

![Transmission](https://user-images.githubusercontent.com/3459374/115125563-ac24b480-9fd1-11eb-84f6-0767b70ee4a0.png)

[Transmission](https://transmissionbt.com/) is a popular BitTorrent client. It can be hosted as a Docker container — that's exactly what I did.

I use it for downloading media to [my hard drive](../../hardware#media-volume).

## Sonarr, Radarr, Prowlar

![Radarr](https://user-images.githubusercontent.com/3459374/224509674-9486bf8d-73f2-438e-90dd-de1914fee56c.png)

_Servarr_ stack containers provide media managing platform. [Prowlarr](https://github.com/Prowlarr/Prowlarr) provides proxy-API for popular torrent trackers. [Sonarr](https://sonarr.tv) monitors TV Series, downloads and organize them. [Radarr](https://radarr.video) does the same as Sonarr, but for movies.

## Bitwarden

![Bitwarden](https://user-images.githubusercontent.com/3459374/116572155-642c5880-a914-11eb-964c-1db0c962a5ef.png)

[Bitwarden](https://bitwarden.com/) is an open-source password manager that can be self-hosted. I'm using [Vaultwarden](https://github.com/dani-garcia/vaultwarden), which is an unofficial Bitwarden client written in Rust. Vaultwarden is especially useful for low powerful machines, like Raspberry Pi.
