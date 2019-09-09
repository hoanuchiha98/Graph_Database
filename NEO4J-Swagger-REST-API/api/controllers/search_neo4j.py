from connect import neo4j_connect

def search_neo4j_by_json(conditions):
    list_node = []
    list_rel = []
    node_sql=""
    rels_sql=""
    if conditions.get("nodes") not in ("{}", "", None):
        list_get_node = conditions.get("nodes")
        # n SQL
        n_sql_select_conditions = ""
        list_key_node_name_1 = []
        list_key_node_name_2 = []
        for key in list_get_node.keys():
            if len(list_get_node.get(key)) > 0:
                list_key_node_name_1.append(key)
            else:
                list_key_node_name_2.append(key)
            list_node.append(key)
        for x_n in range(len(list_key_node_name_1)):
            list_2_n = list_get_node.get(list_key_node_name_1[x_n])
            list_2_1_n = []
            for t_n in list_2_n.keys():
                list_2_1_n.append(t_n)
            if x_n > 0 and len(list_2_1_n) > 0:
                n_sql_select_conditions += " or "
            for y_n in range(len(list_2_1_n)):
                list_3_n = list_2_n.get(list_2_1_n[y_n]).split(",")
                if y_n == 0:
                    n_sql_select_conditions += "("
                elif y_n != 0:
                    n_sql_select_conditions += " and "
                for z_n in range(len(list_3_n)):
                    if list_2_1_n[y_n] == "date":
                        print(list_2_1_n[y_n])
                        print(list_3_n[z_n].split(";"))
                        list_3_1_n = list_3_n[z_n].split(";")
                        if len(list_3_1_n) == 1:
                            n_sql_select_conditions += f"(date(n.date_time) = date('{list_3_1_n[0]}'))"
                        elif len(list_3_1_n) == 2:
                            n_sql_select_conditions += f"(date(n.date_time) >= date('{list_3_1_n[0]}') and date(n.date_time) <= date('{list_3_1_n[1]}'))"
                        else:
                            return ("Date Error")
                    else:
                        if len(list_3_n) == 1:
                            n_sql_select_conditions += f"""(n.{list_2_1_n[y_n]}=~'.*{list_3_n[z_n]}.*')"""
                        else:
                            if z_n == 0:
                                n_sql_select_conditions += f"""(n.{list_2_1_n[y_n]}=~'.*{list_3_n[z_n]}.*'"""
                            elif z_n == len(list_3_n) - 1:
                                n_sql_select_conditions += f""" or n.{list_2_1_n[y_n]}=~'.*{list_3_n[z_n]}.*')"""
                            else:
                                n_sql_select_conditions += f""" or n.{list_2_1_n[y_n]}=~'.*{list_3_n[z_n]}.*'"""
                if y_n == len(list_2_1_n) - 1:
                    n_sql_select_conditions += ")"

        node_n_sql = ""
        for n in range(len(list_node)):
            if len(list_node) == 1:
                node_n_sql += f"(n:{list_node[n]})"
            else:
                if n == 0:
                    node_n_sql += f"(n:{list_node[n]}"
                elif n == (len(list_node) - 1):
                    node_n_sql += f" or n:{list_node[n]})"
                else:
                    node_n_sql += f" or n:{list_node[n]}"
        # p SQL
        node_p_sql = ""
        for p in range(len(list_node)):
            if len(list_node) == 1:
                node_p_sql += f"(p:{list_node[p]})"
            else:
                if p == 0:
                    node_p_sql += f"(p:{list_node[p]}"
                elif p == (len(list_node) - 1):
                    node_p_sql += f" or p:{list_node[p]})"
                else:
                    node_p_sql += f" or p:{list_node[p]}"
        p_sql_select_conditions = ""
        for x_p in range(len(list_key_node_name_1)):
            list_2_p = list_get_node.get(list_key_node_name_1[x_p])
            list_2_1_p = []
            for t_p in list_2_p.keys():
                list_2_1_p.append(t_p)
            if x_p > 0 and len(list_2_1_p) > 0:
                p_sql_select_conditions += " or "
            for y_p in range(len(list_2_1_p)):
                list_3_p = list_2_p.get(list_2_1_p[y_p]).split(",")
                if y_p == 0:
                    p_sql_select_conditions += "("
                elif y_p != 0:
                    p_sql_select_conditions += " and "
                for z_p in range(len(list_3_p)):
                    if list_2_1_p[y_p] == "date":
                        print(list_2_1_p[y_p])
                        print(list_3_p[z_p].split(";"))
                        list_3_1_p = list_3_p[z_p].split(";")
                        if len(list_3_1_p) == 1:
                            p_sql_select_conditions += f"(date(p.date_time) = date('{list_3_1_p[0]}'))"
                        elif len(list_3_1_p) == 2:
                            p_sql_select_conditions += f"(date(p.date_time) >= date('{list_3_1_p[0]}') and date(p.date_time) <= date('{list_3_1_p[1]}'))"
                        else:
                            return ("Date Error")
                    else:
                        if len(list_3_p) == 1:
                            p_sql_select_conditions += f"""(p.{list_2_1_p[y_p]}=~'.*{list_3_p[z_p]}.*')"""
                        else:
                            if z_p == 0:
                                p_sql_select_conditions += f"""(p.{list_2_1_p[y_p]}=~'.*{list_3_p[z_p]}.*'"""
                            elif z_p == len(list_3_p) - 1:
                                p_sql_select_conditions += f""" or p.{list_2_1_p[y_p]}=~'.*{list_3_p[z_p]}.*')"""
                            else:
                                p_sql_select_conditions += f""" or p.{list_2_1_p[y_p]}=~'.*{list_3_p[z_p]}.*'"""
                if y_p == len(list_2_1_p) - 1:
                    p_sql_select_conditions += ")"
        n_or_node_not_choose = ""
        print(list_key_node_name_2)
        if len(list_key_node_name_2) > 0:
            if len(list_key_node_name_2) == 1:
                n_or_node_not_choose = f" or n:{list_key_node_name_2[0]}"
            else:
                for no in range(len(list_key_node_name_2)):
                    if no == 0:
                        n_or_node_not_choose += f" or (n:{list_key_node_name_2[no]}"
                    elif no == len(list_key_node_name_2) - 1:
                        n_or_node_not_choose += f" or n:{list_key_node_name_2[no]})"
                    else:
                        n_or_node_not_choose += f" or n:{list_key_node_name_2[no]}"
        p_or_node_not_choose = ""
        print(list_key_node_name_2)
        if len(list_key_node_name_2) > 0:
            if len(list_key_node_name_2) == 1:
                p_or_node_not_choose = f" or n:{list_key_node_name_2[0]}"
            else:
                for po in range(len(list_key_node_name_2)):
                    if po == 0:
                        p_or_node_not_choose += f" or (p:{list_key_node_name_2[po]}"
                    elif po == len(list_key_node_name_2) - 1:
                        p_or_node_not_choose += f" or p:{list_key_node_name_2[po]})"
                    else:
                        p_or_node_not_choose += f" or p:{list_key_node_name_2[po]}"
        if len(list_key_node_name_1) > 0:
            node_sql = f"""{node_n_sql} and {node_p_sql} and ({n_sql_select_conditions} {n_or_node_not_choose}) and ({p_sql_select_conditions} {p_or_node_not_choose})"""
        else:
            node_sql = f"""{node_n_sql} and {node_p_sql}"""
    # Relationship SQL
    if conditions.get("relationships") not in ("{}", "", None):
        list_get_rels = conditions.get("relationships")
        r_sql_select_conditions = ""
        list_key_rels_name_1 = []
        list_key_rels_name_2 = []
        for key in list_get_rels.keys():
            if len(list_get_rels.get(key)) > 0:
                list_key_rels_name_1.append(key)
            else:
                list_key_rels_name_2.append(key)
            list_rel.append(key)
        for x_r in range(len(list_key_rels_name_1)):
            list_2_r = list_get_rels.get(list_key_rels_name_1[x_r])
            list_2_1_r = []
            for t_r in list_2_r.keys():
                list_2_1_r.append(t_r)
            if x_r > 0 and len(list_2_1_r) > 0:
                r_sql_select_conditions += " or "
            for y_r in range(len(list_2_1_r)):
                list_3_r = list_2_r.get(list_2_1_r[y_r]).split(",")
                if y_r == 0:
                    r_sql_select_conditions += "("
                elif y_r != 0:
                    r_sql_select_conditions += " and "
                for z_r in range(len(list_3_r)):
                    if list_2_1_r[y_r] == "date":
                        print(list_2_1_r[y_r])
                        print(list_3_r[z_r].split(";"))
                        list_3_1_r = list_3_r[z_r].split(";")
                        if len(list_3_1_r) == 1:
                            r_sql_select_conditions += f"(date(r.to_date) >= date('{list_3_1_r[0]}') and date(r.from_date) <= date('{list_3_1_r[0]}'))"
                        elif len(list_3_1_r) == 2:
                            r_sql_select_conditions += f"(date(r.to_date) >= date('{list_3_1_r[0]}') and date(r.from_date) <= date('{list_3_1_r[1]}'))"
                        else:
                            return ("Date Error")
                    else:
                        if len(list_3_r) == 1:
                            r_sql_select_conditions += f"""(r.{list_2_1_r[y_r]}=~'.*{list_3_r[z_r]}.*')"""
                        else:
                            if z_r == 0:
                                r_sql_select_conditions += f"""(r.{list_2_1_r[y_r]}=~'.*{list_3_r[z_r]}.*'"""
                            elif z_r == len(list_3_r) - 1:
                                r_sql_select_conditions += f""" or r.{list_2_1_r[y_r]}=~'.*{list_3_r[z_r]}.*')"""
                            else:
                                r_sql_select_conditions += f""" or r.{list_2_1_r[y_r]}=~'.*{list_3_r[z_r]}.*'"""
                if y_r == len(list_2_1_r) - 1:
                    r_sql_select_conditions += ")"

        or_rels_not_choose = ""
        if len(list_key_rels_name_2) > 0:
            or_rels_not_choose += f" or (type(r) in {list_key_rels_name_2})"
        if len(list_key_rels_name_1) > 0:
            rels_sql = f"""(type(r) in {list_rel} and ({r_sql_select_conditions} {or_rels_not_choose}))"""
        else:
            rels_sql = f"""(type(r) in {list_rel})"""

    if conditions.get("nodes") in ("{}", "", None) and conditions.get("relationships") in ("{}", "", None):
        pattern = f"""MATCH path=(n) OPTIONAL MATCH (n)-[r]-()"""
    elif conditions.get("nodes") in ("{}", "", None):
        pattern = f"""MATCH path = (n)-[r]-(p) WHERE {rels_sql}"""
    elif conditions.get("relationships") in ("{}", "", None):
        pattern = f"""MATCH path = (n)-[r]-(p) WHERE {node_sql}"""
    else:
        pattern = f"""MATCH path = (n)-[r]-(p) WHERE {node_sql} and {rels_sql}"""

    print(pattern)
    query = f"""CALL apoc.export.json.query("{pattern} with nodes(path) as nodes, relationships(path)
                           as rels unwind nodes as nodes1 unwind rels as rels1 with nodes1, rels1 RETURN
                           collect(distinct nodes1) as nodes, collect(distinct rels1) as relationships","query.json",{{}})"""
    json_load = """WITH "query.json" AS url CALL apoc.load.json(url) YIELD value return value.nodes as node, value.relationships as relationships"""
    try:
        graph = neo4j_connect()
        print(query)
        print(graph.run(f"{pattern} return path").data())
        if (graph.run(f"{pattern} return path").data() not in ([], None)):
            graph.run(query)
            query_json = graph.run(json_load).to_data_frame()
            result = query_json.to_dict(orient='records')
            return result
        else:
            return ("Not Found")
    except:
        return ("Not Found")

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


