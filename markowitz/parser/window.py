""" Window holder """

# pylint: disable=too-few-public-methods
class Window:
    """ Abstraction of a matplotlib window """

    def __init__(self, name, cols, config, content):
        self.name = name
        self.cfg = config
        self.content = content

        self.span = self.span_matrix(len(content), cols)

    def span_matrix(self, rows, cols):
        """ create a matrix to  """
        matrix = [[None for _ in range(cols)] for _ in enumerate(rows)]

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
