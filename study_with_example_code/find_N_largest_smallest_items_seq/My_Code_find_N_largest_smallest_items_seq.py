# 내장모듈 heapq 모듈을 사용하여 시퀀스에서 N개의 가장 큰 항목과 가장 작은 항목 찾기
import heapq
import copy

def make_max_heap(seq) :
    max_heap = []
    for i in seq :
        heapq.heappush(max_heap,(-i,i)) #최대 힙 구현
    return max_heap

def find_N_largest_items_seq(seq, N) :
    return_list = []
    heap = make_max_heap(seq)

    for _ in range(N) :
        return_list.append(heapq.heappop(heap)[1])

    return return_list


def find_N_largest_items_seq_sorted(seq,N) :
    return_list = []
    heap = make_max_heap(seq)

    for _ in range(N):
        return_list.append(heapq.heappop(heap)[1])

    return_list.sort()
    return return_list

def find_N_smallest_items_seq(seq,N) :
    return_list = []
    heap = copy.deepcopy(seq)
    heapq.heapify(heap)

    for _ in range(N) :
        return_list.append(heapq.heappop(heap))

    return return_list

def find_N_smallest_items_seq_sorted(seq,N) :
    return_list = []
    heap = copy.deepcopy(seq)
    heapq.heapify(heap)

    for _ in range(N) :
        return_list.append(heapq.heappop(heap))

    return_list.sort()
    return return_list


def find_smallest_items_seq(seq) :
    min_value = None
    for i in seq :
        if not min_value :
            min_value = i
        if min_value > i :
            min_value = i

    return min_value

def find_smallest_items_seq_heap(seq) :
    heap = copy.deepcopy(seq)
    heapq.heapify(heap)
    return heapq.heappop(heap)


def find_N_largest_smallest_items_seq():
    seq = [1, 3, 2, 9, 6, 10, 8]
    N = 3
    assert(find_N_largest_items_seq(seq, N) == [10, 9, 8])
    assert(find_N_largest_items_seq_sorted(seq, N) == [8, 9, 10])
    assert(find_N_smallest_items_seq(seq, N) == [1, 2, 3])
    assert(find_N_smallest_items_seq_sorted(seq, N) == [1, 2, 3])
    assert(find_smallest_items_seq(seq) == 1)
    assert(find_smallest_items_seq_heap(seq) == 1)

    print("테스트 통과!")


if __name__ == "__main__":
    find_N_largest_smallest_items_seq()
