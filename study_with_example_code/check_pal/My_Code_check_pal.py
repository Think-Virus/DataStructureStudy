# 연결 리스트가 회문인지 확인하는 코드

from linkedListFIFO import LinkedListFIFO
from node import Node

def checkllPal(ll) :
    for i in range(ll.length) :
        if ll._find(i)[0].value != ll._find(ll.length-1-i)[0].value :
            return False
    return True

def checkllPal_check():
    ll = LinkedListFIFO()
    l1 = [1, 2, 3, 2, 1]
    for i in l1:
        ll.addNode(i)
    assert(checkllPal(ll) is True)

    ll.addNode(2)
    ll.addNode(3)
    assert(checkllPal(ll) is False)

    print("테스트 통과!")


if __name__ == "__main__":
    checkllPal_check()