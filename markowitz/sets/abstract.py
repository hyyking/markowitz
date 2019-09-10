""" Abstract Set Class """

from abc import ABC, abstractmethod

__all__ = "AbstractSet"

class AbstractSet(ABC):
    """ Abstract Representation of a mathematical set that can be turned in a point generator """

    @abstractmethod
    def __iter__(self):
        """ AbstractSets must be valid iterators """

    @abstractmethod
    def __next__(self):
        """ AbstractSets must be valid iterators """

    def gen(self):
        """ Method to create a point generator """
        return iter(self)

    def map(self, func, *margs, **mkwargs):
        """ Method to map a function on the point generator """
        return map(lambda x: func(x, *margs, **mkwargs), iter(self))
