def main():
    pa1 = str(input("Ingrese una palabra: "))
    pa2 = str(input("Ingrese otra palabra: "))
    
    if(pa1[-3:] == pa2[-3:]): #[-3:] las ultimas 3 palabras
        print("Si riman.")
    elif(pa1[-2:] == pa2[-2:]): #[-2:] las ultimas 2 palabras
        print("riman un poco.")
    else:
        print("no riman")


if __name__ == '__main__':
    main()