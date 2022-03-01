# 각 행과 열이 정렬되어 있는 행렬에서 한 항목을 검색
# 즉, 모든 행은 왼쪽에서 오른쪽으로, 모든 열은 위에서 아래로 정렬(오름차순)되어있다.

"""
정렬되어있다고 했으니까 이진검색하면 될 거 같음
"""
def searching_in_a_matrix(seq,val) :
    # seq -> m x n 메트릭스
    for m in range(len(seq)) :
        for n in range(len(seq[0])) :
            if val == seq[m][n] :
                return True
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