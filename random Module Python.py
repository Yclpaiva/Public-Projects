import random

choice = random.choice
randint= random.randint
shuffle = random.shuffle


coin = choice(['heads','tails'])
randomnumber = randint(1,100)
cards = ['jack','queen','king']

shuffle(cards)
print(coin)
print(randomnumber)
print(cards[0])
