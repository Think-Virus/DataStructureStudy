# 못하겠다..
# 거의 비슷하게 접근하긴 한 것 같은데 ㅜㅜ

def merge_sort(seq) :
    half_point = len(seq) // 2
    if half_point >= 1 : # 분할 결과가 1개만 남았을 때, break
        merge_sort(seq[:half_point]) # half_point 이전 값 확인
        merge_sort(seq[half_point:]) # half_point 다음 값(half_point포함)

    else:
        print(seq[half_point])
        print()


def check_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    merge_sort(seq)

check_merge_sort()