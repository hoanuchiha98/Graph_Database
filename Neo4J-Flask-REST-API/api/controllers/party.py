# Lưu tên các đảng phái chính trị
#name, full_name, image, object_id, weight, keywords


from api.models.nodes import NodeObject
from connect import neo4j_connect

def create_party(partys):
    party = NodeObject("Party")
    party.name = partys.get('name')
    print(party.name)
    party.full_name = partys.get("full_name")
    print(party.full_name)
    party.image = partys.get("image")
    party.object_id = partys.get("object_id")
    party.weight = partys.get("weight")
    party.keywords = party.get("keywords")
    # print(party.keywords)
    graph = neo4j_connect()
    graph.create(party)
    graph.push(party)
    return party.__node__

def update_party(partys, key):
    party = NodeObject("Party")
    party.name = key
    print(party.name)
    party.full_name = partys.get("full_name")
    print(party.full_name)
    party.image = partys.get("image")
    party.object_id = partys.get("object_id")
    party.weight = partys.get("weight")
    party.keywords = partys.get("keywords")
    # print(party.keywords)
    graph = neo4j_connect()
    graph.nodes.match("Party")
    graph.merge(party)
    graph.push(party)
    return party.__node__

def find_all_party():
    graph = neo4j_connect()
    return list(graph.nodes.match("Party"))

def find_party_with_key(key):
    graph = neo4j_connect()
    party = graph.nodes.match("Party").where("_.name = '{name}'".format(name=key)).first()
    graph.exists(party)
    return party

def delete_party(key):
    graph = neo4j_connect()
    party = graph.nodes.match("Party").where("_.name = '{name}'".format(name=key)).first()
    graph.delete(party)
    graph.exists(party)
    # graph.push(party)
    return ("Success")