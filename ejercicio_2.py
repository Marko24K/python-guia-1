def main():
    def cm_in(x): #centímetros -> pulgadas
        return x * (1 / 2.54)
    
    def m_km(x): #metros -> kilometros
        return x * (1 / 1000)
    
    def oz_g(x): #onzas -> gramos
        return x * (28.3495/1)
    
    def mi_km(x): #milla -> kilometro
        return x * (1/0.621371)
    
    def c_f(x): #celcius -> fahrenheit
        return (1.8 * x) + 32 
    
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
            print(f"Su unidad convertida es: {round(cm_in(valor), 4)} pulgadas")
        if(opcion == 2):
            valor= float(input("Ingrese valor a convertir: "))
            print(f"Su unidad convertida es: {round(m_km(valor), 4)} kilometros")
        if(opcion == 3):
            valor= float(input("Ingrese valor a convertir: "))
            print(f"Su unidad convertida es: {round(oz_g(valor), 4)} gramos")
        if(opcion == 4):
            valor= float(input("Ingrese valor a convertir: "))
            print(f"Su unidad convertida es: {round(mi_km(valor), 4)} kilometros")
        if(opcion == 5):
            valor= float(input("Ingrese valor a convertir: "))
            print(f"Su unidad convertida es: {round(c_f(valor),4)} fahrenheit")
        print("\n")
    print("Adios que tenga buen día")


if __name__ == '__main__':
    main()    