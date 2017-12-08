#!/usr/bin/python
import pickle
import sys
import shared_tools
import sqlite3
import os

def main ():
  if len(sys.argv) < 3:
    print "usage : process_nerd_reply.py <file_name> <database_path>"
  else:  
    file_name = sys.argv[1]
    database_file_path = sys.argv[2]
    cache_path = shared_tools.get_cache_path(file_name)
    oapen_id = sys.argv[1].split('/')[-1].split('.')[0]
    
    nerd_data=pickle.load( open (cache_path, "rb") )
    for key,val in nerd_data.items():
      print key

    if 'entities' in nerd_data:
      prepare_tables(database_file_path)
      save_entities(oapen_id, nerd_data['entities'], database_file_path)
    
def save_entities(oapen_id, entities,database_file_path):
  db = sqlite3.connect(database_file_path)
  db.execute("delete from oapen_entities where oapen_id = ? ",(oapen_id,))      

  for e in entities:
    if 'wikipediaExternalRef' in e:
      t = e['type'] if 'type' in e else ''
      d = ",".join (e['domains']) if 'domains' in e else ''
      values = (oapen_id, e['wikipediaExternalRef'], e['rawName'], e['nerd_score'], e['nerd_selection_score'], t, d)
      db.execute('insert into oapen_entities values (?,?,?,?,?,?,?) ',values)      

  db.commit()


def prepare_tables(database_file_path):
  if os.path.exists(database_file_path):
    print database_file_path +" found." 
  else:
    db = sqlite3.connect(database_file_path)
   
    db.execute('CREATE TABLE IF NOT EXISTS oapen_entities ( oapen_id INT,  wikipediaExternalRef TEXT, rawName TEXT, nerd_score REAL, nerd_selection_score REAL, type TEXT, domains TEXT)' )

if __name__ == "__main__":
    main()
