# 내가 짠 코드가 더 비효율적

def gnome_sort(in_list) :
    var_stop = 1
    while var_stop :
        var_stop = 0
        for i in range(len(in_list)) :
            j = i
            if j > 0 and in_list[j-1] > in_list[j] :
                in_list[j-1], in_list[j] = in_list[j], in_list[j-1]
                var_stop = 1
                break
    print(in_list)


if __name__ == "__main__":
    test_list = [11, 3, 28, 43, 9, 4]
    gnome_sort(test_list)