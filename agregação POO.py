#Cria classe Salário
class Salario:
    def __init__(self,base,bonus):
        self.base = base
        self.bonus = bonus
    
    def salario_anual(self):
        return (self.base*12)+self.bonus
    
class Empregado:
    def __init__(self,nome,idade,salario):
        self.nome = nome
        self.idade = idade
        self.salario_agregado = salario
#Recebe o valor de 'self.salario_agregado' que é igual a 'Salario(10000,700)';
#E da classe 'Salario', recebe a o retorno da função 'salario_anual'
    def salario_total(self):
        return self.salario_agregado.salario_anual()
    
#Envia dados para as classes
salarioatribuido = Salario(10000,700)
empregado1 = Empregado('Yuri',46,salarioatribuido)
print(empregado1.salario_total())