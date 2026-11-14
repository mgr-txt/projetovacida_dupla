# 💉 Projeto  — Sistema de Gerenciamento de Vacinação Fictícia

Aplicação de terminal (CLI) desenvolvida em **Python** para organizar, controlar e analisar dados de campanhas de vacinação fictícia. O sistema opera em memória durante a execução, permitindo realizar múltiplas operações de cadastro, movimentação de estoque e geração de indicadores em um menu interativo contínuo.

## 👥 Equipe
* **Josué Araujo**
* **Miguel Gomes**

---

## 🏗️ Arquitetura e Estrutura de Dados

O sistema mantém o estado dos dados em memória utilizando **listas de dicionários**, organizadas em três entidades principais:

* **`unidades`**: Armazena os postos de atendimento (`id`, `nome`, `publico_alvo`).
* **`lotes`**: Controla as remessas de vacinas disponíveis (`id`, `vacina`, `quantidade_inicial`, `quantidade_disponivel`, `validade`).
* **`aplicacoes`**: Registra o histórico de doses aplicadas por posto e lote (`unidade_id`, `unidade`, `lote_id`, `vacina`, `quantidade`).

---

## ✅ Funcionalidades Implementadas (Base Atual)

O código inicial já conta com a estrutura principal de execução e as seguintes operações:

- [x] **Menu Interativo Contínuo:** Loop principal (`while True`) com navegação por opções e encerramento seguro (`0`).
- [x] **Gestão de Unidades:** Cadastro de novos postos (`cadastrar_unidade`) e listagem geral (`listar_unidades`).
- [x] **Gestão de Lotes:** Cadastro de lotes de vacinas (`cadastrar_lote`) e consulta de disponibilidade (`consultar_estoque`).
- [x] **Registro de Aplicações:** Baixa automática no estoque disponível (`registrar_aplicacao`) com bloqueio para quantidade inválida (`<= 0`) e trava contra **estoque insuficiente**.
- [x] **Relatórios Parciais:** Cálculo de cobertura vacinal por unidade (`relatorio_unidades`) e panorama geral de público e aplicações (`relatorio`).

---

## 🚀 Roadmap de Melhorias e Requisitos da Entrega

Para atender 100% aos requisitos obrigatórios da avaliação e aprimorar a consistência dos dados, as seguintes implementações estão planejadas:

### 1. Ajustes de Consistência e Validação
- [ ] **Geração segura de IDs nos lotes:** Substituir `len(lotes) + 1` por incremento baseado no maior ID existente (`max(..., default=0) + 1`), evitando duplicidade.
- [ ] **Bloqueio de entradas inválidas:** Impedir cadastro de lotes com quantidade `<= 0`, unidades com `publico_alvo < 0` e campos de texto vazios (aplicando `.strip()`).
- [ ] **Tratamento explícito para público-alvo zero:** Adicionar bloco `else` na função `relatorio_unidades()` exibindo aviso claro (*"Cobertura indisponível: público-alvo zero"*) em vez de omitir o dado silenciosamente.

### 2. Novas Funcionalidades Obrigatórias
- [ ] **Carga inicial de 12 registros:** Popular `unidades` e `lotes` na inicialização do script, incluindo cenários de estoque zerado/baixo e público-alvo igual a zero para testes imediatos.
- [ ] **Busca por identificador (`buscar_por_id`):** Consultar detalhes de uma unidade ou lote específico a partir do seu `id`.
- [ ] **Atualização de registros (`editar_registro`):** Permitir editar informações cadastradas (público-alvo, quantidade ou validade) preservando valores não negativos.
- [ ] **Listagem de doses críticas (`listar_criticos`):** Filtrar e alertar unidades/lotes com estoque baixo ou zerado (ex.: `quantidade_disponivel <= 50`).
- [ ] **Relatório consolidado completo (`relatorio`):** Exibir os **3 indicadores gerais** atualizados dinamicamente (total de doses em estoque, total de doses aplicadas e cobertura percentual média da rede).

### 3. Documentação de Testes (Notebook)
- [ ] Executar e registrar os **8 testes obrigatórios** (entrada, saída esperada e saída observada), cobrindo o fluxo normal e os dois casos-limite (*estoque insuficiente* e *público-alvo zero*).

---

## 🤝 Divisão de Tarefas

| Integrante | Responsabilidades |
| :--- | :--- |
| **Miguel Gomes** | Carga inicial dos 12 registros, funções de busca (`buscar_por_id`), edição (`editar_registro`) e consolidação dos 3 indicadores no `relatorio()`. |
| **Josué Araujo** | Função de alerta crítico (`listar_criticos`), ajuste explícito do caso-limite `publico_alvo == 0`, revisão das travas de estoque e integração do menu. |
| **Dupla** | Execução do roteiro de demonstração, registro dos 8 testes no notebook e revisão da explicação técnica. |

---

## ▶️ Como Executar Localmente

1. Clone este repositório para a sua máquina:
   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd NOME_DO_REPOSITORIO
   ```
3. Execute o arquivo principal com Python 3:
   ```bash
   python main.py
   ```

---

## 🔮 Evoluções Futuras (Pós-Entrega)
* **Persistência em Arquivo/Banco:** Salvar os dados em `.json` ou **SQLite** para não perder os registros ao encerrar o terminal.
* **Tratamento de Exceções:** Adicionar blocos `try/except ValueError` nos inputs numéricos para evitar que digitação acidental de letras interrompa o programa.
* **Migração para API Web:** Transformar as funções de regra de negócio em endpoints REST utilizando **FastAPI**.
