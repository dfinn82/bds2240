#simple implementation of the card game war
import random

class Card():
    def __init__(self,suit,rank):
        #each card object has a suit and a rank
        self.suit = suit
        self.rank = rank
    def __gt__(self,other):
        #If rank is equal compare suit
        if self.rank == other.rank:
            return self.suit > other.suit
        else:
            return self.rank > other.rank
    def __str__(self):
        return str(self.rank) + ":" + str(self.suit)
        
class Deck():
    #suit is a single character to make card comparison easier
    suits = ["c","d","h","s"]
    ranks = list(range(1,14))
    def __init__(self):
        #build a deck, no jokers
        self.deck = []
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        return ' '.join(self.deck)
    def __len__(self):
        return len(self.deck)

class Player():
    def __init__(self,name):
        self.cards = []
        self.points = 0
        self.name = name
    def score(self):
        self.points += 1
    def draw(self):
        #return card and remove it from pile
        return self.cards.pop()
    def addCard(self,card):
        self.cards.append(card)
    def __len__(self):
        return len(self.cards)
    def __str__(self):
        return self.name + ":" + str(self.points)

def war(p1,p2):
    #each player draws a card
    #player with highest rank and suit gets the point
    #assume each player has the same amount of cards
    while len(p1) > 0:
        c1 = p1.draw()
        c2 = p2.draw()
        if c1 > c2:
            p1.score()
        else:
            p2.score()

def deal(deck,p1,p2):
    #Evenly handout cards to each player
    for i in range(0,len(deck),2):
        p1.addCard(deck[i])
        p2.addCard(deck[i+1])

def winner(p1,p2):
    #compare points, print winner
    if p1.points > p2.points:
        print("Winner Player 1")
    elif p2.points > p1.points:
        print("Winner Player 2")
    else:
        print("Tie")

def main():
    deck = Deck()
    random.shuffle(deck.deck)
    p1 = Player("Player1")
    p2 = Player("Player2")
    deal(deck.deck,p1,p2)
    war(p1,p2)
    print(str(p1),str(p2))
    winner(p1,p2)

if __name__ == '__main__':
    main()
