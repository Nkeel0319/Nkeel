#Nummer 3 Get va
#Take a randome card from the deck and list its value
import random
deck = ['3 of hearts','10 of spades','6 of clubs']

def get_value(deck):
    draw_number=random.randint(0,len(deck))
    draw= deck[draw_number]
    number =draw[0:2]
    print(number)
#Number 3 Same value
#Take 2 randome cards from the deck and see if they are the same value 
def same_value(deck):
    number_2 = random.randint(0,len(deck))
    draw1= deck[number_2]
    card1 =draw1[0:2]
            
    number_3  =  random.randrange(0,len(deck))
    draw2 = deck[number_3]
    card2 = draw2[0:2]
    if card1 == card2:
        print("true")
    else:
        print("false")
    print(card1)
    print(card2)
get_value(deck)
same_value(deck)

