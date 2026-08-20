"""
Módulo Avançado: Manipulação de Estruturas Multidimensionais e Associativas.

Este programa soluciona o desafio semanal de persistência em memória:
- Armazena dados cadastrais heterogêneos (Nome, RG, Data de Nascimento).
- Processa um vetor dinâmico de X notas por aluno.
- Manipula uma coleção de faltas mensais (Y períodos) ao longo do ano.

Conceitos Aplicados:
- Dicionários para mapeamento de propriedades e dados cadastrais.
- Vetores (listas simples) para o armazenamento linear de notas.
- Estruturas compostas (Dicionário de vetores) para séries temporais (faltas).
"""

# Inicialização da lista principal que conterá todas as matrizes de dados dos alunos
sistema_escolar = []

# =====================================================================
# ETAPA 1: ESTRUTURAÇÃO DO CADASTRO (Exemplo de entrada de 1 aluno)
# =====================================================================

# Criação do dicionário do Aluno 1 para mapear dados heterogêneos de forma clara
aluno_1 = {
    "nome": "João Silva",
    "rg": "12.345.678-9",
    "nascimento": "15/05/2005",
    
    # Vetor de notas (X notas armazenadas linearmente)
    "notas": [8.5, 7.0, 9.0, 8.0],
    
    # Histórico de faltas (Chave associada ao número de faltas do respectivo mês)
    "faltas_mensais": {
        "Janeiro": 0, "Fevereiro": 2, "Março": 1, "Abril": 0,
        "Maio": 3, "Junho": 0, "Julho": 0, "Agosto": 1,
        "Setembro": 2, "Outubro": 0, "Novembro": 1, "Dezembro": 0
    }
}

# Criação do Aluno 2 para simular o comportamento de múltiplos registros (Y alunos)
aluno_2 = {
    "nome": "Maria Santos",
    "rg": "98.765.432-1",
    "nascimento": "22/10/2006",
    "notas": [9.5, 10.0, 8.5, 9.0],
    "faltas_mensais": {
        "Janeiro": 0, "Fevereiro": 0, "Março": 0, "Abril": 1,
        "Maio": 0, "Junho": 1, "Julho": 0, "Agosto": 0,
        "Setembro": 0, "Outubro": 2, "Novembro": 0, "Dezembro": 0
    }
}

# Aninhamento das estruturas: adicionando os dicionários na lista global
sistema_escolar.append(aluno_1)
sistema_escolar.append(aluno_2)

# =====================================================================
# ETAPA 2: PROCESSAMENTO MULTIDIMENSIONAL EFICIENTE
# =====================================================================
print("--- RELATÓRIO ESCOLAR MULTIDIMENSIONAL ---")

# Laço para percorrer a lista de alunos (Dimensão 1)
for aluno in sistema_escolar:
    print(f"\nAluno: {aluno['nome']} | RG: {aluno['rg']} | Nasc: {aluno['nascimento']}")
    
    # Processamento do vetor de notas (Dimensão 2 - A)
    total_notas = sum(aluno["notas"])
    quantidade_notas = len(aluno["notas"])
    media_calculada = total_notas / quantidade_notas
    print(f"-> Média das {quantidade_notas} notas: {media_calculada}")
    
    # Processamento do dicionário/matriz de faltas (Dimensão 2 - B)
    # Soma de forma automatizada todos os valores contidos nas chaves de meses
    total_faltas_ano = sum(aluno["faltas_mensais"].values())
    print(f"-> Total de faltas acumuladas no ano: {total_faltas_ano}")
