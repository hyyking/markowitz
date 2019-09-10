""" Abstract Set Class """

from abc import ABC, abstractmethod

__all__ = "AbstractSet"

class AbstractSet(ABC):
    """ Abstract Representation of a mathematical set that can be turned in a point generator """

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        """ AbstractSets must be valid iterators """

    @abstractmethod
    def map(self, func, *args, **kwargs):
        """ Abstract method to map a function on the point generator """

    @abstractmethod
    def gen(self):
        """ Abstract method to map a function on the point generator """
