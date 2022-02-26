import json

datos = {
    "nombre": "Mauricio",
    "apellido": "Chávez",
    "puntuación": 100,
    "lenguajes": ["Python", "Elixir", "JavaScript"],
    "activo": True,
    "extras": {
        "comida_favorita": "Tacos",
        "cumpleaños": "21 de Diciembre"
    }
}

my_json = json.dumps(datos)
print(my_json)

other_json = '{"nombre": "Juan", "apellido": "Álvarez", "activo": false}'
my_dict = json.loads(other_json)
print(my_dict)
print(my_dict['nombre'])
