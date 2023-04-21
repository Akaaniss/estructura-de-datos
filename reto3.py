palabra=input("ingrese palabra:")
vocales="aeiou"
conteoVocales=[0,0,0,0,0]

for letra in palabra:
    if letra.lower() in vocales:
        index= vocales.index(letra.lower())
        conteoVocales[index]+= 1

print("la palabra",palabra,"contiene:")
print("la vocal 'A' está presente",conteoVocales[0],"veces")
print("la vocal 'E' está presente",conteoVocales[1],"veces")
print("la vocal 'I' está presente",conteoVocales[2],"veces")
print("la vocal 'O' está presente",conteoVocales[3],"veces")
print("la vocal 'U' está presente",conteoVocales[4],"veces")