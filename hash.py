# Hash simples interativo com blocos de 16 bits (2 bytes)

def dividir_em_blocos(texto):
    dados = texto.encode()
    if len(dados) % 2 != 0:
        dados = dados + b"\x00"   # completa com zero se faltar 1 byte
    blocos = []
    for i in range(0, len(dados), 2):
        bloco = dados[i] * 256 + dados[i + 1]   # junta 2 bytes em 16 bits
        blocos.append(bloco)
    return blocos


def girar_direita(valor):
    ultimo_bit = valor & 1                      # pega o bit da direita
    return (valor >> 1) | (ultimo_bit << 15)    # ele volta para a esquerda


def hash_xor(texto):
    h = 0
    for bloco in dividir_em_blocos(texto):
        h = h ^ bloco
    return h


def hash_xor_rotacao(texto):
    h = 0
    for bloco in dividir_em_blocos(texto):
        h = girar_direita(h)
        h = h ^ bloco
    return h


def mostrar(nome, h):
    print(f"  {nome}: {format(h, '04x')}  ({format(h, '016b')})")


print("=== Hash simples (16 bits) ===")
print("Digite um texto para ver o hash. Digite 'sair' para encerrar.\n")

while True:
    texto = input("Texto: ")
    if texto.lower() == "sair":
        break

    print("Blocos de 16 bits:", [format(b, "04x") for b in dividir_em_blocos(texto)])
    mostrar("XOR           ", hash_xor(texto))
    mostrar("XOR com rotacao", hash_xor_rotacao(texto))
    print()

print("Fim.")