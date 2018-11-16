import random
import time
from iterator.iterator import iterador

# blackjack - use as control for run the different's modes
def blackjack(array,CardValue,count,value):
    if value == 0:
        array.remove(CardValue)
        for i in range(1,8):
            blackjackProb(array,CardValue,i)
    elif value == 1:
        blackjackProb(array,0,count)
    elif value == 2:
        for i in range(1,8):
            blackjackProb(array,0,i)
    else:
        array.remove(CardValue)
        blackjackProb(array,CardValue,count)

# blackjackProb - calculates the probability of not passing in blackjack
def blackjackProb(array,CardValue,count):
    start = round(time.time() * 1000)
    wins=0
    plays=0
    a = iterador(len(array),count)
    while a.hasNext():
        hand = a.GetComb()
        result = CardValue
        for i in hand:
            result = result + array[i]
        if result  <= 21:
            wins = wins + 1
        plays = plays + 1

    
    porcentaje =  wins/plays * 100
    print("The probability of not passing in blackjack with a " + str(CardValue)  + 
    " choosing " + str(count) + " cards is of " + str(round(porcentaje, 2))+ 
    "%. TIME: "+ str(round(round(time.time() * 1000) - start)) + "ms")