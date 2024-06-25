from enum import Enum
from uuid import uuid4

hand_size = 7

card_values = {
    "Ace" : 11,
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five" : 5,
    "Six" : 6,
    "Seven" : 7,
    "Eight" : 8,
    "Nine" : 9,
    "Ten" : 10,
    "Jack" : 10,
    "Queen" : 10,
    "King" : 10
}

class Suits(Enum):
    Spade = 1
    Diamond = 2
    Club = 3
    Heart = 4

class Faces(Enum):
    Two = 1
    Three = 2
    Four  = 3
    Five = 4
    Six = 5
    Seven = 6
    Eight = 7
    Nine  = 8
    Ten = 9
    Jack = 10
    Queen = 11
    King  = 12
    Ace = 13

class HandTypes(Enum):
    High_Card = 1
    Pair = 2
    Two_Pair = 3
    Three_Of_A_Kind = 4
    Straight = 5
    Flush = 6
    Full_House = 7
    Four_of_a_Kind = 8
    Straight_Flush = 9
    Five_of_a_Kind = 10
    Flush_House = 12
    Five_Flush = 13


class Card:
    def __init__(self, value, face, suit, enhancement, edition, seal):
        self.id = uuid4().hex
        self.value = value
        self.face = face
        self.suit = suit
        self.enhancement = enhancement
        self.edition = edition
        self.seal = seal

    def __str__(self):
        return f'{self.face} of {self.suit}'
    
    def add_effect(self, effect):
        self.enhancement = effect

    def is_gold(self):
        if self.enhancement == 'gold':
            return True
        return False
    
    def is_steel(self):
        if self.enhancement == 'steel':
            return True
        return False
    
    def is_bonus(self):
        if self.enhancement == 'bonus':
            return True
        return False
    
    def is_mult(self):
        if self.enhancement == 'mult':
            return True
        return False
    
    def is_lucky(self):
        if self.enhancement == 'lucky':
            return True
        return False
    
    def is_wild(self):
        if self.enhancement == 'wild':
            return True
        return False

    def is_stone(self):
        if self.enhancement == 'stone':
            return True
        return False
    
    def is_glass(self):
        if self.enhancement == 'glass':
            return True
        return False
            

class Hand:
    def __init__(self, cards: list[Card]):
        self.cards = cards

class PlayedHand:
    def __init__(self, cards: list[Card]):
        self.cards: list[Card] = []
        self.chips = 0
        self.mult = 0
        self.score = self.chips * self.mult

class Deck:
    def __init__(self):
        self.cards = []
        self.length = len(self.cards)
    
    def add_card(self, card):
        self.cards.append(card)

    def delete_card(self, card):
        self.cards.pop(self.cards.index(card.id))

class Voucher:
    pass

class Joker:
    name: str = ''
    effect: str = ''

    def __calculate__(hand) -> Hand:
        pass

    def activate(hand) -> int:
        score: int = Joker.__calculate(hand)
        return score
        

class OGJoker(Joker):
    name = 'Joker'
    effect = 'add 4 mult'

    def __calculate__(self, hand) -> Hand:
        hand.mult += 4

        
planets: list[str] = []
jokers: list[Joker] = [OGJoker()]
vouchers: list[Voucher] = []
deck = Deck()
hand: Hand = Hand([])

for suit in Suits:
    for face in Faces:
        new_card = Card(card_values[face.name], face.name, suit.name, '', '', '')
        deck.add_card(new_card)


for i in range(0,7):
    hand.cards.append(deck.cards.pop(0))

for i in hand.cards:
    print(i)

input('something')

PlayedHand()