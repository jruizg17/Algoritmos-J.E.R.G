cantidad_productos = int(input("¿Cuántos productos va a comprar? "))

total = 0

for i in range(cantidad_productos):

    print("\nProducto", i + 1)

    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad comprada: "))

    subtotal = precio * cantidad

    print("Subtotal:", subtotal)

    total = total + subtotal


print("\nTotal antes del descuento:", total)

if total > 300000:
    descuento = total * 0.10

elif total >= 150000:
    descuento = total * 0.05

else:
    descuento = 0

total_pagar = total - descuento

print("Descuento aplicado:", descuento)
print("Total a pagar:", total_pagar)