ESTOQUE_CRITICO = 50

unidades = [
    {"id": 1, "nome": "UBS Centro", "publico_alvo": 500, "estoque": 0},
    {"id": 2, "nome": "UBS Norte", "publico_alvo": 420, "estoque": 0},
    {"id": 3, "nome": "UBS Sul", "publico_alvo": 600, "estoque": 0},
    {"id": 4, "nome": "UBS Leste", "publico_alvo": 350, "estoque": 0},
    {"id": 5, "nome": "UBS Oeste", "publico_alvo": 480, "estoque": 0},
    {"id": 6, "nome": "UBS Aldeota", "publico_alvo": 750, "estoque": 0},
    {"id": 7, "nome": "UBS Messejana", "publico_alvo": 900, "estoque": 0},
    {"id": 8, "nome": "UBS Benfica", "publico_alvo": 300, "estoque": 0},
    {"id": 9, "nome": "UBS Parangaba", "publico_alvo": 640, "estoque": 0},
    {"id": 10, "nome": "UBS Montese", "publico_alvo": 510, "estoque": 0},
    {"id": 11, "nome": "UBS Barra do Ceará", "publico_alvo": 820, "estoque": 0},
    {"id": 12, "nome": "UBS Rural (Caso-Limite)", "publico_alvo": 0, "estoque": 0},
]

lotes = [
    {
        "id": 1,
        "vacina": "COVID-19 (Pfizer)",
        "quantidade_inicial": 400,
        "quantidade_disponivel": 400,
        "validade": "30-04-2027",
    },
    {
        "id": 2,
        "vacina": "Influenza (Gripe)",
        "quantidade_inicial": 250,
        "quantidade_disponivel": 250,
        "validade": "25-11-2026",
    },
    {
        "id": 3,
        "vacina": "Tríplice Viral",
        "quantidade_inicial": 35,
        "quantidade_disponivel": 35,
        "validade": "15-10-2026",
    },
    {
        "id": 4,
        "vacina": "Febre Amarela",
        "quantidade_inicial": 100,
        "quantidade_disponivel": 0,
        "validade": "10-09-2026",
    },
]

aplicacoes = []


def pedir_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Digite apenas números inteiros!")


def encontrar_id(lista, id_alvo):
    for item in lista:
        if item["id"] == id_alvo:
            return item
    return None


def cadastrar_unidade():
    novo_id = max([u["id"] for u in unidades], default=0) + 1

    nome = input("Nome da unidade: ").strip()
    publico = pedir_inteiro("Publico-alvo: ")

    if publico < 0:
        print("Publico-alvo nao pode ser negativo.")
        return

    unidades.append(
        {
            "id": novo_id,
            "nome": nome,
            "publico_alvo": publico,
            "estoque": 0,
        }
    )

    print("Unidade cadastrada com sucesso!")


def listar_unidades():
    for unidade in unidades:
        print("\nID:", unidade["id"])
        print("Nome:", unidade["nome"])
        print("Publico-alvo:", unidade["publico_alvo"])
        print("Estoque:", unidade["estoque"])


def cadastrar_lote():
    novo_id = max([lote["id"] for lote in lotes], default=0) + 1

    vacina = input("Nome da vacina: ").strip()
    quantidade = pedir_inteiro("Quantidade de doses: ")

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    validade = input("Validade (DD-MM-AAAA): ").strip()

    lotes.append(
        {
            "id": novo_id,
            "vacina": vacina,
            "quantidade_inicial": quantidade,
            "quantidade_disponivel": quantidade,
            "validade": validade,
        }
    )

    print("Lote cadastrado com sucesso!")


def consultar_estoque():
    if not lotes:
        print("Nenhum lote cadastrado.")
        return

    for lote in lotes:
        print("\nLote:", lote["id"])
        print("Vacina:", lote["vacina"])
        print("Inicial:", lote["quantidade_inicial"])
        print("Disponivel:", lote["quantidade_disponivel"])
        print("Validade:", lote["validade"])


