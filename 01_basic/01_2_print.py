
producto  = "Laptop"
precio  = 15000.00
descuento = 10
en_oferta = True


print ("Producto" , producto)
print ("Precio" , precio)
print ("Descuento" , descuento)
print ("En oferta", en_oferta)

descuento = precio*(descuento/100)

p_final = precio - descuento

print (f"Precio Neto: ${p_final:,.2f}")