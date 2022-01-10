# 스택에 용량이 정해져있다고 가정
# 한 스택의 용량이 초과하면, 새 스택을 만들어야 함
# 이 경우 여러 스택이 있게 될텐데 이 스택 집합에서도 단일 스택과 같이 push()와 pop을 이용하려면 어떻게 해야 할까?
# 실패...
from stack import Stack

class SetOfStacks(object) :
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = Stack()
        self.pointer = None
        self.count = 0

    def push(self, value):
        self.count += 1
        if self.stack.size() == self.capacity : # 분기
            self.stack = Stack()
            self.pointer = self.stack

        self.stack.push(value)

    def isEmpty(self):
        return not self.count

    def sizeStack(self):
        tmp_value = self.count / self.capacity
        if int(tmp_value) == tmp_value :
            return tmp_value
        else :
            return int(tmp_value)+1

    def peek(self):
        if self.isEmpty() :
            print("stack is empty")
            return

        if self.stack.isEmpty() :
            self.stack = self.pointer
        return self.stack.peek()


if __name__ == "__main__":
    capacity = 5
    stack = SetOfStacks(capacity)
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print("스택에 숫자 0~9를 추가합니다.")
    for i in range(10):
        stack.push(i)
    print(stack)
    print("스택 크기: {0}".format(stack.sizeStack()))
    print("peek: {0}".format(stack.peek()))
    #print("pop: {0}".format(stack.pop()))
    print("peek: {0}".format(stack.peek()))
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print(stack)