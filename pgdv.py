from csv import reader


class PGDV:
    def __init__(self, data):
        self.data = data  # 2D array of width 4

    def __str__(self):
        return "\n".join([f"   Pitch: {i[0]}\n     Gap: {i[1]}\nDuration: {i[2]}\nVelocity: {i[3]}\n"
                          for i in self.data])

    tps = 960  # ticks per second

    @classmethod
    def from_csv(cls, path):
        with open(path) as f:
            data = [[int(i) for i in row] for row in reader(f)]
        return cls(data)

    def to_csv(self, path):
        pass

    @classmethod
    def from_midi(cls, path):
        pass

    def to_midi(self, path):
        pass

    def transpose(self):
        pass

