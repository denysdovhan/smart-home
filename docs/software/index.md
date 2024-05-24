# Introduction

This page describes my system setup. Here you can find software I rely on for running my smart home system.

## Using Proxmox

## Ubuntu LXC

I use [Ubuntu](https://ubuntu.com/) as a primary OS for my Raspberry Pi. Ubuntu is a well-maintained Linux distribution with a huge community and large support forums.

It officially [supports Raspberry Pi](https://ubuntu.com/download/raspberry-pi) and can be easily installed via the official Raspberry Pi Imager.

## [Docker](https://www.docker.com/)

I use [Docker](https://www.docker.com/) for managing all containers in my smart home.

Docker allows to encapsulate everything related to a single service within a container. This approach helps to maintain host system clean and manage (start, stop, update and delete) every container separately.

### Enabling hardware acceleration

## smart-home CLI

This is just a bash script I wrote for personal need. You can [find it here](https://github.com/denysdovhan/smart-home/blob/master/bin/smart-home).

This performs typical tasks I do in my smart home, like bootstraping, controlling server, updating, etc.
