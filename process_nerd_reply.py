#!/usr/bin/python
import pickle
import sys
import shared_tools
import sqlite3
import os

def main ():
  if len(sys.argv) < 4:
    print "usage : process_nerd_reply.py <file_name> <database_path> <English_or_German>"
  else:  
    file_name = sys.argv[1]
    database_file_path = sys.argv[2]
    cache_path = shared_tools.get_cache_path(file_name)
    oapen_id = sys.argv[1].split('/')[-1].split('.')[0]
   
    lang = shared_tools.get_language_code(sys.argv[3])
 
    nerd_data=pickle.load( open (cache_path, "rb") )

    #for key,val in nerd_data.items():
     # print key

    if 'entities' in nerd_data:
      prepare_tables(database_file_path)
      save_entities(oapen_id, nerd_data['entities'], database_file_path, lang)
    else:
      print 'No entities found for file: '+ file_name
      print 'Response was: '+ str(nerd_data)
    
def save_entities(oapen_id, entities,database_file_path, lang ):
  db = sqlite3.connect(database_file_path)
  # remove possible duplicates
  db.execute("delete from oapen_entities where oapen_id = ? ",(oapen_id,))      
   
  # insert terms
  for e in entities:
    if 'wikipediaExternalRef' in e:
      t = e['type'] if 'type' in e else ''
      d = ",".join (e['domains']) if 'domains' in e else ''
      a = 'https://'+lang+'.wikipedia.org/?curid=' + str(e['wikipediaExternalRef'])
      values = (oapen_id, e['rawName'], e['nerd_score'], e['nerd_selection_score'], str(e['wikipediaExternalRef']), a, t, d)
      db.execute('insert into oapen_entities values (?,?,?,?,?,?,?,?) ',values)      

  db.commit()
  print "Result stored in: " + database_file_path

def prepare_tables(database_file_path):
  if os.path.exists(database_file_path):
    print database_file_path +" found." 
  else:
    db = sqlite3.connect(database_file_path)
   
    db.execute('CREATE TABLE IF NOT EXISTS oapen_entities ( oapen_id INT,  rawName TEXT, nerd_score REAL, nerd_selection_score REAL, wikipediaExternalRef TEXT, wiki_URL TEXT, type TEXT, domains TEXT)' )
    db.commit()
    print database_file_path + ' created.'
if __name__ == "__main__":
    main()
