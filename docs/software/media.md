# Media Managing

My media stack is based on [Serarr containers](https://wiki.servarr.com/), namely: Radarr, Sonarr and Prowlarr.

I've written a thread about my media stack (in Ukrainian):

<blockquote class="twitter-tweet"><p lang="uk" dir="ltr">Витратив свій сьогоднішній вихідний, щоб налаштувати собі ультимативний медіа стек на домашньому сервері. <br><br>Тепер фактично маю домашній стрімінг з моніторингом нового контенту та автоматичним менеджментом.<br><br>Питайте. <a href="https://t.co/W4Za4ZWcVr">pic.twitter.com/W4Za4ZWcVr</a></p>&mdash; Denys 👨‍💻🇺🇦 (@denysdovhan) <a href="https://twitter.com/denysdovhan/status/1634305295512944640?ref_src=twsrc%5Etfw">March 10, 2023</a></blockquote>

## Downloading

[Prowlarr](https://github.com/Prowlarr/Prowlarr) indexes vairous torrent trackers with content. [Sonarr](https://sonarr.tv) and [Radarr](https://radarr.video) use these indexes to find new TV series and movies in a best possible quality. They send content to download client, which is Transmission. [Transmission](https://transmissionbt.com/) downloads content to my hard drive. [Plex](https://plex.tv) takes content on the hard drive and serves it, like self-hosted streaming service.

## Media Organisation

Sonarr and Radarr use hard-links in order to keep files in two places, but take only single space on the hard drive.

Why? Because we also want to seed torrents and we should maintain original filenames in order to do that.

## Custom Profiles for better downloads

I took some inspirations from [TRaSH Guides](https://trash-guides.info) in order to create my custom quality profiles for downloads.

I also added a few more profiles for lanuages, since I prefer to watch my content in my native language - Ukrainian.

I have three major lanuage profiles:

- Ukrainian audio - +3500 points
- Ukrainian subs - +3000 points
- Not Ukrainian or English - -10000

As you see from above, movies and series with Ukrainian lanuage get promoted, when movies without both English and Ukrainian will practivally never be downloaded.
