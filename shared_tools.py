import sys
import pickle
import re



def get_cache_path(file_path):
  extension=re.compile('[\/\.]+',re.IGNORECASE) 
  cache_name = extension.sub('_',file_path)
  
  cache_path = "/tmp/"+cache_name
  return cache_path
