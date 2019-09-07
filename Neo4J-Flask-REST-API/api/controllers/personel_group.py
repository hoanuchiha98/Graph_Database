# Lưu tên các tổ chức cá nhân
#name, full_name, image, object_id, weight, keywords

from api.models.nodes import NodeObject
from py2neo import Graph
from connect import neo4j_connect

def create_personel_group(personel_groups):
    personel_group = NodeObject("Personel_Group")
    personel_group.name = personel_groups.get('name')
    print(personel_group.name)
    personel_group.full_name = personel_groups.get("full_name")
    print(personel_group.full_name)
    personel_group.image = personel_groups.get("image")
    personel_group.object_id = personel_groups.get("object_id")
    personel_group.weight = personel_groups.get("weight")
    personel_group.keywords = personel_groups.get("keywords")
    # print(personel_group.keywords)
    graph = neo4j_connect()
    graph.create(personel_group)
    graph.push(personel_group)
    return personel_group.__node__

def update_personel_group(personel_groups, key):
    personel_group = NodeObject("Personel_Group")
    personel_group.name = key
    print(personel_group.name)
    personel_group.full_name = personel_groups.get("full_name")
    print(personel_group.full_name)
    personel_group.image = personel_groups.get("image")
    personel_group.object_id = personel_groups.get("object_id")
    personel_group.weight = personel_groups.get("weight")
    personel_group.keywords = personel_groups.get("keywords")
    # print(personel_group.keywords)
    graph = neo4j_connect()
    graph.nodes.match("Personel_Group")
    graph.merge(personel_group)
    graph.push(personel_group)
    return personel_group.__node__

def find_all_personel_group():
    graph = neo4j_connect()
    return list(graph.nodes.match("Personel_Group"))

def find_personel_group_with_key(key):
    graph = neo4j_connect()
    personel_group = graph.nodes.match("Personel_Group").where("_.name = '{name}'".format(name=key)).first()
    graph.exists(personel_group)
    return personel_group

def delete_personel_group(key):
    graph = neo4j_connect()
    personel_group = graph.nodes.match("Personel_Group").where("_.name = '{name}'".format(name=key)).first()
    graph.delete(personel_group)
    graph.exists(personel_group)
    # graph.push(personel_group)
    return ("Success")