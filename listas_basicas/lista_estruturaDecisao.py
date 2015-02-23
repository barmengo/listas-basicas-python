# -*- coding: utf-8 -*-

def item3():
    genero = raw_input('gênero (F ou M):').upper()

    if genero == 'F':
        print 'feminino'

    elif genero == 'M':
        print 'masculino'

    else:
        print 'Parabéns você reconhece um programa sexista e mesmo assim se afirma como é!\
Ou você não sabe ler instruções!'

def item4():
    char = raw_input('digite uma letra:').lower()

    if len(char) > 1 or char.isdigit():
        print 'letra inválida, digite apenas uma letra'
        return item4()

    if char in 'aeiou':
        print '{} é uma vogal'.format(char)

    else:
        print '{} é uma consoante'.format(char)

def item7():
    numero = []
    print 'digite três números:'

    for x in range(3):
        numero.append(input())

    # maior = menor = numero[0]

    # for x in numero:
    #     if x >= maior:
    #         maior = x

    #     if x <= menor:
    #         menor = x

    maior = max(numero)
    menor = min(numero)

    print 'menor: {}\nmaior:{}'.format(menor, maior)

def item9():
    numero = []
    print 'digite três números:'

    for x in range(3):
        numero.append(input())

    print'ordem decrescente:', sorted(numero, reverse = True)

def item18():
    from datetime import datetime
    data = raw_input('informe uma data (dd/mm/aaaa):').split('/')
    dia, mes, ano = map(lambda x: int(x), data)

    try:
        data = datetime(ano, mes, dia)
        print '{}/{}/{} é válida'.format(dia, mes, ano)

    except Exception, e:
        print 'data inválida'
        return item18()

def item23():
    num = input('digite um número:')
    num_round = round(num)

    if num - num_round:
        print '{} é decimal'.format(num)

    else:
        print '{} é inteiro'.format(num)

def item28():
    mercado = {
        'filé duplo': (4.9, 5.8),
        'alcatra': (5.9, 6.8),
        'picanha': (6.9, 7.8)
    }

    carne = raw_input('carne(filé duplo, alcatra ou picanha):')
    kilo = input('quilos de {}:'.format(carne))

    preco_total = kilo * mercado.get(carne)[0 if kilo <= 5 else 1]

    cartao = raw_input('pagamento pelo cartão Tabajara (s ou n):')

    desconto = preco_total * 0.05

    preco_final = preco_total if cartao == 'n' else preco_total - desconto

    print """
Tipo de carne: {}
Quantidade de {}: {}kg
Preço Total: {} reais
Tipo de pagamento: {}
Valor de desconto: {} reais

Valor a pagar: {} reais
""".format(carne,
        carne,
        kilo,
        preco_total,
        ('Cartão Tabajara' if cartao == 's' else 'Dinheiro'),
        (desconto if cartao == 's' else 0),
        preco_final
    )


if __name__ == "__main__":
    import sys
    globals().get('item{}'.format(sys.argv[1]))()


