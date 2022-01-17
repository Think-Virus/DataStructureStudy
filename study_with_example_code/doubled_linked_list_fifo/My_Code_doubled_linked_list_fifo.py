# 11_linkedlist_FIFO 코드를 사용하여 이중 연결 리스트를 구현해보자
from linkedListFIFO import LinkedListFIFO

class Double_Node(object) :
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    # def getData(self):
    #     return self.value
    #
    # def getNext(self):
    #     return self.right
    #
    # def getBefore(self):
    #     return self.left
    #
    # def setData(self, newdata):
    #     self.value = newdata
    #
    # def setNext(self, newpointer):
    #     self.right = newpointer

class DLinkedList(LinkedListFIFO) :
    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.right
        print()

    def printListInverse(self):
        node = self.tail
        while node :
            print(node.value, end=" ")
            node = node.left
        print()

    def _addFirst(self, value):
        self.length = 1
        node = Double_Node(value)
        self.head = node
        self.tail = node

    def _add(self, value):
        self.length += 1
        node = Double_Node(value)
        if self.tail:
            self.tail.right = node
            node.left = self.tail
        self.tail = node

    # 새 노드를 추가한다.
    def addNode(self, value):
        if not self.head:
            self._addFirst(value)
        else:
            self._add(value)

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            _next = node.right.right
            node = node.right
            i += 1
        return node, prev, i,_next

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                _next = node.right.right
                node = node.right

        return node, prev, found,_next

    def deleteNode(self, index):
        if not self.head or not self.head.right:
            self._deleteFirst()
        else:
            node, prev, i,_next = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = _next
                    self.tail = _next
                else:
                    prev.right = _next
                    if _next :
                        _next.left = prev
            else:
                print("인덱스 {0}에 해당하는 노드가 없습니다.".format(index))

    def deleteNodeByValue(self, value):
        if not self.head or not self.head.right:
            self._deleteFirst()
        else:
            node, prev, i, _next = self._find_by_value(value)
            if node and node.value == value:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = _next
                    self.tail = _next
                else:
                    prev.right = _next
                    _next.left = prev
            else:
                print("값 {0}에 해당하는 노드가 없습니다.".format(value))


if __name__ == "__main__":
    from collections import Counter

    ll = DLinkedList()
    for i in range(1, 5):
        ll.addNode(i)
    print("연결 리스트 출력:")
    ll._printList()
    print("연결 리스트 반대로 출력:")
    ll.printListInverse()
    print("값이 15인 노드 추가 후, 연결 리스트 출력:")
    ll._add(15)
    ll._printList()
    print("모든 노드 모두 삭제 후, 연결 리스트 출력:")
    for i in range(ll.length-1, -1, -1):
        ll.deleteNode(i)
    ll._printList()

    # ll.deleteNode(2)
    # ll.printListInverse()