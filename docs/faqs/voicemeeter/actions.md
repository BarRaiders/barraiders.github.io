---
title: 'VoiceMeeter - Actions'
tags: 
    - streamdeck
    - barraider
    - voicemeeter
description: "Explanation of all the available actions in the VoiceMeeter plugin by BarRaider for the Elgato Stream Deck."
---

# Available Actions

## VoiceMeeter Mute/Unmute
- Allows you to easily connect to one of VoiceMeeter's Strips or Buses
- 3 different modes: Toggle/Push-To-Talk/Single Setting (on/off)
- See a live indication of the current status on Stream Deck (never forget your microphone on again!)
- Can also be used to mute/unmute different Strips/Buses such as Spotify/Background music/etc.
- Choose from 4 different icons to display the mute/unmute settings
- Choose your own images to display, instead of the 4 pre-defined icons

## VoiceMeeter Modify Setting
- Allows you to easily modify various VoiceMeeter settings
- Supports a whole list of options for each Strip/Bus
- Options include modifying the: Gain slider, gate, comp, mono button, solo button, audibility, color_x, color_y, eqgain1, eqgain2, eqgain3, fx_x, fx_y, mc,pan_x, pan_y (Valid values can be found starting on page 9 of [VoiceMeeter API PDF](https://download.vb-audio.com/Download_CABLE/VoicemeeterRemoteAPI.pdf#page=9).
- Live feedback on the current value of that setting
- Supports both Press and Long Press (allows you to toggle between two preset values for this setting)
- Option to turn off the Live feedback and set the title to whatever you want (including a prefix using the TitlePrefix parameter)

## <a name="advancedpress"></a> VoiceMeeter Advanced Press/Long-Press

!!! info "Advanced users"

    **Note:** This is for advanced users, but you can find field explanations under the available fields page.

- Allows you to directly modify a whole set of settings
    - Example: `Strip[0].mono=1;Strip[1].Mute=1;Bus[2].Gain=-20;`
- Additional examples can be found on the [VoiceMeeter forum](https://forum.vb-audio.com/viewtopic.php?f=8&t=346&sid=a773394396c10847fd6fd7e332a55e49#p495) and the [VoiceMeeter API PDF](https://download.vb-audio.com/Download_CABLE/VoicemeeterRemoteAPI.pdf).
- Supports both Press and Long Press (allows you to change between two preset list of settings)
- Live feedback on whatever setting you choose
- Option to turn off the Live feedback and set the title to whatever you want (including a prefix using the TitlePrefix parameter)

## VoiceMeeter Advanced Toggle
Note: This is for advanced users but there are explanations under the Fields explained section below

- Focused on toggling between two modes (versus press and long press in the VoiceMeeter Advanced Press/Long-Press)
- Mode1 should always turn things ON and Mode2 should turn things OFF
    - Example: `Strip[0].mono=1;Strip[1].Mute=1;Bus[2].Gain=-20;`
- Additional examples can be found on the [VoiceMeeter forum](https://forum.vb-audio.com/viewtopic.php?f=8&t=346&sid=a773394396c10847fd6fd7e332a55e49#p495) and the [VoiceMeeter API PDF](https://download.vb-audio.com/Download_CABLE/VoicemeeterRemoteAPI.pdf).
- Supports toggling between two preset list of settings
- Supports different user-defined icons for each preset
- Live feedback on whatever setting you choose
- Option to turn off the Live feedback and set the title to whatever you want (including a prefix using the TitlePrefix parameter)

## VoiceMeeter Advanced PTT
- The Advanced PTT action allows you to set a bunch of settings until you release the key.

## MacroButton Toggle
- Allows running VoiceMeeter macros from the Stream Deck. Supports both Toggle and Push modes. The Logical ID number is shown at the top-center of every VoiceMeeter macro.