salariobase = float(input("Qual o seu salário base?: "))
ajuste = [0.20,0.15,0.10,0.5]
if salariobase < 280:
    salarioajuste = ajuste [0]
elif  salariobase <700:
    salarioajuste = ajuste [1]
elif salariobase <1500:
    salarioajuste = ajuste [2]
elif salariobase:
    salarioajuste = ajuste [3]
valorajuste = salariobase*salarioajuste
print(f"Salário antes do reajuste: R${salariobase}")
print(f"O Valor de ajuste é: {salarioajuste*100}%")
print(f"Seu salário ajustado é: R${valorajuste}")
print(f"Seu salário ajustado é: R${valorajuste+salariobase}")