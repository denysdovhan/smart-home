# Introduction

I use [Home Assistant][ha] as my primary smart home software. It allows me to tied down every separate ecosystem, every device, and every service together.

This is a very powerful tool, allowing to built complex and smart automation based on multiple triggers and conditions, performing different actions.

So far, I'm happy with [Home Assistant][ha] and strongly recommend trying it if you are a smart home enthusiast.

## Limitations

I'm renting my apartment. My landlord handles fixing stuff in my home, covering all the expenses. The only downside is that I can't change anything in my home.

I can't disassemble anything and use custom switches or sockets. It means I can't change only easily accessible parts, like bulbs.

## Prior Art

I began my smart home journey with an [Aqara Hub](https://www.aliexpress.com/item/32910909157.html) and a few bulbs.

In the beginning, I was hoping to consolidate my smart home over HomeKit, because I'd already had a few Apple devices. Shortly after, I run into multiple limitations. After a year of using Aqara setup, I decided to switch to the more universal and powerful solution — [Home Assistant][ha].

Now I easily pass my devices to the HomeKit as well as to the Google Home app.

## How I make my automations

<!-- prettier-ignore -->
!!! tip
    I highly suggest reading a blog post called [Perfect Home Automation](https://www.home-assistant.io/blog/2016/01/19/perfect-home-automation/) written by Home Assistant creator Paulus Schoutsen.

    This article contains valid points about developing home automation. This will help you develop the right mindset while building your smart home.

There are a few rules I use while building my smart home:

- **You should not adapt to technologies.** Things should _just work_. You shouldn't break your own daily routines in order to adapt to your home. Home automation should blend with your current workflow, not replace it.
- **You are not the only user of your home automation.** Even when you live alone, you may have guests. Think about how they're going to use your home.
- **Limit the impact of failures.** Smart homes are complex: eventually, things will go wrong. Make sure things will have a limited impact when they fail. Ideally, devices should fall back to a pre-smart home experience.
- **Automations must be seamless.** Nobody controls lights from the phone except for showing off. This means that everything you automate has to work flawlessly. Even when automation works perfectly 90% of the time, the rest 10% will ruin the whole positive experience.

That's what I keep in mind. This helps a lot.

## Device Tracking

![Presence cards](https://user-images.githubusercontent.com/3459374/109867009-afa4ec00-7c6e-11eb-9fa2-eb3d64cf7dd2.png)

Presence detection is done by combination of two components: [ASUSWRT][asuswrt] and [Mobile App][mobile_app].

- [ASUSWRT][asuswrt] connects to my [ASUS router](/hardware/#wireless-router) and checks, if any of family members phones is connected to WiFi.
- [Mobile App][mobile_app] tracks our phone locations when we are not home. This integration also provides muscles info, like battery levels.

<!-- References -->

[ha]: https://www.home-assistant.io/
[asuswrt]: https://www.home-assistant.io/integrations/asuswrt
[mobile_app]: https://www.home-assistant.io/integrations/mobile_app/
