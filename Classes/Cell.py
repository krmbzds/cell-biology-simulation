

class Cell:
    """ A cell. """

    def __init__(self):
        """ (Cell) -> NoneType

        Initialize a cell.
        """
        self.contains = []


class ProkaryoticCell(Cell):
    """ A prokaryotic cell. """

    def __init__(self):
        """ (ProkaryoticCell) -> NoneType

        Initialize a prokaryotic cell.
        """
        super().__init__()
        self.contains = []
        # self.reproduction = 'Binary Fission'


class EukaryoticCell(Cell):
    """ An eukaryotic cell. """

    def __init__(self):
        """ (EukaryoticCell) -> NoneType

        Initialize an eukaryotic cell.
        """
        super().__init__()
        self.contains = []
        # self.organelles.append('Mitochondrion')
        # self.organelles.append('Smooth Endoplasmic Reticulum')
        # self.organelles.append('Rough Endoplasmic Reticulum')


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# So classy.
