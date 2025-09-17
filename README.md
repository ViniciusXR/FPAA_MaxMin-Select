# FPAA_MaxMin-Select
Programa desenvolvido em Python que implementa o algoritmo de seleção simultânea do maior e do menor elementos (MaxMin Select) de uma sequência de números, utilizando a abordagem de divisão e conquista.

## Autor: Vinicius Xavier Ramalho

## Índice

- [Implementação do Algoritmo MaxMin Select em Python](#implementação-do-algoritmo-maxmin-select-em-python)
- [O que é o Algoritmo MaxMin Select](#o-que-é-o-algoritmo-maxmin-select)
- [Descrição do Projeto](#descrição-do-projeto)
  - [Implementação Linha por Linha](#implementação-linha-por-linha)
- [Como Executar o Projeto](#como-executar-o-projeto)
  - [Pré-requisitos](#pré-requisitos)
  - [Passo 1: Preparar o Ambiente](#passo-1-preparar-o-ambiente)
  - [Passo 2: Executar o Programa](#passo-2-executar-o-programa)
  - [Exemplo de Execução](#exemplo-de-execução)
- [Relatório Técnico](#relatório-técnico)
  - [Análise Detalhada do Número de Comparações](#análise-detalhada-do-número-de-comparações)
  - [Análise da Complexidade Assintótica pelo Teorema Mestre](#análise-da-complexidade-assintótica-pelo-teorema-mestre)
  - [Análise da Complexidade Ciclomática](#análise-da-complexidade-ciclomática)
  - [Análise da Complexidade Assintótica](#análise-da-complexidade-assintótica)
  - [Análise de Performance Prática](#análise-de-performance-prática)
- [Versão do Python](#versão-do-python)
- [Conclusão](#conclusão)
- [Referências](#referências)
- [Licença](#licença)

# Implementação do Algoritmo MaxMin Select em Python

O **Algoritmo MaxMin Select** é um método eficiente para encontrar simultaneamente o maior e o menor elemento de um array, desenvolvido utilizando a estratégia "divide e conquista". Este algoritmo reduz o número de comparações necessárias em relação à abordagem iterativa tradicional, realizando aproximadamente 3n/2 - 2 comparações para n elementos.

## O que é o Algoritmo MaxMin Select

O algoritmo MaxMin Select é baseado na estratégia de dividir o problema em subproblemas menores, resolver cada um recursivamente, e combinar os resultados. Ao invés de percorrer o array uma vez para encontrar o mínimo e outra para encontrar o máximo (2n-2 comparações), ou percorrer uma única vez comparando cada elemento com ambos os valores atuais (2(n-1) comparações), este algoritmo otimiza o processo através da divisão e conquista.

## Descrição do Projeto

O algoritmo implementado em `main.py` utiliza a abordagem recursiva do método MaxMin Select para realizar a busca eficiente do maior e menor elemento. A lógica do algoritmo pode ser explicada linha por linha:

### Implementação Linha por Linha

```python
def maxmin_select(arr, low, high):
```
**Linha 2:** Define a função principal que recebe o array e os índices inicial e final do subarray a ser processado.

```python
    # Caso base 1: apenas um elemento
    if low == high:
        return arr[low], arr[low]
```
**Linha 4-5:** Define o primeiro caso base da recursão. Quando há apenas um elemento, ele é tanto o mínimo quanto o máximo. Nenhuma comparação é necessária.

```python
    # Caso base 2: dois elementos
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
```
**Linha 7-11:** Define o segundo caso base para dois elementos. Uma única comparação determina qual é o menor e qual é o maior elemento.

```python
    # Caso geral: dividir o array
    mid = (low + high) // 2
```
**Linha 14:** Calcula o ponto médio para dividir o array em duas partes aproximadamente iguais.

```python
    # Conquista: resolver recursivamente os subproblemas
    min1, max1 = maxmin_select(arr, low, mid)
    min2, max2 = maxmin_select(arr, mid + 1, high)
```
**Linha 16-17:** Realiza duas chamadas recursivas para resolver os subproblemas da primeira e segunda metade do array.

```python
    # Combinar os resultados
    overall_min = min(min1, min2)
    overall_max = max(max1, max2)
    
    return overall_min, overall_max
```
**Linha 20-23:** Combina os resultados dos subproblemas através de duas comparações: uma para determinar o mínimo geral e outra para o máximo geral.

```python
if __name__ == "__main__":
    test_maxmin()
```
**Linha 25-26:** Código principal que executa os testes do algoritmo.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.13.7 ou superior instalado no sistema
- Terminal ou prompt de comando

### Passo 1: Preparar o Ambiente

1. Navegue até o diretório do projeto:

2. (Opcional) Criar um ambiente virtual:
```bash
python -m venv .venv
```

3. (Opcional) Ativar o ambiente virtual:
   - No Windows:
   ```bash
   .venv\Scripts\activate
   ```
   - No macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

### Passo 2: Executar o Programa

Execute o arquivo principal:
```bash
python main.py
```

### Exemplo de Execução

```
=== Teste do Algoritmo MaxMin Select ===

Array 1: [5, 2, 8, 1, 9, 3]
Mínimo: 1, Máximo: 9

Array 2: [10]
Mínimo: 10, Máximo: 10

Array 3: [3, 7]
Mínimo: 3, Máximo: 7

Array 4: [9, 4, 2, 1, 8, 5, 6, 3, 7]
Mínimo: 1, Máximo: 9

Array 5: [-5, -2, -8, -1, -9, -3]
Mínimo: -9, Máximo: -1
```

## Relatório Técnico

### Análise Detalhada do Número de Comparações

O algoritmo MaxMin Select realiza comparações em diferentes etapas, sendo importante analisar cada uma:

#### Casos Base:
- **n = 1**: 0 comparações (elemento único é min e max)
- **n = 2**: 1 comparação (para determinar qual é maior e menor)

#### Caso Geral (n > 2):
Para um array de tamanho n > 2, o algoritmo:

1. **Divisão**: Divide o array em duas partes de tamanho aproximadamente n/2
2. **Conquista**: Resolve recursivamente dois subproblemas de tamanho n/2
3. **Combinação**: Realiza 2 comparações para combinar os resultados:
   - 1 comparação entre min1 e min2
   - 1 comparação entre max1 e max2

#### Recorrência para o Número de Comparações:

**T(n) = T(⌊n/2⌋) + T(⌈n/2⌉) + 2** para n > 2  
**T(1) = 0**  
**T(2) = 1**

#### Resolução da Recorrência:

Para simplificar, assumindo n = 2^k, temos:  
**T(n) = 2T(n/2) + 2**

Expandindo a recorrência:
- T(n) = 2T(n/2) + 2
- T(n) = 2[2T(n/4) + 2] + 2 = 4T(n/4) + 6
- T(n) = 4[2T(n/8) + 2] + 6 = 8T(n/8) + 14
- ...
- T(n) = 2^k × T(1) + 2(2^k - 1) = 0 + 2n - 2 = 2n - 2

Porém, esta análise não considera que os casos base para n=1 e n=2 têm comportamentos diferentes. A análise mais precisa resulta em:

**T(n) = 3⌊n/2⌋ + T(n mod 2) - 2**

Para n par: **T(n) = 3n/2 - 2**  
Para n ímpar: **T(n) = 3(n-1)/2**

#### Demonstração Prática:

| Tamanho (n) | Comparações MaxMin | Comparações Iterativo | Economia |
|-------------|-------------------|----------------------|----------|
| 1           | 0                 | 0                    | -        |
| 2           | 1                 | 1                    | 0%       |
| 3           | 3                 | 4                    | 25%      |
| 4           | 4                 | 6                    | 33%      |
| 6           | 7                 | 10                   | 30%      |
| 8           | 10                | 14                   | 29%      |
| 16          | 22                | 30                   | 27%      |

### Análise da Complexidade Assintótica pelo Teorema Mestre

Considerando a recorrência do MaxMin Select:  
**T(n) = 2T(n/2) + O(1)**

#### Aplicação do Teorema Mestre:

**1. Identificação dos valores na fórmula T(n) = a⋅T(n/b) + f(n):**
- **a = 2** (número de subproblemas)
- **b = 2** (fator de divisão do tamanho)
- **f(n) = O(1)** (custo para dividir e combinar)

**2. Cálculo de log_b(a):**
- **p = log_b(a) = log_2(2) = 1**

**3. Determinação do caso do Teorema Mestre:**

Comparando f(n) = O(1) com n^p = n^1 = n:
- f(n) = O(1) = O(n^0)
- n^p = n^1

Como f(n) = O(n^(p-ε)) onde ε = 1 > 0, temos:
**Caso 1 do Teorema Mestre**: f(n) = O(n^(log_b(a)-ε)) para algum ε > 0

**4. Solução assintótica:**

Pelo Caso 1 do Teorema Mestre:
**T(n) = Θ(n^(log_b(a))) = Θ(n^1) = Θ(n)**

Portanto, a **complexidade temporal é O(n)**.

### Análise da Complexidade Ciclomática

#### Grafo de Fluxo de Controle

O grafo de fluxo da função `maxmin_select(arr, low, high)` pode ser representado pelos seguintes nós e arestas:

**Nós:**
1. **N1**: Início da função
2. **N2**: Verificação do caso base `if low == high`
3. **N3**: Retorno para um elemento
4. **N4**: Verificação do caso base `if high == low + 1`
5. **N5**: Comparação `if arr[low] < arr[high]`
6. **N6**: Retorno `(arr[low], arr[high])`
7. **N7**: Retorno `(arr[high], arr[low])`
8. **N8**: Cálculo do ponto médio e divisão
9. **N9**: Chamadas recursivas
10. **N10**: Combinação dos resultados e retorno
11. **N11**: Fim da função

**Arestas:**
1. N1 → N2: Início para primeira verificação
2. N2 → N3: Se low == high (true)
3. N2 → N4: Se low != high (false)
4. N3 → N11: Retorno do caso base 1
5. N4 → N5: Se high == low + 1 (true)
6. N4 → N8: Se high != low + 1 (false)
7. N5 → N6: Se arr[low] < arr[high] (true)
8. N5 → N7: Se arr[low] >= arr[high] (false)
9. N6 → N11: Retorno do caso base 2a
10. N7 → N11: Retorno do caso base 2b
11. N8 → N9: Cálculo do meio para chamadas recursivas
12. N9 → N10: Chamadas recursivas para combinação
13. N10 → N11: Combinação para fim

#### Cálculo da Complexidade Ciclomática

Usando a fórmula **M = E - N + 2P**, onde:
- **E** = 13 (número de arestas)
- **N** = 11 (número de nós)
- **P** = 1 (número de componentes conexos)

**M = 13 - 11 + 2(1) = 4**

A complexidade ciclomática da função `maxmin_select` é **4**, indicando que existem 4 caminhos lineares independentes no código:
1. Caminho para um elemento (low == high)
2. Caminho para dois elementos com arr[low] < arr[high]
3. Caminho para dois elementos com arr[low] >= arr[high]
4. Caminho recursivo (caso geral)

### Análise da Complexidade Assintótica

#### Complexidade Temporal

**Melhor Caso: O(n)**
- Ocorre para qualquer configuração do array
- O número de comparações é sempre aproximadamente 3n/2 - 2
- A complexidade não varia com a distribuição dos dados

**Caso Médio: O(n)**
- Comportamento linear independente da entrada
- Cada elemento é processado uma única vez
- Divisão balanceada garante eficiência constante

**Pior Caso: O(n)**
- Mesmo no pior cenário, a complexidade permanece linear
- O algoritmo não degrada para O(n²) como alguns algoritmos
- Garantia de performance previsível

#### Complexidade Espacial

**Espaço: O(log n)**
- A profundidade da recursão é proporcional a log₂(n)
- Cada chamada recursiva consome espaço na pilha de execução
- O espaço adicional para variáveis temporárias é O(1) por nível

#### Comparação com Abordagens Alternativas

| Algoritmo | Complexidade Temporal | Comparações | Complexidade Espacial |
|-----------|----------------------|-------------|----------------------|
| Iterativo Simples | O(n) | 2(n-1) | O(1) |
| Duas Passadas | O(n) | 2(n-1) | O(1) |
| MaxMin Select | O(n) | 3n/2 - 2 | O(log n) |

#### Vantagens do Algoritmo MaxMin Select

1. **Eficiência**: Reduz o número de comparações em ~25% comparado à abordagem iterativa
2. **Otimalidade**: Próximo ao limite teórico inferior de comparações
3. **Elegância**: Demonstra poder da técnica divide e conquista
4. **Didático**: Excelente exemplo de otimização algorítmica

#### Limitações

1. **Espaço extra**: Utiliza O(log n) de espaço devido à recursão
2. **Overhead**: Para arrays muito pequenos, pode ser menos eficiente
3. **Implementação**: Mais complexa que a versão iterativa simples

### Análise de Performance Prática

Para arrays grandes, o algoritmo MaxMin Select demonstra vantagens consistentes:

- **100 elementos**: ~25% menos comparações
- **1000 elementos**: ~25% menos comparações  
- **10000 elementos**: ~25% menos comparações
- **Comportamento**: Vantagem percentual constante independente do tamanho

## Versão do Python

Este projeto foi desenvolvido e testado na versão **Python 3.13.7** e é compatível com versões mais recentes.

## Conclusão

O algoritmo MaxMin Select representa uma aplicação elegante da estratégia "divide e conquista" para otimizar um problema aparentemente simples. Embora a diferença de performance possa parecer modesta para arrays pequenos, a redução consistente de ~25% no número de comparações demonstra como técnicas algorítmicas sofisticadas podem melhorar soluções básicas. O algoritmo serve como excelente exemplo educacional e mantém aplicabilidade prática em cenários onde cada comparação tem custo significativo.

## Referências

- [Introduction to Algorithms - Cormen, Leiserson, Rivest, Stein](https://mitpress.mit.edu/books/introduction-algorithms)
- [Algorithm Design - Jon Kleinberg, Éva Tardos](https://www.pearson.com/us/higher-education/program/Kleinberg-Algorithm-Design/PGM319216.html)
- [The Design and Analysis of Computer Algorithms - Aho, Hopcroft, Ullman](https://www.pearson.com/us/higher-education/program/Aho-Design-and-Analysis-of-Computer-Algorithms-The/PGM14901.html)

## Licença

Este projeto está licenciado sob a Licença MIT. 
