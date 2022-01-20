# input -> [11,3,28,43,9,4]

def selection_sort(in_list) :
    length = len(in_list)

    for i in range(length) :
        min_val = None
        for val_index, val in enumerate(in_list[i:]) :
            if not min_val :
                min_val = val
                min_index = val_index + i
            elif min_val > val :
                min_val = val
                min_index = val_index + i
        in_list[i],in_list[min_index] = in_list[min_index],in_list[i]
    print(in_list)





if __name__ == "__main__":
    test_list = [11, 3, 28, 43, 9, 4]
    selection_sort(test_list)