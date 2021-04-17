# Getting Started

My smart home can be quickly deployed using this guide:

- Backup everything before performing any action.
- Install [Ubuntu Server](https://ubuntu.com/download/raspberry-pi) on card via [Raspberry Pi Imager](https://www.raspberrypi.org/software/).
- Once flashing is done, add a file called `ssh` in the root of the card. This is required to turn on SSH access.
- Insert card and plug in Raspberry Pi. Let it a few minutes to start.
- Connect via ssh using `ssh ubuntu@<ip>`. You can get the IP in router's connected devices panel.
- Clone `smart-home` to home folder.
- Add smart-home binaries to `PATH` and set `SMART_HOME_DIR`:
  ```bash
  echo 'export SMART_HOME_DIR="$HOME/smart-home"' >> ~/.bashrc
  echo 'export PATH="$PATH:$HOME/smart-home/bin"' >> ~/.bashrc
  source ~/.bashrc
  ```
- Init smart-home via `smart-home init`.
- Fix network manager vie `smart-home setup-network`.
- Generate new mqtt user via `smart-home add-mosquitto-user`.
- Fill secret credentials in `.env` file. Use `smart-home password` to generate new passwords.
- Go to Cockpit dashboard (`https://<ip>:`) and set hostname, mount external storage. Reboot after changes.
- Run `smart-home adguard-resolved` to free up port 53 for AdGuard Home.
- Spin up containers via `smart-home start`. This command will pull down images and star up containers.

## Development

Sometime I might want to test something simple localy. [Multipass](https://multipass.run/) is a very nice command line tool for creating Ubuntu VMs on demand.

These commands will help launch and connect to a Ubuntu VM:

```sh
# Launch a new machine called `smart-home` with 16GB disk and 2GB RAM
multipass launch --name smart-home --disk 16G --mem 2G

# Mount a smart-home folder to ~/smart-home on a created VM
multipass mount . smart-home:~/smart-home

# SSH into created VM
multipass shell smart-home
```
