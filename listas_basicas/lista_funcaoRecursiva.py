# -*- coding: utf-8 -*-

def mult3(n):
    if n == 1:
        return 3

    else:
        return mult3(n - 1) + 3

def soma(n):
    if n == 1:
        return 1

    else:
        return n + soma(n - 1)

def tripascal(n):
    if n == 1:
        return 1

    else:
        linha = [1]
        ant_linha = tripascal(n - 1)

        for x in range(1, n - 1):
            linha.insert(x, ant_linha[x - 1] + ant_linha[x])

        linha += [1]
        return linha

def fatorial(n):
    if n == 1:
        return 1

    else:
        fator = n * fatorial(n - 1)
        return fator

def euler(n):
    if n ==1:
        return 2

    else:
        num_euler = 1.0 / fatorial(n) + euler(n - 1)
        return num_euler


numero = input('digite um número: ')

if numero <= 0:
    raise Exception('número inválido') #tratar a exception

if __name__ == "__main__":
    print '{} x 3 = {}'.format(numero, mult3(numero))
    print '{}! = {}'.format(numero, fatorial(numero))
    print 'Soma dos {} primeiros números inteiros: {}'.format(numero, soma(numero))
    print 'Valor de Euler com prescisão de {}: {}'.format(numero, euler(numero))
    print 'A {} linha do triângulo de Pascal: {}'.format(numero, tripascal(numero))

