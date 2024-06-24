from enum import Enum
from uuid import uuid4

class Suit(Enum):
    Spade = 1
    Diamond = 2
    Club = 3
    Heart = 4

class Face(Enum):
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14



class Card:
    def __init__(self, value, face, suit, enhancement, aura, seal):
        self.id = uuid4().hex
        self.value = value
        self.face = face
        self.suit = suit
        self.enhancement = enhancement
        self.aura = aura
        self.seal = seal
    
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
    def __init__(self, cards: list[Card]):
        self.cards = cards
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
jokers: list[Joker] = []
vouchers: list[Voucher] = []