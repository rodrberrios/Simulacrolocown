lista_trabajadores=[]

cargos=("CEO","DESARROLLADOR","ANALISTA") #0,1,2 

def opcion_1():
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

def opcion_2():
    if len(lista_trabajadores)==0:
        print("No hay trabajadores agregados, elija opcion n°1")
    else:
        print("Lista Trabajadores")
        print("Trabajador\tCargo\tSueldo Bruto\tDesc. Salud\tDesc. AFP\tSueldo Líquido")
        for t in lista_trabajadores: #t: seria cada trabajador de la lista, T es una lista
            print(f"{t[0]}\t{t[1]}\t{t[2]}\t{t[3]}\t{t[4]}\t{t[5]}")

def opcion_3():
    if len(lista_trabajadores)==0:
        print("No hay trabajadores agregados, elija opcion n°1")
    else:
        opc2=int(input("¿Que cargo desea imprimir?\n1. CEO\n2. Desarrollador\n3. Analista\4. Todos\n > "))
        if opc2==4:
            with open("Todos_trabajadores.txt","w") as archivo:
                for t in lista_trabajadores:
                    texto=f"{t[0]}  {t[1]}  {t[2]}  {t[3]}  {t[4]} {t[5]}\n"
                    archivo.write(texto)
        else:
            with open("trabajadores_por_cargo.txt","w") as archivo:
                for t in lista_trabajadores:
                    if opc2==t[1]:
                        texto=f"{t[0]}  {t[1]}  {t[2]}  {t[3]}  {t[4]} {t[5]}\n"
                        archivo.write(texto)    


def opcion_4():
    print("Hasta luego")
    exit()