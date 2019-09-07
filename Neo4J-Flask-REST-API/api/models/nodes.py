from py2neo.ogm import GraphObject, Property, RelatedTo
from connect import neo4j_connect
from py2neo import Node, Relationship

#labels, name, full_name, image, object_id, weight, keywords, type1, datetime, type2
class NodeObject(GraphObject):
    __primarykey__ = "name"
    name  = Property()
    full_name = Property()
    image = Property()
    object_id = Property()
    weight = Property()
    keywords = Property()
    type = Property()
    date_time = Property()
    location = Property()

    def __init__(self, labels):
        self.__primarylabel__ = labels

def create_node(node):
    graph = neo4j_connect()
    transaction = graph.begin()
    node_find = find_node(node.get("labels"), node.get("name"))
    # print(node_find)
    if node_find in ('', None):
        nodes = NodeObject(node.get("labels"))
        nodes.name = node.get("name")
        nodes.full_name = node.get("full_name")
        # if full_name == '':
        #     full_name = ''
        nodes.image = node.get("image")
        # if image == '':
        #     image = ''
        nodes.object_id = node.get("object_id")
        # if object_id == 0:
        #     object_id = ''
        nodes.weight = node.get("weight")
        # if weight == 0:
        #     weight = ''
        nodes.keywords = node.get("keywords")
        # if keywords == '':
        #     keywords = ''
        type1 = node.get("type")
        nodes.date_time = node.get("date_time")
        # if date_time == '':
        #     date_time = ''
        # node_temp = Node(labels, name=name, full_name=full_name, image=image, object_id=object_id,
        #             weight=weight, keywords=keywords, date_time=date_time)
        # node_temp.__primarylabel__ = labels
        # node_temp.__primarykey__ = name
        graph = neo4j_connect()
        transaction = graph.begin()
        # transaction.merge(node_temp, labels, "name", name)
        graph.create(nodes)
        graph.push(nodes)
    else:
        return ("Node đã tồn tại")
    if type1 not in ('', None):
        event_type = Node("event_category", name=type1)
        event_type.__primarylabel__ = "event_category"
        event_type.__primarykey__ = type
        transaction.create(event_type)
        rels_event = Relationship(nodes.__node__, "Belong to the type of event", event_type)
        transaction.create(rels_event)
        #Create rels event category

    transaction.commit()
    transaction.finished()
    cypher = """MATCH path = (n:`{labels}`)-[]-() where n.name = '{name}' """.format(labels=nodes.__primarylabel__,
                                                                                     name=nodes.name)
    result = export_json_run_cypher(cypher)
    return result

def update_node(node):
    if node.get("labels") in ('', None) or node.get("name") in ('', None):
        return None, 201
    node_find = find_node(node.get("labels"), node.get("name"))
    print(node_find)
    # print(node_find)
    if node_find not in ('', None):
        nodes = NodeObject(node.get("labels"))
        nodes.name = node.get("name")
        nodes.full_name = node.get("full_name")
        # if full_name == '':
        #     full_name = ''
        nodes.image = node.get("image")
        # if image == '':
        #     image = ''
        nodes.object_id = node.get("object_id")
        # if object_id == 0:
        #     object_id = ''
        nodes.weight = node.get("weight")
        # if weight == 0:
        #     weight = ''
        nodes.keywords = node.get("keywords")
        # if keywords == '':
        #     keywords = ''
        type1 = node.get("type")
        nodes.date_time = node.get("date_time")
        # if date_time == '':
        #     date_time = ''
        # node_temp = Node(labels, name=name, full_name=full_name, image=image, object_id=object_id,
        #             weight=weight, keywords=keywords, date_time=date_time)
        # node_temp.__primarylabel__ = labels
        # node_temp.__primarykey__ = name
        graph = neo4j_connect()
        transaction = graph.begin()
        # transaction.merge(node_temp, labels, "name", name)
        graph.merge(nodes)
        graph.push(nodes)
        graph.run("MATCH(n:event)-[r]->(p:event_category) detach delete r, p return p")
        if type1 not in ('', None):
            event_type = Node("event_category", name=type1)
            event_type.__primarylabel__ = "event_category"
            event_type.__primarykey__ = type1
            transaction.create(event_type)
            rels_event = Relationship(nodes.__node__, "Belong to the type of event", event_type)
            transaction.create(rels_event)

    transaction.commit()
    transaction.finished()
    cypher = """MATCH path = (n:`{labels}`)-[]-() where n.name = '{name}' """.format(labels=nodes.__primarylabel__, name=nodes.name)
    result = export_json_run_cypher(cypher)
    return result

def delete_node(node):
    labels = node.get("labels")
    name = node.get("name")
    graph = neo4j_connect()
    cypher = """match(n:`{labels}`)-[r]-(p) where n.name = '{name}' detach delete n, r, p""".format(labels=labels, name=name)
    graph.run(cypher)
    return ("Success")

def find_node(labels, name):
    if labels in (None, '') or name in (None, ''):
        return None
    graph = neo4j_connect()
    node = graph.nodes.match(labels, name = name).first()
    # matcher = NodeMatcher(graph)
    # node = matcher.match(labels, name = name).first()
    #graph.exists(node)
    return node

def export_json_run_cypher(sql):
    #sql = '''MATCH path = (n:country)-[r:`Đồng minh`]->(p:country) return n ,r, p'''
    query = """CALL apoc.export.json.query("%s with nodes(path) as nodes, relationships(path)
                       as rels unwind nodes as nodes1 unwind rels as rels1 with nodes1, rels1 RETURN
                       collect(distinct nodes1) as nodes, collect(distinct rels1) as relationships","query.json",{})""" % (sql)
    json_load = """WITH "query.json" AS url CALL apoc.load.json(url) YIELD value return value.nodes as node, value.relationships as relationships"""
    try:
        graph = neo4j_connect()
        print(query)
        if (graph.run(f"{sql} return path").data() not in ([], None)):
            graph.run(query)
            query_json = graph.run(json_load).to_data_frame()
            result = query_json.to_dict(orient='records')
            return result
        else:
            return ("Not Found")
    except:
        return ("Not Found")
def export_json_node(sql):
    #sql = '''MATCH path = (n:country)-[r:`Đồng minh`]->(p:country) return n ,r, p'''
    query = """CALL apoc.export.json.query("%s RETURN n as nodes","nodej.json",{})""" % (sql)
    json_load = """WITH "nodej.json" AS url CALL apoc.load.json(url) YIELD value return value.nodes as node"""
    try:
        graph = neo4j_connect()
        print(query)
        if (graph.run(f"{sql} return n").data() not in ([], None)):
            graph.run(query)
            query_json = graph.run(json_load).to_data_frame()
            result = query_json.to_dict(orient='records')
            return result
        else:
            return ("Not Found")
    except:
        return ("Not Found")

def export_json_relationship(sql):
    #sql = '''MATCH path = (n:country)-[r:`Đồng minh`]->(p:country) return n ,r, p'''
    query = """CALL apoc.export.json.query("%s RETURN r as relationships","rels.json",{})""" % (sql)
    json_load = """WITH "rels.json" AS url CALL apoc.load.json(url) YIELD value return value.relationships as relationships"""
    try:
        graph = neo4j_connect()
        print(query)
        if (graph.run(f"{sql} return r").data() not in ([], None)):
            graph.run(query)
            query_json = graph.run(json_load).to_data_frame()
            result = query_json.to_dict(orient='records')
            return result
        else:
            return ("Not Found")
    except:
        return ("Not Found")