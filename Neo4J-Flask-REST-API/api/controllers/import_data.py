from api.controllers.country import create_country
from api.controllers.continent import create_continent
from api.controllers.event import create_event
from api.controllers.relationship import create_relationship
from api.controllers.person import create_person
from api.controllers.personel_group import create_personel_group
from api.controllers.internaltional_group import create_internaltional_group
from api.controllers.party import create_party
import pandas as pd
import re

def import_data_csv(path, type_object):
    data = pd.read_csv(path, na_filter=False)
    # for test in list(data.columns.values):
    #     data[test] = data[test].apply(lambda x: re.sub(r"""["']""",'',x))
    convert = data.to_dict(orient='records')
    if type_object == "Country":
        for dict in convert:
            create_country(dict)
            print(dict)
    elif type_object == "Continent":
        for dict in convert:
            create_continent(dict)
            print(dict)
    elif type_object == "Internaltional_Group":
        for dict in convert:
            create_internaltional_group(dict)
            print(dict)
    elif type_object == "Party":
        for dict in convert:
            create_party(dict)
            print(dict)
    elif type_object == "Person":
        for dict in convert:
            create_person(dict)
            print(dict)
    elif type_object == "Personel_Group":
        for dict in convert:
            create_personel_group(dict)
            print(dict)
    elif type_object == "Relationship":
        for dict in convert:
            create_relationship(dict)
            print(dict)
    elif type_object == "Event":
        for dict in convert:
            create_event(dict)
            print(dict)
    else:
        return ("Object type is not defined"), 201
    return (f"""{len(convert)} {type_object} have been created"""), 200
