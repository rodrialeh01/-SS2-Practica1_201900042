def menu_principal():
    opcion = 0
    print('-----------------------------------------------')
    print('| Nombre: Rodrigo Alejandro Hernández de León |')
    print('| Carné: 201900042                            |')
    print('| Curso: Seminario de Sistemas 2              |')
    print('| Sección: A                                  |')
    print('|                  PRACTICA 1                 |')
    print('-----------------------------------------------')
    while opcion != 6:
        print('                Menu principal')
        print('1. Borrar Modelo')
        print('2. Crear Modelo')
        print('3. Extraer Información')
        print('4. Cargar Información')
        print('5. Realizar Consultas')
        print('6. Salir')
        opcion = int(input('Ingrese la opción: '))
        if opcion == 1:
            print('Borrar Modelo')
            borrar_modelo()
        elif opcion == 2:
            print('Crear Modelo')
            crear_modelo()
        elif opcion == 3:
            print('Extraer Información')
            extraer_informacion()
        elif opcion == 4:
            print('Cargar Información')
            cargar_informacion()
        elif opcion == 5:
            print('Realizar Consultas')
            realizar_consultas()
        elif opcion == 6:
            print('Salir')
        else:
            print('Opción no válida')

def borrar_modelo():
    pass

def crear_modelo():
    pass

def extraer_informacion():
    pass

def cargar_informacion():
    pass

def realizar_consultas():
    print('=========== CONSULTAS ===========')
    print('1. Cantidad de datos por cada tabla')
    print('2. Cantidad de tsunamis por año')
    print('3. Tsunamis por país')
    print('4. Promedio de Total Damage por país')
    print('5. Top 5 de países con más muertes')
    print('6. Top 5 de años con más muertes')
    print('7. Top 5 de años que más tsunamis han tenido')
    print('8. Top 5 de países con mayor número de casa destruidas')
    print('9. Top 5 de países con mayor número de casas dañadas')
    print('10. Promedio de altura máxima del agua por cada país')
    print('11. Regresar')
    opcion = int(input('Ingrese la opción: '))

    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass
        case _:
            print('Opción no válida')

menu_principal()