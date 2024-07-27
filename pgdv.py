class PGDV:
    """
    PGDV is a series of NOTES (quadruples) where
        - the 1st element is the Pitch      (integer from 0 to 127 inclusive)
        - the 2nd element is the Gap        (integer equal to or greater than 0)
        - the 3rd element is the Duration   (integer equal to or greater than 0)
        - the 4th element is the Velocity   (integer from 0 to 127 inclusive)
    """

    tps = 960  # ticks per second

    def __init__(self, array):
        self.array = array  # List of 4-tuples

    def __str__(self):
        return "\n".join(["\t".join(i) for i in self.data])

    @classmethod
    def from_txt(cls, path):
        """
        Creates a PGDV object from a file. NOTES are separated by newlines and NOTE elements are seperated by tabs.
        :param path: The path and name of the file
        :return: PGDV instance
        """
        f = open(path, 'r')
        dat = [i.split(" ") for i in f.read().split("\t")]
        f.close()
        return cls(dat)

    @classmethod
    def from_midi(cls, path):
        pass

