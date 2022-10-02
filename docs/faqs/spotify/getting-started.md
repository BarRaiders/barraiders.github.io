## Installation
Please follow the step-by-step instructions below to create your own Spotify Developer Application. (Client ID & Client Secret)

!!! info "Spotify Premium required"

    **Note:** Spotify Premium is required for the plugin to work.

!!! info "Keep it to yourself"

    **Reminder:** Do NOT share your Client ID or Client Secret with anybody!

!!! info "Follow the instructions!"

    **Important:** The plugin will not work if you skip a step! Follow the steps slowly, ensuring everything is done correctly.

1. Open https://developer.spotify.com/dashboard/ and Login with your account.
2. Choose to “Create An App” on the Developer Dashboard.
    <figure markdown>
    ![Step 2](img/spotauth1.png)
    </figure>
3. Give your App a unique name and description. (these can be set to anything of your choice)
Select the checkboxes at the bottom and click CREATE.
    <figure markdown>
    ![Step 3](img/spotauth2b.png)
    </figure>
4. Congrats! You have created your App! Now click Edit Settings to add a few necessary details.
    <figure markdown>
    ![Step 4](img/spotauth5.png)
    </figure>
5. Copy the text bellow and paste into the **Website field**
```
http://localhost:4202
```
    <figure markdown>
    ![Step 5](img/spotapp1b.png)
    </figure>
6. Copy the text bellow and paste into the **Redirect URIs field** then click **add**.
```
http://localhost:4202
``` 
    <figure markdown>
    ![Step 6](img/spotapp2b.png)
    </figure>
7. Compare your App settings with ours below. If the Website or Redirect URI is any different, make changes before saving.
    <figure markdown>
    ![Step 7](img/spotapp3b.png)
    </figure>
    !!! info "Save button"

        **Note:** The Save button may reappear. If it does, click it again to save your changes and return to the Dashboard.

8. On the left hand side, you’ll now be able to reveal your Client ID and Client Secret which you’ll now need.
Copy & Paste both the Client ID and Client Secret into the relevant fields in the plugin’s Setup Wizard.
    <figure markdown>
    ![Step 8](img/spotauth8.png)
    </figure>

9. That’s it! Continue with the instructions in the plugin’s Setup Wizard.
10. Once the entire setup is complete, ensure you have the Play/Pause action on your Stream Deck and your device is selected!
    <figure markdown>
    ![Step 10](img/spothelp3.png)
    </figure>

Failing to do so will result in an alert () symbol when the key is pressed, or a red connection symbol as shown in the image below.