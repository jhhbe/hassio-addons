import re, time, datetime, json
import requests

config_json = json.loads(open("/data/options.json").read())

token = config_json["token"]
ip = config_json["ip"]
port = config_json["port"]
pwd =  'Bearer ' + token
hdr = { 'Authorization' : pwd }
upd_interval = config_json["upd_interval"]

slugs = config_json["slugs"]
try:
    notify = config_json["notify"]
except:
    notify = ""

while True:
    for item in config_json["slugs"]:
        print(item["slug"])
        Base_URL = 'http://192.168.2.153:8123/api/hassio/addons/' + item["slug"] + '/info'
        try:
            r = requests.get(Base_URL, headers = hdr)
            detail_json = r.json()
            t = datetime.datetime.now()
            print(t.strftime('%d %b - %H:%M'))
            print(detail_json["data"]["name"])
            print(detail_json["data"]["slug"])
            print(detail_json["data"]["state"])
            print("----------")

            if (detail_json["data"]["state"] == "stopped"):
                url = "http://" + ip + ":" + port + "/api/hassio/addons/" + item["slug"] + "/start"
                try:
                    r = requests.post(url, headers = hdr)
                except:
                    pass
                if (notify != ""):
                    t = datetime.datetime.now()
                    txt = "Herstarten addon, " + detail_json["data"]["name"] + " om " + t.strftime('%d %b - %H:%M') + " !"
                    url = "http://" + ip + ":" + port + "/api/services/notify/" + notify
                    payload = {"message": txt}
                    try:
                        r = requests.post(url, data=json.dumps(payload), headers=hdr)
                    except:
                        pass
        except:
            pass
    time.sleep(upd_interval)
