# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Datos de ejemplo: Diccionario de películas y géneros
peliculas = {
    'Pelicula1': ['Aventura', 'Acción'],
    'Pelicula2': ['Comedia'],
    'Pelicula3': ['Aventura', 'Fantasía'],
    'Pelicula4': ['Comedia', 'Romance'],
    'Pelicula5': ['Acción']
}

# Base de conocimiento: Usuarios y sus preferencias
usuarios = {
    'Usuario1': {'Pelicula1', 'Pelicula3'},
    'Usuario2': {'Pelicula2', 'Pelicula4'},
    'Usuario3': {'Pelicula3', 'Pelicula5'}
}

# Recomendación de películas basada en intereses del usuario
def recomendar_peliculas(usuario):
    recomendaciones = set()
    for pelicula, generos in peliculas.items():
        if not peliculas_vistas(usuario, pelicula):
            for genero in generos:
                if tiene_interes(usuario, genero):
                    recomendaciones.add(pelicula)
                    break
    return recomendaciones

# Función para verificar si un usuario ha visto una película
def peliculas_vistas(usuario, pelicula):
    return pelicula in usuarios.get(usuario, set())

# Función para verificar si un usuario tiene interés en un género
def tiene_interes(usuario, genero):
    for pelicula in usuarios.get(usuario, set()):
        if genero in peliculas[pelicula]:
            return True
    return False

# Ejemplo de recomendación para Usuario1
usuario = 'Usuario1'
recomendaciones = recomendar_peliculas(usuario)
print(f"Recomendaciones para {usuario}: {recomendaciones}")
