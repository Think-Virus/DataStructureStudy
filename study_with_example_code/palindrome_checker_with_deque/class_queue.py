class Class_Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enClass_Queue(self, item):
        self.items.insert(0, item)


    def deClass_Queue(self):
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


if __name__ == "__main__":
    Class_Queue = Class_Queue()
    print("큐가 비었나요? {0}".format(Class_Queue.isEmpty()))
    print("큐에 숫자 0~9를 추가합니다.")
    for i in range(10):
        Class_Queue.enClass_Queue(i)
    print("큐 크기: {0}".format(Class_Queue.size()))
    print("peek: {0}".format(Class_Queue.peek()))
    print("deClass_Queue: {0}".format(Class_Queue.deClass_Queue()))
    print("peek: {0}".format(Class_Queue.peek()))
    print("큐가 비었나요? {0}".format(Class_Queue.isEmpty()))
    print(Class_Queue)
