def main():
    def area(radio):
        return 3.14 * (radio ** 2)
        
    def volumen(area,altura):
        return area * altura
    
    #Ejemplo con un radio de 3 y una altura de 18
    print(f"Area: {area(3)}")
    print(f"Volumen: {volumen(area(3),18)}")

if __name__ == '__main__':
    main()