# Getting Started

My smart home can be quickly deployed using this guide:

1.  Backup everything before performing any action.

1.  Install [Raspberry Pi OS x64](https://downloads.raspberrypi.org/raspios_arm64/images/).

1.  Press CMD-Shift-X during flashing and setup SSH access, password and timezone before flashing.

1.  Insert card and plug in Raspberry Pi. Let it a few minutes to start.

1.  Connect via ssh using `ssh pi@<ip>`. You can get the IP in router's connected devices panel.

1.  `sudo apt update && sudo apt upgrade -y`

1.  `sudo rpi-update`

1.  `sudo reboot`

1.  `sudo apt-get install -y jq wget curl udisks2 apparmor-utils libglib2.0-bin network-manager dbus`

1.  Setup WiFi and Ethernet

    1.  `sudo nano /etc/dhcpcd.conf`
    1.  Add `denyinterfaces wlan0` at the end of the file.
    1.  `sudo reboot`
    1.  `sudo nmtui`. Connect to the WiFi. Set static IP.
    1.  Add route for WiFi `0.0.0.0/0` with `204` as a metric. In order to fallback to WiFi when Ethernet is disconnected.

1.  `sudo raspi-config`. Setup locales.

1.  Fix AppArmor issues.

    1. `sudo nano /boot/cmdline.txt`
    1. Add `lsm=apparmor` and the end of the line.

1.  `sudo reboot`

1.  Install Docker

    ```bash
    sudo curl -fsSL get.docker.com | sh
    sudo gpasswd -a $USER docker
    newgrp docker
    ```

1.  Installing OS-Agent

    ```bash
    wget https://github.com/home-assistant/os-agent/releases/download/1.2.2/os-agent_1.2.2_linux_aarch64.deb
    sudo dpkg -i os-agent_1.2.2_linux_aarch64.deb
    ```

1.  Installing Home Assistant Supervised

    ```bash
    wget https://github.com/home-assistant/supervised-installer/releases/latest/download/homeassistant-supervised.deb
    sudo dpkg -i homeassistant-supervised.deb
    ```

1.  Recover from the latest backup.

1.  Add smart-home binaries to `PATH` and set `SMART_HOME_DIR`:

    ```bash
    echo 'export SMART_HOME_DIR="/usr/share/hassio/homeassistant"' >> ~/.bashrc
    echo 'export PATH="$PATH:$SMART_HOME_DIR/bin"' >> ~/.bashrc
    source ~/.bashrc
    ```

1.  Go to Cockpit dashboard (`https://<ip>:`) and set hostname, mount external storage. Reboot after changes.

1.  Spin up containers via `smart-home start`. This command will pull down images and star up containers.
