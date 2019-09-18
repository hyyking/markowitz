""" Window Class """

__all__ = ["Window"]


class Window:
    """ Abstraction of a matplotlib figure
    Contains:
    - the name of the graph obj
    - the name of the assets
    - the config of the window (passed down to the graphs)
    - the span matrix so the subplot are adjusted correctly
    """

    def __init__(self, name, cols, config, content):
        self.name = name
        self._cols = cols
        self._cfg = config

        self.content = content
        self.span = self.span_matrix(len(content), cols)

    @property
    def rows(self):
        """ length of rows """
        return len(self.content)

    @property
    def cols(self):
        """ length of columns """
        return self._cols

    @property
    def cfg(self):
        """ length of columns """
        return self._cfg

    def span_matrix(self, rows, cols):
        """ create a matrix to  """
        matrix = [[None for _ in range(cols)] for _ in range(rows)]

        for i, row in enumerate(self.content):
            row_t = len(row)

            if cols % row_t == 0:
                matrix[i] = [cols / row_t for _ in range(row_t)]

            elif row_t == 1:
                matrix[i] = [cols]

            elif row_t % 2 == 0:  # EVEN
                left = cols % row_t
                even = (cols - left) / row_t
                matrix[i] = [even for _ in range(row_t)]
                matrix[i][0] += left

            elif not row_t % 2 == 0:  # ODD
                left = cols % row_t
                even = (cols - left) / row_t
                matrix[i] = [even for _ in range(row_t)]
                index = row_t // (2 - 0.5)
                matrix[i][int(index)] += left
            else:
                print("Don't know how to determin the layout")

        return matrix
