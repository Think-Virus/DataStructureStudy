class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value #저장된 데이터
        self.pointer = pointer #다음 노드 가리키는 변수


    def getData(self):
        return self.value

    def getNext(self):
        return self.pointer

    def setData(self, newdata):
        self.value = newdata

    def setNext(self, newpointer):
        self.pointer = newpointer
