class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender= gender

    def introduce(self):
        print('My name is', self.name, ', I am', self.age, 'years old and I am ', self.gender)


pers1 = Person("Mohamed", 28, "Male")
pers1.introduce()
