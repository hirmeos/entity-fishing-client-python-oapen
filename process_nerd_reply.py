#!/usr/bin/python

import pickle
import sys
import shared_tools
import sqlite3
import os

def main ():
  if len(sys.argv) < 3:
    print "usage : process_nerd_reply.py <file_name> <receiving_database_name>"
  else:  
    if 
    file_name = sys.argv[1]
    cache_path = shared_tools.get_cache_path(file_name)
    
    nerd_data=pickle.load( open (cache_path, "rb") )

    for key,val in nerd_data.items():
      print key

    if 'entities' in nerd_data:
      print nerd_data['entities']


def prepare_tables(data_base_file_path):
  if os.path.exists(database_file_path):
    print database_file_path +" found." 
  else:
    db = sqlite3.connect(database_file_path)
    db.execute('CREATE TABLE IF NOT EXISTS entities(wikipediaExternalRef TEXT UNIQUE PRIMARY KEY )')


def process_entities()


if __name__ == "__main__":
    main()
