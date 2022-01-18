# 원형 연결 리스트 : 헤드와 테일이 연결된 연결 리스트
from linkedListFIFO import LinkedListFIFO
from node import Node

class CicularLinkedListFIFO(LinkedListFIFO) :
    def _add(self, value):
        self.length += 1
        node = Node(value, self.head)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

def isCircularll(linked_list) :
    return linked_list.head == linked_list.tail.pointer

def check_isCircularll():
    ll = LinkedListFIFO()
    for i in range(10):
        ll.addNode(i)
    assert(isCircularll(ll) is False)

    lcirc = CicularLinkedListFIFO()
    for i in range(10):
        lcirc.addNode(i)
    assert(isCircularll(lcirc) is True)

    print("테스트 통과!")


if __name__ == "__main__":
    check_isCircularll()
