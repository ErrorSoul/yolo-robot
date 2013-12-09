import random 

class Pockets(object):
    __slots__ = ('_number','_color')
    def __init__(self, number):
        self._number = number
        g  = {0:'black', 1:'red'}
        g1 = {0:"red",   1:'black'}
        self._color = 'green' if self.number == 0 else (g[self.number%2] if
                                                       (self.number in range(1,11) or
                                                        self.number in range(19,29)) else
                                                       g1[self.number%2])
        del g,g1
                      

    @property
    def number(self):
        return self._number

    @property
    def color(self):
        return self._color

    def __str__(self):
        return "({0},{1})".format(self.number,self.color)

    def __repr__(self):
        return "({0},{1})".format(self.number,self.color)

class Wheel(object):
    s = ("0-32-15-19-4-21-2-25-17-34-6-27-13-36-11-30-8-23-10-5-24-16-33-1-20-14-31-9-22-18-29-7-28-12-35-3-26")

    poc = s.split('-')
    __slots__ = ('_pockets', '_last_bet')
    def __init__(self):
        self._pockets = [Pockets(int(c)) for c in self.poc ]
        self._last_bet = None

    def __iter__(self):
        bet = None
        while True:
            self.last_bet = bet
            bet = random.choice(self.pockets)
            yield bet
    def make_bet(self):
        g = iter(self)
        return g.next()

    @property
    def pockets(self):
        return self._pockets

    @property
    def last_bet(self):
        return self._last_bet

    @last_bet.setter
    def last_bet(self, bet):
        self._last_bet = bet
    

class Player(object):
    def play(self, wheel):
        pass




if __name__ == "__main__":
    player = Player()
    wheel  = Wheel()
    player.play(wheel)
