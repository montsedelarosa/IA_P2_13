# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Encadenamiento hacia adelante

# Base de conocimiento de reglas (Reglas de ejemplo)
base_de_conocimiento = {
    "Regla 1": {"antecedentes": ["A"], "consecuente": "B"},
    "Regla 2": {"antecedentes": ["B", "C"], "consecuente": "D"},
    "Regla 3": {"antecedentes": ["E"], "consecuente": "C"},
    "Regla 4": {"antecedentes": ["D", "F"], "consecuente": "G"}
}

# Hechos iniciales (Hechos conocidos)
hechos_conocidos = ["A", "E"]

# Función de encadenamiento hacia adelante
def encadenamiento_hacia_adelante(base_de_conocimiento, hechos_conocidos):
    nuevos_hechos = set(hechos_conocidos)
    while True:
        cambios = False
        for regla, datos in base_de_conocimiento.items():
            antecedentes = datos["antecedentes"]
            consecuente = datos["consecuente"]
            if all(antecedente in nuevos_hechos for antecedente in antecedentes) and consecuente not in nuevos_hechos:
                nuevos_hechos.add(consecuente)
                cambios = True
                print(f"Aplicando {regla}: {' ,'.join(antecedentes)} => {consecuente}")
        if not cambios:
            break
    return nuevos_hechos

# Ejecutar encadenamiento hacia adelante
nuevos_hechos = encadenamiento_hacia_adelante(base_de_conocimiento, hechos_conocidos)
print("Nuevos hechos encontrados:", nuevos_hechos)

# Encadenamiento hacia atrás

# Base de conocimiento de reglas (Reglas de ejemplo)
base_de_conocimiento = {
    "Regla 1": {"consecuente": "A", "antecedentes": []},
    "Regla 2": {"consecuente": "B", "antecedentes": ["A"]},
    "Regla 3": {"consecuente": "C", "antecedentes": ["B"]},
    "Regla 4": {"consecuente": "D", "antecedentes": ["C"]}
}

# Función de encadenamiento hacia atrás
def encadenamiento_hacia_atras(base_de_conocimiento, objetivo, hechos_conocidos):
    if objetivo in hechos_conocidos:
        return True
    for regla, datos in base_de_conocimiento.items():
        consecuente = datos["consecuente"]
        antecedentes = datos["antecedentes"]
        if consecuente == objetivo:
            print(f"Objetivo alcanzado: {objetivo}")
            for antecedente in antecedentes:
                if not encadenamiento_hacia_atras(base_de_conocimiento, antecedente, hechos_conocidos):
                    return False
            return True
    return False

# Hechos iniciales (Hechos conocidos)
hechos_conocidos = ["D"]

# Objetivo a demostrar
objetivo = "A"

# Ejecutar encadenamiento hacia atrás
resultado = encadenamiento_hacia_atras(base_de_conocimiento, objetivo, hechos_conocidos)

if resultado:
    print(f"Objetivo '{objetivo}' alcanzado.")
else:
    print(f"No se pudo alcanzar el objetivo '{objetivo}'.")
