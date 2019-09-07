# Lưu tên các event
#name, full_name, image, object_id, weight, keywords, type, date_time

from api.models.nodes import NodeObject
from py2neo import Node, Relationship
from connect import neo4j_connect

def create_event(events):
    # print(object)
    # event = NodeObject("event")
    name = events.get('name')
    full_name = events.get("full_name")
    image = events.get("image")
    object_id = events.get("object_id")
    weight = events.get("weight")
    type1 = events.get("type")
    location = events.get("location")
    date_time = events.get("date_time")
    keywords = events.get("keywords")
    graph = neo4j_connect()
    event_find = graph.nodes.match("Event", name=name).first()
    if event_find not in ('', None):
        return ("Event da ton tai")
    pattern = """ Create(m:Event{{name:'{name}', full_name:'{full_name}', image:'{image}', object_id:{object_id}, weight:{weight}, location:'{location}', date_time: datetime("{date_time}"), keywords:'{keywords}'}}) return m"""
    pattern = pattern.format(name = name, full_name = full_name, image = image, object_id = object_id, weight = weight, location = location, date_time = date_time, keywords = keywords)
    print(pattern)
    graph.run(pattern)
    event = graph.nodes.match("Event", name = name).first()
    print(event)
    transaction = graph.begin()
    if type1 not in ('', None):
        event_type = Node("Event_Category", name=type1)
        event_type.__primarylabel__ = "Event_Category"
        event_type.__primarykey__ = type
        transaction.create(event_type)
        rels_event = Relationship(event, "BELONG TYPE OF EVENT", event_type)
        transaction.create(rels_event)
        #Create rels event category
    object = events.get("object")
    if len(object) not in ('', None):
        for x in object.split(","):
            if x not in('', None):
                object_find = graph.nodes.match(name = x.strip()).first()
                transaction.create(Relationship(object_find, events.get("object_rels"), event))

    transaction.commit()
    transaction.finished()
    return event

def update_event(events, key):
    event = NodeObject("Event")
    event.name = key
    event.full_name = events.get("full_name")
    print(event.full_name)
    event.image = events.get("image")
    event.object_id = events.get("object_id")
    event.weight = events.get("weight")
    type1 = events.get("type")
    event.location = events.get("location")
    event.keywords = events.get("keywords")
    # print(event.keywords)
    graph = neo4j_connect()
    graph.nodes.match("Event")
    graph.merge(event)
    graph.push(event)
    graph.run("MATCH(n:Event)-[r]->(p:Event_Category) detach delete r, p return p")
    if type1 not in ('', None):
        transaction = graph.begin()
        event_type = Node("event_category", name=type1)
        event_type.__primarylabel__ = "Event_Category"
        event_type.__primarykey__ = type1
        transaction.create(event_type)
        rels_event = Relationship(event.__node__, "BELONG TYPE OF EVENT", event_type)
        transaction.create(rels_event)
        transaction.commit()
        transaction.finished()

    return event.__node__

def find_all_event():
    graph = neo4j_connect()
    return list(graph.nodes.match("Event"))

def find_event_with_key(key):
    graph = neo4j_connect()
    event = graph.nodes.match("Event").where("_.name = '{name}'".format(name=key)).first()
    graph.exists(event)
    return event

def delete_event(key):
    graph = neo4j_connect()
    event = graph.nodes.match("Event").where("_.name = '{name}'".format(name=key)).first()
    graph.delete(event)
    graph.exists(event)
    return ("Success")