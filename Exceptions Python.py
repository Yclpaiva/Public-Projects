while True:
    try:
        x = int(input('What is "X"? '))


    except ValueError:
        print("Error, the value writed it's not an int of the input ")
    else:
        print(f'"x" exponiated by "x" is {x**x}')