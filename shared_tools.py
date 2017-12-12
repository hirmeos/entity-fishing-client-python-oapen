import sys
import pickle
import re


def get_language_code(language_string):
  languages = {'English' : 'en', 'German' : 'de'}
  if language_string in languages:
    return languages[language_string]
  else:
    "Print language not found: " +language_string
    quit()  

def get_cache_path(file_path):
  extension=re.compile('[\/\.]+',re.IGNORECASE) 
  cache_name = extension.sub('_',file_path)
  
  cache_path = "/tmp/"+cache_name
  return cache_path
