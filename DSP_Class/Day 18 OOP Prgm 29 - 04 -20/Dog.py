class Dog:
    # attribute of Dog

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bark(self):
        print('huf huf')

    def wiggleTail(self):
        print('wiggle wiggle')
        self.__bark()

    def __del__(self):
        # self.bark()
        print('Del is on the go ')


d = Dog('John', 3)
d.wiggleTail()
d.__bark()
