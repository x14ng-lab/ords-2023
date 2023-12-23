class Card():
    '''
    A playing card from a card deck.
    '''
    # pass

    def __init__(self, provided_value, provided_suit):
        '''
        Initialise a card with a particular value and suit.
        '''
        self.value = provided_value
        self.suit = provided_suit

    def __str__(self):
        '''
        String representation of the card.
        '''
        if self.value == 1:
            display_value = 'ace'
        elif self.value == 11:
            display_value = 'jack'
        elif self.value == 12:
            display_value = 'queen'
        elif self.value == 13:
            display_value = 'king'
        else:
            display_value = self.value

        # With a dictionary
        # value_dict = {1: 'ace', 11: 'jack', 12: 'queen', 13: 'king'}
        # Complete the dictionary with the numbers 2 to 10
        #... 

        return f'{display_value} of {self.suit}'
    
    def __eq__(self, other):
        '''
        Decide how two cards are equal.
        '''
        return self.value == other.value and self.suit == other.suit

        # if self.value == other.value and self.suit == other.suit:
        #     return True
        # else:
        #     return False

    def __gt__(self, other):
        '''
        Decide how one card is greater than another card.
        Greater value wins, but hearts win over everything else.
        '''
        # If suits are the same, compare values
        if self.suit == other.suit:
            return self.value > other.value
        
        # If suits are different but no hearts, compare values
        elif self.suit != 'hearts' and other.suit != 'hearts':
            return self.value > other.value
        
        # Otherwise, heart always wins
        else:
            return self.suit == 'hearts'
            # if self.suit == 'hearts':
            #     return True
            # else:
            #     return False

# Exercise: change the __gt__ method to have Ace have greater value than
# every other card.
# print(Card(1, 'spades') > Card(13, 'spades')) # should be True

my_card = Card(13, 'spades')
my_next_card = Card(13, 'spades')
my_other_card = Card(3, 'clubs')
my_further_card = Card(1, 'diamonds')
heart_card = Card(9, 'hearts')
heart_card_2 = Card(10, 'hearts')
# print(my_card.value) # should print 1
# print(my_card.suit) # should print "spades"
# print(my_card, my_other_card, my_further_card, sep='\n')

# print(my_card == my_other_card)
# print(my_card == my_next_card)

# print(my_card > my_other_card)
# print(my_further_card > my_other_card)
# print(heart_card > my_other_card)
# print(heart_card > heart_card_2)
print(heart_card_2 > heart_card)
print(heart_card < heart_card_2)


# import numpy as np
# A = np.zeros((4, 3))
# print(A.shape)