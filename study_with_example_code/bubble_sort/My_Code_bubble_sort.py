# input -> [11,3,28,43,9,4]

def bubble_sort(in_list):
    size = len(in_list)
    size_i = size - 1
    for _ in range(size) :
        for i in range(size_i) :
            if in_list[i] > in_list[i+1] :
                in_list[i],in_list[i+1] =in_list[i+1],in_list[i] #val2,val1
        size_i -= 1
    print(in_list)




if __name__ == "__main__" :
    test_list = [11,3,28,43,9,4]
    bubble_sort(test_list)