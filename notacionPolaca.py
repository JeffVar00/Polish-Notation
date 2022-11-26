
#Integrantes
#Guirsley Rodriguez Batodano
#Jose Rodriguez Martinez
#Jeff Vargas Barrantes

def notacionPolaca(expresion):
    invalido = False
    pila = []

    for i in reversed(expresion):
        if i == " ":
            pass
        elif i.isnumeric() is False:
            if len(pila) <= 1:
                invalido = True
                break
            elif i == "+":
                aux1 = pila.pop()
                aux2 = pila.pop()
                pila.append(aux1 + aux2)
            elif i == "-":
                aux1 = pila.pop()
                aux2 = pila.pop()
                pila.append(aux1 - aux2)
            elif i == "*":
                aux1 = pila.pop()
                aux2 = pila.pop()
                pila.append(aux1 * aux2)
            elif i == "/":
                aux1 = pila.pop()
                aux2 = pila.pop()
                pila.append(aux1 / aux2)
            else:
                invalido = True
                break
        else:
            pila.append(int(i))

    if len(pila) >= 2:
        invalido = True

    if invalido is True:
        return "Expresion invalida"
    else:
        return pila.pop()

def notacionPolacaInversa(expresion):
    invalido = False
    pila = []

    for i in expresion:
        if i == " ":
            pass
        elif i.isnumeric() is False:
            if len(pila) <= 1:
                invalido = True
                break
            elif i == "+":
                aux2 = pila.pop()
                aux1 = pila.pop()
                pila.append(aux1 + aux2)
            elif i == "-":
                aux2 = pila.pop()
                aux1 = pila.pop()
                pila.append(aux1 - aux2)
            elif i == "*":
                aux2 = pila.pop()
                aux1 = pila.pop()
                pila.append(aux1 * aux2)
            elif i == "/":
                aux2 = pila.pop()
                aux1 = pila.pop()
                pila.append(aux1 / aux2)
            else:
                invalido = True
                break
        else:
            pila.append(int(i))

    if len(pila) >= 2:
        invalido = True

    if invalido is True:
        return "Expresion invalida"
    else:
        return pila.pop()

def main():
    a = True
    while a is True:
        expresion = input("Ingrese la expresion: ")
        print("""1- Aplicar notacio polaca
2- Aplicar notacion polaca inversa""")
        opcion = input("Opcion: ")
        if opcion == "1":
            print(notacionPolaca(expresion))
        elif opcion == "2":
            print(notacionPolacaInversa(expresion))
        else:
            print("Opcion invalida")

if __name__ == '__main__':
    main()