import numpy
import os
import time
import msvcrt
array=numpy.zeros((2,10))
lista_ruts_d=[]
lista_nom_d=[]
lista_id_mascota=[]
lista_nom_mascota=[]
lista_pisos=["A","B"]
lista_letras=[]

valor_dia=15000

print("""Menu de opciones
        1.Grabar Mascota:
        2.Buscar Mascota: 
        3.Retirar Mascota:
        4.Salir """)

def validar_opcion():
      while True:
            try:
                  opc=int(input("Ingrese la opción que desea: "))
                  if opc in (1,2,3,4):
                        return opc
                  else:
                        print("Error! Deber ser una opción indicada")
            except:
                  print("Error! debe ser un número entero")


def validar_ruts():
                while True:
                    try:
                        rut=int(input("Ingrese rut sin número verificador: "))
                        if rut >=1000000 and rut<=99999999:
                            return rut
                        else:
                            print("Error! Rut mal ingresado")
                    except:
                        print("Error! Debe ser número entero ")
                    lista_ruts_d.append()
                    
def validar_nom_d():
                while True:
                    nombre_dueno=input("Ingrese su nombre: ")
                    if len(nombre_dueno)>=3 and nombre_dueno.isalpha:
                        return nombre_dueno
                    else:
                        print("Error! Nombre mal ingresado")
                    lista_nom_d.append()

def validar_nom_mascota():
                while True:
                    nomb_mascota=input("Ingrese nombre de la mascota: ")
                    if len(nomb_mascota)>=3 and nomb_mascota.isalpha:
                        return nomb_mascota
                    else:
                        print("Error! nombre de la mascota mal ingresada ")

while True:
                try:
                    cant_dias=int(input("Ingrese cantidad de días que permanecerá su mascota: "))
                    if cant_dias<0:
                        break
                    else:
                        print("Error! debe ser mayor a 0 días")
                except:
                    print("Error! deben ser números enteros")

def validar_pisos():
                while True:
                    try:
                        piso=int(input("Cual piso desea (1-2): "))
                        if piso in lista_pisos:
                            return piso
                        else:
                            print("Error! debe ingresar un piso entre 1 y 2")
                    except:
                        print("Error! debe ser un número entero")
                        lista_pisos.append()

def validar_letra():
                while True:
                    letra=int("Ingrese la habitación que desea (1-10): ")
                    if letra in lista_letras:
                        return letra
                    else:
                        print("Error! Debe elegir una habitación entre 1-10")

while True:
            try:
                rut=int(input("Ingrese rut sin guión: "))
                if rut in lista_ruts_d:
                    break
                else:
                    print("Rut no registrado")
            except:
                print("Error! debe ser nros enteros")
            print("Rut", rut[lista_ruts_d], end=" ")
            print("Nombre Dueño", nombre_dueno[lista_nom_d], end=" ")
            print("Nombre Mascota", nomb_mascota[lista_nom_mascota], end=" ")

while True:
            try:
                cant_dias=int(input("Ingrese la cantidad de días que estuvó: "))
                if cant_dias>=1:
                    valor=cant_dias*valor_dia
                    break
                else:
                    print("Error! no alcanzó a estar un día")
            except:("Error! deben ser números enteros")
print("Su total a pagar es: $", valor)

while True:
      salir=input("Aprete T si desea para salir: ")
      if salir.upper =="T":
            time.sleep(2)
            msvcrt.getch
      else:
            print("Debe ingresar T si desea salir" )
        








