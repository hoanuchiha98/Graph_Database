from py2neo import Relationship, NodeMatcher
from connect import neo4j_connect
from api.models.nodes import export_json_run_cypher, find_node

def create_relationship(rels):
    labels_node1 = rels.get('labels_node1')
    if labels_node1 in ('', None):
        return None, 201
    name_node1 = rels.get('name_node1')
    if name_node1 in ('', None):
        return None, 201
    labels_node2 = rels.get('labels_node2')
    if labels_node2 in ('', None):
        return None, 201
    name_node2 = rels.get('name_node2')
    if name_node2 in ('', None):
        return None, 201
    labels = rels.get('labels')
    name = rels.get('name')
    if labels in ('', None) or name in ('', None):
        return None, 201
    full_name = rels.get('full_name')
    if full_name == '':
        full_name = None
    image = rels.get('image')
    if image == '':
        image == None
    object_id = rels.get('object_id')
    if object_id == 0:
        object_id == None
    weight = rels.get('weight')
    if weight == 0:
        weight == None
    keywords = rels.get('keywords')
    if keywords == '':
        keywords == None
    areas = rels.get('areas')
    if areas == '':
        areas == None
    from_date = rels.get('from_date')
    if from_date == '':
        from_date == None
    to_date  = rels.get('to_date')
    if to_date == '':
        to_date == None
    node1= find_node(labels_node1, name_node1)
    print(node1)
    node2=find_node(labels_node2, name_node2)
    print(node2)
    if node1 in ('', None) or node2 in ('', None):
        return None, 201
    relationship = Relationship(node1, labels, node2, name = name, full_name = full_name,
                                image = image, object_id = object_id, weight = weight, keywords = keywords,
                                areas = areas, from_date = from_date, to_date = to_date)
    relationship.__primarylabel__ = labels
    relationship.__primarykey__ = name
    graph = neo4j_connect()
    transaction = graph.begin()
    transaction.create(relationship)
    transaction.commit()
    transaction.finished()
    graph.exists(relationship)
    # constrain = f"""CREATE CONSTRAINT ON ()-[r:{labels}]-() ASSERT exists(r.name)"""
    # graph.run(constrain)
    return relationship, 200

def update_relationship(rels, key):
    labels_node1 = rels.get('labels_node1')
    if labels_node1 in ('', None):
        return None, 201
    name_node1 = rels.get('name_node1')
    if name_node1 in ('', None):
        return None, 201
    labels_node2 = rels.get('labels_node2')
    if labels_node2 in ('', None):
        return None, 201
    name_node2 = rels.get('name_node2')
    if name_node2 in ('', None):
        return None, 201
    labels = rels.get('labels')
    name = key
    if labels in ('', None) or name in ('', None):
        return None, 201
    full_name = rels.get('full_name')
    if full_name == '':
        full_name = None
    image = rels.get('image')
    if image == '':
        image == None
    object_id = rels.get('object_id')
    if object_id == 0:
        object_id == None
    weight = rels.get('weight')
    if weight == 0:
        weight == None
    keywords = rels.get('keywords')
    if keywords == '':
        keywords == None
    areas = rels.get('areas')
    if areas == '':
        areas == None
    from_date = rels.get('from_date')
    if from_date == '':
        from_date == None
    to_date  = rels.get('to_date')
    if to_date == '':
        to_date == None
    node1= find_node(labels_node1, name_node1)
    print(node1)
    node2=find_node(labels_node2, name_node2)
    print(node2)
    if node1 in ('', None) or node2 in ('', None):
        return None, 201
    relationship = Relationship(node1, labels, node2, name = name, full_name = full_name,
                                image = image, object_id = object_id, weight = weight, keywords = keywords,
                                areas = areas, from_date = from_date, to_date = to_date)
    relationship.__primarylabel__ = labels
    relationship.__primarykey__ = name
    print(relationship)
    graph = neo4j_connect()
    transaction = graph.begin()
    transaction.merge(relationship, primary_key=name, primary_label=labels)
    transaction.commit()
    transaction.finished()
    graph.exists(relationship)
    return relationship, 200

def find_relationship(labels, name):
    print(labels)
    cypher = """MATCH path = ()-[r:`{labels}`]-() where r.name = '{name}' """.format(labels=labels, name=name)
    print(cypher)
    result = export_json_run_cypher(cypher)
    return result
#
# test ={"date_time": "2019-08-25", \
#    "full_name": "sóng thống khổ", \
#    "image": "zxy", \
#    "keywords": "xxx", \
#    "labels": "Bình đẳng", \
#    "name": "Song phương", \
#    "object_id": 0, \
#    "type": "aksak", \
#    "weight": 0}
#
# reltest = {
# "areas": "string", \
#    "from_date": "", \
#    "full_name": "Tết nhá ae", \
#    "keywords": "string", \
#    "labels": "Bình đẳng", \
#    "labels_node1": "Đất nước", \
#    "labels_node2": "Đất nước", \
#    "name": "Song phương", \
#    "name_node1": "Việt Nam", \
#    "name_node2": "Thái Lan", \
#    "object_id": 0, \
#    "to_date": "", \
#    "weight": 0
# }
# print(update_relationship(reltest))

