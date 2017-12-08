#!/bin/bash

if [ $# -lt 2 ]
  then
    echo "Usage: run.sh <PDF_FILE_PATH> <RESULT_DB>"
    exit 1
fi

INPUT_FILE=$1
RESULT_DB=$2

echo "INPUT: "$INPUT_FILE
echo "OUTPUT: "$RESULT_DB

./post_nerd.py "$INPUT_FILE" http://nerd.huma-num.fr/nerd/service/disambiguate
./process_nerd_reply.py $INPUT_FILE $RESULT_DB
