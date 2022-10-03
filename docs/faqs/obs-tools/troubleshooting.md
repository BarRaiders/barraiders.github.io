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

---

## ERROR: The scene item doesn't exist
Make sure the source you are trying to edit is in your current active scene in OBS. (It cannot be in Studio Preview)


