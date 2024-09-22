# if elif else
# loops 


# a= int(input())


# print( "even" if (a%2==0) else "odd")


# for i in range(0,5):
#     print("AH",end="")

# st= "Lovish Bansal"
# for i in st:
#     print(i, end=" ")


# def fact(a):
#     fact=1
#     for i in range(2,a+1):
#         fact *= i
#     return fact
# a= int(input())
# print(fact(a))


# def sum_n(a, b):
#     sum=0
#     for i in range(a,b+1):
#         sum = sum + i
#     return sum
# a= int(input("A:"))
# b= int(input("B:"))
# print(    sum_n(a,b)  )


# while True:
#     a=int(input("Enter n: "))
#     if(a==9):
#         print("hi")
#         break
#     else:
#         print("hey")

# while True:
#     passwd= input("Enter The password: ")
#     # print(passwd.lower())
#     if(passwd.lower() == "lovish"):
#         print("Good Job")
#         break
#     print("Try Again")\

# name= input()
# print("hello, My name is {}".format(name)) #format
# print(f"Hello, My name is {name}") #fstring

# name= 'harry potter'
# print(name.split()[0])

# passwd= input("Enter Anything").lower()
# passwd= list(passwd.split("lovish"))
# if(len(passwd)>1):
#     print("hello")
# else:
#     print("No")

# st= 'harry potter'
# print(st.count('r'))

# st= 'harry potter'
# st= st.replace('ha','rr')
# print(st)

# st= 'harry potter'
# print(st.endswith('er'))
# print(st.startswith('ha'))

# def check_upper(str):
#     for i in str:
#         if (ord(i)<65 or ord(i)>90):
#             return False
#     return True

# str= input("Enter Name: ")
# print(check_upper(str))

# def do_upper(str):
#     str1= ""
#     for i in range(0, len(str)):
#         str1+= str[i] if (check_upper(str[i]) or str[i]==" ") else chr(ord(str[i]) - 32)
#     return str1

# str= "Lovish Bansal"
# print(do_upper(str))
