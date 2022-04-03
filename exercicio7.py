timecasa = str(input("digite o nome do time que ta jogando em casa : "))
timefora = str(input("digie o nome do time que esta jogando fora : "))
golcasa = int(input(f"difite quantos gols que o {timecasa} fez nesse jogo :"))
golfora = int(input(f"digite quanos gols que o {timefora} fez nesse jogo : "))
if golcasa < golfora:
    print(f"o time {timefora} ganhou o jogo")
if golcasa > golfora:
    print(f"o time {timecasa} ganhou o jogo")
else:
    print(f"então deu empate")