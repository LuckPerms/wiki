#!/bin/sh
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

npm install
pip3 install -r requirements.txt

python3 gen_plain.py ../pages/ > plain.json
cat plain.json | node gen_index.js > index.json
