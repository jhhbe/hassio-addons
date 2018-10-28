# Update OmenWild ZWAVE graph addon

This is a conversion of https://github.com/OmenWild/home-assistant-z-wave-graph into an addon. Requires HASSIO 0.78.0 or higher as it is using a long-lived access token for authentication.

Improvement areas:

* I kept commenting out lines from the original z-wave-graph.py script until it worked so that needs to be cleaned up a bit to avoid embarrasment (for which I cannot blame the original author).

* In order to reduce dependencies I've copied the html file into the docker setup. When the addon starts it copies the html into the /config/www folder. Probably not the most elegant way to achieve this.



## Config

upd_interval: value in seconds to be used as interval between graph data refreshes.

ip: HASSIO ip address, use actual local ip address of your server. HASSIO proxy or 127.0.0.1 will not work.

port: port, default 8123.

token: provide the long-lived access token here. See also: https://www.home-assistant.io/docs/authentication/

## Manual config

In your Home Assistant configuration.yaml add an iframe link in:

**panel_iframe:**
```javascript
    z_wave_graph:
        title: "Z-Wave Graph"
        icon: mdi:vector-square
        url: "http://ip:port/local/z-wave-graph.html"
```
note: you must change ip and port to reflect your setup.