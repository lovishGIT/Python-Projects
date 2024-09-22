# users= {
#     'a': 'Machine Learning',
#     'b': 'AI/ML',
# }

# def add(a,b):
#     return a+b

# def login_req(f):
#     def wrapper(username, password, *args, **kwargs):
#         if username in users and users[username] == password :
#             f(*args, **kwargs)
#         else:
#             print("Authentication Failed")
#     return wrapper

# adder= login_req(print)
# adder('a','Machine Learning','Teacher= Koyi bhi nahi', 2 )

# @login_req
# def add(a, b):
#     print(a+b)
# add('a','Machine Learning', 2,3)



class bestfriend:

    best_friends= {}
    def __init__(self, name):
        self.best_friends[str(name)]= []

    def addbestfriends(self, name, name_bestfriend):
        self.best_friends[str(name)].append(str(name_bestfriend))

class Person(bestfriend):

    def __init__(self, name, age):
        super().__init__(name)
        self.name= name
        self.age= age

    def my_bestfriend(self, bestfriend):
        super().addbestfriends(self.name, bestfriend)

a= Person("Lovish", 18)
a.my_bestfriend("koyi bhi")
# print(a.best_friends)

b= Person("Koyi aur", 19)
b.my_bestfriend("Koyi nhi")


print(a.best_friends)

# file= open('eight.txt', 'r')

# print(file.read())  # cursor chla gaya end pe to kbhi bi kuch bhi print nhi hoga
# print(file.read())

# print(file.read(6)) #phele 6 print hogaye
# print(file.read(3)) # ab agle 3 honge firse nahi hoga

# print(file.read(-1)) # default is -1 in file.read()

# print(file.readline())
# print(file.readline())
# # cursor on 3 line
# print(file.readlines())

# file.seek(6)
# print(file.read())

# file.close()

# BAR BAR CLOSE OPEN SO...
# with open('eight.txt','r') as file:
#     print(file.read())