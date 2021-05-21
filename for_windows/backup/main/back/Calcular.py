# Calculadora de apenas uma linha

def Operacao(linha_completa):
    p_direita = -1
    while True:
        p_direita += 1
        linha_atual = linha_completa[p_direita]
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
    p_esquerda = p_direita + 1
        
    valor_1 = float(linha_completa[:p_direita])
    valor_2 = float(linha_completa[p_esquerda:])
        
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
