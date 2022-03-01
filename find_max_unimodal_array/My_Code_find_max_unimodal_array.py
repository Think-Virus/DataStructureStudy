# 단봉형 배열 : 배열 요소들의 산포도를 그렸을 때 값이 증가했다가 다시 감소하는 곡선
# 이진 검색을 사용하여 최댓값 찾기

def find_max_unimodal_array(seq) :
    low = 0
    high = len(seq)
    if high < 3 :
        if seq[0] > seq[1] :
            return seq[0]
        else:
            return seq[1]
    while low < high :
        mid = (low + high) // 2
        if seq[mid] < seq[mid-1] :
            high = mid
            continue
        if seq[mid] < seq[mid + 1] :
            low = mid+1
            continue
        return seq[mid]


def check_find_max_unimodal_array():
    seq = [1, 2, 5, 6, 7, 10, 12, 9, 8, 7, 6]
    if find_max_unimodal_array(seq) == max(seq) :
        print("테스트 통과!")


if __name__ == "__main__":
    check_find_max_unimodal_array()