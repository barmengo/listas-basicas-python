# -*- coding: utf-8 -*-

def item3():
    print 'informe dois números:'
    num1, num2 = input(), input()

    print """
primeiro número: {}
segundo número: {}
soma: {}
    """.format(num1, num2, num1 + num2)

def item4():
    notas = []
    soma = 0
    print 'informe 4 notas bimestrais'

    for x in xrange(4):
        notas.append(input())

    for x in notas:
        soma += x

    print 'média das notas bimestrais:', soma / 4.0

def item5():
    metros = input('informe o tamanho em metros:')
    print '{}m em centímetros é {}cm'.format(metros, metros * 100)

def item6():
    import math
    raio = input('informe o raio do círculo:')
    print 'área do círculo:', 2 * math.pi * raio

def item7():
    lado = input('informe o tamanho do lado do quadrado:')
    print 'dobro da área do quadrado:', 2 * (lado ** 2)

def item8():
    valor = input('quanto ganha por hora:')
    hora = input('quantas horas trabalha por mês:')
    print 'valor do salário:', valor * hora

def item9():
    pass

def item10():
    pass

def item11():
    num1 = int(input('informe o primeiro número inteiro:'))
    num2 = int(input('informe o segundo número inteiro:'))
    num3 = int(input('informe o terceiro número real:'))
    print 'o produto do dobro do primeiro com metade do segundo:', (2 * num1) * (num2 / 2)
    print 'a soma do triplo do primeiro com o terceiro:', 3 * num1 + num3
    print 'o terceiro elevado ao cubo:', num3 ** 3

def item12():
    pass

def item13():
    pass

def item14():
    multa = 0
    peso = input('peso (kg):')
    excesso = peso - 50 if (peso - 50) >= 1 else 0
    multa = 4 * excesso
    print 'excesso:{}\nmulta:{} reais'.format(excesso, multa)

def item15():
    pass

def item16():
    pass

def item17():
    lata, galao = 18, 3.6
    tamanho = input('tamanho em m²:')
    litros = int((tamanho / 6) + 1) if tamanho % 6 else tamanho / 6
    latas = int((litros / lata) + 1) if litros % lata else litros / lata
    preco_latas = latas * 80

    print '{} latas, {} reais'. format(latas, preco_latas)

    galoes = int((litros / galao)) + 1 if litros % galao else int(litros / galao)
    preco_galoes = galoes * 25

    print '{} galões, {} reais'. format(galoes, preco_galoes)

    latas = int(litros / lata)

    if litros - (latas * lata) > 0:
        litros -= lata
        galoes = int((litros / galao)) + 1 if litros % galao else int(litros / galao)

    preco_econ = (80 * latas) + (25 * galoes)

    print 'compra econômica: {} latas, {} galões. {} reais'.format(latas, galoes, preco_econ)


if __name__ == "__main__":
    item17()


















