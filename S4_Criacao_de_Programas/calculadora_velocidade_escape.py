"""
Módulo de Integração Definitivo: Algoritmos e Engenharia de Computação.

Este programa materializa o desafio de consolidação da disciplina:
1. Aplica o conceito de Algoritmo (sequência finita e lógica de passos).
2. Utiliza variáveis tipadas para armazenar dados complexos de entrada.
3. Importa funções analíticas específicas da biblioteca padrão (math).
4. Processa expressões aritméticas avançadas para gerar uma saída precisa.

Cenário Prático: Cálculo da velocidade de escape de um corpo celeste e
sua eficiência em relação a um fator de amortecimento atmosférico.
"""

# Importação da Biblioteca Padrão Matemática (Conceito da Semana)
import math

# =====================================================================
# ETAPA 1: ALGORITMO - ENTRADA DE DADOS
# =====================================================================
# Captura de dados textuais convertidos explicitamente para decimais (float)
massa_planeta = float(input("Digite a massa do corpo celeste em kg (ex para Terra: 5.97e24): "))
raio_planeta = float(input("Digite o raio do corpo celeste em metros (ex para Terra: 6.37e6): "))
fator_amortecimento = float(input("Digite o fator de amortecimento atmosférico (ex: 1.2): "))

# Definição de Constantes Físicas com variáveis de nomenclatura limpa
CONSTANTE_GRAVITACIONAL = 6.674e-11

# =====================================================================
# ETAPA 2: ALGORITMO - PROCESSAMENTO DAS EXPRESSÕES
# =====================================================================
# Passo 1: Calcula a velocidade de escape pura usando a função de raiz quadrada math.sqrt()
# Fórmula física: v = raiz_quadrada( (2 * G * M) / R )
velocidade_escape_pura = math.sqrt((2 * CONSTANTE_GRAVITACIONAL * massa_planeta) / raio_planeta)

# Passo 2: Aplica o fator de amortecimento atmosférico via expressão aritmética
# O cálculo simula a perda de eficiência devido à resistência do ar
velocidade_efetiva = velocidade_escape_pura * (1 / fator_amortecimento)

# =====================================================================
# ETAPA 3: ALGORITMO - GERAÇÃO DA SAÍDA ESPERADA
# =====================================================================
# Exibição dos resultados processados de forma limpa e estruturada no console
print("Velocidade de escape teórica (m/s):", velocidade_escape_pura)
print("Velocidade efetiva corrigida pelo amortecimento (m/s):", velocidade_efetiva)
