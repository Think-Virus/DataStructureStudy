class BunchClass(dict):
    def __init__(self, *args, **kwds): # 여기 예시에선 *args 이거 없어도 될듯
        super(BunchClass, self).__init__(*args, **kwds) # super().__init__()이라는 코드가 다른 클래스의 속성 및 메소드를 자동으로 불러와 해당 클래스에서도 사용이 가능하도록 해줍니다.
        self.__dict__ = self


def main():
    # 1) 딕셔너리 특수화
    bc = BunchClass  # ()가 없다.
    tree = bc(left=bc(left="Buffy", right="Angel"),
              right=bc(left="Willow", right="Xander"))
    print(tree)

    # 2) 일반 딕셔너리
    tree2 = dict(left=dict(left="Buffy", right="Angel"),
                 right=dict(left="Willow", right="Xander"))
    print(tree2)

if __name__ == "__main__":
    main()
