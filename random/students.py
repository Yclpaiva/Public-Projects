import csv

students = []
studentscsv = '/home/yuri/Área de Trabalho/projetos/estudos/students.csv'
with open(studentscsv) as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({'name':row['name'], 'house':row['house']})

def get_name(student):
    return student['name']

def get_house(student):
    return student['house']

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

print('\n')

for student in sorted(students, key=lambda student:student['house']):
    print(f"{student['name']} is in {student['house']}")

print('\n')

name = input("What's your name? ")
house = input("Where's your house? ")

with open(studentscsv, "a") as file:
#csv.DictWriter().writerow()
    writer = csv.DictWriter(file,fieldnames=['name','house'])
    writer.writerow({'name':name,"house":house})