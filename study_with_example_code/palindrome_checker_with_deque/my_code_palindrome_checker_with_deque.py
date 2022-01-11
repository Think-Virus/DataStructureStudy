#데크를 이용하여 회문 확인
from deque import Deque

#띄어쓰기와 대소문자 구분하는 함수
"""def palindrome_checker_with_deque(string) :
    deque_front = Deque()
    deque_back = Deque()
    for char in string :
        deque_front.enClass_Queue(char)
        deque_back.enqueue_back(char)
    return deque_front == deque_back"""

#띄어쓰기와 대소문자 구분하지 않는 함수
def palindrome_checker_with_deque(string) :
    string = string.lower().replace(' ','')
    deque_front = Deque()
    deque_back = Deque()
    for char in string :
        deque_front.enqueue(char)
        deque_back.enqueue_back(char)
    return deque_front.items == deque_back.items

if __name__ == "__main__":
    str1 = "Madam Im Adam"
    str2 = "Buffy is a Slayer"
    print(palindrome_checker_with_deque(str1))
    print(palindrome_checker_with_deque(str2))