#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 2

def media_final_aprovado_reprovado(prova1,prova2,exercicios_programacao1,
    exercicios_programacao2):
    ''' Recebe as notas das 2 provas e 2 exercícios de programação e retorna 
    se o aluno foi ou não aprovado. As provas tem peso 7 e os exercícios 
    tem peso 3. Cada parcial tem peso igual.'''
    nota1 = round(float(prova1 * 0.7) + (float(exercicios_programacao1 * 0.3)), 2)
    nota2 = round(float(prova2 * 0.7) + (float(exercicios_programacao2 * 0.3)), 2)
    media = (nota1 + nota2) / 2
    if media>= 7:
        return bool(True)
    else:
        return bool(False)

def excesso_peso_peixes(peso_peixes_kg, peso_limite):
    ''' Recebe o peso dos peixes pescados, e o limite legal e devolve 
    o peso em excesso, ou zero se não houver'''
    if peso_peixes_kg > peso_limite:
        return round(float(peso_peixes_kg - peso_limite),2)
    else:
        return 0

def testa_lados(a,b,c):
    ''' Receba os três lados de um triângulo. Informe se os valores
    podem ser um triângulo. Indique, caso os lados formem um triângulo,
    se o mesmo é: equilátero, isósceles ou escaleno. '''
    if a <= b*2 and b <= c*2 and c <= a*2:
        if a != b != c:
            return 'Triangulo escaleno'
        if a == b == c:
            return 'Triangulo equilatero'
        if a == b !=c or b == c != a:
            return 'Triangulo isosceles'
    else:
        return 'Nao forma um triangulo'


def ano_bissexto(ano):
    ''' Determine se um ano é bissexto'''
    if ano % 4 != 0:
        return bool(False)
    else:
        if str(ano)[2:] == '00':
            if ano%400 == 0:
                return bool(True)
            else:
                return bool(False)
        else:
            return bool(True)

def data_valida(data):
    '''Valida data'''
    date = data.split('/')
    dia = int(date[0])
    mes = int(date[1])
    ano = int(date[2])
    if dia and mes and ano != 0:
        if mes > 12:
            return bool(False)
        else:
            if mes >= 8:
                if mes%2 == 0:
                    if dia <= 31:
                        return bool(True)
                    else:
                        return bool(False)
                else:
                    if dia <= 30:
                        return bool(True)
                    else:
                        return bool(False)
            if mes < 8:
                if mes%2 == 0:
                    if mes == 2:
                        if ano % 4 != 0:
                            if dia == 28:
                                return bool(True)
                            else:
                                return bool(False)
                        else:
                            if str(ano)[2:] == '00':
                                if ano%400 == 0:
                                    if dia == 29:
                                        return bool(True)
                                    else:
                                        return bool(False)
                                else:
                                    if dia == 28:
                                        return bool(True)
                                    else:
                                        return bool(False)
                            else:
                                if dia == 29:
                                    return bool(True)
                                else:
                                    return bool(False)
                    else:
                        if dia <= 30:
                            return bool(True)
                        else:
                            return bool(False)
                else:
                    if dia <= 31:
                        return bool(True)
                    else:
                        return bool(False)
    else:
        return bool(False)

def maior3(a,b,c):
    ''' Recebe tres valores, e retorna o maior dos tres'''
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c

def menor3(a,b,c):
    ''' Recebe tres valores, e retorna o menor dos tres'''
    if a < b and a < c:
        return a
    if b < a and b < c:
        return b
    if c < a and c < b:
        return c

def salario(dinheiro_horas,horas_mensais):
    ''' Recebe quanto ganha por hora e quantas horas trabalho ao mês,
    e retorna o salário líquido.
    Descontos:
    - INSS é 8% do salário bruto
    - IR é 11% do salário bruto
    - Sindicato é 5% do salário bruto'''
    salario_bruto = int(dinheiro_horas * horas_mensais)
    return salario_bruto - (salario_bruto*0.08) - (salario_bruto*0.11) - (salario_bruto*0.05)

def tinta(metros_pintar):
    ''' Recebe quanto metros quadrados precisa pintar, 
    e retorna a quantidade de latas de tinta a comprar.
    A cobertura da tinta é de 3 metros por litro de tinta
    Cada lata possui 18 litros de tinta'''
    litros_tinta = float(metros_pintar/3)
    if litros_tinta <= 18:
        return 1
    else:
        latas_tinta = float(litros_tinta/18)
        if latas_tinta >= round(latas_tinta):
            return round(latas_tinta) + 1
        else:
            return round(latas_tinta);


