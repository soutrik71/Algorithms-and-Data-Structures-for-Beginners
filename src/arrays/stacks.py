class Stacks:
    def __init__(self):
        self.stack = []

    def push(self, data: int):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None


if __name__ == "__main__":
    stack = Stacks()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
