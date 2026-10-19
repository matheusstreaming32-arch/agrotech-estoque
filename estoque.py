# Projeto AgroTech
# Sistema de Controle de Estoque Agricola

produtos = [
    "Sementes",
    "Fertilizantes",
    "Defensivos agricolas"
]


def apresentar_sistema():
    print("Bem-vindo ao AgroTech")
    print("Sistema de Controle de Estoque Agricola")


def listar_produtos():
    print("Produtos cadastrados:")

    for produto in produtos:
        print("-", produto)


apresentar_sistema()
listar_produtos()