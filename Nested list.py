if __name__ == '__main__':
    lista = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append({'name':name,'score':score})
    def get_score(score):
        return score['score']
    gradelist = []
    for student in sorted(lista, key=get_score):
        gradelist.append(student['score'])
        print(f"{student['name']} is in {student['score']}")
    settedlist = set(gradelist)
    second = settedlist[-1]
    for i in range(len(lista)):
        if second in lista[i]['score']:
            print(lista[i]['name'])
    print(settedlist)