"""
Módulo de Desafio: Processador de Entradas e Expressões Aritméticas.

Este programa implementa a solução para o desafio semanal de cálculo de média:
1. Recebe um conjunto de valores numéricos fornecidos pelo usuário (Entrada).
2. Processa a soma e a divisão dos dados via operadores aritméticos (Processamento).
3. Exibe o resultado final consolidado na tela do console (Saída).

Regras de sintaxe aplicadas:
- Coerção explícita de tipos com a função construtora float().
- Uso estratégico de parênteses para isolar a precedência da soma sobre a divisão.
"""

# Entrada de dados: Captura as notas e converte o texto do input em decimal (float)
nota_p1 = float(input("Digite a nota da primeira prova: "))
nota_p2 = float(input("Digite a nota da segunda prova: "))
nota_p3 = float(input("Digite a nota da terceira prova: "))

# Definição da constante de partição
quantidade_provas = 3

# Processamento: Aplica a expressão aritmética respeitando a ordem de execução
# Os parênteses garantem que a soma aconteça ANTES da divisão (/), evitando erros de cálculo
media_calculada = (nota_p1 + nota_p2 + nota_p3) / quantidade_provas

# Saída de dados: Gera o resultado esperado e imprime no console para o usuário
print("A média final calculada para o aluno é:", media_calculada)
