#!/bin/bash

if [ $# -lt 2 ]
  then
    echo "Usage: export_to_csv.sh <path_to_sqlite_DB> <path_to_export_file.csv>"
    exit 1
fi

INPUT_DB=$1
EXPORT_FILE=$2

sqlite3 -header -csv $INPUT_DB "select * from oapen_entities;" > $EXPORT_FILE

