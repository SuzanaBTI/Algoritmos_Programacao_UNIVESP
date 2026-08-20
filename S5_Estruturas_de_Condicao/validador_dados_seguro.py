"""
Módulo de Controle: Estruturas de Condição e Tolerância a Falhas.

Este programa soluciona o desafio unificando duas frentes de proteção:
1. try/except para interceptar e tratar erros operacionais (Divisão por Zero).
2. if/else para validar regras de negócio e desviar caminhos (Idade Negativa).

Regras de sintaxe aplicadas:
- Uso do bloco de captura de exceções específicas (ZeroDivisionError).
- Desvios condicionais de fluxo baseados em validações lógicas iniciais.
- Indentação estrita de 4 espaços para demarcação de escopo.
"""

# =====================================================================
# SOLUÇÃO 1: BLINDAGEM CONTRA EXCEÇÃO DE MÁQUINA (try/except)
# =====================================================================
print("--- SISTEMA 1: PROCESSAMENTO DE DIVISÃO PROTEGIDA ---")

try:
    # O bloco try monitora a execução para interceptar falhas críticas
    numerador = float(input("Digite o numerador da operação: "))
    denominador = float(input("Digite o denominador da operação: "))
    
    # Se o denominador for zero, o Python disparará um ZeroDivisionError aqui
    resultado = numerador / denominador
    print("O resultado do processamento aritmético é:", resultado)

except ZeroDivisionError:
    # O except captura a falha antes que ela interrompa o programa
    print("Exceção Contida: Não é possível realizar divisões por zero!")

print("\n" + "-" * 40 + "\n")

# =====================================================================
# SOLUÇÃO 2: DESVIO DE INSTRUÇÃO POR CONDIÇÃO INICIAL (if/else)
# =====================================================================
print("--- SISTEMA 2: VALIDAÇÃO DE DOMÍNIO E CÁLCULO DE PESO ---")

altura = float(input("Digite a altura da pessoa em metros (ex: 1.75): "))
idade = int(input("Digite a idade da pessoa em anos: "))
sexo = input("Digite o sexo biológico (M ou F): ").upper()

# Possibilitando diferentes instruções dependendo da condição inicial:
# Se a idade não possuir a característica desejada, o fluxo muda de caminho
if idade <= 0:
    print("Caminho de Erro: A idade informada é inválida (negativa ou nula)!")
else:
    print("Caminho Sucesso: Idade validada. Processando equações do peso ideal...")
    
    # Condicional aninhada para segmentar o cálculo de acordo com o sexo
    if sexo == "M":
        peso_ideal = (72.7 * altura) - 58
    else:
        peso_ideal = (62.1 * altura) - 44.7
        
    print(f"Para {idade} anos e sexo {sexo}, o peso ideal é:", peso_ideal)

print("\nFluxo contínuo: Script finalizado com total estabilidade de execução.")
