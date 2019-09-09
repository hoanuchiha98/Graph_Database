from py2neo import Graph

from api.models.nodes import export_json_run_cypher, export_json_node
from connect import neo4j_connect
import datetime, json

def create_node(node):
    node_find = f"""Match (n:{node.get("labels")}) where n.name='{node.get("name")}'"""
    graph = neo4j_connect()
    if (graph.run(f"{node_find} return r").data() not in ([], None)):
        return ("Nodes already exists")
    else:
        create_query = ""
        for x in node:
            if x!= "labels":
                if isinstance(node.get(x), (int, float)) == True:
                    create_query += f"{x}:{node.get(x)},"
                else:
                    if valid_date(node.get(x)) == True:
                        create_query += f"""{x}:date("{node.get(x)}"),"""
                    else:
                        create_query += f"{x}:'{node.get(x)}',"

        create_query = create_query.rstrip(",")
        print(create_query)
        pattern = f"""CREATE (n:{node.get("labels")}{{{create_query}}}) return n"""
        print(pattern)
        graph.run(pattern)
        return export_json_node(f"""Match (n:{node.get("labels")}) where n.name='{node.get("name")}'""")

def delete_node(node1):
    graph = neo4j_connect()
    node_temp = graph.nodes.match(f"""{node1.get("labels")}""").where("_.name = '{name}'".format(name=node1.get("name"))).first()
    graph.delete(node_temp)
    graph.exists(node_temp)
    return ("Success")

# def merge_node(node):
#     merge_query = ""
#     for x in test:
#         if x!= "labels":
#             if isinstance(node.get(x), (int, float)) == True:
#                 merge_query += f"{x}:{node.get(x)},"
#             else:
#                 if valid_date(node.get(x)) == True:
#                     merge_query += f"""{x}:date("{node.get(x)}"),"""
#                 else:
#                     merge_query += f"{x}:'{node.get(x)}',"
#         # create_query += f"{x}:{node.get(x)}"
#     merge_query = merge_query.rstrip(",")
#     print(merge_query)
#     pattern = f"""MERGE (n:{node.get("labels")}{{{merge_query}}}) return n"""
#     print(pattern)
#     graph = neo4j_connect()
#     graph.run(pattern)
#     return json.dumps(graph.nodes.match(f"""{node.get("labels")}""").where("_.name = '{name}'".format(name=node.get("name"))).first())
def update_node(node):
    node_find = f"""Match (n:{node.get("labels")}) where n.name='{node.get("name")}'"""
    graph = neo4j_connect()
    if (graph.run(f"{node_find} return n").data() in ([], None)):
        return ("Nodes is not found")
    else:
        create_query = ""
        for x in node:
            if x != "labels" and x!="name":
                if node.get(x)=="":
                    create_query += f"{x}:null,"
                elif isinstance(node.get(x), (int, float)) == True:
                    create_query += f"{x}:{node.get(x)},"
                else:
                    if valid_date(node.get(x)) == True:
                        create_query += f"""{x}:date("{node.get(x)}"),"""
                    else:
                        create_query += f"{x}:'{node.get(x)}',"

        create_query = create_query.rstrip(",")
        print(create_query)
        pattern = f"""MATCH (n:{node.get("labels")}) set n+={{{create_query}}} return n"""
        print(pattern)
        graph.run(pattern)
        return export_json_node(f"""Match (n:{node.get("labels")}) where n.name='{node.get("name")}'""")

def valid_date(datestring):
    try:
        datetime.datetime.strptime(datestring, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def find_all_labels_node():
    return neo4j_connect().run("call db.labels").data()
def find_all_node_field(labels):
    pattern = f"""MATCH(n: {labels.get("labels")}) WITH DISTINCT keys(n) AS keys UNWIND keys AS keyslisting WITH DISTINCT keyslisting AS fields RETURN fields"""
    print(pattern)
    return neo4j_connect().run(pattern).data()
def find_all_progesties_nodes_with_field(node):
    pattern = f"""MATCH (n:{node.get("labels")}) return n.{node.get("field_name")} as {node.get("field_name")}"""
    print(pattern)
    return neo4j_connect().run(pattern).data()
if __name__ == "__main__":
    test = {
        "name": "Nicolás Maduro",
        "labels": "Person",
        "full_name": "Nicolás Maduro Moros",
        "image": "no",
        "object_id": 4,
        "weight": "",
        "keywords": "NMM",
        "type": "leader"
    }