def main():
    def palabra_larga(lista):
        p_larga=""
        for p in lista:
            if(len(p) > len(p_larga)):
                p_larga = p
        return p_larga

    palabras=["volumen","ácido desoxirribonucleico","cilindro","moléculas", "calculadora","lapiz"]         
    print(f"La palabra mas larga es: {palabra_larga(palabras)}")
if __name__ == '__main__':
    main()