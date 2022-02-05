"""Tipos numéricos"""

edad = 23  # Entero (int)
cociente = 2.4  # Flotante (float)
numero = complex(7, 1)  # Complejos (complex)

# Podemos separar enteros con guiones bajos
dinero = 1_000_000

# Cómo declarar números "enteros" como flotantes
mi_numero = 7.0
mi_numero = 7.
mi_numero = float(7)

### Operaciones

# Para suma, resta, multiplicación, módulo (%), exponenciación (**)

resultado = 7 + 8  # resultado entero
resultado = 7 + 8.0  # resultado flotante

# División
resultado = 8 / 4  # resultado flotante SIEMPRE
resultado = 8 // 4  # resultado entero SIEMPRE

# División - módulo
cociente, residuo = divmod(7, 2)
cociente = 7 // 2
residuo = 7 % 2

# Convertir de float a int
entero = int(7.125)

# Convertir de int a float
flotante = float(7)
