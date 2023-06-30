import funciones as fn

while True:
    print("""Menú opciones
    1. Grabar Mascota
    2. Buscar Mascota
    3. Retirar Mascota
    4. Salir""")
    while True:
        try:
            opc=int(input("Ingrese la opción: "))
            if opc in (1,2,3,4):
                break
            else:
                print("Debe elegír una opción indicada")
        except:
            print("Error! debe ser un numero entero")
    if opc==1:
        
    