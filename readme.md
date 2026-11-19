# 💉 Sistema de Gerenciamento de Vacinação

Aplicação de terminal desenvolvida em Python para o gerenciamento, distribuição e controle de aplicação de vacinas em Unidades Básicas de Saúde (UBS). O sistema mantém todo o estado dos dados em memória durante a execução, simulando entidades relacionais por meio de listas e dicionários.

---

## 🔄 Fluxo de Negócio e Modelagem de Dados

O controle de doses segue um fluxo em **três etapas** ($\text{Lote} \rightarrow \text{Unidade} \rightarrow \text{Aplicação}$), garantindo rastreabilidade e impedindo saldos negativos:

1. **`lotes` (Estoque Central):** Armazena `id`, `vacina`, `quantidade_inicial`, `quantidade_disponivel` e `validade`. Separar a quantidade inicial da disponível permite calcular o percentual de distribuição de cada lote sem perder o histórico original.
2. **`unidades` (Postos de Vacinação):** Armazena `id`, `nome`, `publico_alvo` e o saldo local `estoque` (inicializado em `0`). Recebe doses transferidas dos lotes por meio da função de abastecimento.
3. **`aplicacoes` (Histórico de Atendimento):** Registra cada aplicação realizada vinculando `unidade_id`, `unidade`, `quantidade` e `data` (`DD-MM-AAAA`), permitindo consolidar indicadores tanto por UBS quanto por dia.

> **Base inicial pré-carregada:** O sistema já inicia com **12 unidades** (incluindo a `UBS Rural (Caso-Limite)` com `publico_alvo: 0`) e **4 lotes** (incluindo lotes com estoque crítico e zerado) para facilitar testes imediatos.

---

## ⚙️ Funcionalidades

O menu principal utiliza um dicionário de despacho (`acoes`) para mapear cada opção diretamente à sua respectiva função:

* **1 - Cadastrar unidade:** Adiciona uma nova UBS com ID sequencial automático e estoque inicial zerado.
* **2 - Listar unidades:** Exibe todas as unidades cadastradas, seus públicos-alvo e saldos atuais em estoque.
* **3 - Cadastrar lote de vacinas:** Registra novos lotes validando quantidades maiores que zero.
* **4 - Consultar estoque dos lotes:** Lista os lotes disponíveis, quantidades iniciais, saldos atuais e validades.
* **5 - Abastecer unidade:** Transfere doses de um lote específico para o estoque local de uma unidade.
* **6 - Registrar aplicação:** Dá baixa no estoque local da unidade e registra a quantidade aplicada junto com a data (`DD-MM-AAAA`).
* **7 - Relatório geral:** Consolida total de unidades, público-alvo, doses aplicadas, cobertura vacinal geral, saldo em estoque e aplicações agrupadas por dia.
* **8 - Relatório por unidade:** Calcula o total aplicado e o percentual de cobertura individual de cada UBS.
* **9 - Relatório por lote:** Exibe a quantidade distribuída, o saldo disponível e o percentual de distribuição de cada lote.
* **10 - Listar estoques críticos:** Alerta unidades e lotes com saldo menor ou igual ao limite definido na constante `ESTOQUE_CRITICO = 50`.
* **11 - Buscar por ID:** Consulta detalhada de qualquer unidade ou lote pelo seu identificador único.
* **12 - Editar registro:** Permite atualizar dados de unidades e lotes preservando a consistência dos saldos.
* **0 - Sair:** Encerra o loop principal do sistema de forma limpa.

---

## 🛡️ Validações e Casos-Limite Tratados

* **Prevenção de Estoque Negativo:** Bloqueia transferências acima do saldo do lote e aplicações em unidades sem estoque ou com quantidade superior ao disponível.
* **Tratamento de Divisão por Zero (`ZeroDivisionError`):** Nos relatórios, o cálculo percentual só é executado quando o divisor (`publico_alvo` ou `quantidade_inicial`) é maior que zero; caso contrário, o sistema exibe um aviso controlado.
* **Consistência na Edição:** Ao editar um lote, o sistema impede que `quantidade_disponivel` seja negativa ou ultrapasse `quantidade_inicial`.
* **Blindagem de Entradas Numéricas:** A função auxiliar `pedir_inteiro()` encapsula `try/except ValueError` para impedir que entradas inválidas interrompam a execução.
* **Reaproveitamento de Busca:** A função `encontrar_id()` centraliza a busca linear em listas, evitando duplicação de código.

---

## 📁 Estrutura do Projeto

```text
├── sistema_vacinacao.py     # Código-fonte principal da aplicação de terminal
├── relatorio_testes.ipynb   # Explicação técnica e documentação dos 8 casos de teste
└── README.md                # Documentação geral do repositório
```

*(Nota: Caso o arquivo principal receba outro nome definitivo pela dupla, atualize a referência acima e no comando de execução).*

---

## 🚀 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   cd SEU_REPOSITORIO
   ```

2. **Execute o sistema no terminal** (requer Python 3.x instalado, sem dependências externas):
   ```bash
   python sistema_vacinacao.py
   ```

---

## 👨‍💻 Autores

* **Miguel** (`@mgr-txt`)
* **Josué Araujo**
