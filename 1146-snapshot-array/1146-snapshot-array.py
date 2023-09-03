class SnapshotArray:
    def __init__(self, length: int):
        self.id = 0
        self.history = [[[0, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.history[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap: int) -> int:
        indexs = bisect.bisect_right(self.history[index], [snap, 10 ** 9])
        return self.history[index][indexs-1][1]
