# heapq 모듈을 이용하여 정렬된 두 시퀀스를 적은 비용으로 병합
import heapq

def merge_sorted_seqs(seq1, seq2) :
    return list(heapq.merge(seq1,seq2))

def test_merge_sorted_seqs():
    seq1 = [1, 2, 3, 8, 9, 10]
    seq2 = [2, 3, 4, 5, 6, 7, 9]
    seq3 = seq1 + seq2
    assert(merge_sorted_seqs(seq1, seq2) == sorted(seq3))

    print("테스트 통과!")


if __name__ == "__main__":
    merge_sorted_seqs()