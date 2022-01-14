#연결리스트의 끝에서 K번째 항목 찾기
#연결리스트 공부 더 필요 못풀겠다..
from linkedListFIFO import LinkedListFIFO
from node import Node

class KthFromLast(LinkedListFIFO) :
    def __init__(self):
        self.head = None  # 헤드(머리)
        self.length = 0
        self.tail = None  # 테일(꼬리)

    def find_kth_to_last(self,k):
        prev = None
        node = self.tail
        i = 0
        while node and i < k :
            prev = node
            node = node.pointer
            i +=1
        return node.value

if __name__ == "__main__":
    ll = KthFromLast()
    for i in range(1, 11):
        ll.addNode(i)
    print("연결 리스트: ", end="")
    ll._printList()
    k = 3
    k_from_last = ll.find_kth_to_last(k)
    print("연결 리스트의 끝에서 {0}번째 항목은 {1}입니다.".format(k, k_from_last))