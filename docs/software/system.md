# System Overview

This page describes my system setup. Here you can find software I rely on for running my smart home system.

## [Ubuntu Server 22.04 LTS](https://ubuntu.com/download/server)

I use [Ubuntu](https://ubuntu.com/) as a primary OS for my Raspberry Pi. Ubuntu is a well-maintained Linux distribution with a huge community and large support forums.

It officially [supports Raspberry Pi](https://ubuntu.com/download/raspberry-pi) and can be easily installed via the official Raspberry Pi Imager.

## [Docker](https://www.docker.com/)

I use [Docker](https://www.docker.com/) for managing all containers in my smart home.

Docker allows to encapsulate everything related to a single service within a container. This approach helps to maintain host system clean and manage (start, stop, update and delete) every container separatly.

[`docker-compose`](https://docs.docker.com/compose/`) helps to describe my whole setup in a single file and manage it with a few commands.

## [Cockpit](https://cockpit-project.org/)

![Cockpit UI](https://user-images.githubusercontent.com/3459374/115122655-bdfe5b80-9fc1-11eb-9a68-9ce67f12ce8e.png)

[Cockpit](https://cockpit-project.org/) is a web-based graphical interface for servers. Ubuntu is officially supported.

This tool let me easily manage my system from web browser: network, external drives, processes and services, system update, etc.

## [smart-home](https://github.com/denysdovhan/smart-home/blob/master/bin/smart-home)

Thi is just a bash script I wrote for personal need. You can [find it here](https://github.com/denysdovhan/smart-home/blob/master/bin/smart-home).

This performs typical tasks I do in my smart home, like bootstraping, controlling server, updating, etc.

## Prior art

### Home Assistant OS

Previously, I've been using [Home Assistant OS](https://www.home-assistant.io/installation/#compare-installation-methods) installation. Home Assistant OS was installed directly on my Raspberry Pi, controlling every aspect of it.

<!-- prettier-ignore -->
!!! info
    Home Assistant OS is nice, especially for newbies. Supervisor handles everything: networking, addons, updates, backups, etc. This lets you start quickly, automate your home, thinking in a safe box.

    **Please, use it if you don't fell confident enough** in networking, Linux, and DevOps stuff.

The only major downside is an inability to control the system. You cannot host custom software alongside Home Assistant, you don't have full access to your system, you cannot mount external drives.

As my knowledge was growing, so was my demands. Raspberry Pi is a very capable device, so I knew I can host more useful things for my home on it. First of all, I wanted to hook up an external hard drive and stream my media via Plex.

However, leaving Home Assistant OS means **no more benefits of Supervisor**. I should manage my system myself: network, updates, backups. This bears more responsibility and headache.

I've been developing an alternative solution gradually for a few months, looking for a replacement for every part of the Supervisor's functionality. Then, when I felt confident, I migrated to my new setup.

### Home Assistant Supervised

I was running HA Supervies for a year or so. This worked well for me, though I've decied to move back to Container since it gives much more freedom and control over my system.
