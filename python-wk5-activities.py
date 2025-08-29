# activity 1 

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class marks(student):  #creation of marks as a subclass of student
    pass #inherits from student

#creation of an instance
student1 = student("Alice", 20)
student2 = student("Bob", 22)
student3 = student("Charlie", 21)

print(student1.name, student1.age)
print(student2.name, student2.age)
print(student3.name, student3.age)  

# activity 2
class horse:
    def move(self):
        return "gallop"

class flea:
    def move(self):
        return "leaps high off the ground"

class dog:
    def move(self):
        return "runs fast"

#polymorphism in action
for animal in [horse(), flea(), dog()]:
    print(animal.move())