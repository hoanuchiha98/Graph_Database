# Lưu tên các tổ chức quốc tế
#name, full_name, image, object_id, weight, keywords

from api.models.nodes import NodeObject
from connect import neo4j_connect

def create_internaltional_group(internaltional_groups):
    internaltional_group = NodeObject("Internaltional_Group")
    internaltional_group.name = internaltional_groups.get('name')
    print(internaltional_group.name)
    internaltional_group.full_name = internaltional_groups.get("full_name")
    print(internaltional_group.full_name)
    internaltional_group.image = internaltional_groups.get("image")
    internaltional_group.object_id = internaltional_groups.get("object_id")
    internaltional_group.weight = internaltional_groups.get("weight")
    internaltional_group.keywords = internaltional_groups.get("keywords")
    # print(internaltional_group.keywords)
    graph = neo4j_connect()
    graph.create(internaltional_group)
    graph.push(internaltional_group)
    return internaltional_group.__node__

def update_internaltional_group(internaltional_groups, key):
    internaltional_group = NodeObject("Internaltional_Group")
    internaltional_group.name = key
    print(internaltional_group.name)
    internaltional_group.full_name = internaltional_groups.get("full_name")
    print(internaltional_group.full_name)
    internaltional_group.image = internaltional_groups.get("image")
    internaltional_group.object_id = internaltional_groups.get("object_id")
    internaltional_group.weight = internaltional_groups.get("weight")
    internaltional_group.keywords = internaltional_groups.get("keywords")
    # print(internaltional_group.keywords)
    graph = neo4j_connect()
    graph.nodes.match("Internaltional_Group")
    graph.merge(internaltional_group)
    graph.push(internaltional_group)
    return internaltional_group.__node__

def find_all_internaltional_group():
    graph = neo4j_connect()
    return list(graph.nodes.match("Internaltional_Group"))

def find_internaltional_group_with_key(key):
    graph = neo4j_connect()
    internaltional_group = graph.nodes.match("Internaltional_Group").where("_.name = '{name}'".format(name=key)).first()
    graph.exists(internaltional_group)
    return internaltional_group

def delete_internaltional_group(key):
    graph = neo4j_connect()
    internaltional_group = graph.nodes.match("Internaltional_Group").where("_.name = '{name}'".format(name=key)).first()
    graph.delete(internaltional_group)
    graph.exists(internaltional_group)
    # graph.push(internaltional_group)
    return ("Success")