def abastecer_unidade():
    listar_unidades()

    unidade_id = pedir_inteiro("\nID da unidade: ")
    unidade = encontrar_id(unidades, unidade_id)

    if unidade is None:
        print("Unidade nao encontrada.")
        return

    consultar_estoque()

    lote_id = pedir_inteiro("\nID do lote: ")
    lote = encontrar_id(lotes, lote_id)

    if lote is None:
        print("Lote nao encontrado.")
        return

    quantidade = pedir_inteiro("Quantidade para transferir: ")

    if quantidade <= 0:
        print("Quantidade deve ser maior que zero.")
        return

    if quantidade > lote["quantidade_disponivel"]:
        print("Estoque insuficiente no lote.")
        return

    lote["quantidade_disponivel"] -= quantidade
    unidade["estoque"] += quantidade

    print("Unidade abastecida com sucesso!")


def registrar_aplicacao():
    listar_unidades()

    unidade_id = pedir_inteiro("\nID da unidade: ")
    unidade = encontrar_id(unidades, unidade_id)

    if unidade is None:
        print("Unidade nao encontrada.")
        return

    quantidade = pedir_inteiro("Quantidade de doses aplicadas: ")

    if quantidade <= 0:
        print("Quantidade invalida.")
        return

    if unidade["estoque"] <= 0:
        print("Unidade sem estoque disponivel.")
        return

    if quantidade > unidade["estoque"]:
        print("Estoque insuficiente na unidade.")
        return
    
    data = input("Data da aplicacao (DD-MM-AAAA): ").strip()

    unidade["estoque"] -= quantidade

    aplicacoes.append(
        {
            "unidade_id": unidade_id,
            "unidade": unidade["nome"],
            "quantidade": quantidade,
            "data": data,
        }
    )

    print("Aplicacao registrada com sucesso!")


def buscar_id():
    while True:
        consulta = pedir_inteiro(
            "Selecione onde deseja consultar:\n"
            "1 - Unidade\n2 - Lote\nEscolha uma opção: "
        )
        if consulta == 1 or consulta == 2:
            break
        print("Opção inválida! Tente novamente...")

    if consulta == 1:
        lista_escolhida = unidades
    else:
        lista_escolhida = lotes

    id_consultado = pedir_inteiro("Qual ID deseja consultar: ")
    registro = encontrar_id(lista_escolhida, id_consultado)

    if registro is None:
        print("ID não encontrado!")
    else:
        print("\n--- REGISTRO ENCONTRADO ---")
        for key, value in registro.items():
            print(f"{key}: {value}")


def editar_registro():
    while True:
        consulta = pedir_inteiro(
            "Selecione onde deseja editar:\n"
            "1 - Unidade\n2 - Lote\nEscolha uma opção: "
        )
        if consulta == 1 or consulta == 2:
            break
        print("Opção inválida! Tente novamente...")

    if consulta == 1:
        lista_escolhida = unidades
    else:
        lista_escolhida = lotes

    id_editar = pedir_inteiro("Digite o ID onde deseja editar: ")
    registro = encontrar_id(lista_escolhida, id_editar)

    if registro is None:
        print("ID não encontrado!")
    elif consulta == 1:
        registro["nome"] = input("Digite o novo NOME: ").strip()
        while True:
            novo_pub = pedir_inteiro("Digite a nova quantidade de PUBLICO-ALVO: ")
            if novo_pub >= 0:
                registro["publico_alvo"] = novo_pub
                break
            else:
                print("ERRO: Quantidade não pode ser negativa!\n" "Tente novamente...")
        print("\nUnidade alterada com sucesso!")
    else:
        registro["vacina"] = input("Digite o novo nome da Vacina: ").strip()
        while True:
            nova_qtd = pedir_inteiro("Digite a nova QUANTIDADE DISPONIVEL: ")
            if nova_qtd < 0:
                print("ERRO: Quantidade não pode ser negativa!\n" "Tente novamente...")
            elif nova_qtd > registro["quantidade_inicial"]:
                print(
                    "ERRO: Quantidade disponível não pode ser maior que a "
                    f"inicial ({registro['quantidade_inicial']})!"
                )
            else:
                registro["quantidade_disponivel"] = nova_qtd
                break
        registro["validade"] = input("Nova validade (DD-MM-AAAA): ").strip()
        print("\nLote alterado com sucesso!")


