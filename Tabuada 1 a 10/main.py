print("Tabuada dos números de 1 a 10")

# Entrada e validação de entrada
while True:
    ent = input("Deseja consultar uma tabuada de soma ou multiplicação? \n1 - Adição \n2 - Multiplicação \n")

    while ent.isnumeric() == False or int(ent) != 1 and int(ent) != 2:
        ent = input("Por favor, entre com um número válido. \n")

    # Tabuada de adição
    # Teste e entrada com validação de número
    if ent == "1":
        nmr = input("Digite um número para ver sua tabuada:")
        while nmr.isnumeric() == False or int(nmr) < 1 or int(nmr) > 10:
            nmr = input("Por favor, digite um número válido entre 1 e 10 \n")
        nmr = int(nmr)

        # Conta para tabuada de adição
        for count in range(10):
            print("%d + %d = %d" % (nmr, count + 1, nmr + (count + 1)))

        # Consulta de Nova Tabela
        CNT = input("Deseja consultar outra tabuada? \n1 - Sim \n2 - Não \n")
        while CNT.isnumeric() == False or int(CNT) != 1 and int(CNT) != 2:
            CNT = input("Por favor, digite uma resposta válida. \n")
        if CNT == '2':
            print("Espero ter ajudado!")
            break

    # Tabudada de Multiplicação
    # Teste e entrada com validação de número
    if ent == "2":
        nmr = input("Digite um número para ver sua tabuada:")
        while nmr.isnumeric() == False or int(nmr) < 1 or int(nmr) > 10:
            nmr = input("Por favor, digite um número válido entre 1 e 10 \n")
        nmr = int(nmr)

        # Conta para tabuada de multiplicação
        for count in range(10):
            print("%d x %d = %d" % (nmr, count + 1, nmr * (count + 1)))

        # Consulta de Nova Tabela
        CNT = input("Deseja consultar outra tabuada? \n1 - Sim \n2 - Não \n")
        while CNT.isnumeric() == False or int(CNT) != 1 and int(CNT) != 2:
            CNT = input("Por favor, digite uma resposta válida. \n")
        if CNT == '2':
            print("Espero ter ajudado!")
            break