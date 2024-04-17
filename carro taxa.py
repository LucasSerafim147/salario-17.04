#porcetagem
veiculo = int(input("insira o ano do carro: "))
valor = float(input("insira o valor do carro: "))
porcetagem1 = 1/100
porcetagem2 = 1.5/100
 #Calculo
taxa = (valor * porcetagem1) + valor
taxa1 = (valor * porcetagem2) + valor 
 #codigo
if veiculo < 1990:
    print(f"A taxa do seu veiculo é: {taxa}")
elif veiculo >= 1990:
   print(f"A taxa do seu veiculo é: {taxa1}" )