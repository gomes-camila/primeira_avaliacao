def numero_unico_repete_3():
    """
    5. Escreva um algoritmo para encontrar um único número de um array onde cada
    número repete três vezes, exceto um:
    Input : array(5, 3, 4, 3, 5, 5, 3);
    Output : array
    (
    [0] => 5,
    [1] => 3,
    [2] => 4,
    [3] => 3,
    [4] => 5,
    [5] => 5,
    [6] => 3,
    );
    Single Number: 4
    """
    print("Número Único Não se Repete 3 Vezes")
    lista_original = [5, 3, 4, 3, 5, 5, 3]
    dict = {}
    for i in lista_original:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
    numero_unico = list(dict.keys())[list(dict.values()).index(1)]    
    print(f"O número único da lista {lista_original} é {numero_unico}")

numero_unico_repete_3()