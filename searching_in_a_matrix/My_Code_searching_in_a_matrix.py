# 주어진 행렬은 한 행의 마지막 숫자가 다음 행의 첫 번째 숫자보다 작다
# -> 즉 모든 행이 오름 차순으로 정렬되어있다.


def searching_in_a_matrix(seq,val) :
    high = len(seq) * len(seq[0])
    low = 0
    while high > low :
        mid = (high+low) // 2
        row = mid // len(seq[0])
        col = mid % len(seq[0])
        if val == seq[row][col] :
            return True
        elif val > seq[row][col] :
            low = mid+1
        else:
            high = mid

    return False



def test_searching_in_a_matrix():
    a = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    import numpy
    b = numpy.array([(1, 2), (3, 4)])
    assert(searching_in_a_matrix(a, 13) is True)
    assert(searching_in_a_matrix(a, 14) is False)
    assert(searching_in_a_matrix(b, 3) is True)
    assert(searching_in_a_matrix(b, 5) is False)
    print("테스트 통과!")


if __name__ == "__main__":
    test_searching_in_a_matrix()