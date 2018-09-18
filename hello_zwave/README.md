# Update ZWAVE graph

This local addon is an attempt to get some interest going into converting https://github.com/OmenWild/home-assistant-z-wave-graph into a proper addon.

Improvement areas:

* I kept commenting out lines from the original z-wave-graph.py script until it worked so that needs to be cleaned up a bit to avoid embarrasment (for which I cannot blame the original author). Commmunication with addon is using what 'works': API password goes over environment variable, while upd_interval value is read from config file.

* In order to reduce dependencies I've copied the html file into the docker thing. When the addon starts it copies the html into the /config/www folder. Probably not the most elegant way to achieve this.



## Config

upd_interval: value in seconds to be used as interval between graph data refreshes.


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