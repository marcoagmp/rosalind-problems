"""
FIB - Rabbits and Recurrence Relations
========================================================================
Code for FIB exercise without using BioPython Package
========================================================================
Problem
A sequence is an ordered collection of objects (usually numbers), which are 
allowed to repeat. Sequences can be finite or infinite. Two examples are the 
finite sequence (π,−2–√,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…). 

We use the notation An to represent the nth term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect 
to the values of previous terms. In the case of Fibonacci's rabbits from the 
introduction, any given month will contain the rabbits that were alive the 
previous month, plus any new offspring. A key observation is that the number of 
offspring in any month is equal to the number of rabbits that were alive two 
months prior. 

As a result, if Fn represents the number of rabbit pairs alive after the nth 
month, then we obtain the Fibonacci sequence having terms Fn that are defined 
by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). 
Although the sequence bears Fibonacci's name, it was known to Indian mathematicians 
over two millennia ago.

When finding the nth term of a sequence defined by a recurrence relation, we can 
simply use the recurrence relation to generate terms for progressively larger 
values of n. This problem introduces us to the computational technique of dynamic 
programming, which successively builds up solutions by using the answers to smaller cases.

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, 
if we begin with 1 pair and in each generation, every pair of reproduction-age 
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Sample Dataset
5 3
Sample Output
19
"""
from utils.files import encontrar_arquivo, extrair_multiplas_linhas_arquivo
from functools import lru_cache

@lru_cache(maxsize=None) 
def usando_cache(n: int):
    if n == 2:
        return 6
    if n == 1:
        return 1

    return funcao(n-1) + 5*funcao(n-2)

# Didática e interativa. O próximo valor guarda o valor do anterior.
# Complexidade de tempo fica O(n).
# Complexidade de espaço fica constante também
def funcao_otimizada(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 6
        
    a, b = 1, 6
    for _ in range(3, n):
        a, b = b, b + 5 * a
        print(b)
        
    return b

# Complexidade de tempo dessa função é exponencial (2^n)
def funcao(n:int):
    if n == 2:
        return 4
    if n == 1:
        return 1

    return funcao(n-1) + 3*funcao(n-2)

if __name__ == "__main__":
    print(funcao_otimizada(32))