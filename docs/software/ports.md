# Ports

Here's a table of services and ports exposed via `docker-compose`:

| Service             | Exposed port                                                     |
| ------------------- | ---------------------------------------------------------------- |
| Cockpit             | 9090                                                             |
| Portainer CE        | 9000                                                             |
| Home Assistant      | 8123                                                             |
| Mosquitto           | 1888                                                             |
| Zigbee2MQTT         | 8099                                                             |
| ESPHome             | 6052                                                             |
| Duplicati           | 8200                                                             |
| Adminer             | 8080                                                             |
| Nginx Proxy Manager | 80, 443, 8081                                                    |
| Samba               | 139, 445, 137, 138                                               |
| Pi-hole             | 53, 67, 5300                                                     |
| Plex                | 32400, 3005, 5353, 1900, 8324, 32469, 32410, 32412, 32413, 32414 |
| Transmission        | 9091, 51413                                                      |
| Vaultwarden         | 3880                                                             |
| Sonarr              | 8989                                                             |
| Jackett             | 9117                                                             |
| PS5MQTT             | 8645                                                             |

<!-- prettier-ignore -->
!!! info
    Some services are exposed as `network_mode: host`, so some exposed port might not be listed in the table below.
