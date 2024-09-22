# Encapsulation


# Inheritance

# class School_member: 
#     def __init__(self, name, age):
#         self.name= name
#         self.age= age
#         print(f"initialized Member: {self.name} with age {self.age}")
#     def tell(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
# class Teachers(School_member):
#     def __init__(self, tName, tAge, tSubject):
#         School_member.__init__(self, tName, tAge)
#         self.tName= tName
#         self.tAge= tAge
#         self.subject= tSubject
#     def tell(self):
#         School_member.tell(self)
#         print(f"Subject: {self.subject}")
# rohan= School_member("Rohan", 18)
# rohan.tell()
# teacher= Teachers("Lovish", 18, "Programming")
# teacher.tell()    
# teacher= Teachers("koyi bhi", 40, "CPP")
# teacher.tell()


# def add(a,b):
#     return a+b
# print(add(add(add(1,1),1),add(1,1)))


users= {
    'a': 'Machine Learning',
    'b': 'AI / ML',
}
# def show(username, password):
#     if username in users :
#         if users[username] == password :
#             print("Authentication passed")
#             return
#     print("Authentication failed")

# show('a' , 'Machine Learning')


# def add(a,b):
#     return a+b

# def login_req(f):
#     def wrapper(username, password, *args, **kwargs):
#         if username in users and users[username] == password :
#             f(*args, **kwargs)
#         else:
#             print("Authentication Failed")
#     return wrapper

# login_req(print)('a','Machine Learning','Teacher= Koyi bhi nahi',  teacher='koyi bhi nhi', new_teacher= 'koyi to hai' )
# error in next class

