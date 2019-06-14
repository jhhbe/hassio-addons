# Meter Reader

Put a webcam in front of your utility meter and AWS Rekognition sends the reading over MQTT to a MQTT server of your choice.


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