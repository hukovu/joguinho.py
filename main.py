import os

player = {"nome": "Python", "x": 0, "y": 0}

def andar(direcao): # dando a função de movimentação
    if direcao == "d":
        player['x'] += 1
    elif direcao == "a":
        player['x'] -= 1
    elif direcao =="w":
        player ['y'] -= 1
    elif direcao == "s":
        player ['y'] += 1

while True: #impondo as condições das movimentações usando do loop
    os.system('clear')

    print("--------------------")
    for y in range (5):
        print("\n")
        for x in range (10):
            if player ['x'] == x and player['y'] == y:
                print ("🤺", end="")
            else:
                print("🟩", end="")
    print("--------------------")

    direcao = input("Próxima direção (w, a, s, d): ")
    andar(direcao)
