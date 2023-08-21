def main():
    def factorial(x):
        i = x
        fact = 1
        while(x > 0):
            fact = fact * x
            x -= 1
        print(f"El valor del factorial {i} es {fact}")
    
    n = int(input("Ingrese un numero para saber su factorial: "))
    factorial(n)

if __name__ == '__main__':
    main()