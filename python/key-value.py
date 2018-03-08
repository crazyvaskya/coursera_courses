import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#print (storage_path)
args = parser.parse_args ()
key = args.key
value = args.value
#with open(storage_path, 'w') as f:
#    f.seek (0)
open (storage_path, 'a').close ()
with open(storage_path, 'r+') as f:
    if key and value:
       # print ("key {} & value {}".format (key, value))
        if os.stat(storage_path).st_size == 0:
            storage = {}
        else:
            storage = json.loads(f.read())
            f.seek (0)
        #print (storage) 
        if storage.get(key) is None:
            storage[key] = [value]
        else:
            storage[key].append(value)
#      a = json.JSONEncoder ()
        json.dump (storage, f)
    elif key:
        #print ("key {}".format(key))
        string = ""
        if os.stat(storage_path).st_size != 0:
            storage = json.load(f)
            if key in storage:
                for i in storage[key]:
                    string += i + ', '
        print (string[:-2])

