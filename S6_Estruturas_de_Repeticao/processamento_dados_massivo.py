"""
Módulo de Automação: Processamento Massivo e Loops de Eventos.

Este programa soluciona o desafio semanal demonstrando a aplicação prática de
estruturas de repetição para construir fluxos eficientes e contínuos:
1. Comando for com gerador range() para média massiva (Páginas 4 e 5).
2. Comando while True para simulação de escuta contínua de eventos (Página 7).

Regras de sintaxe aplicadas:
- Otimização de memória RAM via avaliação sob demanda (lazy evaluation).
- Controle de fluxo e saída de laços indeterminados com a instrução break.
- Indentação estrita de 4 espaços para demarcação de escopos internos.
"""

# =====================================================================
# SOLUÇÃO 1: PROCESSAMENTO MASSIVO (1 MILHÃO DE VALORES)
# =====================================================================
print("--- SISTEMA 1: CÁLCULO MASSIVO EM MEMÓRIA OTIMIZADA ---")

soma_acumulada = 0
quantidade_valores = 1000000

# O construtor range() gera um número por vez, entrega ao laço e o descarta.
# Isso impede que o programa consuma megabytes de memória RAM inutilmente.
for valor in range(1, quantidade_valores + 1):
    soma_acumulada = soma_acumulada + valor

# Expressão aritmética final para consolidação da média
media_final = soma_acumulada / quantidade_valores

print("Quantidade de dados processados com sucesso:", quantidade_valores)
print("Soma total acumulada:", soma_acumulada)
print("Média final do milhão de valores:", media_final)

print("\n" + "-" * 40 + "\n")

# =====================================================================
# SOLUÇÃO 2: EXECUÇÃO ADAPTATIVA POR EVENTOS (Event Loop)
# =====================================================================
print("--- SISTEMA 2: MONITORAMENTO DE EVENTOS EM SEGUNDO PLANO ---")

print("Eventos Disponíveis no Painel:")
print("1 - Disparar Rotina de Backup de Dados")
print("2 - Sincronizar Relatório com o Servidor")
print("sair - Desectar sistema e encerrar programa")

# O laço while True mantém o programa ativo por tempo indeterminado (Página 7)
while True:
    # O programa pausa a execução e aguarda a ocorrência de um evento externo
    evento_atual = input("\nAguardando comando do evento: ").lower().strip()
    
    # Estruturas de condição direcionam o comportamento para cada evento detectado
    if evento_atual == "1":
        print("Executando tarefa: [BACKUP] Compactando arquivos de código...")
        
    elif evento_atual == "2":
        print("Executando tarefa: [SINCRONIZAR] Enviando pacotes para nuvem...")
        
    elif evento_atual == "sair":
        print("Evento de encerramento interceptado. Finalizando monitoramento...")
        break  # O break interrompe a repetição e projeta o fluxo para fora do while
        
    else:
        print("Aviso: Evento desconhecido. Nenhuma instrução foi disparada.")

print("\nFluxo contínuo: Todos os laços de repetição foram concluídos com estabilidade.")
