# Welcome to my Smart Home!

![Screenshot 2024-05-24 at 18 48 01](https://github.com/denysdovhan/smart-home/assets/3459374/3eb9c007-4443-4e8d-98bf-cce0e85d631e)

[![GitHub Workflow Status][github-img]][github-url]
[![Last Commit][last-commit-img]][github-url]
[![Commit Activity][commit-activity-img]][github-url]
[![License][license-img]][license-url]
[![GitHub Stars][stars-img]][github-url]
[![Twitter Followers][twitter-img]][twitter-url]

This is my personal smart-home configuration, awakening my home with services and tools. I hope this will help you inspire on the way to built your own smart home.

<!-- prettier-ignore -->
!!!attention "Beware of changes"
    I constantly improve my home. It evolves as I add new devices and services. It's changing as my daily routines are changing.

    Please, keep in mind **this documentation might be outdated** in covering some details. However, I'll try my best to keep this updated.

The best way to discover new ideas and inspire is by [reading the code][github-url], copying-pasting parts of my configuration and adjusting it to your needs.

Read this documentation to see the bigger picture:

[Hardware](./hardware){: .md-button }
[Software](./software/system){: .md-button }
[Inspiration](./resources){: .md-button }

Also, checkout my Home Assistant configuration:

[Home Assistant](https://denysdovhan.com/home-assistant-config){: .md-button }

## What's inside?

My home setup for those who are too lazy to read everything:

- [Proxmox](https://www.proxmox.com/) run on [Beelink Mini S12 Pro](https://www.aliexpress.com/item/1005005200158913.html) as a home server.
- Reverse proxy using [Nginx Proxy Manager](https://nginxproxymanager.com/) with [CloudFlare](https://www.cloudflare.com/).
- [Wireguard VPN](https://www.wireguard.com/) for SSH, Samba and development using [VSCode Remote Containers](https://code.visualstudio.com/docs/devcontainers/containers).
- [Pi-hole](https://pi-hole.net) for blocking ads within home network.
- [Plex Media Server](https://www.plex.tv/media-server-downloads/#plex-media-server) with an external hard drive for hosting movies and TV series.
- [Radarr + Sonarr + Prowlarr + Bazarr](https://wiki.servarr.com/) tools for media management.
- [Transmission](https://transmissionbt.com/) for downloading new media to the hard drive.
- [Vaultwarden](https://github.com/dani-garcia/vaultwarden) for password management (Rust implementation of [Bitwarden](https://bitwarden.com/)).

## Motivation

I write this documentation for two main reasons:

1. **To keep track of growing my smart home.** To maintain an understanding of how things are working.
2. **To help other enthusiasts inspire.** People often ask about my smart home setup. Now I can give them a link to this documentation, instead of explaining everything once again.

## Future Plans

I have a [public Notion board][notion-board] with ideas and tasks for my smart home. You can follow and comment my plans there.

[See future plans][notion-board]{: .md-button }

## License

[MIT][license-url] © [Denys Dovhan][denysdovhan]

<!-- References -->

[notion-board]: https://www.notion.so/denysdovhan/f09ea06da5db4cfa84d3ca50417b93b2?v=5fccab53c2fd4ac188ee0b92c2ca1cb9
[github-url]: https://github.com/denysdovhan/smart-home
[github-img]: https://img.shields.io/github/actions/workflow/status/denysdovhan/smart-home/docs.yml?style=flat-square
[last-commit-img]: https://img.shields.io/github/last-commit/denysdovhan/smart-home?style=flat-square
[commit-activity-img]: https://img.shields.io/github/commit-activity/m/denysdovhan/smart-home?style=flat-square
[license-url]: https://github.com/denysdovhan/smart-home/blob/master/LICENSE
[license-img]: https://img.shields.io/github/license/denysdovhan/smart-home?style=flat-square
[twitter-url]: https://twitter.com/denysdovhan
[twitter-img]: https://img.shields.io/twitter/follow/denysdovhan?label=Follow
[stars-img]: https://img.shields.io/github/stars/denysdovhan/smart-home?style=social
[denysdovhan]: https://denysdovhan.com
