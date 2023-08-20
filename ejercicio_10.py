compra={}
total=0
opcion = int(input("""
                    Bienvenido al supermercado Walmart
                   ¿Que operacion desea realizar?
                    1) Comprar
                    2) Salir """))
while (opcion != 2):
    producto = str(input("Seleccione un producto: "))
    compra[producto] = int(input(f"Ingresar el valor del producto {compra[producto]}: "))
    opcion = int(input("1) Continuar comprando \n 2) Salir"))

print("Lista de compras")
for llave in compra:
    print(f"{llave}   {compra[llave]}")
    print("-------------------")
    total+=compra[llave]
print(f"Total   {total}")
