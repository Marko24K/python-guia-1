def main():
    palabra = str(input("Ingresa una palabra: "))
    while (palabra.lower() != "salir"):
        print(palabra[::-1])
        palabra=str(input("Si desea continuar ingrese otro nombre, si desea salir escriba salir: "))
    print("Tenga buen día")

if __name__ == '__main__':
    main()