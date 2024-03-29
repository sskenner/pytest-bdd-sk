"""
this module contains a simple class modeling a cucumber basket. 
cucumbers may be added or removed from the basket.
the basket has a maximum size, however.
"""

class CucumberBasket:

    def __init__(self, initial_count=0, max_count=10): #/
        if initial_count < 0:
            raise ValueError("initial cucumber basket count must not be negative")
        if max_count < 0:
            raise ValueError("max xuxumber basket count must not be negative")

        self._count = initial_count #/
        self._max_count = max_count #/
    
    @property #
    def count(self): #/
        return self._count #/
    
    @property
    def full(self):
        return self.count == self.max_count
    
    @property
    def empty(self):
        return self.count == 0
    
    @property
    def max_count(self):
        return self._max_count
    
    #? why @prop decorators above & not below?
    def add(self, count=1):
        new_count = self.count + count
        if new_count > self.max_count:
            raise ValueError("attempted to add too many cucumbers")
        self._count = new_count
    
    def remove(self, count=1):
        new_count = self.count - count
        if new_count < 0:
            raise ValueError("attempted to remove too many cucumbers")
        self._count = new_count
    
