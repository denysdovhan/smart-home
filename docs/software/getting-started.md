# Getting Started

My smart home can be quickly deployed using this guide:

TODO: Update the guideline

- Backup everything before performing any action.
  - Backup `smart-home` folder `tar czvf smart-home.tar.gz smart-home`
  - Backup Plex libary `tar czvf plex.tar.gz ~/Plex`
  - Copy archives locally via `scp`
- Install [Ubuntu Server](https://ubuntu.com/download/raspberry-pi) on card via [Raspberry Pi Imager](https://www.raspberrypi.org/software/).
- Plug SSD in Raspberry Pi. Let it a few minutes to start.
- Connect via ssh using `ssh ubuntu@<ip>`. You can get the IP in router's connected devices panel.
- Clone `smart-home` to home folder or restore from backups
- Add smart-home binaries to `PATH` and set `SMART_HOME_DIR`:
  ```bash
  echo 'export SMART_HOME_DIR="$HOME/smart-home"' >> ~/.bashrc
  echo 'export PATH="$PATH:$HOME/smart-home/bin"' >> ~/.bashrc
  source ~/.bashrc
  ```
- Init smart-home via `smart-home init`.
- Fix network manager vie `smart-home setup-network`.
- Fix network manager vie `smart-home fix-systemd-resolved`.
- Fill secret credentials in `.env` file. Use `smart-home password` to generate new passwords.
- Go to Cockpit dashboard (`https://<ip>:`) and set hostname, mount external storage. Reboot after changes.
- Spin up containers via `smart-home start`. This command will pull down images and star up containers.
