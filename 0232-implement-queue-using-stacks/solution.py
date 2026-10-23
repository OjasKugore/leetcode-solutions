
class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.temp:
            while self.stack:
                self.temp.append(self.stack.pop())
        return self.temp.pop()

    def peek(self) -> int:
        if not self.temp:
            while self.stack:
                self.temp.append(self.stack.pop())
        return self.temp[-1]

    def empty(self) -> bool:
        return not self.stack and not self.temp

