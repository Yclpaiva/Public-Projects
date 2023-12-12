#Conversor de contas
import kivy
import pyperclip
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

#Cria o Box Layout
class FirstLayout(BoxLayout):
#Se chamado, printa o texto que 'Funcionou' no label_1
    def load_text(self):
        self.ids.label_1.text = 'Funcionou'
#Se chamado, limpa o texto que estiver no label_1
    def clear_text(self):
        self.ids.label_1.text = ''
#quando aperta o botão "Button 1", recebe o que está no paste, e converte para o Tipo 2
    def receber_texto_tipo1(self):
        contaslista = pyperclip.paste()
        lista_conta = contaslista.strip().split()
        i = 0
        loopstr = ''
#Faz a conversão do formato
        while i < len(lista_conta):
            contas = ''
            containdividual = ''
            containdividual = str(lista_conta[i])
            senhaconta = str(lista_conta[i+1])
            conta1 = str(containdividual+' '+ senhaconta)
            loopstr = loopstr + conta1 +'\n'
            print (conta1)
            i = i+2
#Envia o resultado de loopstr no copiar, e printa no Label_1
        pyperclip.copy(loopstr)
        self.ids.label_1.text = loopstr

#quando aperta o botão "Button 2", recebe o que está no paste, e converte para o Tipo 1
    def receber_texto_tipo2(self):
        contaslista = pyperclip.paste()
        lista_conta = contaslista.strip().split()
        i = 0
        loopstr = ''
#Faz a conversão do formato
        while i < len(lista_conta):
            contas = ''
            containdividual = ''
            containdividual = str(lista_conta[i]+'\n')
            senhaconta = str(lista_conta[i+1]+'\n\n')
            conta1 = str(containdividual + senhaconta)
            loopstr = loopstr + conta1 
            i += 2
#Envia o resultado de loopstr no copiar, e printa no Label_1
        pyperclip.copy(loopstr)
        self.ids.label_1.text = loopstr

class Conversor(App):
    def build(self):
        return FirstLayout()
    
Conversor().run()




