contador = 0 
somador = 0 
while contador < 10: 
    contador = contador + 1 
    valor = float(input("Digite a nota " +str(contador)+": ")) 
    somador = somador + valor 
print("Média = ", somador/10) 