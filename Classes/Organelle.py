

class Organelle:
    """ An organelle. """

    def __init__(self):
        """ (Organelle) -> NoneType

        Initialize an organelle.
        """


class SmoothEndoplasmicReticulum(Organelle):
    """ Smooth Endoplasmic Reticulum. """

    def __init__(self):
        """ (SmoothEndoplasmicReticulum) -> NoneType

        Initialize a Smooth Endoplasmic Reticulum.
        """
        super().__init__()
        self.contains = []


class RoughEndoplasmicReticulum(Organelle):
    """ Rough Endoplasmic Reticulum. """

    def __init__(self):
        """ (RoughEndoplasmicReticulum) -> NoneType

        Initialize a Rough Endoplasmic Reticulum.
        """
        super().__init__()
        self.contains = []


class Ribosome(Organelle):
    """ A ribosome. """

    def __init__(self):
        """ (Ribosome) -> NoneType

        Initialize a ribosome organelle.
        """
        super().__init__()
        self.contains = []


class Mitochondrion(Organelle):
    """ A mitochondrion. """

    def __init__(self):
        """ (Mitochondrion) -> NoneType

        Initialize a mitochondrion.
        """
        super().__init__()
        self.contains = []


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# How beautiful is OOP?
