'''Dada una cadena de longitud N, compuesta únicamente de signos de agrupación (
"()", "{}", "[]" ),
haga un programa o algoritmo que determine si dicha cadena está estructurada
correctamente, es decir,
que cada carácter de apertura tenga su carácter de cerrado correspondiente.
Ej.
[()()(){[][]}{([]{})}] -> correcto
([(]{)}) -> incorrecto '''


def aceppter(string):
    chars = {
        '{' : '}',
        '(' : ')',
        '[' : ']'
    }
    pila = []
    aceppted = True
    for char in string:
        if char in chars:
            pila.append(chars[char])
        elif len(pila) and char == pila[-1]:
            pila.pop()
        else:
            aceppted = False
            break
    if len(pila):
        aceppted = False
    print(aceppted)    





if __name__=='__main__':
    aceppter('{{{}')