def acrescimo_nota_bb(nota_sozinho,nota_com_ajuda):
    ''' Recebe a nota do litle brother antes de receber ajuda, e a nota
    depois que o big brother ajudou, e retorna o acrecimo que o big
     brother recebera em sua nota pela ajuda.
     O acréscimo é de 1/4 da diferença das notas, se for positivo'''
    if nota_com_ajuda > nota_sozinho:
        return round(float(nota_com_ajuda - nota_sozinho) * float(1.0/4.0), 2)
    else:
        return 0

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = ' Falhou.'
    else:
        prefixo = ' Passou.'
        acertos += 1
    print ('%s Esperado: %s \tObtido: %s' % (prefixo, repr(esperado), 
        repr(obtido)))

def main():
    print('Média final:')
    test(media_final_aprovado_reprovado(10,10,0,0), True)
    test(media_final_aprovado_reprovado(0,0,10,10), False)
    test(media_final_aprovado_reprovado(10,10,10,10), True)
    test(media_final_aprovado_reprovado(0,0,5,0), False)

    print('Pesca em excesso:')
    test(excesso_peso_peixes(10,50),0)
    test(excesso_peso_peixes(50,50), 0)
    test(excesso_peso_peixes(50.01,50), 0.01)
    test(excesso_peso_peixes(190.99,50), 140.99)

    print('Triângulos:')
    test(testa_lados(7,1,2),'Nao forma um triangulo')
    test(testa_lados(7,2,1),'Nao forma um triangulo')
    test(testa_lados(1,7,2),'Nao forma um triangulo')
    test(testa_lados(1,2,7),'Nao forma um triangulo')
    test(testa_lados(2,1,7),'Nao forma um triangulo')
    test(testa_lados(2,7,1),'Nao forma um triangulo')
    test(testa_lados(2,2,2),'Triangulo equilatero')
    test(testa_lados(3,3,3),'Triangulo equilatero')
    test(testa_lados(2,3,4),'Triangulo escaleno')
    test(testa_lados(2,4,3),'Triangulo escaleno')
    test(testa_lados(3,4,2),'Triangulo escaleno')
    test(testa_lados(3,2,4),'Triangulo escaleno')
    test(testa_lados(2,3,3),'Triangulo isosceles')
    test(testa_lados(3,2,2),'Triangulo isosceles')
    test(testa_lados(3,3,2),'Triangulo isosceles')

    print('Ano bissexto:')
    test(ano_bissexto(1000),False)
    test(ano_bissexto(1200),True)
    test(ano_bissexto(1004),True)
    test(ano_bissexto(1040),True)
    test(ano_bissexto(2012),True)
    test(ano_bissexto(2014),False)

    print('Valida datas:')
    test(data_valida("01/01/2014"),True)
    test(data_valida("31/01/2014"),True)
    test(data_valida("00/00/0000"),False)
    test(data_valida("29/02/2014"),False)
    test(data_valida("29/02/2016"),True)
    test(data_valida("30/04/2014"),True)
    test(data_valida("31/04/2014"),False)
    test(data_valida("30/06/2014"),True)
    test(data_valida("31/06/2014"),False)
    test(data_valida("30/09/2014"),True)
    test(data_valida("31/09/2014"),False)
    test(data_valida("30/11/2014"),True)
    test(data_valida("31/11/2014"),False)
    test(data_valida("32/01/2014"),False)
    test(data_valida("01/01/0000"),False)
    test(data_valida("01/13/2014"),False)

    print('Maior de 3 valores:')
    test(maior3(1,2,3), 3)
    test(maior3(1.01,1.02,1.1), 1.1)
    test(maior3(0,-1,-2), 0)
    test(maior3(-100,0,100), 100)

    print('Menor de 3 valores:')
    test(menor3(1,2,3), 1)
    test(menor3(1.01,1.02,1.1), 1.01)
    test(menor3(0,-1,-2), -2)
    test(menor3(-100,0,100), -100)

    print('Salário líquido:')
    test(salario(10,80), 608)
    test(salario(100,30), 2280)
    test(salario(2.5,300), 570)
    test(salario(5,120), 456)

    print('Latas de tinta:')
    test(tinta(10), 1)
    test(tinta(100), 2)
    test(tinta(560), 11)
    test(tinta(50001), 926)

    print('Acréscimo BB:')
    test(acrescimo_nota_bb(1,10), 2.2)
    test(acrescimo_nota_bb(7,6), 0.0)
    test(acrescimo_nota_bb(0,10), 2.5)
    test(acrescimo_nota_bb(6.9,7.1), 0.0)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
