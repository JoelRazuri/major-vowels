"""
    * Enunciado: Crea un función que reciba un texto y retorne la vocal que más veces se repita.
    * - Ten cuidado con algunos casos especiales.
    * - Si no hay vocales podrá devolver vacío. 
"""


def max_amount_vowel(text: str) -> list :
    
    vowels = ["a", "e", "i", "o", "u"]
    count_vowels = [0, 0, 0, 0, 0]
    max_count = 0
    index = 0

    for letter in text.lower():
        if (letter == "a" or letter == "á"):
            count_vowels[0]+=1
        
        if (letter == "e" or letter == "é"):
            count_vowels[1]+=1
        
        if (letter == "i" or letter == "í"):
            count_vowels[2]+=1
        
        if (letter == "o" or letter == "ó"):
            count_vowels[3]+=1
        
        if (letter == "u" or letter == "ú" or letter == "ü"):
            count_vowels[4]+=1

    for i, count in enumerate(count_vowels):
        if (count > max_count):
            max_count = count
            index = i
    
    if max_count == 0:
        message = f"Texto: '{text}'\nEl texto no tiene vocales.\n"
    else:
        message = f"Texto: '{text}'\nLa vocal que más a aparece es la: '{vowels[index]}', aparece {max_count} veces.\n"

    return message

print(max_amount_vowel("hola como estas? á AU"))
print(max_amount_vowel("kkkkkqrtls"))    