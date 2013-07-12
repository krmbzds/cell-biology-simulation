

class Structure:
    """ A subcellular component. """

    def __init__(self):
        """ (Organelle) -> NoneType

        Initialize a subcellular component.
        """


class Cytosol(Structure):
    """ Cytosol. """

    def __init__(self):
        """ (Cytosol) -> NoneType

        Initialize Cytosol.
        """
        super().__init__()
        self.contains = []


class PlasmaMembrane(Structure):
    """ Plasma Membrane. """

    def __init__(self):
        """ (PlasmaMembrane) -> NoneType

        Initialize Plasma Membrane.
        """
        super().__init__()
        self.contains = []


class Nucleoid(Structure):
    """ Nucleoid. """

    def __init__(self):
        """ (Nucleoid) -> NoneType

        Initialize a Nucleoid.
        """
        super().__init__()
        self.contains = []


class Nucloelus(Structure):
    """ Nucloelus. """

    def __init__(self):
        """ (Nucloelus) -> NoneType

        Initialize a Nucloelus.
        """
        super().__init__()
        self.contains = []


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Huge classification problems.
