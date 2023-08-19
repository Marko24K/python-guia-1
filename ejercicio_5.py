def main():
    palabra = str(input("Ingresa una palabra: "))
    letra = str(input("¿Que letra desea saber cuantas veces se repite?: "))
    c=0
    for letras in palabra:
        if(letras == letra):
            c+=1
    print(f"Su letra {letra} en la palabra {palabra} se repite {c} veces")
    

if __name__ == "__main__":
    main()