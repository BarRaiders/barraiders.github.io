---
title: Spotify Plugin - Getting Started
description: Follow this step-by-step guide to create your own Spotify Developer Application, and get started with the Spotify plugin on your Stream Deck. Once setup is complete, control spotify from your Stream Deck and enjoy your music!
---


# Spotify - Getting Started

## Installation
Please follow the step-by-step instructions below to create your own Spotify Developer Application. (Client ID & Client Secret)

!!! note

    Spotify Premium is required for the plugin to work.

!!! warning

    Do NOT share your Client ID or Client Secret with anybody!

!!! warning

    The plugin will not work if you skip a step! Follow the steps slowly, ensuring everything is done correctly.

1. Open [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and Login with your Spotify account.
2. Choose to **Create An App** on the Developer Dashboard.
    ![Step 2](img/spotauth1.png)
3. Give your App a unique name and description. (these can be set to anything of your choice)
    Select the checkboxes at the bottom and click **Create**.
    ![Step 3](img/spotauth2b.png)
4. Congrats! You have created your App! Now click Edit Settings to add a few necessary details.
    ![Step 4](img/spotauth5.png)
5. Copy the text bellow and paste into the **Website field** <a name="step-5"></a>
    ```
    http://localhost:4202
    ```
    ![Step 5](img/spotapp1b.png)
6. Copy the text bellow and paste into the **Redirect URIs field** then click **add**.
    ```
    http://localhost:4202
    ``` 
    ![Step 6](img/spotapp2b.png)
7. Compare your App settings with ours below. If the Website or Redirect URI is any different, make changes before saving.
    ![Step 7](img/spotapp3b.png)

    !!! note

        The Save button may reappear. If it does, click it again to save your changes and return to the [Dashboard](https://developer.spotify.com/dashboard/applications).

8. On the left hand side, you’ll now be able to reveal your Client ID and Client Secret which you’ll now need.
    Copy & Paste both the Client ID and Client Secret into the relevant fields in the plugin’s Setup Wizard.

    ![Step 8](img/spotauth8.png)

9. That’s it! Continue with the instructions in the plugin’s Setup Wizard.
10.  Once the entire setup is complete, ensure you have the Play/Pause action on your Stream Deck and your device is selected!

    ![Step 10](img/spothelp3.png)

    Failing to do so will result in an alert (⚠️) symbol when the key is pressed, or a red connection symbol as shown in the image below.