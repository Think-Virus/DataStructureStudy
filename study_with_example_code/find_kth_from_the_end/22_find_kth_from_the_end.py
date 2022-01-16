from linkedListFIFO import LinkedListFIFO
from node import Node


class KthFromLast(LinkedListFIFO):
    def find_kth_to_last(self, k):
        p1, p2 = self.head, self.head   # 왜 p1, p2로 나눠서 하는 걸까?
                                        # p1은 Linked List 끝까지 돌기 위해 사용한 거 -> 가장 끝이 None이니까 끝까지 가면 while문 종료됨
                                        # p2는 우리가 원하는 값을 찾기 위한 것 -> 끝에서 9번째면 딱 한 번만 이동하면(pointer가 가르키는 노드의 값으로) 되는 거니까 i>k-1로 사용한 듯

        print("p1 : {}, p2 : {}".format(p1,p2))
        i = 0
        while p1:
            print("i : {}, k : {}".format(i,k-1))
            if i > k-1:
                try:
                    p2 = p2.pointer
                except AttributeError: # None.pointer하면 AttributeError나오게 한 거
                    break
            p1 = p1.pointer
            i += 1
            print("i : {}, p1 : {}, p2 : {}".format(i, p1, p2))
        return p2.value


if __name__ == "__main__":
    ll = KthFromLast()
    for i in range(1, 11):
        ll.addNode(i)
    print("연결 리스트: ", end="")
    ll._printList()
    k = 9
    k_from_last = ll.find_kth_to_last(k)
    print("연결 리스트의 끝에서 {0}번째 항목은 {1}입니다.".format(k, k_from_last))
