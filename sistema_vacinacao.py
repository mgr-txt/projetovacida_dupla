# ==========================================
# SISTEMA DE GERENCIAMENTO DE VACINACAO
# ==========================================

# DADOS INICIAIS

unidades = [
    {"id": 1, "nome": "Unidade Centro", "publico_alvo": 500},
    {"id": 2, "nome": "Unidade Norte", "publico_alvo": 80},
    {"id": 3, "nome": "Unidade Sul", "publico_alvo": 70},
    {"id": 4, "nome": "Unidade Leste", "publico_alvo": 100}
]

lotes = []
aplicacoes = []


# ==========================================
# CADASTRO DE UNIDADES
# ==========================================

def cadastrar_unidade():
    novo_id = max([u["id"] for u in unidades], default=0) + 1

    nome = input("Nome da unidade: ")
    publico = int(input("Publico-alvo: "))

    unidades.append({
        "id": novo_id,
        "nome": nome,
        "publico_alvo": publico
    })

    print("Unidade cadastrada com sucesso!")


# ==========================================
# LISTAR UNIDADES
# ==========================================

def listar_unidades():
    for unidade in unidades:
        print("\nID:", unidade["id"])
        print("Nome:", unidade["nome"])
        print("Publico-alvo:", unidade["publico_alvo"])


# ==========================================
# CADASTRAR LOTE DE VACINAS
# ==========================================

def cadastrar_lote():
    novo_id = len(lotes) + 1

    vacina = input("Nome da vacina: ")
    quantidade = int(input("Quantidade de doses: "))
    validade = input("Validade: ")

    lotes.append({
        "id": novo_id,
        "vacina": vacina,
        "quantidade_inicial": quantidade,
        "quantidade_disponivel": quantidade,
        "validade": validade
    })

    print("Lote cadastrado com sucesso!")


# ==========================================
# CONSULTAR ESTOQUE
# ==========================================

def consultar_estoque():
    if not lotes:
        print("Nenhum lote cadastrado.")
        return

    for lote in lotes:
        print("\nLote:", lote["id"])
        print("Vacina:", lote["vacina"])
        print("Disponivel:", lote["quantidade_disponivel"])
        print("Validade:", lote["validade"])


# ==========================================
# REGISTRAR APLICACAO
# ==========================================

def registrar_aplicacao():
    listar_unidades()

    unidade_id = int(input("\nID da unidade: "))

    unidade = next(
        (u for u in unidades if u["id"] == unidade_id),
        None
    )

    if unidade is None:
        print("Unidade nao encontrada.")
        return

    consultar_estoque()

    lote_id = int(input("\nID do lote: "))

    lote = next(
        (l for l in lotes if l["id"] == lote_id),
        None
    )

    if lote is None:
        print("Lote nao encontrado.")
        return

    quantidade = int(input("Quantidade de doses aplicadas: "))

    if quantidade <= 0:
        print("Quantidade invalida.")
        return

    if quantidade > lote["quantidade_disponivel"]:
        print("Estoque insuficiente.")
        return

    lote["quantidade_disponivel"] -= quantidade

    aplicacoes.append({
        "unidade_id": unidade_id,
        "unidade": unidade["nome"],
        "lote_id": lote_id,
        "vacina": lote["vacina"],
        "quantidade": quantidade
    })

    print("Aplicacao registrada com sucesso!")


# ==========================================
# RELATORIO DE VACINACAO
# ==========================================

def relatorio():
    total_publico = sum(
        u["publico_alvo"] for u in unidades
    )

    total_aplicacoes = sum(
        a["quantidade"] for a in aplicacoes
    )

    print("\n===== RELATORIO GERAL =====")

    print("Unidades cadastradas:", len(unidades))
    print("Publico-alvo total:", total_publico)
    print("Doses aplicadas:", total_aplicacoes)

    if total_publico > 0:
        cobertura = (total_aplicacoes / total_publico) * 100
        print("Cobertura vacinal: {:.2f}%".format(cobertura))


# ==========================================
# RELATORIO POR UNIDADE
# ==========================================

def relatorio_unidades():
    for unidade in unidades:

        total = sum(
            a["quantidade"]
            for a in aplicacoes
            if a["unidade_id"] == unidade["id"]
        )

        print("\nUnidade:", unidade["nome"])
        print("Publico-alvo:", unidade["publico_alvo"])
        print("Doses aplicadas:", total)

        if unidade["publico_alvo"] > 0:
            cobertura = (
                                total / unidade["publico_alvo"]
                        ) * 100

            print("Cobertura: {:.2f}%".format(cobertura))


# ==========================================
# MENU PRINCIPAL
# ==========================================

while True:

    print("\n========== SISTEMA DE VACINACAO ==========")
    print("1 - Cadastrar unidade")
    print("2 - Listar unidades")
    print("3 - Cadastrar lote de vacinas")
    print("4 - Consultar estoque")
    print("5 - Registrar aplicacao")
    print("6 - Relatorio geral")
    print("7 - Relatorio por unidade")
    print("0 - Sair")

    opcao = input("\nEscolha uma opcao: ")

    if opcao == "1":
        cadastrar_unidade()

    elif opcao == "2":
        listar_unidades()

    elif opcao == "3":
        cadastrar_lote()

    elif opcao == "4":
        consultar_estoque()

    elif opcao == "5":
        registrar_aplicacao()

    elif opcao == "6":
        relatorio()

    elif opcao == "7":
        relatorio_unidades()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opcao invalida.")
