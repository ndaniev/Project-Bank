import csv
import os


def interfaz():
    os.system('cls')
    print()
    print('-' * 50)
    print('-' * 19, 'BanPlatzi', '-' * 20)
    print('-' * 50)
    print('')
    print('Selecciona una opción')
    print()
    print('\t1 - Agregar cliente a fila de depósito')
    print('\t2 - Agregar cliente a fila de apertura de cuenta')
    print('\t3 - Atender cliente')
    print('\t4 - Listar clientes en fila')
    print()


def agregar_clientes_apertura(nombre):
    clientes_apertura.append([nombre])
    with open('db.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(clientes_apertura)


def agregar_cliente_deposito(nombre):
    clientes_deposito.append([nombre])

    with open('db2.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(clientes_deposito)


def atender_cliente(list1, list2):
    if bool(list1) is True:
        print('Hay elementos en clientes de apertura')
        list1.pop(0)
    elif bool(list2) is True:
        print('Hay elementos en clientes de deposito')
        list2.pop(0)
    else:
        print('Se acabaron los clientes, Lo siento:c')


def listar_clientes(list1, list2):
    print('Clientes Apertura:', len(list1))
    for row in list1:
        print(str(row))

    print('Clientes Deposito: ', len(list2))
    for row in list2:
        print(row)

    salir = True
    while salir is True:
        opcionInterfaz = input('Deseas ir a Inicio? (y/n) >> ')
        if opcionInterfaz == 'y' or 'Y':
            salir = False


def nombre():
    nombre = str(input('Inserta Nombre Completo :  '))
    return nombre


if __name__ == '__main__':
    clientes_apertura = []
    clientes_deposito = []
    while True:
        interfaz()
        opcionMenu = input('Inserta un Caracter >> ')

        if opcionMenu == '1':
            agregar_clientes_apertura(nombre())
        elif opcionMenu == '2':
            agregar_cliente_deposito(nombre())
        elif opcionMenu == '3':
            atender_cliente(clientes_apertura, clientes_deposito)
        elif opcionMenu == '4':
            listar_clientes(clientes_apertura, clientes_deposito)
        elif opcionMenu == '9':
            break
        else:
            print('Intentalo de Nuevo! ')
