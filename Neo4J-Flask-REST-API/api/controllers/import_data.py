from api.controllers.nodes import create_node
import pandas as pd

def import_data_csv(path):
    data = pd.read_csv(path, na_filter=False)
    # for test in list(data.columns.values):
    #     data[test] = data[test].apply(lambda x: re.sub(r"""["']""",'',x))
    convert = data.to_dict(orient='records')
    for dict in convert:
        create_node(dict)
        print(dict)
    return (f"""{len(convert)} have been created"""), 200
