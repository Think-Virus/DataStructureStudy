# 이 정렬을 얘기한 게 아닌 것 같음
# 예제 코드 이해 완료

def count_sort(seq) :
    return_seq = []
    for i in range(len(seq)) :
        for j in range(seq[i]) :
            return_seq.append(i)

    print(return_seq)


# def check_count_sort():
#     seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
#     assert (count_sort(seq) == sorted(seq))
#     print("테스트 통과!")

if __name__ == "__main__":
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    count_sort(seq)