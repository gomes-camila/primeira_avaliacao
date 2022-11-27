def soma_tres_consecutivos():
    """
    3. Escreva um algoritmo para encontrar três números consecutivos de um array que
    somados o resultado é igual a um outro número fornecido:
    Input : (array(2, 7, 7, 1, 8, 2, 7, 8, 7), 16));
    Output : array(
    [0] => 2 + 7 + 7 = 16,
    [1] => 7 + 1 + 8 = 16
    );
    """
    print("Soma Três Consecutivos")
    lista_original = [2, 7, 7, 1, 8, 2, 7, 8, 7]
    numero_fornecido = 16
    for i in range(len(lista_original) - 2):
        if lista_original[i] + lista_original[i + 1] + lista_original[i + 2] == numero_fornecido:
            print(f"{lista_original[i]} + {lista_original[i + 1]} + {lista_original[i + 2]} = {numero_fornecido}")

soma_tres_consecutivos()