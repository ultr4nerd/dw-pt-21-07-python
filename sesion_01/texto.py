"""Tipos de texto"""

simples = 'Mi nombre es Mauricio'
dobles = "Mi apellido es Chávez"


# Cómo usar las comillas que estoy usando para la cadena dentro de la cadena misma
cita = "Einstein dijo: \"La comida sabe mejor fría\""
cita = 'Einstein dijo: "La venganza es mala"'
simple = 'I don\'t care'
simple = "I don't care"
texto = """Einstein dijo: "La comida picante es muy buena" :)"""
texto = '''I don't care'''


# ¿Comillas triples?
# Para hacer cadenas de texto largas y para documentar
cadena_larga = """

Este es mi testamento

* Que mis cosas se incineren
"""

## Operaciones

# Concatenación
cadena = "Hola " + "mundo"
cadena = 'Hola' + " mundo"

# Multiplicación de cadenas
cadena = "hola" * 4

## Formato de cadenas

# Formato antiguo
cadena = "Hola %s" % "mundo"
cadena = "Hola %s cruel %d" % ("mundo", 7)

# format
palabra = "mundo"
cadena = "Hola {} {} :)".format(palabra, 7)

# f-string (3.6+)
numero = 7
cadena = f"Hola {palabra} {numero}"

# Concatenar números
cadena = "Mi número favorito es: " + str(7)
