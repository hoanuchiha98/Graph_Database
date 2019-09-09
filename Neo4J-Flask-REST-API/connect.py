"""
	Config for all app
"""
import os
import connexion
from py2neo import Graph
from flask_marshmallow import Marshmallow
from flask import abort


# Get current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connex_app = connexion.App(
    __name__, specification_dir=basedir + "/swagger-doc")

# Get the underlying Flask app instance
app = connex_app.app
# CONFIG
CONFIG = {
    'address':'http://171.244.51.223:7474/db/data',
    'username':'neo4j',
    'password':'vnas@v2'
}
# Base connection URL
def neo4j_connect():
    try:
        graph = Graph(CONFIG['address'], username=CONFIG['username'], password=CONFIG['password'])
        # print(graph.run("return apoc.version()").data())
        return graph
    except:
        print("Fail Connect")
        return abort(400)

# Config connect to Database
# app.config["PY2NEO_ECHO"] = False
# app.config["PY2NEO_DATABASE_URI"] = neo4j_connect()
# app.config["PY2NEO_TRACK_MODIFICATIONS"] = False

# Initialize Marshmallow
ma = Marshmallow(app)