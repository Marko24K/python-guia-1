compra={}
total=0
opcion = int(input("1) comprar \n 2) salir \n"))
while (opcion != 2):
    producto = str(input("seleccione un producto: "))
    compra[producto] = int(input("el valor del producto: "))
    opcion = int(input("1) comprar \n 2) salir"))

print("Lista de compras")
for llave in compra:
    print(f"{llave}   {compra[llave]}")
    print("-------------------")
    total+=compra[llave]
print(f"Total   {total}")
