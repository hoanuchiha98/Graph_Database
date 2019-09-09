from connect import neo4j_connect
import datetime, json
from api.models.nodes import export_json_relationship

def create_relationship(rels):
    graph = neo4j_connect()
    create_query = ""
    relationship_properties = rels.get("Relationship")
    list_node = []
    for y in rels:
        if y!= "Relationship":
            list_node.append(y)
    relation_find = f"""MATCH (a:{list_node[0]})-[r:`{relationship_properties.get("type")}`]->(b:{list_node[1]}) WHERE a.name = '{rels.get(list_node[0]).get("name")}' AND b.name = '{rels.get(list_node[1]).get("name")}'"""
    if (graph.run(f"{relation_find} return r").data() not in ([], None)):
        return ("relationship already exists")
    else:
        for x in relationship_properties:
            if x != "type":
                if isinstance(relationship_properties.get(x), (int, float)) == True:
                    create_query += f"{x}:{relationship_properties.get(x)},"
                else:
                    if valid_date(relationship_properties.get(x)) == True:
                        create_query += f"""{x}:date("{relationship_properties.get(x)}"),"""
                    else:
                        create_query += f"{x}:'{relationship_properties.get(x)}',"

        create_query = create_query.rstrip(",")
        # list_node =[]
        # for y in rels:
        #     if y!= "Relationship":
        #         list_node.append(y)
        pattern = f"""MATCH (a:{list_node[0]}),(b:{list_node[1]}) WHERE a.name = '{rels.get(list_node[0]).get("name")}' AND b.name = '{rels.get(list_node[1]).get("name")}' CREATE (a)-[r:`{relationship_properties.get("type")}` {{{create_query}}}]->(b) return a, b, r"""
        print(create_query)
        print(pattern)
        print(graph.run(pattern))
        if relationship_properties.get("name")in ('', None):
            pattern_find = f"""MATCH (a:{list_node[0]})-[r:`{relationship_properties.get("type")}`]->(b:{list_node[1]}) WHERE a.name = '{rels.get(list_node[0]).get("name")}' AND b.name = '{rels.get(list_node[1]).get("name")}'"""
        else:
            pattern_find = f"""MATCH (a:{list_node[0]})-[r:`{relationship_properties.get("type")}`]->(b:{list_node[1]}) WHERE a.name = '{rels.get(list_node[0]).get("name")}' AND b.name = '{rels.get(list_node[1]).get("name")}' AND r.name = '{relationship_properties.get("name")}'"""
        print(pattern_find)
        return export_json_relationship(pattern_find)

