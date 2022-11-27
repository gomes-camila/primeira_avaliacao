def sequencia_fibonacci():
    """
    6. Escreva um algoritmo que receba um numero e que apartir deste numero construa
    um array com a sequencia fibonacci e com o numero de elementos sendo o
    informado:
    Input : 6;
    Output : array (1, 1, 2, 3, 5, 8);
    """
    print("Sequência Fibonacci")
    numero_de_elementos = 6
    a = 0
    b = 1
    sequencia_fibinacci = []
    for i in range(numero_de_elementos):
        sequencia_fibinacci.append(b)
        a,b = b, a+b
    print(f"Sequência Fibonacci com número de elementos {numero_de_elementos} = {sequencia_fibinacci}")

sequencia_fibonacci()