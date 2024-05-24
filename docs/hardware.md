# Hardware

This is the list of the hardware that is present in my smart home.

You can read more about my hardware (WiFi, ESPHome and Zigbee devices) on my Home Assistant configuration:

[Home Assistant Config](https://denysdovhan.com/home-assistant-config){ .md-button }

## Homelab Server

My homelab server is running on [Beelink Mini S12 Pro](https://www.aliexpress.com/item/1005005200158913.html) with Intel 12th Gen 4-Cores N100 (up to 3.4GHz), 16GB of RAM and 500GB of SSD memory.

It can easily run multiple VMs or LXCs, transcode a few 4K streams, while staying quite and consuming only 8.2 watts at idle and 22.5 watts on max load. It's also very small – a little larger than Apple TV box. This combination of characteristics makes it a perfects smart home server.

=== "Beelink Mini S12 Pro"

    ![Beelink Mini S12 Pro](https://github.com/denysdovhan/home-assistant-config/assets/3459374/c687d08c-10c1-453c-b5b6-74c4e8cf8600)

=== "Packaging"

    ![Packaging](https://github.com/denysdovhan/home-assistant-config/assets/3459374/51dfc5c6-f7bf-4218-8bf0-8cc4ffe9c951)

I use [Seagate Barracuda 2TB 5400rpm 128MB](https://www.amazon.com/Seagate-BarraCuda-Internal-2-5-Inch-ST2000LM015/dp/B01LX13P71?th=1) as a hard driver for media files. 2TB is not much, but there's no much room withing the mini PC casing. I'll work on a better NAS solution in the future. Here's how it looks when open:

![Opened mini PC with HDD within](https://github.com/denysdovhan/home-assistant-config/assets/3459374/975dfa43-878d-4dec-8987-6f981a6bc814)

<!-- prettier-ignore -->
??? note "Previous setup with Raspberry Pi 4B"
    The heart of my smart home is a home server based on [Raspberry Pi 4 Model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) with 4GB of RAM onboard. It's a small, affordable, but nonetheless a very capable device. It's held within an [aluminum alloy case](https://www.aliexpress.com/item/4000039821460.html?spm=a2g0s.9042311.0.0.27424c4dyqD1Vd) I bought on AliExpress. The aluminum case itself helps to disperse heat. Additionally, it came with a heat sink set and a tiny cooling fan.

    I use official [Raspberry Pi 15W USB-C Power Supply](https://www.raspberrypi.org/products/type-c-power-supply/) for powering my smart home server. It is important to get enough power for Raspberry Pi to work properly. Home Assistant requires at least 3A power and this power supply cable handles it just right.

    === "Home Server Hardware"

        Here's a photo of my home server hardware, right after I received it:

        ![My home server hardware](https://user-images.githubusercontent.com/3459374/108915547-b3fd5380-7635-11eb-8b3f-2826d6d2bc54.jpeg)

    === "Alluminium Case Assembling"

        A photo of the aluminum case when I was assembling it:

        ![An aluminum case for my Raspberry Pi](https://user-images.githubusercontent.com/3459374/108916909-9cbf6580-7637-11eb-844e-a701bc01dec7.jpeg)

    === "Assembled and Connected"

        Here's a whole kit assembled and connected to power:

        ![A whole kit assembled and connected to power](https://user-images.githubusercontent.com/3459374/108917386-50c0f080-7638-11eb-9ae2-7bfc379b04d7.jpeg)

    ### Storage

    I use [Kingston SSDNow A400 240GB 2.5"](https://www.kingston.com/en/ssd/a400-solid-state-drive) as a system data storage. It's connected to Raspberry Pi via Ugreen US221 USB 3.0 case adapter. As a media storage I use [Transcend StoreJet 25M3 2TB](https://www.transcend-info.com/Products/No-284) hard drive (which I got from my dad as my birthday present in 2020). Both storages are connecterd via USB 3.0 interface on Raspberry to allow high speed reading, so I can easily stream my media using [Plex](https://plex.tv).

    Media is downloaded directly to my HDD using [Transmission](https://hub.docker.com/r/linuxserver/transmission) container.

    === "SSD and HDD Assembled and Connected"

        ![Assembled Storage and Raspberry Pi](https://user-images.githubusercontent.com/3459374/181816177-1f5a1954-845f-4da3-a3e2-fdc2917474bd.jpeg)

    === "SSD whithin a Case"

        ![Kingston SSD in a case](https://user-images.githubusercontent.com/3459374/181772178-48d26d58-8e62-4522-a452-c3b4832da175.jpeg)

    === "HDD Connected"

        ![HDD connected to Raspberry Pi](https://user-images.githubusercontent.com/3459374/115119826-0eba8800-9fb3-11eb-9b54-ddbe2ea732fb.jpeg)

<!-- prettier-ignore -->
??? note "Previous media storage solution with external HDD"
    ![Transcend volume connected to my Raspberry Pi](https://user-images.githubusercontent.com/3459374/115119826-0eba8800-9fb3-11eb-9b54-ddbe2ea732fb.jpeg)

    I've got a [Transcend StoreJet 25M3 2TB](https://www.transcend-info.com/Products/No-284) hard drive from my dad as my birthday present in 2020.

    I have this HDD connected to my Raspberry Pi. It is used as a storage for my media files (primarly movies and TV-series). USB 3.0 interface on Raspberry allows high speed reading, so I can easily stream my media using [Plex](https://plex.tv).

    Media is downloaded directly to my HDD using [Transmission](https://hub.docker.com/r/linuxserver/transmission) container.

### Installation

I use [Proxmox VE](https://www.proxmox.com/en/). Proxmox allows me to host multiple servers as LXCs and VMs on a single physical machine.

There are multiple guides on [how to install HA in Proxmox](https://www.youtube.com/results?search_query=home+assistant+proxmox+install).
