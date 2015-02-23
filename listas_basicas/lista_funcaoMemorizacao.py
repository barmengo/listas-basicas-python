# -*- coding: utf-8 -*-

def find_index(n, **memoria):
    encontrado = 0

    for index, value in memoria.items():
        if n == value:
            encontrado = 1
            return index

    if encontrado == 0:
        return -1

def fibonacci(n, ** memoria): #não é uma função recursiva
    while memoria[len(memoria) - 1] < n:
        memoria[len(memoria)] = memoria[len(memoria) - 1] + memoria[len(memoria) - 2]

    return memoria


if __name__ == "__main__":
    memo = {0: 0, 1: 1}
    numero = input('digite um número: ')

    if numero < 0:
        raise Exception('número inválido')

    if find_index(numero, memo) == -1:
        print 'Número não encontrado na sequência de Fibonacci'

    else:
        print'Número {} na posição {} da sequência de Fibonacci'.format(numero, find_index(numero, memo))