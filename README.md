# FPAA -  MaxMin Select - Algoritmo de Seleção Simultânea

Este projeto implementa o algoritmo **MaxMin Select** utilizando a técnica de **divisão e conquista** de forma recursiva para encontrar simultaneamente o maior e menor elemento de um array.

## 📋 Descrição

O algoritmo MaxMin Select resolve o problema de encontrar tanto o valor máximo quanto o valor mínimo de um array em uma única passada, utilizando a estratégia de divisão e conquista.

## 🚀 Como Funciona

### Estratégia de Divisão e Conquista

1. **Divisão**: O array é dividido recursivamente pela metade
2. **Conquista**: Os subproblemas são resolvidos recursivamente  
3. **Combinação**: Os resultados são combinados comparando os mínimos e máximos encontrados

### Casos Base

- **Um elemento**: O elemento é tanto o mínimo quanto o máximo
- **Dois elementos**: Uma comparação determina qual é o mínimo e qual é o máximo

## 🔧 Estrutura do Código

### Funções

1. **`maxmin_select(arr, low, high)`**
   - Função principal que implementa o algoritmo recursivo
   - Retorna uma tupla (min, max)

2. **`test_maxmin()`**
   - Executa testes com diferentes arrays
   - Demonstra o funcionamento do algoritmo

## 💻 Como Executar

### Pré-requisitos
- Python 3.x instalado

### Execução
```bash
python main.py
```

## 📝 Exemplo de Uso

```python
# Array de exemplo
arr = [5, 2, 8, 1, 9, 3]

# Encontrar min e max
min_val, max_val = maxmin_select(arr, 0, len(arr) - 1)

print(f"Mínimo: {min_val}")  # Output: Mínimo: 1
print(f"Máximo: {max_val}")  # Output: Máximo: 9
```

## 🎯 Casos de Teste

O programa testa com:
- Arrays de diferentes tamanhos
- Array com um elemento
- Array com dois elementos  
- Arrays com números negativos
- Arrays desordenados

---

**Algoritmo implementado utilizando divisão e conquista recursiva**
Programa desenvolvido em Python que implementa o algoritmo de seleção simultânea do maior e do menor elementos(MaxMin Select) de uma sequência de números, utilizando a abordagem de divisão e conquista. 
