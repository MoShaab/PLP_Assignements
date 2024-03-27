class Person:
    def __init__(self, name, age, gender):
        self.Name = name
        self.Age = age
        self.Gender= gender

    def introduce(self):
        print('My name is', self.Name, ', I am', self.Age, 'years old and I am ', self.Gender)


pers1 = Person("Mohamed", 28, "Male")
pers1.introduce()
