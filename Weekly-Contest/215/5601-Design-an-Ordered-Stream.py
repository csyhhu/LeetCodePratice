from typing import List

class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.ptr = 0
        self.container = [(0, None) for _ in range(n)]
        # print(self.container)

    def insert(self, id: int, value: str) -> List[str]:
        id = id - 1
        self.container[id] = (id, value)
        new_list = []
        if self.ptr == id:
            for i in range(id, self.n):
                if self.container[i][1] is None:
                    break
                new_list.append(self.container[i][1])
            self.ptr = i
        return new_list


obj = OrderedStream(5)
print(obj.insert(3, "ccccc"))
print(obj.insert(1, "aaaaa"))
print(obj.insert(2, "bbbbb"))
print(obj.insert(5, "eeeee"))
print(obj.insert(4, "ddddd"))