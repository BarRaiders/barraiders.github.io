---
title: SuperMacro - Available Actions
description: Explore all the available actions in the SuperMacro plugin by BarRaider for the Elgato Stream Deck.
---

<!-- NOTE: To you, the Contributor!
    Ironically, the double-bracket syntax used in SuperMacro conflicts with a special Marco syntax we can use here.
    See custom-functions.md in the *root* of the repository for the workaround
-->

# SuperMacro - Available actions 
The plugin includes six actions. Bellow you will find a more in depth description of each action.

## Super Macro
This is the basic implementation. Create a macro and run it on keypress. Examples can be seen in the [Usage Examples](./examples.md) section.

## Super Macro Toggle
Toggle between two different macros on the same key.

## Sticky Super Macro
Click once to enable, the macro will run again and again until either the button is pressed again OR until the [loop](./loops.md) ends.

## Keystroke PTT
This action limits the action to either one command (such as `{{ "{{ctrl}{c}}" }}`) or one character. The command will be run again and again as long as you continue to press the key.

## Sticky Keystroke
This action limits the action to either one command (such as `{{ "{{ctrl}{c}}" }}`) or one character. The command will be run again and again until the button is pressed again OR until the [loop](./loops.md) ends.

## Mouse Location
!!! info "Long pressing button"

    **Note:** Long pressing the button on the Stream Deck will copy the current X,Y shown on the key to your Clipboard.
Consider this more of a helper action, it shows you the current position of your mouse cursor. You can use it to determine where you want SuperMacro to move your mouse (Using the `{{ "{{MOUSEXY}}" }}` [mouse command](./commands.md)).
