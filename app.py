import os
from unittest.main import MAIN_EXAMPLES

AGREGAR = 1
INSERTAR = 2
MOSTRAR = 3
BUSCAR = 4
ELIMINAR = 5
ORDENAR = 6
LIMPIAR = 7
SALIR = 0

COMPRAS = [2, 3, 4]
print(COMPRAS)

def imprimir_menu():
    os.system("cls")

    print(f"""           Compras 
    {AGREGAR})Agregar 
    {INSERTAR})Insertar
    {MOSTRAR})Mostrar
    {BUSCAR})Buscar
    {ELIMINAR})Eliminar
    {ORDENAR})Ordener
    {LIMPIAR})Limpiar
    {SALIR}) Salir""")
    


def agregar_registros():
    print("           Agregar Reg")
    Nombre = input("Ingrese Nombre: ")
    COMPRAS.append(Nombre)
    print("Reg agregado")

def insertar_registros():
    print("           Insertar Reg")
    Nombre = ("Inserta Nombre: ")
    Positionz = int(input("Ubicacion: "))
    COMPRAS.insert(Positionz, Nombre)
    print("Reg insertado")


def mostrar_registros():
    print("           Mostrar ")
    if len(COMPRAS) > 0:
        for COSAS in COMPRAS:
            print(COSAS)
    else:
        print("No hay lista de compras")


def buscar_registros():
    print("           Buscar en compras")
    if len(COMPRAS) > 0:
        Nombre = input("Nombre a buscar: ")
        if Nombre in COMPRAS:
            cantidad = COMPRAS.count(Nombre)
            inicio = 0
            for i in range(cantidad):
                Positionz = COMPRAS.index(Nombre, inicio)
                print(f"{Nombre} se encuentra posicion {Positionz+1}")
                inicio = Positionz + 1    
        else:
            print(f"{Nombre} no se encuentra en la lista")
    else:
        print("No hay lista de compras")
def eliminar_reg():
    print("           Eliminar registro")
    if len(COMPRAS) > 0:
        for i in range(len(COMPRAS)):
            print(f"{i+1}. {COMPRAS[i]}")
            print("0.CANCELAR")
            Positionz = int(input("Posicion a a eliminar: (1 - {len(COMPRAS)})"))
            if 0 < Positionz <= len(COMPRAS):
                COMPRAS.pop(Positionz-1)
                print("Registro eliminado")                
            else:
                print("No hay para eliminar")


def ordenar_reg():
    print("           Ordenar")
    if len(COMPRAS) > 0:
        COMPRAS.sort()
        print("Registros ordeandos")
    else:
        pritn("no hay registros")

def limpiar_registros():
    print("           Limpiar")
    COMPRAS.clear()
    print("Registros limpiados")

def main():
    continuar = True
    while continuar:
        imprimir_menu()
        opc = int(input("Seleciona un opcion: "))
        os.system("cls")
        if opc == AGREGAR:
            agregar_registros()
        elif opc == INSERTAR:
            insertar_registros()
        elif opc == MOSTRAR():
           mostrar_registros()
        elif opc ==  BUSCAR():
            buscar_registros()
        elif opc == ELIMINAR():
            eliminar_reg()
        elif opc == ORDENAR():
            ordenar_reg()
        elif opc == LIMPIAR():
            limpiar_registros()
        elif opc == SALIR():
            Print("bay")
            continuar = False
        else:
            print("opcion no valida")
        input("precione una tecla...")

if __name__ == "__main__":
    main()