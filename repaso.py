import os
import time

os.system("cls")


lista_trabajadores=[]


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
        print("registrar")
        nombre_apellido=input("Ingrese nombre y apeññido\n > ")
        cargo=int(input("Ingrese cargo\n 1. CEO\n 2. Desarrollador\n 3. Analista\n > "))
        bruto=int(input("Ingrese sueldo bruto\n > "))
        
        salud=bruto*0.07
        afp=bruto*0.12
        total=afp+salud
        liquido=bruto-total


        trabajador=[nombre_apellido,cargo,bruto,salud,afp,liquido]
        lista_trabajadores.append(trabajador)

        print("Trabajador registrado con éxito")
        pass
    elif opc==2:
        if len(lista_trabajadores)==0:
            print("No hay trabajadores agregados, elija opcion n°1")
        else:
            print("Lista Trabajadores")
            print("Trabajador\tCargo\tSueldo Bruto\tDesc. Salud\tDesc. AFP\tSueldo Líquido")
            for t in lista_trabajadores: #t: seria cada trabajador de la lista, T es una lista
                print(f"{t[0]}\t{t[1]}\t{t[2]}\t{t[3]}\t{t[4]}\t{t[5]}")

    elif opc==3:
        pass
    elif opc==4:
        break
