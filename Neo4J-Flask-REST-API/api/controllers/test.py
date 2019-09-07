import re
import pandas as pd

strs = """how much for th"e maple syrup? $20.99? That's r"icidulous!!!"""
print (strs)
nstr = re.sub(r'[?|$|.|!]',r'',strs)
print (nstr)
nestr = re.sub(r"""["']""",r'',nstr)
print (nestr)

data = pd.read_csv("/Users/albert/Desktop/VietAI/Neo4J-Flask-API/test_data/personel_group.csv", na_filter=False)

for test in list(data.columns.values):
    data[test] = data[test].apply(lambda x: re.sub(r"""["']""",'',x))

print(data)

