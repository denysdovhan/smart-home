# Ad Blocking

I'm using [AdGuard Home](https://adguard.com/en/adguard-home/overview.html) as my primary ad-blocking solution. AdGuard is a DNS-based ad-blocking tool that checks and blocks requests to advertisement domains.

Home Assistant provides an addon for [AdGuard](https://github.com/hassio-addons/addon-adguard-home). It's easy to install and doesn't configure in most cases.

However, make sure your Internet provider allows custom DNS. My provider was blocking this, and I spend a lot of time trying to figure out what's wrong.

<!-- prettier-ignore -->
!!! note
    AdGuard blocks requests. This means it can break some websites sometimes.

## Ad Blocking List

Here are ad-blocking lists I use:

- AdAway `https://adaway.org/hosts.txt`
- Malware Domain List `https://www.malwaredomainlist.com/hostslist/hosts.txt`
- NoTracking List `https://github.com/notracking/hosts-blocklists`
- YouTube Ads `https://github.com/kboghdady/youTube_ads_4_pi-hole`
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
