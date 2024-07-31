from csv import reader


class PGDV:
    """
    a PGDV is a series of quadruples where, in each quadruple, the elements are

    1. Pitch      (integer from 0 to 127 inclusive)
    2. Gap        (integer equal to or greater than 0)
    3. Duration   (integer equal to or greater than 0)
    4. Velocity   (integer from 0 to 127 inclusive)
    """
    tps = 960  # ticks per second

    def __init__(self, data):
        self.data = data  # 2D array of width 4

    def __str__(self):
        return "\n".join([f"   Pitch: {i[0]}\n     Gap: {i[1]}\nDuration: {i[2]}\nVelocity: {i[3]}\n"
                          for i in self.data])

    @classmethod
    def from_csv(cls, path):
        with open(path) as f:
            data = list(reader(f))
        return cls(data)

    @classmethod
    def to_csv(cls, path):
        pass
