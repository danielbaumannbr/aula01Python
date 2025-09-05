nota1=float(input("Informe a 1ª nota: "))
nota2=float(input("Informe a 2ª nota: "))
nota3=float(input("Informe a 3ª nota: "))
media=(nota1+nota2+nota3)/3
print("Sua média é: ",round(media,2))
if media>7:
    print("\nAprovado.")