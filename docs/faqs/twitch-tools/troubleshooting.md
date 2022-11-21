# Troubleshooting

## Validation failed error
Solution depends on what you're seeing in your browser.

### Browser shows and error
1. Try restarting the Stream Deck Software and try setting up again.
![restarting stream deck](https://barraider.com/images/restart.png"Restarting SD Software")
1. Change the default browser to Edge and try again.
2. Using the Edge browser follow [this guide](https://www.whatismybrowser.com/guides/how-to-enable-javascript/edge) and when you come across the allow/block list, add `localhost:4201` to the allow list.

### Browser shows success but not connecting
This is usually a Firewall/Antivirus/VPN/PiHole blocking the connection. Find the culprit and fix/disable it and try again.