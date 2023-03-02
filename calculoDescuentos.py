#precio de base de los huevos = 1800
#precio de base de las arepas = 5000
#si alguien compra más de 10 canastas, el precio es de 1000
#si alguien compra más de 10 canastas de huevos y además compra 10 paquetes de arepas, el precio de los huevos es 800 y el de las arepas es 2000
#paso1: preguntar cuantos huevos quiere comprar la persona
cantidadHuevos = int(input("Cuantos huevos desea comprar: "))

#paso2: preguntar si la persona quiere comprar arepas
quiereArepas = input("Usted desea llevar arepas?: ")

#paso3: preguntar cuantas arepas quiere comprar

cantidadArepas = 0
if quiereArepas == "si" or quiereArepas == "sí" or quiereArepas == "SI" or quiereArepas == "Si":
    cantidadArepas = int(input("¿Cuantas arepas desea comprar? "))

#paso4: calcular el total de la compra
if cantidadArepas > 10 and cantidadHuevos > 10:
    precioArepas = 2000
    precioHuevos = 800

elif cantidadHuevos > 10:
    precioHuevos = 1000
    precioArepas = 5000

else:
    precioHuevos = 1800
    precioArepas = 5000

totalCompra = cantidadHuevos * precioHuevos + precioArepas * cantidadArepas
print(f"El total de la compra fue {totalCompra}")

if totalCompra > 50000:
    descuento = totalCompra * 0.1
    totalCompraDescuento = totalCompra - descuento
    print(f"El total del descuento fue {descuento} y el valor total de la compra fue de {totalCompraDescuento}")

elif totalCompra > 50000 and cantidadHuevos > 0 and cantidadArepas > 0:
    descuentoGrande = totalCompra * 0.15
    totalCompraDescuentoGrande = totalCompra - descuentoGrande
    print(f"El total del descuento fue {descuentoGrande} y el valor total de la compra fue {totalCompraDescuentoGrande}")



#Condiciones adicionales que se deben cumplir:
#si el total de la compra es mayor a 50.000, dar un descuento adicional del 10%
#si el total de la compra es mayor a 50.000 y ademas se están comprando huevos y arepas el descuento no es 10% sino que es 15%
#mostrar el total de la compra y el total del descuento

