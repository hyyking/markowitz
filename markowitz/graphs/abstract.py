""" Abstract Graph Object """

from abc import ABC, abstractmethod


class AbstractGraph(ABC):
    """ Abstraction of a graph object """

    _precision = 1000
    _legend = ""

    @abstractmethod
    def points(self):
        """ Abstract method for generating an iterable object of graph points """

    @property
    def precision(self):
        """ precision value of a graph """
        return self._precision

    @precision.setter
    def precision(self, value):
        self._precision = value

    @property
    def legend(self):
        """ legend of a graph """
        return self._legend

    @legend.setter
    def legend(self, value):
        self._legend = value
