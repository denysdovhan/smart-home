# Ad Blocking

I'm using [AdGuard Home](https://adguard.com/en/adguard-home/overview.html) as my primary ad-blocking solution. AdGuard is a DNS-based ad-blocking tool that checks and blocks requests to advertisement domains.

There is a Docker container for [AdGuard Home](https://hub.docker.com/r/adguard/adguardhome).

<!-- prettier-ignore -->
!!! warning
    On Ubuntu, there's [an issue with `systemd-resolved` consuming port `53`](https://medium.com/@niktrix/getting-rid-of-systemd-resolved-consuming-port-53-605f0234f32f), which is required for AdGuard.

    I've made a script `smart-home adguard-resolved` that automatically fixes that issue.

However, make sure your Internet provider allows custom DNS. My provider was blocking this, and I spend a lot of time trying to figure out what's wrong.

<!-- prettier-ignore -->
!!! note
    AdGuard blocks requests. This means it can break some websites sometimes.

## Ad Blocking List

Here are ad-blocking lists I use:

- AdAway `https://adaway.org/hosts.txt`
- Malware Domain List `https://www.malwaredomainlist.com/hostslist/hosts.txt`
- NoTracking List `https://raw.githubusercontent.com/notracking/hosts-blocklists/master/adblock/adblock.txt`
- YouTube Ads DNS `https://raw.githubusercontent.com/kboghdady/youTube_ads_4_pi-hole/master/youtubelist.txt`
- AdGuard Base Filter `https://filters.adtidy.org/extension/chromium/filters/2.txt`
- AdGuard Annoyances Filter `https://filters.adtidy.org/extension/chromium/filters/14.txt`
- AdGuard Russian Ad Filter `https://filters.adtidy.org/extension/chromium/filters/1.txt`
- AdGuard Mobile Ads Filter `https://filters.adtidy.org/extension/chromium/filters/11.txt`
- AdGuard Safari Filter `https://filters.adtidy.org/extension/chromium/filters/11.txt`

## Considerations

<!-- prettier-ignore -->
!!! caution
    AdGuard is a Russian company, and this opens security concerns.

    Though it's legally located in Cyprus, most of its developers are work from Russian offices.

Make sure you use only the self-hosted and open-source version of AdGuard.
