# 두 연결 리스트의 숫자 더하기
# 연결 리스트의 각 항목은 양의 정수
# 한 연결 리스트의 항목으로 예를들어 1,7,6,2가 추가되었다면, 이 연결 리스트의 숫자는 2671


from linkedListFIFO import LinkedListFIFO
from node import Node

class LinkedListFIFOYield(LinkedListFIFO) :
    def _popNode(self):
        return_value = self.head.value
        self.head = self.head.pointer
        self.length -= 1
        return return_value

    def chang_list(self):
        return_list = []
        node = self.head
        while node:
            return_list.append(node.value)
            node = node.pointer
        return return_list

def sumlls(l1,l2) :
    return_list = LinkedListFIFOYield()
    if l1.length > l2.length :
        iter_num = l1.length
    else:
        iter_num = l2.length
    for _ in range(iter_num):
        if l1.head and l2.head :
            sum_value = l1._popNode() + l2._popNode()
        elif l1.head and not l2.head :
            sum_value = l1._popNode()
        elif not l1.head and l2.head :
            sum_value = l2._popNode()

        return_list.addNode(sum_value)

    node = return_list.head
    while node :
        upper_val = node.value // 10
        if upper_val >= 1 and node.pointer :
            node.value = node.value - upper_val*10
            node = node.pointer
            node.value = node.value + upper_val
        else:
            node = node.pointer

    return return_list


if __name__ == "__main__":
    l1 = LinkedListFIFOYield()  # 2671
    l1.addNode(1)
    l1.addNode(7)
    l1.addNode(6)
    l1.addNode(2)
    #l1.addNode(1)

    l2 = LinkedListFIFOYield()  # 455
    l2.addNode(5)
    l2.addNode(5)
    l2.addNode(4)

    lsum = sumlls(l1, l2)
    l = list(lsum.chang_list())
    for i in reversed(l):
        print(i, end="") # 결과 3126
    print()