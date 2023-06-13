class Stack:
    def __init__(self):
        self.items = []

    def clear(self):
        self.items.clear()

    def pop(self):
        return self.items.pop(0)

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    ret = s.pop()
    print(ret)
    print(s.is_empty())
