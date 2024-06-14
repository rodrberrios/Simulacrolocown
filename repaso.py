import os
import time

from funciones import *

os.system("cls")





while True:
    print("Menu Trabajadores")
    print("")
    print("""
           1. Registrar trabajador
           2. Listar Trabajadores
           3. Imprimir plantilla de sueldos
           4. salir
          """)
    opc=int(input("Ingrese Opcion\n> "))

    if opc==1:
        opcion_1() 

    elif opc==2:
        opcion_2()


    elif opc==3:
        opcion_3()

    else:
        opcion_4()
