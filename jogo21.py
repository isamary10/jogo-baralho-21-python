import random
def embaralhar(deck):
    qtd = random.randint(200, 1000)
    while qtd > 0:
        #pegando dois índices aleatórios
        i = random.randint(0, 51)
        j = random.randint(0, 51)
        #trocando as cartas
        aux = deck[i]
        deck[i] = deck[j]
        deck[j] = aux
        qtd = qtd - 1

def criar_baralho():
    bar = []
    for naipe in ('♦', '♠', '♥', '♣'):
        for valor in range(1, 14):
            c = (valor, naipe)
            bar.append(c)
    return bar

def comprar(deck):
    return deck.pop()

def distribuir(qtd, deck):
    mao = []
    while qtd > 0:
        mao.append(comprar(deck))
        qtd = qtd - 1
    return mao

def soma_pontos(mao):
    soma = 0
    for c in mao:
        if c[0] > 10:
            soma += 10
        else:
            soma += c[0]
    return soma

def formata_mao(mao):
    texto = ''
    for c in mao:
        if c[0] == 1:
            texto += 'A' + c[1] + " "
        elif c[0] == 11:
            texto += 'J' + c[1] + " "
        elif c[0] == 12:
            texto += 'K' + c[1] + " "
        else:
            texto += str(c[0]) + c[1] + " "
    return texto

baralho = criar_baralho()
embaralhar(baralho)

humano = distribuir(2, baralho)
cpu = distribuir(2, baralho)
pontoH = soma_pontos(humano)

print(formata_mao(humano))

print("Pontos: ", pontoH)

resp = input("Quer mais cartas (s/n)? ")
while resp == 's' or resp == 'S' and pontoH <= 21:
    c = comprar(baralho)
    humano.append(c)
    pontoH = soma_pontos(humano)
    print(formata_mao(humano))
    print("Pontos: ", pontoH)

    if pontoH <= 21:
        resp = input("Quer mais cartas (s/n)? ")

while soma_pontos(cpu) < 17:
    cpu.append(comprar(baralho))

pontoH = soma_pontos(humano)
pontoC = soma_pontos(cpu)

if pontoH > 21:
    print("O vencedor  o computador!")
elif pontoH <= 21 and pontoC > 21:
    print("Parabéns! Você venceu!")
elif pontoH <= pontoC:
    print("O vencedor é o computador!")
else:
    print("Parabéns, você venceu!")
print("Computador: ", cpu)
print("Pontos: ", pontoC)
