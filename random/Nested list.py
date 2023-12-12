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
     #   print(f"{student['name']} is in {student['score']}")
    settedlist = set(gradelist)
    #print(settedlist)
    second = list(settedlist)[1]
    result = []
    for i in range(len(lista)):
        if second == lista[i]['score']:
            result.append(lista[i]['name'])
    for i in sorted(result):
        print(i)