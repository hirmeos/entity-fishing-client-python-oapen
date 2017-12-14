#!/bin/bash
set -e

if [ $# -lt 3 ]
  then
    echo "Usage: run.sh <PDF_FILE_PATH> <RESULT_DB> <English_or_German>"
    exit 1
fi

INPUT_FILE=$1
RESULT_DB=$2
LANGUAGE=$3

echo "INPUT: "$INPUT_FILE
echo "OUTPUT: "$RESULT_DB
echo "LANGUAGE: "$LANGUAGE

./post_nerd.py "$INPUT_FILE" http://nerd.huma-num.fr/nerd/service/disambiguate $LANGUAGE
./process_nerd_reply.py $INPUT_FILE $RESULT_DB $LANGUAGE
