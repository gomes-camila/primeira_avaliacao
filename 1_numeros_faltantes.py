def numeros_faltantes():
    """
    1. Escreva um algoritmo para encontrar os números faltantes de um array:
    Input : array(1,2,3,6,7,8);
    Output : array([3] => 4, [4] => 5);
    """
    print("Números Faltantes")
    lista_original = [1, 2, 3, 6, 7, 8]
    numeros_que_faltam = []
    for i in range(lista_original[0], lista_original[-1] + 1):
        if i not in lista_original:
            numeros_que_faltam.append(i)
    print(f"Lista = {lista_original}\nNúmeros que faltam na lista = {numeros_que_faltam}")

numeros_faltantes()