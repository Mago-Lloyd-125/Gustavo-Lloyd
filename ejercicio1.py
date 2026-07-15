#clave examen: 863428

peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español',
False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles',
False],
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}

def cupos_genero(genero):
    print("Ingrese género a consultar: ")
    if cupos_genero(genero):
        genero=input()
        genero==(peliculas,list)
        print(f"El total de cupos disponibles es: ")
    return

p_min= 0
p_max= 0
def busqueda_precio(cartelera):
    print("Ingrese precio mínimo: ")
    if busqueda_precio(cartelera):
        p_min = int(input())
        p_max = int(input())
    return

def buscar_codigo(codigo):
        print("Ingrese código de película: ")
        if buscar_codigo(codigo):
            codigo= input()
        return

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d,
precio, cupos):
    while True:
        if agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d,
precio, cupos):
            input(codigo)
            print("Película agregada.")
        return

leer_opcion=(
        print("""========== MENÚ PRINCIPAL ==========
1. Cupos por género
2. Búsqueda de películas por rango de precio
3. Actualizar precio de película
4. Agregar película
5. Eliminar película
6. Salir
=====================================""")
)

while True:
    leer_opcion = int(input())
    if leer_opcion ==1:
        print(cupos_genero)
    elif leer_opcion == 2:
        print(busqueda_precio)
    elif leer_opcion == 3:
        print(buscar_codigo)
    elif leer_opcion == 4:
        print(agregar_pelicula)
    elif leer_opcion == 5:
        pass
    else:
        print("Programa finalizado.")
        break
