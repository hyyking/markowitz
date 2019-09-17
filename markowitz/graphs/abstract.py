""" Abstract Graph Object """

from abc import ABC, abstractmethod

__all__ = "AbstractGraph"


class AbstractGraph(ABC):
    """ Abstraction of a graph object """

    _precision = 1000
    _scale = 1
    _legend = "Default Legend"

    @abstractmethod
    def points(self):
        """ Abstract method for generating an iterable object of graph points """

    @property
    def legend(self):
        """ legend of a graph """
        return self._legend

    @legend.setter
    def legend(self, value):
        """ legend might be modified internally """
        self._legend = value

    @property
    def scale(self):
        """ scale of the graph """
        return self._scale

    @property
    def precision(self):
        """ precision value of a graph """
        return self._precision
