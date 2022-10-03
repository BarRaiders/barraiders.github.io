# General Issues (Not plugin specific)
On this page you will find troubleshooting steps for general issues that are not specific to a plugin.

## Plugin isn't displaying any text/information on the Stream Deck Key
Some plugins will display information on the key. For example, the **"Stream Counter"** plugin will display a counter for how many times the Stream Deck key has been pressed.

If you do not see any information on the key, please make sure the **"Title"** field at the top of the action settings is **empty**. Anything entered in this field will override all the text/information the plugin is trying to display.

## Install / uninstall
### Installing a plugin
Plugins can be installed from the Elgato Store in the Stream Deck software, or from our [Discord](http://discord.barraider.com) in the [#plugin-releases](https://discord.com/channels/538862772285603880/545898345286336513) channel.

We also offer Early access version of plugins. Read more about it bellow

### Early Access
You can get early access to new plugin updates or plugin releases.
This is all done trough our Discord. Head over to the [#roles](https://discord.com/channels/538862772285603880/748692804263215204) channel and follow the steps there to get the *@Early Access* role. You now have access to the [#early-access](https://discord.com/channels/538862772285603880/571354742144368685) channel.

### Uninstalling a plugin
From the right-hand action bar, find one of the plugin's actions, right click it and choose uninstall.
![How to uninstall](img/uninstall.png"How to uninstall plugin")

Alternativly you can go to the Stream Deck Store, find the plugin and click "uninstall".

#### I can't Install/Uninstall the plugin (pressing Install doesn't do anything)
This issue is usually related to Stream Deck not updating/uninstalling the plugin properly. Try uninstalling and reinstalling the plugin. 

If you can't reinstall, haed to `%appdata%\elgato\streamdeck\plugins` and delete the plugin folder (`com.barraider.<PLUGINNAME>`)

### Installing plugins on Mac
BarRaider's plugins are officially supported **only on Windows**. There’s no ETA for Mac support as BarRaider does not own a Mac. Any Mac devs interested in porting them can contact BarRaider.

## Stream Deck crashes
### Stream Deck Crashes when dragging a plugin to a key
This is probably related to a bug in Stream Deck when the app is not on your Primary Monitor. Move the app to your primary monitor and try again.

### A plugin is crashing the Stream Deck app
Plugins cannot crash the Stream Deck app. This tends to be a Stream Deck issue rather than a plugin problem. Please try uninstalling your Stream Deck app and reinstalling the [latest version from Elgato](https://www.elgato.com/en/gaming/downloads). If that still doesn't help please reach out to [Elgato support](https://help.elgato.com/).

### None of the plugins are working or have weird visuals
BarRaider's plugins use a CDN to ensure all plugins are using the latest library versions. Please whitelist `https://cdn.jsdelivr.net` on your **firewall, network and/or PiHole** (or an alternative) if you have one setup.
![CDN issues](img/cdn.png"CDN whitelisted vs. blacklisted")