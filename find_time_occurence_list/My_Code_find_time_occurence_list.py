# binary_search.py를 사용하여 정렬된 리스트에서 요소 k가 나타나는 횟수를 구해보자
from binary_search import binary_search_iter

def find_time_occurrence_list(seq,k) :
    Cnt = 0
    while True :
        idx = binary_search_iter(seq,k)
        if idx :
            Cnt +=1
            del seq[idx]
        else:
            return Cnt


def test_find_time_occurrence_list():
    seq = [1, 2, 2, 2, 2, 2, 2, 5, 6, 6, 7, 8, 9]
    k = 2
    assert(find_time_occurrence_list(seq, k) == 6)
    print("테스트 통과!")


if __name__ == "__main__":
    test_find_time_occurrence_list()