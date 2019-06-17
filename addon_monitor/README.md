# Addon monitor

Periodically checks if your addon is still running. If not it will try to restart the addon and send a notification.

## Configuration

upd_interval: interval in seconds to check if addons are still active

ip: ip of your Home assistant server

port: port of your server, default 8123

token: provide the long-lived access token here. See also: https://www.home-assistant.io/docs/authentication/

slug: part after addon/ in http:.../hassio/addon/______

notify: which notification platform to use, only tested on tweet


note: you must change ip, port and other settings to reflect your setup.