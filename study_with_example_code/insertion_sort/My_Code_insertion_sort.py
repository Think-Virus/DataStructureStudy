# input -> [11,3,28,43,9,4]

def insertion_sort(in_list):
    length = len(in_list)

    for i in range(1, length-1):
        min_index = 0
        pre_index = 0
        k = -1
        while k < i+1 :
            k += 1
            if in_list[pre_index] > in_list[k] :
                in_list[k], in_list[pre_index] = in_list[pre_index], in_list[k]
                if k < 2 : # k가 2보다 작으면 -1이 되어서 루프가 안끝남
                    continue
                k -= 2 # 한 칸 앞으로 이동하고 나서 다시 그 이전 값하고 값 비교하기 위해 있는 부분
                pre_index = k
                continue
            pre_index = k

        print(in_list)


if __name__ == "__main__":
    test_list = [11, 3, 28, 43, 9, 4]
    insertion_sort(test_list)