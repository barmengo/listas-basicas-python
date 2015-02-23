# -*- coding: utf-8 -*-

def item1():
    nota = input('digite uma nota:')
    if not 0 < nota < 10:
        return item1()

def item3():
    nome = raw_input('nome: ')

    if len(nome) < 4:
        raise Exception('nome inválido') # If é uma expressão
                                         # Expressão não retorna uma afirmativa(raise).
                                         # Expressão retorna o resultadode uma expressão
    idade = input('idade: ')

    if not 0 < idade < 150:
        raise Exception('idade inválida')


    salario = input('salário: ')

    if salario <= 0:
        raise Exception('salário inválido')

    sexo = raw_input('sexo (f ou m): ').lower()

    if len(sexo) > 1 or sexo not in 'fm':
        raise Exception('sexo inválido')

    estado_civil = raw_input('estado civil (s, c, v ou d): ').lower()

    if len(estado_civil) < 1 or estado_civil not in 'scvd':
        raise Exception('estado civil inválido')

def item6():
    numeros = map(lambda x: str(x), range(1, 21))
    print '\n'.join(numeros)
    print ' '.join(numeros)

def item44():
    import os

    candidatos = {
        1: {
            'nome': 'João',
            'votos': 0
        },
        2: {
            'nome': 'Maria',
            'votos': 0
        },
        3: {
            'nome': 'Fernanda',
            'votos': 0
        },
        4: {
            'nome': 'Carolina',
            'votos': 0
        },
        5: {
            'nome': 'Voto nulo',
            'votos': 0
        },
        6: {
            'nome': 'Voto branco',
            'votos': 0
        }
    }

    eleitores = input('numero de eleitores: ')

    if eleitores <= 0:
            raise Exception('Opção inválida')

    os.system('clear')

    while eleitores > 0:

        for key, candidato in candidatos.iteritems():
            print '{} - {}'.format(key, candidato['nome'])

        voto = input('Seu voto: ')

        if voto < 1 or voto > 6:
            raise Exception('Opção inválida')

        candidatos[voto]['votos'] += 1

        os.system('clear')

        eleitores -= 1

    for key, candidato in candidatos.iteritems():
        print '{}: {} votos'.format(candidato['nome'], candidato['votos'])

    vencedor = reduce(lambda x, y: x if x > y else y, list())
    # recuperar  programa do git

    print 'Vencedor: ', nome_vencedor

def chamada(nome):
    try:
        globals().get(nome)()

    except TypeError, e:
        print 'função inválida'

    except Exception, e:
        print e, '\n'

        return chamada(nome)

if __name__ == "__main__":
    import sys
    chamada('item{}'.format(sys.argv[1]))