from connect import neo4j_connect
import datetime

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