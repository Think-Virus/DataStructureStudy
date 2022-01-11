class Class_Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)


    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Class_Class_Queue is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Class_Queue is empty.")

    def __repr__(self):
        return repr(self.items)
