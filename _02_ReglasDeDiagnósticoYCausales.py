# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Definición de reglas de diagnóstico y causales
reglas_diagnosticas = {
    "Regla 1": ["Síntoma A", "Síntoma B", "Síntoma C"],
    "Regla 2": ["Síntoma D", "Síntoma E"],
    "Regla 3": ["Síntoma F", "Síntoma G", "Síntoma H"]
}

reglas_causales = {
    "Síntoma A": ["Causa X"],
    "Síntoma B": ["Causa Y"],
    "Síntoma C": ["Causa Z"],
    "Síntoma D": ["Causa X"],
    "Síntoma E": ["Causa Z"],
    "Síntoma F": ["Causa Y"],
    "Síntoma G": ["Causa X"],
    "Síntoma H": ["Causa Z"]
}

# Función para diagnosticar
def diagnosticar(sintomas):
    causas = set()
    for sintoma in sintomas:
        if sintoma in reglas_diagnosticas:
            causas.update(reglas_diagnosticas[sintoma])
    return causas

# Función para encontrar causas
def encontrar_causas(sintoma):
    if sintoma in reglas_causales:
        return reglas_causales[sintoma]
    else:
        return [sintoma]

# Ejemplo de diagnóstico
sintomas_observados = ["Síntoma A", "Síntoma B"]
causas = diagnosticar(sintomas_observados)
print("Posibles causas basadas en los síntomas observados:", causas)

# Ejemplo de búsqueda de causas
sintoma = "Síntoma A"
causas = encontrar_causas(sintoma)
print(f"Causas de {sintoma}:", causas)
