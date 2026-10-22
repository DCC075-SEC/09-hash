# Hash 

Programa em Python que calcula dois hashes simples de 16 bits para um texto digitado pelo usuário. Feito para a disciplina DCC075 (Segurança em Sistemas de Computação, UFJF), com base nas "Duas funções de hash simples" vistas em aula.


## Como executar

Requisito: Python 3.

```
python3 hash_interativo.py
```

Digite um texto e pressione Enter para ver os hashes. Digite `sair` para encerrar.

## Como funciona

1. O texto é convertido em bytes.
2. Se o número de bytes for ímpar, é acrescentado um byte `0` no final.
3. Os bytes são agrupados em blocos de 16 bits (2 bytes).
4. O hash começa em `0` e cada bloco é processado em ordem.

Os dois algoritmos diferem só no passo 4:

| Algoritmo | O que faz com cada bloco |
|---|---|
| **XOR** | `h = h XOR bloco` |
| **XOR com rotação** | gira `h` 1 bit à direita e depois faz `h = h XOR bloco` |

A rotação à direita move o último bit para a primeira posição. Por exemplo, `0001` vira `1000`.

## Exemplo de uso

```
Texto: ABCD
Blocos de 16 bits: ['4142', '4344']
  XOR           : 0206  (0000001000000110)
  XOR com rotacao: 63e5  (0110001111100101)

Texto: CDAB
Blocos de 16 bits: ['4344', '4142']
  XOR           : 0206  (0000001000000110)
  XOR com rotacao: 60e0  (0110000011100000)
```



