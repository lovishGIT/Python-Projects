# class Student:
#     name= None
#     age= None
#     group= None

#     pataNhi= None
#     def __init__(self, stu_name, stu_age, stu_group):
#         self.name= stu_name
#         self.age= stu_age
#         self.group= stu_group
#         print("Name=", self.name, "\nAge=", self.age, "\nGroup=", self.group)

# lovish= Student('Lovish Bansal', 18, 30)


# class Car:
#     model= ''
#     milage= 0

#     def __init__(self, model, milage):
#         self.model= model
#         self.milage= milage
#         print(self.model, self.milage)

#     def __add__(self, other):
#         return int(self.milage) + int(other.milage)
    
#     def __eq__(self, other):
#         return str(self.milage) == str(other.milage)
    
#     def __str__(self):
#         return "{} {}".format(self.model, self.milage)
    
# C1= Car('tesla', 8)
# C2= Car('BMW', 7)

# print(C1 == C2) # eq func
# print(C1) # str func
# print(C1 + C2) # add func


# str= ['lovish', 'bansal']
# print(type(str))

class Dog:
    def __init__(self, name, breed):
        self.name= name
        self.breed= breed
        self.total_tricks=[]

    def tricks(self, tricks):
        self.total_tricks.append(tricks)

    def __str__(self):
        return f"{self.name} naam hai \nUskiki breed hai {self.breed}\nUspe tricks hai {self.total_tricks}"


    def __eq__(self, other):
        return 'same hai' if ( self.breed ) == ( other.breed ) else 'alag hai' 
    
gs= Dog('kutta', 'German Shaphard')
gs.tricks('sit')
print(str(gs))

print("---------------------------")

lb= Dog("Kutti", 'German Shaphard')
lb.tricks('spy')
print(str(lb))

print("----------------------")

print("Breed", gs == lb)