# Lưu tên các quốc gia
# name, full_name, image, object_id, weight, keywords
from api.models.nodes import NodeObject
from connect import neo4j_connect

def create_country(countrys):
    country = NodeObject("Country")
    country.name = countrys.get('name')
    print(country.name)
    country.full_name = countrys.get("full_name")
    print(country.full_name)
    country.image = countrys.get("image")
    country.object_id = countrys.get("object_id")
    country.weight = countrys.get("weight")
    country.keywords = countrys.get("keywords")
    print(countrys.get("keywords"))
    graph = neo4j_connect()
    graph.create(country)
    graph.push(country)
    return country.__node__

def update_country(countrys, key):
    country = NodeObject("Country")
    country.name = key
    print(country.name)
    country.full_name = countrys.get("full_name")
    print(country.full_name)
    country.image = countrys.get("image")
    country.object_id = countrys.get("object_id")
    country.weight = countrys.get("weight")
    country.keywords = countrys.get("keywords")
    graph = neo4j_connect()
    graph.nodes.match("Country")
    graph.merge(country)
    graph.push(country)
    return country.__node__

def find_all_country():
    graph = neo4j_connect()
    return list(graph.nodes.match("Country"))

def find_country_with_key(key):
    graph = neo4j_connect()
    country = graph.nodes.match("Country").where("_.name = '{name}'".format(name=key)).first()
    graph.exists(country)
    return country

def delete_country(key):
    graph = neo4j_connect()
    country = graph.nodes.match("Country").where("_.name = '{name}'".format(name=key)).first()
    graph.delete(country)
    graph.exists(country)
    # graph.push(country)
    return ("Success")