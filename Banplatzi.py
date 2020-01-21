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
    print('\t9 - Salir')
    print()

def agregar_clientes_apertura(nombre):
    clientes_apertura.append([nombre])
    with open('clientesapertura.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(clientes_apertura)

def agregar_cliente_deposito(nombre):
    clientes_deposito.append([nombre])

    with open('clientesdeposito.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(clientes_deposito)

def atender_cliente(list1, list2):
    if bool(list1) is True:
        print('Se atendio el Cliente: {0}'.format(list1[0]))
        list1.pop(0)
    elif bool(list2) is True:
        print('Se atendio el Cliente: {0}'.format(list2[0]))
        list2.pop(0)
    else:
        print('Se acabaron los clientes, Lo siento:c')

    salir = True
    while salir is True:
        opcionInterfaz = str(input('Deseas ir a Inicio? (y/n) >> '))
        if opcionInterfaz == 'y':
            break
        else:
            pass

def listar_clientes(list1, list2):
    os.system('cls')
    print('Clientes Apertura:', len(list1))
    for ca in list1:
        print(str(ca))

    print('Clientes Deposito: ', len(list2))
    for cp in list2:
        print(cp)

    salir = True
    while salir is True:
        opcionInterfaz = str(input('Deseas ir a Inicio? (y/n) >> '))
        if opcionInterfaz == 'y':
            break
        else:
            pass

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
            pass
