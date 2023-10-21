class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

    def bark(self):
        if self.age < 3:
            print('WOOF')
        elif self.age > 3:
            print('WOOF WOOF WOOF')


dog1 = Dog("jessi", 5)
dog1.eat()
dog1.bark()

dog2 = Dog("alex", 2)
dog2.eat()
dog2.bark()

# یک کاراکتر بازی ایجاد کنید با ویژگی ها و رفتارهای دلخواه
