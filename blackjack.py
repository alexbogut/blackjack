
import random
from playsound import playsound

class Deck():
    deck1 = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
    def __init__(self, size=1):
        self.size = size
        self.cards = self.deck1 * self.size
        self.dealercards = []
        self.playercards = []

    def shufflecards(self):
        self.cards = self.deck1 * self.size
        self.dealercards = []
        self.playercards = []
        random.shuffle(self.cards)
        playsound("shuffle.mp3")

    def deal(self):
        playsound("dealing2.mp3")
        playsound("dealing2.mp3")
        self.dealercards.append(self.cards.pop())
        self.playercards.append(self.cards.pop())
        self.dealercards.append(self.cards.pop())
        self.playercards.append(self.cards.pop())
        print(self.playercards)

    def hit(self):
        playsound("dealing1.mp3")
        self.playercards.append(self.cards.pop())
        print(self.playercards)

    def hitdealer(self):
        playsound("dealing1.mp3")
        self.dealercards.append(self.cards.pop())


def checkwinner(obj):
    playercount = bust(obj.playercards)[1]
    while bust(obj.dealercards)[1] < playercount and not bust(obj.dealercards)[0]:
        obj.hitdealer()
        print(obj.dealercards)
    if bust(obj.dealercards)[0]:
        print('DEALER BUSTS, YOU WIN!')
    elif playercount == bust(obj.dealercards)[1]:
        print(obj.dealercards)
        print('PUSH!')
    else:
        print(obj.cards)
        print(obj.dealercards)
        print('DEALER WINS! You Suck!')
    quitGame()
    

def bust(arr):
    sum = 0
    for i in arr:
        if str(i) in 'JQK':
            sum += 10
        elif str(i) == 'A':
            if ((sum + 11) > 21):
                sum += 1
            else:
                sum += 11
        else:
            sum += i
    if sum > 21:
        return [True, sum]
    else:
        return [False, sum]

def quitGame():
    blackJackGame()
        
def blackJackGame():
    while True:
        start = input("New Game?")
        if start == 'yes':
            new = Deck()
            new.shufflecards()
            new.deal()
            if bust(new.playercards)[1] == 21:
                print("BLACKJACK!!!!!!")
                quitGame()
            break
        else:
            print("TRY AGAIN RETARD")
            # playsound("wrong.mp3")


    while not bust(new.playercards)[0]:
        command = input("Hit or Stand?")
        if command == 'hit':
            new.hit()
            if bust(new.playercards)[1] == 21:
                print('21')
                checkwinner()
        elif command == 'stand':
            playsound("dealing1.mp3")
            checkwinner(new)
    print("BUST! Go Home!")
    quitGame()
            

blackJackGame()

    








        





    


    