def main():
    def primo(x):
        for i in range (2, x):
            if (x % i == 0):
                return False
        return True

    x = int(input("Ingrese un número: "))
    if primo(x):
        print(f"{x} es primo")
    else:
        print(f"{x} no es primo")

if __name__ == '__main__':
    main()