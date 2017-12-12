#!/usr/bin/python
import requests
import sqlite3
import sys
import json
import pickle
import shared_tools

def main ():
  if len(sys.argv) < 4:
    print "usage : post_nerd.py <file_name> <remote_url> <English_or_German>"
  else: 
    lang = shared_tools.get_language_code(sys.argv[3])
 
    file_name = sys.argv[1]
    try:
      files = {'file' : open(file_name,'rb')}
    except Exception, e:
      print "Could not open filename: " + file_name
      print str(e)
      quit()
    
    url = sys.argv[2]
    
    print lang

    json_data = '''{
      "language": {
          "lang": "''' + lang + '''"
      },
      "onlyNER": false,
      "resultLanguages": [
          "en",
          "de"
      ],
      "nbest": false,
      "customisation": "generic"
    }'''

    data = { "query" : json_data }
    print "posting " + file_name + " to " + url

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
  print "Nerd response stored in " + cache_path

if __name__ == "__main__":
    main()
