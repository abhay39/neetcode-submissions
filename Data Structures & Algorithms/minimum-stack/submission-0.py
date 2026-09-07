class MinStack:

    def __init__(self):
        self.item=[]

    def isEmpty(self):
        return len(self.item)==0

    def push(self, val: int) -> None:
        self.item.append(val)

    def pop(self) -> None:
        if not self.isEmpty():
            self.item.pop()
        else:
            raise IndexError("pop from empty stack")

    def top(self) -> int:
        if not self.isEmpty():
            return self.item[-1]
        else:
            raise IndexError("peek from empty stack")

    def getMin(self) -> int:
        return min(self.item)
