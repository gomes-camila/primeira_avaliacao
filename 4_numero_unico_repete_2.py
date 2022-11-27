def numero_unico_não_repete_2():
    """
    4. Escreva um algoritmo para encontrar um único número de um array que não se
    repita duas vezes:
    Input : array(5, 3, 4, 3, 4);
    Output : array
    (
    [0] => 5,
    [1] => 3,
    [2] => 4,
    [3] => 3,
    [4] => 4,
    );
    Single Number: 5
    """
    print("Número Único Não se Repete 2 Vezes")
    lista_original = [5, 3, 4, 3, 4]
    dic = {}
    for i in lista_original:
        if i not in dic:
                dic[i] = 1
        else:
                dic[i] = dic[i] + 1
    numero_unico = list(dic.keys())[list(dic.values()).index(1)]
    print(f"O número único da lista {lista_original} é {numero_unico}")

numero_unico_não_repete_2()