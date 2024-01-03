import pandas as pd

# A - Parceiro
# B - Categoria
# C - Mês
# D - Nº total de vendas
# E - Nº de vendas pendentes
# F - Nº de vendas confirmadas
# G - Nº de vendas canceladas
# H - Nº de reclamações por compra pendente
# I - Nº de reclamações por compra cancelada

df = pd.read_excel(
    r"C:\Users\Pamel_tiuajxt\OneDrive\Documents\Desafio Méliuz\Base de Dados - Estágio Transações (1).xlsx",
    engine="openpyxl",
)

menu = """
Bem-vindo! Digite a opção desejada:
[1] Quais são as taxas de validação
[2] Quais são as taxas de confirmação
[3] Quais são as lojas mais reclamadas por mês
[4] Quais são os meses mais reclamados
[5] Qual a relação entre as taxas e o número de reclamações
=> """

opcao = input(menu)

if opcao == "1":  # Quais são as taxas de validação por parceiro/mês/categoria?

    # Coletar os dados de Parceiro, mes e categoria
    nomeParceiro = input("Qual o nome do parceiro? ")
    mes = input("Qual o mes? ")
    categoria = input("Qual a categoria? ")

    # Filtrar os dados por parceiro, mes e categoria
    df2 = df[(df["Parceiro"] == nomeParceiro) & (df["Mês"] == mes) & (df["Categoria"] == categoria)]

    # declarar variaveis
    totalVendasConfirmadas = 0
    vendasCanceladas = 0
    totalVendas = 0

    # somar os valores
    for val in df2["Nº de vendas confirmadas"]:
        totalVendasConfirmadas += val

    for val in df2["Nº de vendas canceladas"]:
        vendasCanceladas += val

    for val in df2["Nº total de vendas"]:
        totalVendas += val

    # calcular o percentual
    percentual = ((totalVendasConfirmadas + vendasCanceladas) / totalVendas) * 100
    print("A taxa de validação é %.2f" % percentual,"%")

elif opcao == "2":  # Quais são as taxas de confirmação por parceiro/mês/categoria?

    # Coletar os dados de Parceiro, mes e categoria
    nomeParceiro = input("Qual o nome do parceiro? ")
    mes = input("Qual o mes? ")
    categoria = input("Qual a categoria? ")

    # Filtrar os dados por parceiro, mes e categoria
    df2 = df[(df["Parceiro"] == nomeParceiro) & (df["Mês"] == mes) & (df["Categoria"] == categoria)]

    # declarar variaveis
    totalVendasConfirmadas = 0
    totalVendas = 0

    # somar os valores
    for val in df2["Nº de vendas confirmadas"]:
        totalVendasConfirmadas += val

    for val in df2["Nº total de vendas"]:
        totalVendas += val

    # calcular o percentual
    percentual = (totalVendasConfirmadas / totalVendas) * 100
    print("A taxa de vendas confirmadas é %.2f" % percentual,"%")

elif opcao == "3":  # Quais são as lojas mais reclamadas por mês?
    
    menu = """
    Digite qual tipo de reclamação deseja visualizar:
    [1] Por compra pendente
    [2] Por compra cancelada
    => """

    escolha = input(menu)
    nomeDaColunaExcel = ""

    if escolha == "1":
        nomeDaColunaExcel = "Nº de reclamações por compra pendente";
    elif escolha == "2":
        nomeDaColunaExcel = "Nº de reclamações por compra cancelada";

    # criar uma lista com todos os Parceiro e somar todas as vendas
    lista = df.groupby("Parceiro")[nomeDaColunaExcel].sum()

    #orderar a lista com o maior valor primeiro
    lista = lista.sort_values(ascending=False)
    print(lista)

elif opcao == "4":  # Quais são os meses mais reclamados?
    
    menu = """
    Digite qual tipo de reclamação deseja visualizar:
    [1] Por compra pendente
    [2] Por compra cancelada
    => """

    escolha = input(menu)
    nomeDaColunaExcel = ""

    if escolha == "1":
        nomeDaColunaExcel = "Nº de reclamações por compra pendente";
    elif escolha == "2":
        nomeDaColunaExcel = "Nº de reclamações por compra cancelada";

    # criar uma lista com todos os Parceiro e somar todas as vendas
    lista = df.groupby("Mês")[nomeDaColunaExcel].sum()

    #orderar a lista com o maior valor primeiro
    lista = lista.sort_values(ascending=False)
    print(lista)

elif opcao == "5":  # Qual a relação entre as taxas e o número de reclamações?

    menu = """
    Digite qual tipo de taxa:
    [1] Confirmação
    [2] Validação
    => """

    tipoTaxaEscolhido = input(menu)

    menu = """
    Digite qual tipo de reclamação:
    [1] Por compra pendente
    [2] Por compra cancelada
    => """

    tipoReclamacaoEscolhido = input(menu)
    nomeReclamacaoEscolhido = ""

    nomeDaColunaExcel = ""
    if tipoReclamacaoEscolhido == "1":
        nomeDaColunaExcel = "Nº de reclamações por compra pendente"
        nomeReclamacaoEscolhido = "pendente"
    elif tipoReclamacaoEscolhido == "2":
        nomeDaColunaExcel = "Nº de reclamações por compra cancelada"
        nomeReclamacaoEscolhido = "cancelada"

    totalVendasConfirmadas = 0
    vendasCanceladas = 0
    totalVendas = 0
    totalReclamacoes = 0

    if tipoTaxaEscolhido == "1":
        
        # somar os valores
        for val in df["Nº de vendas confirmadas"]:
            totalVendasConfirmadas += val

        for val in df["Nº total de vendas"]:
            vendasCanceladas += val

        for val in df[nomeDaColunaExcel]:
            totalReclamacoes += val

        # calcular o percentual
        percentual = (totalVendasConfirmadas / totalReclamacoes)
        print("Do total de", totalVendasConfirmadas, "confirmaçõe, %.2f" % percentual, "% teve reclamação por compra", nomeReclamacaoEscolhido)

    elif tipoTaxaEscolhido == "2":

        for val in df["Nº de vendas confirmadas"]:
            totalVendasConfirmadas += val

        for val in df["Nº de vendas canceladas"]:
            vendasCanceladas += val

        for val in df["Nº total de vendas"]:
            totalVendas += val

        for val in df[nomeDaColunaExcel]:
            totalReclamacoes += val
        
        # calcular o percentual
        percentual = (totalVendasConfirmadas / totalReclamacoes)
        print("Do total de", totalVendasConfirmadas, "validações, %.2f" % percentual, "% teve reclamação por compra", nomeReclamacaoEscolhido)

else:
    print("Opção invalida")
    

def testeFiltro(a):
    return a
