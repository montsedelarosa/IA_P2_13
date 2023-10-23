# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Implementación de la unificación
def unificar(expresion1, expresion2, sustitucion={}):
    if sustitucion is None:
        return None
    elif expresion1 == expresion2:
        return sustitucion
    elif isinstance(expresion1, str):
        return unificar_variable(expresion1, expresion2, sustitucion)
    elif isinstance(expresion2, str):
        return unificar_variable(expresion2, expresion1, sustitucion)
    elif isinstance(expresion1, list) and isinstance(expresion2, list):
        if len(expresion1) != len(expresion2):
            return None
        for e1, e2 in zip(expresion1, expresion2):
            sustitucion = unificar(e1, e2, sustitucion)
        return sustitucion
    else:
        return None

# Unificación de variables
def unificar_variable(variable, expresion, sustitucion):
    if variable in sustitucion:
        return unificar(sustitucion[variable], expresion, sustitucion)
    elif expresion in sustitucion:
        return unificar(variable, sustitucion[expresion], sustitucion)
    else:
        sustitucion[variable] = expresion
        return sustitucion

# Ejemplo de unificación
expresion1 = ['f', 'X', 'a']
expresion2 = ['f', 'b', 'Y']
resultado = unificar(expresion1, expresion2)

if resultado is None:
    print("No se puede unificar las expresiones.")
else:
    print("Sustitución unificada:", resultado)
