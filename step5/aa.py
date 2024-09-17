class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    def get_count(self):
        return MyClass.count
    
a = MyClass()
b = MyClass()
c = MyClass()

print(a.get_count())
print(MyClass.count)