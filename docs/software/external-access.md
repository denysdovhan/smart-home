# External Access

This page describes how I make my smart home accessible from the outer world.

## Prior art

When I was running Home Assistant OS, I had [DuckDNS add-on](https://github.com/home-assistant/addons/tree/master/duckdns) installed. DuckDNS addon is the simplest way to make your HA instance available externally available. It will automatically point your DuckDNS record to your router's IP and request a Let's Encrypt SSL certificate.

Downsides of this approach:

- it is not so convenient when you try to expose more services as subdomains;
- it exposes your router's IP to everyone on the internet, making you vulnerable to DDoS attacks.

That's why I've migrated to a more universal setup.

## Reverse proxy via Nginx Proxy Manager

![Nginx Proxy Manager](https://user-images.githubusercontent.com/3459374/115125358-44219e80-9fd0-11eb-8a72-27383603d546.png)

[Nginx Proxy Manager](https://nginxproxymanager.com) is a Docker container for managing Nginx proxy hosts with a simple, powerful interface. It makes reverse proxying a breeze.

It let you configure proxies via UI, making it easy, especially for those who don't have any experience with Nginx. It automatically requests, invalidates, and renews SSL certificates from [Let's Encrypt](https://letsencrypt.org/). It blocks common attacks. It provides basic auth for unsecured services.

It's simple and powerful. I highly recommend it for your home networks.

## DNS via Cloudflare

![Cloudflare Dashboard](https://user-images.githubusercontent.com/3459374/115260334-54a25800-a13b-11eb-9836-5708a4572389.png)

[Cloudflare](https://cloudflare.com) is a company that provides free DNS and CDN services.

Cloudflare gives lots of useful services for free, and it's easy to set up. It gives a free additional level of security by hiding your router's IP, DDoS mitigation, firewall, access policies, etc. It also improves performance by caching and wide CDN.

The most important use-cases for me: hiding my home IP and protecting from common attacks.

My main DNS A-type record exposes my [Nginx Proxy Manager](#reverse-proxy-via-nginx-proxy-manager) (ports `80` and `443`). This name record points to my Home Assistant instance. Other services are exposed via CNAME-type records pointing to the main A-type record.

To avoid issues with DDNS, I have enabled [Cloudflare integration for Home Assistant](https://www.home-assistant.io/integrations/cloudflare/) for updating my home IP in Cloudflare DNS records.

## Accessing SSH and Samba via OpenVPN

TODO: Update about Wireguard

Using Cloudflare makes it impossible to access my home via SSH using a domain name. Additionally, I don't want to expose any other ports on my router except `80` and `443`.

My router has a built-in [OpenVPN](https://openvpn.net/) server. When I want to SSH into my home server or open a volume over SSH, I just connect to my home VPN. Once I am connected, I can do everything, like I'm connected to my home WiFi.
