S=0
for contador in range(1,11):
    nota = float(input("Digite a nota "+str(contador)+": "))
    S=S+nota
print("Média = ",S/10)
