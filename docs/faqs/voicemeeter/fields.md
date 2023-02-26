---
title: VoiceMeeter - Fields Explanation
description: Get a detailed explanation of the various fields and configurations in the VoiceMeeter plugin for the Elgato Stream Deck.
---

# VoiceMeeter - Fields explanation
- **Mode1 Key Press** - The configuration to set when we're toggling into Mode1 -> Use this to turn ON the setting e.g. `Strip[0].Mute=1`.
- **Mode1 Check** - True/False value to determine if we're in Mode1.
    - Example: If you input: `Strip[0].Mute` the plugin will determine you're in Mode1 every time Strip0 is muted.
- **Mode2 Key Press** - The configuration to set when we're toggling into Mode2 -> Use this to turn OFF the setting e.g. `Strip[0].Mute=0`.
- **Modex Image** - Customizable image that will be shown when you're in Mode1.
- **Title** - Used to determine if you want a dynamic title (Based on the "Title Value" field) or a static title (Based on the "Title field" at the very top).
- **Title Prefix** - Text to add before displaying the Title Value.
    - **Tip:** Type `\n` to make the title multi-line.
- **Title Value** - Value to display in the title. Example: If you input: `Strip[0].Mono` it will display 1 when Mono is enabled on Strip0 and 0 otherwise.