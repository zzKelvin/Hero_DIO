
print("Insira o nome do heroi: ")
HeroName = input()

print(f"Muito prazer em conhece-lo! {HeroName}")
print("")
print("Insira a quantitade de experiência que você possui! ")

while(True):
    try:
        HeroEXP = int(input())
        break
    except:
        print("Digite somente numeros!")

if HeroEXP <= 1000:
    HeroRank = "Ferro"
elif HeroEXP >= 1001 and HeroEXP <= 2000:
    HeroRank = "Bronze"
elif HeroEXP >= 2001 and HeroEXP <= 5000:
    HeroRank = "Prata"
elif HeroEXP >= 6001 and HeroEXP <= 7000:
    HeroRank = "Ouro"
elif HeroEXP >= 7001 and HeroEXP <= 8000:
    HeroRank = "Platina"
elif HeroEXP >= 8001 and HeroEXP <= 9000:
    HeroRank = "Ascendente"
elif HeroEXP >= 9001 and HeroEXP <= 10000:
    HeroRank = "Imortal"
elif HeroEXP >= 10001:
    HeroRank = "Radiante"
       
print(f"O Herói de nome {HeroName} está no nivel de {HeroRank}!")