'''
    Calcular
    A função Operacao recebe uma string e transforma
    ela em uma conta separando os operadores e os 
    operandos
'''
def Operacao(linha_completa):
    '''
        Loop que separa todos os números inteiros e flutuantes
        da String criado uma nova string para o primeiro operando
    '''
    p_direita = -1
    while True:
        # variavel p_direita vai verifica os valores do primeiro número e para no operador
        p_direita += 1
        linha_atual = linha_completa[p_direita]

        # condição para tratar erro de valores difentes de operandos e operadores
        if (linha_atual == "1" or 
            linha_atual == "2" or 
            linha_atual == "3" or
            linha_atual == "4" or
            linha_atual == "5" or
            linha_atual == "6" or
            linha_atual == "7" or
            linha_atual == "8" or
            linha_atual == "9" or
            linha_atual == "0" or
            linha_atual == "-" or
            linha_atual == "+" or
            linha_atual == "x" or
            linha_atual == "*" or
            linha_atual == '.' or
            linha_atual == "/"):
            pass
        else:
            print("Erro, digite um caractere valido!")
            exit()
        # Verifica qual o operandor
        if linha_atual == "+":
            operador = linha_atual
            break
        elif linha_atual == "-":
            operador = linha_atual
            break
        elif linha_atual == "*":
            operador = linha_atual
            break
        elif linha_atual == "x":
            operador = linha_atual
            break
        elif linha_atual == "/":
            operador = linha_atual
            break
        else:
            pass
    # variavel para esquerda pega todos os valores após o operador
    p_esquerda = p_direita + 1
    
    # transforma as Strings em float para efetuar os cálculos
    valor_1 = float(linha_completa[:p_direita])
    valor_2 = float(linha_completa[p_esquerda:])
    
    # executa os calculos e retorna o resultado
    if operador == "+":
        resultado = valor_1+valor_2
    elif operador =="-":
        resultado = valor_1-valor_2
    elif operador == "*" or operador == "x":
        resultado = valor_1*valor_2
    elif operador == "/":
        if valor_1 == 0 and valor_2 == 0:
            resultado = str("Zero dividido por zero é igual a zero.\nObrigado por usar :)")      
        else:
            resultado = valor_1/valor_2
    else:
        pass
    linha_completa = str(resultado)
    return linha_completa
