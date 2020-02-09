import random
pergunta1 = 'sim'
while (pergunta1 == 'sim'):
    pergunta = str(input('Par ou impar?\n'))
    numero = int(input('Qual o numero?\n'))
    num = random.randint(1,100)
    resultado = numero+num
    if resultado % 2==0:
        if pergunta == 'par':
            print ('Você ganhou!!')
            print ('A soma de {} e {} é {} um numero par'.format(numero,num,resultado))
        if pergunta == 'impar':
            print('A maquina ganhou!!')
            print('A soma de {} e {} é {} um numero par'.format(numero, num, resultado))
    if resultado % 2 != 0:
        if pergunta == 'impar':
            print('Você ganhou!!')
            print('A soma de {} e {} é {} um numero {} '.format(numero, num, resultado,pergunta))
        if pergunta == 'par':
            print('A maquina ganhou!')
            print('A soma de {} e {} é {} um numero impar '.format(numero, num, resultado))
    pergunta1 = str(input('Deseja ir de novo?\n'))
