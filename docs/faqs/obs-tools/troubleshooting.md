# Troubleshooting

## Error Images on Keys
If there is an error in the plugin configuration, you might see something like the images below.  Don't worry, they're easy problems to fix!
    <div style="text-align:center;">
        <figure markdown>
            ![OBS is Off](img/obs-off.png)
        </figure>
    </div>
If you see this image, you probably don't have OBS open.  Launch OBS and wait a few seconds. The plugin should update all your keys appropriately.  

If you still see this image after a minute, make sure that OBS Websocket is enabled inside OBS `Tools > obs-websocket Settings > Enable Websocket Server` and make sure you apply any changes you make.
    <div style="text-align:center;">
        <figure markdown>
            ![Disconnected](img/disconnected.png)
        </figure>
    </div>
Something is wrong with the connection between OBS and the plugin.  We need to reconnect them now:

### Re-Connect to OBS
1. Select any OBS Tools action showing the image above. If you already have one selected, click away from it and select it again.
2. The prompt you filled out when you were first [getting started](getting-started.md) will appear.  Fill it out again, extra carefully. Once you close the final prompt, the plugin should reconnect.

## ERROR: The scene item doesn't exist
Make sure the source you are trying to edit is in your current active scene in OBS. (It cannot be in Studio Preview)

## I wish to keep using OBS v27.x

If you're still using OBS **v27.x**, please follow the instructions below to downgrade to **OBS Tools 2.7**:

1. Uninstall **OBS Tools 2.8** from the Stream Deck software.
2. Install **OBS Tools 2.7** following [this link](https://github.com/BarRaider/streamdeck-obstools/releases/download/v2.7/com.barraider.obstools.streamDeckPlugin).
3. Quit the Stream Deck software see image bellow.
4. Navigate to `%appdata%\Elgato\StreamDeck\Plugins\com.barraider.obstools.sdPlugin`.
5. Inside of the directory above, locate the `manifest.json` file, and open it in a text editor of your choice (e.g. Notepad).
6. Use the **Find** feature (`CTRL+F`) and search for `"Version"`. Once located, change the value from **2.7** to **2.8**.
7. Save the file, restart the Stream Deck software and you'll be all set.

![Restart](https://barraider.com/images/restart.png)