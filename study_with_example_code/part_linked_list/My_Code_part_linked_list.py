# 숫자가 담긴 연결 리스트에서 한 항목을 선택했을 때, 그 항목 값의 왼 쪽에는 작은 숫자 항목만 나오고 오른 쪽에는 큰 숫자 항목만 나오도록 연결리스트를 분할
# 연결리스트 따로 공부하고 정리해봤는데도 잘 모르겠다.. 그래도 예제 코드는 이해 완료

from linkedListFIFO import LinkedListFIFO
from node import Node

def partList(linked_list,value):
    return_list = LinkedListFIFO()
    return_list.addNode(value)

    value_node,prev,found = linked_list._find_by_value(value)

    while node :
        if node.value > value :
            self.tail.poine
        node = node.pointer


if __name__ == "__main__":
    ll = LinkedListFIFO()
    l = [6, 7, 3, 4, 9, 5, 1, 2, 8]
    for i in l:
        ll.addNode(i)

    print("분할 전:")
    ll._printList()

    print("분할 후:")
    newll = partList(ll, 6)
    newll._printList() # 결과 : 3 4 5 1 2 6 7 9 8
