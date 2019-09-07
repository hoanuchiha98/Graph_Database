# Lưu tên các cá nhân trong hệ thống
# name, full_name, image, object_id, type, weight, keywordss

from api.models.nodes import NodeObject
from connect import neo4j_connect

def create_person(persons):
    person = NodeObject("Person")
    person.name = persons.get('name')
    print(person.name)
    person.full_name = persons.get("full_name")
    print(person.full_name)
    person.image = persons.get("image")
    person.object_id = persons.get("object_id")
    person.weight = persons.get("weight")
    person.type = persons.get("type")
    person.keywords = persons.get("keywords")
    # print(person.keywords)
    graph = neo4j_connect()
    graph.create(person)
    graph.push(person)
    return person.__node__

def update_person(persons, key):
    person = NodeObject("Person")
    person.name = persons.get('name')
    print(person.name)
    person.full_name = persons.get("full_name")
    print(person.full_name)
    person.image = persons.get("image")
    person.object_id = persons.get("object_id")
    person.weight = persons.get("weight")
    person.type = persons.get("type")
    person.keywords = persons.get("keywords")
    # print(person.keywords)
    graph = neo4j_connect()
    graph.nodes.match("Person")
    graph.merge(person)
    graph.push(person)
    return person.__node__

def find_all_person():
    graph = neo4j_connect()
    return list(graph.nodes.match("Person"))

def find_person_with_key(key):
    graph = neo4j_connect()
    person = graph.nodes.match("Person").where("_.name = '{name}'".format(name=key)).first()
    graph.exists(person)
    return person

def delete_person(key):
    graph = neo4j_connect()
    person = graph.nodes.match("Person").where("_.name = '{name}'".format(name=key)).first()
    graph.delete(person)
    graph.exists(person)
    # graph.push(person)
    return ("Success")