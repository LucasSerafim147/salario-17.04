#vARIAVEIS
salario = float(input("Qual seu sálario: "))
cargo = str(input("Qual seu cargo: "))
#AUMENTOS
aumentoSalarioGerente = 10/100 * salario + salario
aumentoSalarioEngenheiro = 20/100 * salario + salario
aumentoSalarioTecnico = 30/100 * salario + salario 
salarioRandom = 40/100 * salario + salario
#IF's
if cargo == "Gerente" or cargo == "101":
    print(f"seu salario atual é {salario}: salario atual: {aumentoSalarioGerente}")
elif cargo == "Engenheiro" or cargo == "102" or cargo == "Engenheira":
    print(f"seu salario atual é {salario}: salario atual: {aumentoSalarioEngenheiro}")
elif cargo == "Tecnico" or cargo == "103":
    print(f"seu salario atual é {salario}: salario atual: {aumentoSalarioTecnico}")
else:
    print(f"seu salario atual é {salario}: salario atual: {salarioRandom}")