---
title: Windows Mover and Resizer - Troubleshooting
description: Encountering issues with the Windows Mover and Resizer plugin on your Stream Deck? Our troubleshooting guide has the answers. Find solutions to common problems and get your setup back on track with BarRaider's plugin documentation.
---

# Windows mover and resizer - Troubleshooting

## The applications list is missing my app
The plugin will only show you applications that are currently running. If you don't see an application on the list - make sure it's running.

## The "Screens" dropdown is empty
This is usually a result of a corrupted video driver on your PC. The most common culprit is TeamViewer. Try uninstalling it.

## It doesn't move my application
- Verify your app **isn't** running as administrator. Due to Windows restrictions, apps running as admin cannot be moved. 
- Some apps from the **Microsoft Store (UWP Apps)** can have trouble being moved using the Specific Application setting. Please try using **Current Focused Window** setting.

## Using the "Get current window coordinates" button
The Get current window coordinates shows the coordinates relative to the 0,0 (top-left) of your Primary screen. This is due to the way Windows calculates the coordinates. Therefore it will also change the screen selector to show the Primary screen, even if the window is on another screen. **Do not change it back**, or it will yeet your app out of the screens.

## How do I launch an application?
The plugin will not launch an application, it will only move one that is already running. However you can easily create a **multi-action** that.

1. Opens an app (using Advanced Launcher plugin).
2. Runs this plugin to move it to required location.