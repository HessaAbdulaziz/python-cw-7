class Person :
    name = 'hessa'
    age = 15

    def is_adult (self):
        if self.age > 18:
            print('you have too much responsibilities')
        elif self.age < 18:
            print('lucky')

first_person = Person() 
print(first_person.name)
print(first_person.age)
first_person.is_adult()

class Person2:

    def __init__(self, name, age):
        self.name= name
        self.age= age

    def __str__(self):
        return f'my name is{self.name} and I am {self.age} years old'

person = Person2 ('hessa', 15) 
print(person)