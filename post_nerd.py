#!/usr/bin/python
import requests
import sqlite3
import sys
import json
import pickle
import shared_tools

def main ():
  if len(sys.argv) < 3:
    print "usage : post_nerd.py <file_name> <remote_url> <output_file>"
  else:  

    file_name = sys.argv[1]
    files = {'file' : open(file_name,'rb')}
    url = sys.argv[2]

    json_data = '''{
      "language": {
          "lang": "en"
      },
      "onlyNER": false,
      "resultLanguages": [
          "de",
          "fr"
      ],
      "nbest": false,
      "customisation": "generic"
    }'''

    data = { "query" : json_data }
    print "posting " + file_name + " to " + url
    #print json.dumps(json_data)
    r = requests.post(url, data=data, files=files )
    resp = {} 
    print r.status_code
    if r.status_code == 200:
      resp = r.json()
      store_answer(file_name, resp)
    else: 
      print r.reason
    
def store_answer(file_name, resp):
  cache_path = shared_tools.get_cache_path(file_name)
  pickle.dump(resp,open(cache_path,"wb" ))
  print cache_path

if __name__ == "__main__":
    main()
