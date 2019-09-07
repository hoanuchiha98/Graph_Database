# Lưu tên các châu lục
#name, full_name, image, object_id, weight, keywords
from api.models.nodes import NodeObject
from connect import neo4j_connect

def create_continent(continents):
    continent = NodeObject("Continent")
    continent.name = continents.get('name')
    print(continent.name)
    continent.full_name = continents.get("full_name")
    print(continent.full_name)
    continent.image = continents.get("image")
    continent.object_id = continents.get("object_id")
    continent.weight = continents.get("weight")
    continent.keywords = continents.get("keywords")
    # print(continent.keywords)
    graph = neo4j_connect()
    graph.create(continent)
    graph.push(continent)
    return continent.__node__

def update_continent(continents, key):
    continent = NodeObject("Continent")
    continent.name = key
    print(continent.name)
    continent.full_name = continents.get("full_name")
    print(continent.full_name)
    continent.image = continents.get("image")
    continent.object_id = continents.get("object_id")
    continent.weight = continents.get("weight")
    continent.keywords = continents.get("keywords")
    graph = neo4j_connect()
    graph.nodes.match("Continent")
    graph.merge(continent)
    graph.push(continent)
    return continent.__node__

def find_all_continent():
    graph = neo4j_connect()
    return list(graph.nodes.match("Continent"))

def find_continent_with_key(key):
    graph = neo4j_connect()
    continent = graph.nodes.match("Continents").where("_.name = '{name}'".format(name=key)).first()
    graph.exists(continent)
    return continent

def delete_continent(key):
    graph = neo4j_connect()
    continent = graph.nodes.match("Continent").where("_.name = '{name}'".format(name=key)).first()
    graph.delete(continent)
    graph.exists(continent)
    # graph.push(continent)
    return ("Success")
