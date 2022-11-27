def soma_consecutivos_igual_zero():
    """
    2. Escreva um algoritmo para encontrar três números consecutivos de um array que
    somados o resultado é igual a zero:
    Input : array(-1,0,1,2,-1,-4);
    Output : array([0] => -1 + 0 + 1 = 0);0
    """
    print("Soma Consecutivos Igual a Zero")
    lista_original = [-1, 0, 1, 2, -1, -4]
    for i in range(len(lista_original) - 2):
        if lista_original[i] + lista_original[i + 1] + lista_original[i + 2] == 0:
            print(f"{lista_original[i]} + {lista_original[i + 1]} + {lista_original[i + 2]} = 0")

soma_consecutivos_igual_zero()