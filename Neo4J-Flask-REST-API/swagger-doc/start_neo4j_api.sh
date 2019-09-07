#!/bin/bash

cd /home/hoan/virtualenv

source neo4j_rest__env/bin/activate
cd /home/hoan/code/Neo4J-Flask-REST-API
python3 server.py >> rest_api.log 2>&1 &

