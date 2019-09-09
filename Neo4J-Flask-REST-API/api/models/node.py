# from py2neo import Node, Relationship, NodeMatcher
# from connect import neo4j_connect
#
# #labels, name, full_name, image, object_id, weight, keyword, type, datetime, type1
# def create_node(person):
#     labels = person.get("labels")
#     name = person.get("name")
#     if labels in ('', None) or name in ('', None):
#         return None, 201
#     full_name = person.get("full_name")
#     if full_name == '':
#         full_name = None
#     image = person.get("image")
#     if image == '':
#         image = None
#     object_id = person.get("object_id")
#     if object_id == 0:
#         object_id = None
#     weight = person.get("weight")
#     if weight == 0:
#         weight = None
#     keyword = person.get("keyword")
#     if keyword == '':
#         keyword = None
#     type1 = person.get("type")
#     date_time = person.get("date_time")
#     if date_time == '':
#         date_time = None
#
#     node = Node(labels, name = name, full_name = full_name, image = image, object_id = object_id,
#                 weight = weight, keyword = keyword,date_time = date_time)
#     print(node)
#     node.__primarylabel__ = labels
#     node.__primarykey__ = name
#     graph = neo4j_connect()
#     transaction = graph.begin()
#     node_find = find_node(labels, name)
#     # print(node_find)
#     if node_find in ('', None):
#         transaction.create(node)
#     else:
#         return ("Node đã tồn tại")
#     if type1 not in ('', None):
#         event_type = Node("event_category", name=type1)
#         event_type.__primarylabel__ = "event_category"
#         event_type.__primarykey__ = type
#         transaction.create(event_type)
#         rels_event = Relationship(node, "Belong to the type of event", event_type)
#         transaction.create(rels_event)
#         #Create rels event category
#
#     transaction.commit()
#     transaction.finished()
#     return node
#
# def update_node(node):
#     labels = node.get("labels")
#     name = node.get("name")
#     find = find_node(labels, name)
#     if find not in ('', None):
#         return ("Node không tồn tại")
#     if labels in ('', None) or name in ('', None):
#         return None, 201
#     full_name = node.get("full_name")
#     if full_name == '':
#         full_name = None
#     image = node.get("image")
#     if image == '':
#         image = None
#     object_id = node.get("object_id")
#     if object_id == 0:
#         object_id = None
#     weight = node.get("weight")
#     if weight == 0:
#         weight = None
#     keyword = node.get("keyword")
#     if keyword == '':
#         keyword = None
#     type1 = node.get("type")
#     date_time = node.get("date_time")
#     if date_time == '':
#         date_time = None
#
#     return None
#
# # def create_relationship(rels):
# #     labels_node1 = rels.get('labels_node1')
# #     if labels_node1 in ('', None):
# #         return None, 201
# #     name_node1 = rels.get('name_node1')
# #     if name_node1 in ('', None):
# #         return None, 201
# #     labels_node2 = rels.get('labels_node2')
# #     if labels_node2 in ('', None):
# #         return None, 201
# #     name_node2 = rels.get('name_node2')
# #     if name_node2 in ('', None):
# #         return None, 201
# #     labels = rels.get('labels')
# #     name = rels.get('name')
# #     if labels in ('', None) or name in ('', None):
# #         return None, 201
# #     full_name = rels.get('full_name')
# #     if full_name == '':
# #         full_name = None
# #     image = rels.get('image')
# #     if image == '':
# #         image == None
# #     object_id = rels.get('object_id')
# #     if object_id == 0:
# #         object_id == None
# #     weight = rels.get('weight')
# #     if weight == 0:
# #         weight == None
# #     keyword = rels.get('keyword')
# #     if keyword == '':
# #         keyword == None
# #     areas = rels.get('areas')
# #     if areas == '':
# #         areas == None
# #     from_date = rels.get('from_date')
# #     if from_date == '':
# #         from_date == None
# #     to_date  = rels.get('to_date')
# #     if to_date == '':
# #         to_date == None
# #     node1= find_node(labels_node1, name_node1)
# #     print(node1)
# #     node2=find_node(labels_node2, name_node2)
# #     print(node2)
# #     if node1 in ('', None) or node2 in ('', None):
# #         return None, 201
# #     relationship = Relationship(node1, labels, node2, name = name, full_name = full_name,
# #                                 image = image, object_id = object_id, weight = weight, keyword = keyword,
# #                                 areas = areas, from_date = from_date, to_date = to_date)
# #     relationship.__primarylabel__ = labels
# #     relationship.__primarykey__ = name
# #     graph = neo4j_connect()
# #     transaction = graph.begin()
# #     transaction.create(relationship)
# #     transaction.commit()
# #     transaction.finished()
# #     return relationship, 200
# #
# # def find_node(labels, name):
# #     if labels in (None, '') or name in (None, ''):
# #         return None
# #     graph = neo4j_connect()
# #     matcher = NodeMatcher(graph)
# #     node = matcher.match(labels, name = name).first()
# #     return node
#
# # def search_one_node_root(label, name, rels_name, from_date, to_date):
# #     cypher = ""
# #     dict = {'labels.name':label, '{}.name':}
#
#
# # def search_node(label = '', name='', full_name='', type='', key_word='', date_time=''):
# #     query = """MATCH path = (n) where n.name =~ '.*{name}.*' and n.full_name =~ '.*{full_name}.*'""".format(name = name, full_name = full_name, type = type, key_word = key_word)
# #     print(query)
# #     try:
# #         result = export_json_run_cypher(query)
# #         return result
# #     except:
# #         return ("Not Found")
#
# # def export_json_run_cypher(sql):
# #     #sql = '''MATCH path = (n:country)-[r:`Đồng minh`]->(p:country) return n ,r, p'''
# #     query = """CALL apoc.export.json.query("%s with nodes(path) as nodes, relationships(path)
# #                        as rels unwind nodes as nodes1 unwind rels as rels1 with nodes1, rels1 RETURN
# #                        collect(distinct nodes1) as nodes, collect(distinct rels1) as relationships","query.json",{})""" % (sql)
# #     json_load = """WITH "query.json" AS url CALL apoc.load.json(url) YIELD value return value.nodes as node, value.relationships as relationships"""
# #     try:
# #         test1 = graph.run(sql).to_data_frame()
# #         #test1 = graph.run(json_load).to_data_frame()
# #         #result = test1.to_json(orient='records', force_ascii=False, lines=True)
# #         result = test1.to_dict(orient='records')
# #         return result
# #     except:
# #         return ("Not Found")
#
#
# # node = {}
# # labels = node.get('labels', 'label3')
# # name = node.get('name', 'name3')
# # full_name = node.get('full_name', 'namén')
# # image = node.get('image', 'ảnhe')
# # object_id = node.get('object_id', 22)
# # weight = node.get('weight', 26)
# # keyword = node.get('keyword', 'sjjsnj')
# # type = node.get('type', "Meeting")
# # date_time = node.get('date_time', '22-08-2019')
# # test ={"date_time": "2019-08-25", \
# #    "full_name": "string", \
# #    "image": "string", \
# #    "keyword": "string", \
# #    "labels": "string", \
# #    "name": "string", \
# #    "object_id": 0, \
# #    "type": "string", \
# #    "weight": 0}
# # print(test.get("date_time", None))
#
# # print(find_node("label1", "name1"))
#
# # rels = {"areas": "string", \
# #    "from_date": "", \
# #    "full_name": "string", \
# #    "keyword": "string", \
# #    "labels": "string", \
# #    "labels_node1": "Đất nước", \
# #    "labels_node2": "string", \
# #    "name": "string", \
# #    "name_node1": "string", \
# #    "name_node2": "string", \
# #    "object_id": 0, \
# #    "to_date": "", \
# #    "weight": 0 }
# # print(create_relationship(rels))