def valid_date(datestring):
    try:
        datetime.datetime.strptime(datestring, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def find_all_relationship_type():
    return neo4j_connect().run("call db.relationshipTypes").data()

def delete_relationship(rels):
    graph = neo4j_connect()
    if graph.run(f"""MATCH (a)-[r:`{rels.get("type")}`]-(b) where r.name='{rels.get("name")}' return r""").data()==[]:
        return ("No Relationship")
    else:
        rels_temp = f"""MATCH (a)-[r:`{rels.get("type")}`]-(b) where r.name='{rels.get("name")}' detach delete r"""
        rels_find =f"""MATCH (a)-[r:`{rels.get("type")}`]-(b) where r.name='{rels.get("name")}' return r"""
        graph.run(rels_temp)
        print(rels_temp)
        result = graph.run(rels_find).data()
        print(result)
        if result != []:
            return ("Delete Fail")
        else:
            return ("Delete Success")
        return ("Success")

def update_relationship(rels):
    graph = neo4j_connect()
    create_query = ""
    relationship_properties = rels.get("Relationship")
    list_node = []
    for y in rels:
        if y!= "Relationship":
            list_node.append(y)
    if relationship_properties.get("name") in ('', None):
        relation_find = f"""MATCH (a:{list_node[0]})-[r:`{relationship_properties.get("type")}`]->(b:{list_node[1]}) WHERE a.name = '{rels.get(list_node[0]).get("name")}' AND b.name = '{rels.get(list_node[1]).get("name")}'"""
    else:
        relation_find = f"""MATCH (a:{list_node[0]})-[r:`{relationship_properties.get("type")}`]->(b:{list_node[1]}) WHERE a.name = '{rels.get(list_node[0]).get("name")}' AND b.name = '{rels.get(list_node[1]).get("name")}' AND r.name = '{relationship_properties.get("name")}'"""
    print(relation_find)
    if (graph.run(f"{relation_find} return r").data() in ([], None)):
        return ("relationship already exists")
    else:
        for x in relationship_properties:
            if x != "type":
                if isinstance(relationship_properties.get(x), (int, float)) == True:
                    create_query += f"{x}:{relationship_properties.get(x)},"
                else:
                    if valid_date(relationship_properties.get(x)) == True:
                        create_query += f"""{x}:date("{relationship_properties.get(x)}"),"""
                    else:
                        create_query += f"{x}:'{relationship_properties.get(x)}',"

        create_query = create_query.rstrip(",")
        # list_node =[]
        # for y in rels:
        #     if y!= "Relationship":
        #         list_node.append(y)
        if relationship_properties.get("name")in ('', None):
            pattern = f"""MATCH (a:{list_node[0]})-[r:`{relationship_properties.get("type")}`]-(b:{list_node[1]}) WHERE a.name = '{rels.get(list_node[0]).get("name")}' AND b.name = '{rels.get(list_node[1]).get("name")}' set r+={{{create_query}}} return a, b, r"""
        else:
            pattern = f"""MATCH (a:{list_node[0]})-[r:`{relationship_properties.get("type")}`]-(b:{list_node[1]}) WHERE a.name = '{rels.get(list_node[0]).get("name")}' AND b.name = '{rels.get(list_node[1]).get("name")}' AND r.name = '{relationship_properties.get("name")}' set r+={{{create_query}}} return a, b, r"""
        print(create_query)
        print(pattern)
        print(graph.run(pattern))
        if relationship_properties.get("name")in ('', None):
            pattern_find = f"""MATCH (a:{list_node[0]})-[r:`{relationship_properties.get("type")}`]->(b:{list_node[1]}) WHERE a.name = '{rels.get(list_node[0]).get("name")}' AND b.name = '{rels.get(list_node[1]).get("name")}'"""
        else:
            pattern_find = f"""MATCH (a:{list_node[0]})-[r:`{relationship_properties.get("type")}`]->(b:{list_node[1]}) WHERE a.name = '{rels.get(list_node[0]).get("name")}' AND b.name = '{rels.get(list_node[1]).get("name")}' AND r.name = '{relationship_properties.get("name")}'"""
        print(pattern_find)
        return export_json_relationship(pattern_find)

def find_all_relationships_field(type):
    pattern = f"""MATCH(n)-[r:{{{type.get("type")}}}]-(p) WITH DISTINCT keys(r) AS keys UNWIND keys AS keyslisting WITH DISTINCT keyslisting AS fields RETURN fields"""
    return neo4j_connect().run(pattern).data()

def find_all_progesties_relationships_with_field(rels):
    pattern = f"""MATCH (n)-[r:`{{{rels.get("field_name")}}}`]-(p) return n.{rels.get("field_name")} as {rels.get("field_name")}"""
    return neo4j_connect().run(pattern).data()

if __name__ == "__main__":
    test = {
        "Movies":{
            "name":"Harry"
        },
        "FILM":{
            "name":"James Ron"
        },
        "Relationship":{
            "name":"Film by Harry",
            "type":"ACTION IN",
            "date":"2019-10-25"
        }

    }
    test1 = {
        "name":"Film by Harry",
            "type":"ACTION IN"
    }

    print(test1.get("hhhh"))