compra={}
total=0
opcion = int(input("""
                   ¿Que operacion desea realizar? 
                      (para comprar presione 1, para salir presione 2)
                      1) Comprar
                      2) Salir 
                    """))
while (opcion != 2):
    producto = input("Seleccione un producto: ")
    compra[producto] = float(input(f"Ingresar el valor del producto {producto}: "))
    opcion = int(input("1) Continuar comprando\n2) Salir \n"))

print("Lista de compras")
for llave in compra:
    print(f"{llave}  {compra[llave]}")
    print("-------------------")
    total += compra[llave]
print(f"Total: {total}")