def listar_criticos():
    encontrou = False

    print("\n===== ESTOQUES CRITICOS =====")

    print("\nUNIDADES:")
    for unidade in unidades:
        if unidade["estoque"] <= ESTOQUE_CRITICO:
            encontrou = True
            print(unidade["nome"], "- Estoque:", unidade["estoque"])

    print("\nLOTES:")
    for lote in lotes:
        if lote["quantidade_disponivel"] <= ESTOQUE_CRITICO:
            encontrou = True
            print(
                lote["vacina"],
                "- Lote:",
                lote["id"],
                "- Disponivel:",
                lote["quantidade_disponivel"],
            )

    if not encontrou:
        print("Nenhum estoque critico encontrado.")


def relatorio():
    total_publico = sum(u["publico_alvo"] for u in unidades)
    total_aplicacoes = sum(a["quantidade"] for a in aplicacoes)

    print("\n===== RELATORIO GERAL =====")
    print("Unidades cadastradas:", len(unidades))
    print("Publico-alvo total:", total_publico)
    print("Doses aplicadas:", total_aplicacoes)

    if total_publico > 0:
        cobertura = (total_aplicacoes / total_publico) * 100
        print("Cobertura vacinal: {:.2f}%".format(cobertura))
    else:
        print("AVISO: Publico-alvo total igual a zero.")

    estoque_unidades = sum(u["estoque"] for u in unidades)
    estoque_lotes = sum(lote["quantidade_disponivel"] for lote in lotes)

    print("Doses nas unidades:", estoque_unidades)
    print("Doses nos lotes:", estoque_lotes)
    
    if aplicacoes:
        print("\nAplicacoes por dia:")
        for dia in sorted(set(a["data"] for a in aplicacoes)):
            total_dia = sum(a["quantidade"] for a in aplicacoes if a["data"] == dia)
            print(f"- {dia}: {total_dia} doses")

def relatorio_unidades():
    for unidade in unidades:
        total = sum(
            a["quantidade"] for a in aplicacoes if a["unidade_id"] == unidade["id"]
        )

        print("\nUnidade:", unidade["nome"])
        print("Publico-alvo:", unidade["publico_alvo"])
        print("Doses aplicadas:", total)
        print("Estoque atual:", unidade["estoque"])

        if unidade["publico_alvo"] == 0:
            print("AVISO: Unidade sem publico-alvo cadastrado.")
        else:
            cobertura = (total / unidade["publico_alvo"]) * 100
            print("Cobertura: {:.2f}%".format(cobertura))


def relatorio_lotes():
    print("\n===== RELATORIO POR LOTE =====")
    for lote in lotes:
        distribuidas = lote["quantidade_inicial"] - lote["quantidade_disponivel"]

        print(f"\nLote {lote['id']} - {lote['vacina']}")
        print("Inicial:", lote["quantidade_inicial"])
        print("Distribuidas:", distribuidas)
        print("Disponivel:", lote["quantidade_disponivel"])

        if lote["quantidade_inicial"] > 0:
            percentual = (distribuidas / lote["quantidade_inicial"]) * 100
            print("Percentual distribuido: {:.2f}%".format(percentual))
        else:
            print("AVISO: Lote sem quantidade inicial cadastrada.")


while True:
    acoes = {
        "1": cadastrar_unidade,
        "2": listar_unidades,
        "3": cadastrar_lote,
        "4": consultar_estoque,
        "5": abastecer_unidade,
        "6": registrar_aplicacao,
        "7": relatorio,
        "8": relatorio_unidades,
        "9": relatorio_lotes,
        "10": listar_criticos,
        "11": buscar_id,
        "12": editar_registro,
    }
    print("\n========== SISTEMA DE VACINACAO ==========")
    print("1 - Cadastrar unidade")
    print("2 - Listar unidades")
    print("3 - Cadastrar lote de vacinas")
    print("4 - Consultar estoque dos lotes")
    print("5 - Abastecer unidade")
    print("6 - Registrar aplicacao")
    print("7 - Relatorio geral")
    print("8 - Relatorio por unidade")
    print("9 - Relatorio por lote")
    print("10 - Listar estoques criticos")
    print("11 - Buscar por ID")
    print("12 - Editar registro")
    print("0 - Sair")

    opcao = input("\nEscolha uma opcao: ").strip()

    if opcao == "0":
        print("\nSistema encerrado com sucesso!")
        break

    acao = acoes.get(opcao)
    if acao is None:
        print("Opcao invalida. Tente novamente.")
        continue

    acao()
