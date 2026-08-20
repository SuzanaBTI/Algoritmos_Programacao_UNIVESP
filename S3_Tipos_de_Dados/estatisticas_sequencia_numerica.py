"""
Módulo de Estruturas: Armazenamento e Processamento de Grandes Volumes de Dados.

Este programa demonstra como gerenciar uma sequência complexa de 1000 números
utilizando uma única estrutura de lista, combinada com funções nativas
e laços de repetição para realizar cálculos aritméticos automáticos.

Conceitos Aplicados:
- Coleções indexadas mutáveis (Listas).
- Geração de sequências com a função range().
- Funções integradas de agregação (len e sum).
"""

# Armazenamento: Em vez de criar 1000 variáveis, criamos uma única lista.
# A função range(1, 1001) gera os números de 1 até 1000 de forma automática.
sequencia_numeros = list(range(1, 1001))

# Processamento utilizando as funções integradas da biblioteca padrão do Python
# len() calcula a quantidade total de elementos armazenados na lista (Página 4 do slide)
total_elementos = len(sequencia_numeros)

# sum() realiza a soma aritmética de todos os 1000 números em uma única operação
soma_total = sum(sequencia_numeros)

# Expressão aritmética para calcular a média dos 1000 valores
media_valores = soma_total / total_elementos

# Saída de dados: Exibe os resultados consolidados no console do sistema
print("Quantidade de números armazenados:", total_elementos)
print("Soma de todos os 1000 números:", soma_total)
print("Média aritmética da sequência:", media_valores)
