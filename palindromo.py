userinput = input('')
reveresed = userinput.strip()[::-1]
if reveresed == userinput:
    print('é um palindromo')
else:
    print('não é um palindromo')