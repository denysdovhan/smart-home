# Ad Blocking

![Pi-hole](https://user-images.githubusercontent.com/3459374/182233051-71f35e28-ac2e-4541-905d-abff4c09e132.png)

[Pi-hole](https://pi-hole.net) is a powerful network-wide ads & trackers blocking DNS server. Once it's set up, it'll cover **all** home devices, so there's no need to install any client-side software for that.

Why Pi-hole? The have well supported [docker image](https://github.com/pi-hole/docker-pi-hole) and they also have very broad community. Every aspect is well documented, so it's much easier to fix stuff when something goes wrong.

<!-- prettier-ignore -->
!!! note
    Pi-hole blocks requests. This means it can break some websites sometimes.

<!-- prettier-ignore -->
!!! warning
    On Ubuntu, there's [an issue with `systemd-resolved` consuming port `53`](https://medium.com/@niktrix/getting-rid-of-systemd-resolved-consuming-port-53-605f0234f32f), which is required for AdGuard.

    I've made a script `smart-home fix-systemd-resolved` that automatically fixes that issue.

## Ad Blocking List

Here are ad-blocking lists I use:

- Every _green_ list on [firebog.net](https://firebog.net)
- Malware Domain List `https://www.malwaredomainlist.com/hostslist/hosts.txt`
- NoTracking List `https://raw.githubusercontent.com/notracking/hosts-blocklists/master/adblock/adblock.txt`
- YouTube Ads DNS `https://raw.githubusercontent.com/kboghdady/youTube_ads_4_pi-hole/master/youtubelist.txt`
- Mobile Ads Filter `https://filters.adtidy.org/extension/chromium/filters/11.txt`
- Annoyances Filter `https://filters.adtidy.org/extension/chromium/filters/14.txt`
- Russian Ad Filter `https://filters.adtidy.org/extension/chromium/filters/1.txt`
- Safari Filter `https://filters.adtidy.org/extension/chromium/filters/11.txt`

## Prior ard

<!-- prettier-ignore -->
!!! caution
    Previously, I used AdGuard Home to blocks advertisements.

    AdGuard is a Russian company, and this opens security concerns. Though it's legally registered in Cyprus, most of its developers work from Russian offices.

    After Russian invasion in Ukraine I decied to move away from AdGuard.

I was using [AdGuard Home](https://adguard.com/en/adguard-home/overview.html) as my primary ad-blocking solution. AdGuard is a DNS-based ad-blocking tool that checks and blocks requests to advertisement domains.

There is a Docker container for [AdGuard Home](https://hub.docker.com/r/adguard/adguardhome).

However, make sure your Internet provider allows custom DNS. My provider was blocking this, and I spend a lot of time trying to figure out what's wrong.
