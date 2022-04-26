def binary_tree_list(r):
    return [r, [], []]


def insert_left(root, newBranch):
    t = root.pop(1) # left에 있는 값 추출
    # left에 있는 게 트리인지 확인
    if len(t) > 1: # 트리인 경우
        root.insert(1, [newBranch, t, []]) # root에 추가했기 때문에 기존에 있던 값들은 추가하는 가지의 left로 이동
    else:
        root.insert(1, [newBranch, [], []]) # 새롭게 가지 추가
    return root


def insert_right(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t]) # root에 추가했기 때문에 기존에 있던 값들은 추가하는 가지의 right로 이동
    else:
        root.insert(2, [newBranch, [], []]) # 새롭게 가지 추가
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def main():
    r = binary_tree_list(3)
    insert_left(r, 4)
    insert_left(r, 5)
    insert_right(r, 6)
    insert_right(r, 7)
    print(get_root_val(r))
    print(get_left_child(r))
    print(get_right_child(r))


if __name__ == "__main__":
    main()
