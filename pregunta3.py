'''3. Dado una cadena de texto, encontrar el número de veces que se repite cada
palabra, ejemplo “hello world, big WoRld” deberíamos obtener
hello - 2 veces
world - 1 vez
big - 1 vez
Cosas a tener en cuenta
- Palabras en mayusculas y minusculas cuenta como la misma palabra
- Símbolos no cuentan como palabras “,.()!¡?¿” '''
import re


#Función que elimina los caracteres especiales de la cadena de texto, además, las separa en una lista,...
#... luego, las pone en minúsculas para diferenciar asi las palabras.
def count_words(text):

    text_without_especial_character = re.sub(r"[^a-zA-Z ]","",text) # Borrado de caracteres especiales
    ls_words = text_without_especial_character.lower().split()

    words = {}

    for word in ls_words:
        if word in words:
            words[word] = words[word] + 1
        else:
            words[word] = 1
    for word, valor in words.items():
        print(word,'-',valor,' veces')
    
if __name__=='__main__':
    string = input("Plz string : ")
    #prueba CTRL + C : holA Amigos de AmIGOS, Como COMO ESTAN MIS amigos, ¿ESTan bien?, espero Que SI AMIGOS
    count_words(string)


