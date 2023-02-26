---
title: VoiceMeeter - Usage Examples
description: Explore usage examples of VoiceMeeter with our step-by-step guides for changing output devices, disabling output, adjusting gain, and triggering Midi functions. Learn how to make the most out of VoiceMeeter with your Stream Deck!
---

# VoiceMeeter - Usage examples

## Examples
### Changing your output device using VM Advanced:

- `Strip[x].device.wdm = "NAME OF DEVICE";`
    - Replace `wdm` with one of the following if you use another device type: `sr/wdm/ks/mme/asio`.
    - Replace `x` with strip number, strip overview can be found under [getting started](../getting-started).

### Disabling output device:
Using [Advanced toggle action](../actions/#voicemeeter-advanced-toogle)

- Mode1 Key Press: `Strip[3].device.wdm="NAME OF DEVICE"`
- Mode1 Check: `Strip[3].device or Strip[3].device.wdm`
- Mode2 Key Press: `Strip[3].device.wdm=""`
- Replace wdm with one of the following if you use another device type: `sr/wdm/ks/mme/asio`

### Incrementally increase/decrease gain:
Using [Advanced Press/Long-press](../actions/#advancedpress)<br>
`Strip[0].Gain+=10 or Strip[0].Gain-=10`

### Enable / Disable Output
Using [Advanced toggle action](../actions/#voicemeeter-advanced-toogle)

- Mode1 Key Press: `Strip[X].A1=1`
- Mode1 Check: `Strip[X].A1`
- Mode2 Key Press: `Strip[X].A1=0`

Replace `x` with strip number and `A1` with the output, strip overview can be found under [getting started](../getting-started).

### Fade in/out
Using [Advanced Press/Long-press](../actions/#advancedpress)<br>

- Key press: `Strip[x].FadeTo=(-60.0, 3000)`
- Key press: `Strip[x].FadeTo=(00.0, 3000)`
- Title Prefix: `dB`
- Title Value: `Strip[x].Gain`

Replace `x` with strip number, strip overview can be found under [getting started](../getting-started).


## Midi Usage
You can trigger Midi functions using the SendMidi command from the [Advanced actions](../actions/#advancedpress). Syntax: `SendMidi(DEVICE_NAME, COMMAND, CHANNEL, KEY_ID, VALUE);`

- **DEVICE_NAME:** Name of your device. Start of the name is good too (i.e. nano instead of nanoKORG). Name can be found in VoiceMeeter Macro under `MIDI OUT1 device: 
- **COMMAND:** One of 3 options: - note-on - note-of - ctrl-change.
- **CHANNEL:** Integer value between 1 to 16.
- **KEY_ID:** The ID of the Midi key to turn on/off. This can be found using the LEARN feature inside VoiceMeeter Macro.