def main():
    opcion = 0
    print("Bienvenido a la conversión de unidades, seleccione una opcion \n")
    while(opcion != 6):
        opcion=int(input("""¿Que conversión desea realizar?
    1) centímetros -> pulgadas
    2) metros -> kilometros
    3) onzas -> gramos
    4) milla -> kilometro
    5) celcius -> fahrenheit
    6) Salir
        """))
        if(opcion == 1):
            valor = float(input("Ingrese valor a convertir: "))
            conversion = valor * (1 / 2.54)
            print(f"Su unidad convertida es: {round(conversion, 4)} pulgadas")
        if(opcion == 2):
            valor= float(input("Ingrese valor a convertir: "))
            conversion = valor * (1 / 1000)
            print(f"Su unidad convertida es: {round(conversion, 4)} kilometros")
        if(opcion == 3):
            valor= float(input("Ingrese valor a convertir: "))
            conversion = valor * (28.3495/1)
            print(f"Su unidad convertida es: {round(conversion, 4)} gramos")
        if(opcion == 4):
            valor= float(input("Ingrese valor a convertir: "))
            conversion = valor * (1/0.621371)
            print(f"Su unidad convertida es: {round(conversion, 4)} kilometros")
        if(opcion == 5):
            valor= float(input("Ingrese valor a convertir: "))
            conversion =(1.8 * valor) + 32 
            print(f"Su unidad convertida es: {round(conversion, 4)} fahrenheit")
        print("\n")
    print("Adios que tenga buen día")


if __name__ == '__main__':
    main()    