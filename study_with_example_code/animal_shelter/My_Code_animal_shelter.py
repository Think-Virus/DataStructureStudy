# 개와 고양이를 입양(enqueue)했다가 다시 출양(dequeue)하는 동물 보호소를
# 큐로 구현 -> FIFO
# 동물 보호소는 개와 고양이를 지정하여 입출양할 수 있어야 함

class Animal() :
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind

class AnimalShelter(object) :
    def __init__(self):
        self.animal_list = []
        self.lenth = 0

    def enqueue(self,name,kind):
        animal = Animal(name,kind)
        self.animal_list.append(animal)
        self.lenth += 1

    def dequeueDog(self):
        dog_index = 0
        var_find = False
        for i in range(self.lenth) :
            if self.animal_list[i].kind == "dog" :
                dog_index = i
                var_find = True
                break
        if var_find :
            self.lenth -= 1
            return self.animal_list.pop(dog_index).name

    def dequeueCat(self):
        cat_index = 0
        var_find = False
        for i in range(self.lenth) :
            if self.animal_list[i].kind == "cat":
                cat_index = i
                var_find = True
                break
        if var_find :
            self.lenth -= 1
            return self.animal_list.pop(cat_index).name

    def _print(self):
        dog_names = []
        cat_names = []
        for i in range(self.lenth) :
            if self.animal_list[i].kind == "dog":
                dog_names.append(self.animal_list[i].name)
            else :
                cat_names.append(self.animal_list[i].name)
        print('고양이 :\n\t', "\n\t".join(cat_names))
        print('개 :\n\t',"\n\t".join(dog_names))



if __name__ == "__main__": # 테스트 코드
    qs = AnimalShelter()
    qs.enqueue("밥", "cat")
    qs.enqueue("미아", "cat")
    qs.enqueue("요다", "dog")
    qs.enqueue("울프", "dog")
    qs._print()

    print("하나의 개와 고양이에 대해서 dequeue를 실행합니다.")
    qs.dequeueDog()
    qs.dequeueCat()
    qs._print()