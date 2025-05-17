class Stack:
    def __init__(self, *args, **kwargs):
        self.list = [*args, *kwargs.values()]

    def __str__(self):
        return str(self.list)

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.list.append(element)

    def pop(self):
        if len(self.list) == 0:
            raise IndexError
        else:
            element = self.list[-1]
            self.list.remove(self.list[-1])
            return element

    def peek(self):
        if len(self.list) == 0:
            raise IndexError
        else:
            element = self.list[-1]
            return element

    def size(self):
        return len(self.list)