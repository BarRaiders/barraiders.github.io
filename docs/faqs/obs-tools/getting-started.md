---
title: OBS Tools - Getting Started
description: Learn how to install and set up the BarRaider OBS Tools plugin on your Stream Deck to control OBS Studio and troubleshooting issues by checking the troubleshooting page.
---

# OBS Tools - Getting Started

!!! info "Did you turn it on?"

    **Note:** OBS must be open for most of these features to work!

## Installation
Install the BarRaider OBS plugin from the Elgato store or from our [Discord](http://discord.barraider.com).

1. After installing, enable the websocket in OBS Studio: `Tools -> obs-websocket Setting`
2. After following the steps above, drag one of the OBS Tools actions on to your Stream Deck and follow the setup wizard’s instructions. (You’ll need the port and password set in the previous step)
    <p align="center">
        <img src="../img/gs1.png"/>
        <div style="text-align:center">
            <figcaption>
                Check that your settings match the settings in this image. <br /><strong>Set your own password.</strong>
            </figcaption>
        </div>
    </p>
## Testing It Out
There are a ton of [Available Actions](./actions.md) in this plugin, but just to make sure everything is working, let's add the `CPU Usage` action as a test. This action is pretty simple, if OBS Studio is running and everything is connected, it will display the CPU usage of OBS like this.

<p align="center">
    <img src="../img/working.png"/>
    <div style="text-align:center">
        <figcaption>
            A number showing how much CPU OBS is using should display on the key if it is working.
        </figcaption>
    </div>
</p>

## It looks different
We use a few specific images to show when the plugin is having trouble communicating with OBS. Visit [troubleshooting](./troubleshooting.md) to learn what these images mean and how to deal with them.