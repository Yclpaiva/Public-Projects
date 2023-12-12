'''Eduardo Medina Paiva
Arthur Maia de Assis
Vítor Serra Barbosa
Geraldo Dias Álves
Fabiano Ferreira'''


name = {
    'Eduardo':'Medina',
    'Arthur': 'Maia',
    'Vítor': 'Serra',
    'Geraldo':'Dias',
    'Fabiano':'Ferreira',
}

print(name)
print(name['Eduardo'])

for _ in name:
    print(_,name[_])


print('\n\n\n')

namelist = [
    {'name':'Eduardo','surname':'Medina', 'lastname': 'Paiva'},
    {'name':'Arthur','surname':'Maia','lastname':'de Assis'},
    {'name':'Vítor' ,'surname': 'Serra', 'lastname':'Barbosa'},
    {'name':'Geraldo','surname':'Dias' , 'lastname':'Álves'},
    {'name':'Fabiano' ,'surname':None , 'lastname':'Ferreira'}
]

for _ in range(len(namelist)):
    print(namelist[_]['name'])