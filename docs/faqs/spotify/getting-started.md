---
title: Spotify Plugin - Getting Started
description: Follow this step-by-step guide to create your own Spotify Developer Application, and get started with the Spotify plugin on your Stream Deck. Once setup is complete, control spotify from your Stream Deck and enjoy your music!
---


# Spotify - Getting Started

## Installation
Please follow the step-by-step instructions below to create your own Spotify Developer Application. (Client ID & Client Secret)

!!! warning "Spotify Premium required"

    An active Spotify Premium subscription is required to use the plugin.

### Create Spotify Developer App
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/ "Spotify developer dasboard").
2. Login using your Spotify account.
3. Click the **Create app** button.

    ![Step 2](img/spotauth2.png "Click create app in top right corner")

4. Fill out the form with the following information.

    1. **App Name**: `Stream Deck`
        ![Step 3](img/spotauth3.png "Set app name to Stream Deck")

    2. **App description**: `Stream Deck plugin integration`

    3. **Website**: Leave empty.

    4. **Redirect URI**: Copy text below then click **Add**.

        If you see **Auth v2** (1) in top left corner of Spotify Integration setup window:
        { .annotate } 

        1. ![Auth v2](img/spotifyAuthv2.png)

        ```
        http://127.0.0.1:4202
        ```

        !!! warning annotate "Plugin version 3.1 or below"

            If you are using Spotfiy plugin version 3.1 or below, copy the **Redirect URI** below:
            ```
            http://localhost:4202
            ```

        ![Step 3b and 3c](img/spotauth3bc.png "Setting redirect URI to http://127.0.0.1:4202")
            
    5. Check the checkbox for **Web API**.

        ![Step d](img/spotapichoice.png "Enable Web API Checkbox")

5. Accept Spotify's **Terms and Conditions**.

    ![Step 4](img/spotauth4.png "Accepting terms and conditions")

6. Compare your app settings with ours below, then click **Save**.

    ![Step 5](img/spotauthoverview.png "Compare your settings the the ones in the image")

    ### Getting Spotify API Credentials

7. Click the **Settings** button in the application dasboard.

    ![Step 6](img/spothome.png "Button to press to enter application settings")

8. Click **View client secret**.

    ![Step 7](img/spotsettings.png "Displaying client secret")

9. Copy the **Client ID** and **Client secret** and paste them inside of the Spotify Integration setup.

    ![Step 8](img/spotcredentials.png "Copy credentials shown in image")

    !!! danger "Do not share your Client Secret!"

        Do not share your **Client secret**. If you accidentally share it, click **Rotate client secret** to generate a new one.

    ### Setting up play action button

10. Drag and drop the **Play/Pause** action from the sidebar under the **Spotify [BarRaider]** category.

    ![Step 9](img/spotdevice.png "Dragging button and chosing device")

11. To populate the device list:
    1. Start playing a song in the Spotify Application
    2. Whilst a song is playing, click the **Reload devices** button.
    3. Click the drowndown menu and select your device.
    
    !!! warning "Play music in your Spotify App"

        Make sure you are playing music in your Spotify Application before hitting reload devices.

    !!! question "My device list is still emtpy"

        If you don't see your device listed, please refer to the **Device / playlist** section on the [troubleshooting](../troubleshooting/#the-device-dropdown-is-empty "Troubleshooting emtpy device dropdown list") page.
