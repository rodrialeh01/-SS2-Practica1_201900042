import os
import time


def menu_principal():
    opcion = 0
    print('\033[96m-----------------------------------------------\033[0m')
    print('\033[96m| Nombre: Rodrigo Alejandro Hernández de León |\033[0m')
    print('\033[96m| Carné: 201900042                            |\033[0m')
    print('\033[96m| Curso: Seminario de Sistemas 2              |\033[0m')
    print('\033[96m| Sección: A                                  |\033[0m')
    print('\033[96m|                  PRACTICA 1                 |\033[0m')
    print('\033[96m-----------------------------------------------\033[0m')
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
            os.system('cls')
            borrar_modelo()
        elif opcion == 2:
            os.system('cls')
            crear_modelo()
        elif opcion == 3:
            os.system('cls')
            extraer_informacion()
        elif opcion == 4:
            os.system('cls')
            cargar_informacion()
        elif opcion == 5:
            os.system('cls')
            realizar_consultas()
        elif opcion == 6:
            print('\033[95m Saliendo... \033[0m')
            time.sleep(2)
        else:
            os.system('cls')
            print('\033[91m --------Opción no válida-------- \033[0m')

def borrar_modelo():
    rutax = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\use.sql'
    ruta = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\borrarModelo.sql'
    os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {rutax}')
    os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta}')
    print('\033[93m--------------------------------------------------------------\033[0m')
    print('\033[93m------------------------Modelo borrado------------------------\033[0m')
    print('\033[93m--------------------------------------------------------------\033[0m')
    print('Esperando 2 segundos para regresar al menu principal...')
    time.sleep(2)
    os.system('cls')

def crear_modelo():
    rutax = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\use.sql'
    ruta = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\crearModelo.sql'
    os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {rutax}')
    os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta}')
    print('\033[93m--------------------------------------------------------------\033[0m')
    print('\033[93m------------------------Modelo cargado------------------------\033[0m')
    print('\033[93m--------------------------------------------------------------\033[0m')
    print('Esperando 2 segundos para regresar al menu principal...')
    time.sleep(2)
    os.system('cls')

def extraer_informacion():
    rutax = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\use.sql'
    ruta = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\extraerInformacion.sql'
    os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {rutax}')
    os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta}')
    print('\033[93m--------------------------------------------------------------\033[0m')
    print('\033[93m-------------Información extraida correctamente---------------\033[0m')
    print('\033[93m--------------------------------------------------------------\033[0m')
    print('Esperando 2 segundos para regresar al menu principal...')
    time.sleep(2)
    os.system('cls')

def cargar_informacion():
    rutax = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\use.sql'
    ruta = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\cargarInformacion.sql'
    os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {rutax}')
    os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta}')
    print('\033[93m--------------------------------------------------------------\033[0m')
    print('\033[93m--------------Información cargada correctamente---------------\033[0m')
    print('\033[93m--------------------------------------------------------------\033[0m')
    print('Esperando 2 segundos para regresar al menu principal...')
    time.sleep(2)
    os.system('cls')

def realizar_consultas():
    opcion = 0
    while True:
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
        rutax = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\use.sql'
        os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {rutax}')
        match opcion:
            case 1:
                print('\033[92m La cantidad de datos en cada tabla es: \033[0m')
                ruta_c1 = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\consultas\consulta1.sql'
                nombre_archivo = './src/salidas/consulta1.txt'
                os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta_c1} > {nombre_archivo}')
                print("La salida se ha guardado en el archivo:", nombre_archivo)
            case 2:
                print('\033[92m La cantidad de tsunamis por año es: \033[0m')
                ruta_c2 = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\consultas\consulta2.sql'
                nombre_archivo = './src/salidas/consulta2.txt'
                os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta_c2} -f 65001 > {nombre_archivo}')
            case 3:
                print('\033[92m Los tsunamis por país son: \033[0m')
                ruta_c3 = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\consultas\consulta3.sql'
                nombre_archivo = './src/salidas/consulta3.txt'
                os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta_c3} -f 65001 > {nombre_archivo}')
            case 4:
                print('\033[92m El promedio de Total Damage por país es: \033[0m')
                ruta_c4 = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\consultas\consulta4.sql'
                nombre_archivo = './src/salidas/consulta4.txt'
                os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta_c4} -f 65001 > {nombre_archivo}')
            case 5:
                print('\033[92m Los 5 países con más muertes son: \033[0m')
                ruta_c5 = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\consultas\consulta5.sql'
                nombre_archivo = './src/salidas/consulta5.txt'
                os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta_c5} -f 65001 > {nombre_archivo}')
            case 6:
                print('\033[92m Los 5 años con más muertes son: \033[0m')
                ruta_c6 = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\consultas\consulta6.sql'
                nombre_archivo = './src/salidas/consulta6.txt'
                os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta_c6} -f 65001 > {nombre_archivo}')
            case 7:
                print('\033[92m Los 5 años con más tsunamis son: \033[0m')
                ruta_c7 = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\consultas\consulta7.sql'
                nombre_archivo = './src/salidas/consulta7.txt'
                os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta_c7} -f 65001 > {nombre_archivo}')
            case 8:
                print('\033[92m Los 5 países con mayor número de casas destruidas son: \033[0m')
                ruta_c8 = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\consultas\consulta8.sql'
                nombre_archivo = './src/salidas/consulta8.txt'
                os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta_c8} -f 65001 > {nombre_archivo}')
            case 9:
                print('\033[92m Los 5 países con mayor número de casas dañadas son: \033[0m')
                ruta_c9 = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\consultas\consulta9.sql'
                nombre_archivo = './src/salidas/consulta9.txt'
                os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta_c9} -f 65001 > {nombre_archivo}')
            case 10:
                print('\033[92m El promedio de altura máxima del agua por país es: \033[0m')
                ruta_c10 = r'C:\Users\rodri\Documents\REPOSITORIOS\-SS2-Practica1_201900042\src\scripts\consultas\consulta10.sql'
                nombre_archivo = './src/salidas/consulta10.txt'
                os.system(f'sqlcmd -S localhost\SQLEXPRESS -E -d practica1ss2 -i {ruta_c10} -f 65001 > {nombre_archivo}')
            case 11:
                os.system('cls')
                break
            case _:
                os.system('cls')
                print('\033[91m --------Opción no válida-------- \033[0m')

menu_principal()