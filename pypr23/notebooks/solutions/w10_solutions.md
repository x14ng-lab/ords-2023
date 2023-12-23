## Exercise 1

```python
from numpy import arctan2, sqrt, pi

class point:
    '''
    Define a class to describe points in a plane.
    '''
    def magnitude_sq(self):
        '''
        Returns the square of the magnitude of the 
        vector from the origin to a point.
        Input: self (point): point object
        Output: r2 (float): square of the magnitude of the vector
            from the origin to a
        '''
        return self.x**2 + self.y**2
    
    def dist_sq(self, a):
        '''
        Returns the square of the distance of one point 
        from another.
        Input: self (point): point object
               a (point): second point object
        Output: r2 (float): square of the magnitude of the vector
            from self to a
        '''
        return (self.x - a.x)**2 + (self.y - a.y)**2
    
    def angle(self):
        '''
        Returns the angle (in radians) between the positive x-axis
        and the vector between a point and the origin.
        Input: self (point): point object
        Output: theta (float): angle in radians
        '''
        return arctan2(self.y, self.x)
    
    def to_polar(self):
        '''
        Returns the polar coordinates of a point.
        Input: self (point): point object
        Output: r (float): magnitude
                theta (float): angle
        '''
        return sqrt(self.magnitude_sq()), self.angle()

# Create a point
my_point = point()
my_point.x = 2
my_point.y = -2 * sqrt(3)

print(my_point.angle())
print(-pi / 3)

print(my_point.to_polar())
```

---

## Exercise 2

```python
# 1
x = 3
y = 4
loc1 = point(x, y)
loc2 = point(x, y)
print(loc1 == loc2)   # They're 2 different objects in memory!

# Note the difference if we do this instead:
loc2 = loc1
print(loc1 == loc2)   # Now, loc2 is just another name for the *same* object
                      # which was already named loc1
loc2.x = 15
print(loc1)      # and in fact, loc1 is also changed when we change loc2
```

```python
# ---
# 2 and 3
class point:
    '''
    Define a class to describe points in a plane.
    '''
    
    def __init__(self, x=0, y=0):
        '''
        Initialises a point object with attributes x and y
        to represent its x, y coordinates. Uses the origin
        as a default point.
        '''
        self.x = x    # Set attribute .x with value x
        self.y = y    # Set attribute .y with value y
        
    def __str__(self):
        '''
        Returns the string representation of a point object
        as (x, y), with 3 decimal digits for the coordinates.
        '''
        return f'({self.x:.3f}, {self.y:.3f})'
    
    def __mul__(self, a):
        '''
        Define the * operator for multiplying a point by 
        a float.
        '''
        result = point(a * self.x, a * self.y)
        return result
    
    def __add__(self, other):
        '''
        Define the + operator for adding together
        two points.
        '''
        result = point(self.x + other.x, self.y + other.y)
        return result
    
    def __eq__(self, other):
        '''
        Define the == operator for comparing 2 points.
        '''
        return self.x == other.x and self.y == other.y
    
    def __bool__(self):
        '''
        Define what happens when a point is cast to a bool.
        If it's the origin, return False, otherwise True.
        '''
        # One way we can do this, now that we've defined __eq__() and __init__():
        return self != point()
        
        # Another way:
        # return self.x != 0 and self.y != 0
```

---

## Exercise 3

```python
class online_cart(cart):
    '''
    Defines an online cart object.
    '''
    
    def __init__(self, currency='GBP', delivery_method='Free'):
        '''
        Initialise an empty shopping cart. Default currency is GBP,
        default delivery method is 'free'.
        '''
        self.contents = {}
        self.currency = currency
        self.delivery_method = delivery_method
        self.total = 0.0
    
    def add_delivery_cost(self):
        '''
        Returns the delivery cost and adds it to the total.
        '''
        if self.delivery_method == 'Free':
            cost = 0.0
        elif self.delivery_method == 'Express':
            cost = 2.0
        elif self.delivery_method == 'Same day':
            cost = 5.0
        
        self.total += cost
        return cost
        
    def __str__(self):
        '''
        Define the string method for the online shopping cart.
        Display the contents of the cart like a shopping list.
        '''
        out = 'Shopping cart:\n\n'
        
        for item, price in self.contents.items():
            out += f'{item:<15}: {price:>5.2f}\n'
        
        out += '-----------\n'
        out += f'Total: {self.currency} {self.total:.2f}\n\n'
        
        # Calculate and display delivery cost, add it to the total
        cost = self.add_delivery_cost()
        out += f'{self.delivery_method} delivery\n{cost:>22.2f}\n'
        out += '-----------\n'
        out += f'Total with delivery: {self.currency} {self.total:.2f}\n'
        return out

euro_cart = online_cart(currency='EUR', delivery_method='Same day')
euro_cart.add_item('baguette', 0.87)
euro_cart.add_item('camembert', 3.64)
euro_cart.add_item('chablis', 16.80)
print(euro_cart)
```

---

## Exercise 4

```python
class playing_card():
    '''
    Define a playing card object.
    '''
    
    def __init__(self, value=1, suit='hearts'):
        '''
        Instantiate a card. Defaults to ace of hearts.
        '''
        self.suit = suit
        self.value = value
    
    def __str__(self):
        '''
        Returns the string representation of the card.
        '''
        if self.value == 1:
            display_value = 'ace'
        elif self.value == 11:
            display_value = 'Jack'
        elif self.value == 12:
            display_value = 'Queen'
        elif self.value == 13:
            display_value = 'King'
        else:
            display_value = self.value
        return f'{display_value} of {self.suit}'
    
    def __eq__(self, other):
        '''
        Overloads the == operator to compare cards.
        '''
        return self.suit == other.suit and self.value == other.value
    
    def __gt__(self, other):
        '''
        Overloads the > operator to compare cards.
        '''
        # If either both cards are hearts, or both are something else, compare values
        if (self.suit == 'hearts') == (other.suit == 'hearts'):
            return self.value > other.value
        
        # Otherwise, one of them is hearts, but not the other
        else:
            # in this case, return True if the first is hearts, False if the second is hearts
            return self.suit == 'hearts'

# Make some cards
cards = [playing_card(2, 'clubs'),
         playing_card(7, 'hearts'),
         playing_card(9, 'hearts'),
         playing_card(13, 'diamonds'),
         playing_card(11, 'spades'),
         playing_card(11, 'spades'),
         playing_card(1, 'clubs')]

for card in cards:
    print(card)

assert cards[2] > cards[1]
assert cards[1] > cards[3]
assert cards[3] > cards[4]
assert cards[4] == cards[5]

# Note that Python guesses what "<" does by inverting the result of __gt__()
assert cards[6] < cards[0]
```
