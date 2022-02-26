import datetime
import json

with open("data.json", "w") as my_json:
    my_dict = {"nombre": "diccionario", "year": 2019}
    json.dump(my_dict, my_json, indent=4)


with open("ejemplo2.json", "w") as fjson:
    # Las fechas necesitan convertirse
    mi_dicc = {"fecha": datetime.datetime.now().strftime("%c")}
    json.dump(mi_dicc, fjson, indent=4)  # Puede agregarse indentación

with open("data.json") as my_json:
    my_dict = json.load(my_json)
    print(my_dict)
