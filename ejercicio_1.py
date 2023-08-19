import random
def main():
    resultado = random.randint(1, 100) 
    k=1 #contador de intentos
    num_elegido = int(input("Seleccione al azar un número del 1 al 100: "))
    while(num_elegido != resultado):
        if(num_elegido > resultado):
            print(f"El {num_elegido} es mayor al numero elegido.")
        elif(num_elegido < resultado):
            print(f"El {num_elegido} es menor al numero elegido.")
        num_elegido = int(input("Siga participando, vuelva a seleccionar otro número del 1 al 100: "))
        k+=1
    print(f"Le acertaste al número {resultado} y en base a {k} intentos.")


if __name__ == '__main__':
    main()