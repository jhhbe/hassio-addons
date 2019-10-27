import inotify.adapters, os, shutil, glob, json

config_json = json.loads(open("/data/options.json").read())

notifier = inotify.adapters.Inotify()
notifier.add_watch(config_json["source"])

for event in notifier.event_gen():
  if event is not None:
    if 'IN_CLOSE_WRITE' in event[1]:
      if config_json["destination"] != "":
        #print ("file '{0}' created in '{1}'".format(event[3], event[2]))
        #print(config_json["source"]+"/{0}".format(event[3]), config_json["destination"]+"/")
        files = glob.glob(config_json["destination"]+"/*")
        #print("remove latest - - - - - - - ")
        for f in files:
          #print(f)
          os.remove(f)
        #print(config_json["source"]+"/{0}".format(event[3]))
        #print(config_json["destination"]+"/")
        shutil.copy2(config_json["source"]+"/{0}".format(event[3]), config_json["destination"]+"/")
      files = glob.glob(config_json["source"]+"/*.tar")
      files.sort(key=os.path.getmtime, reverse=True)
      i = 0
      #print("removal overtal - - - - ")
      for f in files:
        i = i + 1
        #print(f)
        if (i > config_json["snapshots"]):
          #print("delete")
          os.remove(f)