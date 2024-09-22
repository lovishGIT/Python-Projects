# def remove_all():

# st= "This man is sleeping on the bench."
# st= st.lower()
# for i in range(0, len(st)):
#     for j in range(i+1, len(st)):
#         # print(i,j)
#         if(st[i]==st[j]):
#             st= st.replace(st[i], ":")

# st= st.replace(":","")
# print(st)

# st= "This man is sleeping on the bench."
# dictionary= {}
# for i in st:
# find occurence

# d = {
#     'a':[1,2,2,2,3,4,4,5,65,76,75,76,65],
#     'b':[32,23,2,34,3,43,43,4.3,3,4,4.3,4,8,9,98,7,7]
# }
# def intersect(a,b):
#     a= set(a)
#     b= set(b)
#     print(a.intersection(b))
# intersect(d['a'], d['b'])
# def uni(a,b):
#     a= set(a)
#     b= set(b)
#     print(a.union(b))
# uni(d['a'], d['b'])

# def listToset(a):
#     x= set()
#     for i in a:
#         x.add(i)
#     print(x)
# listToset(d['a'])

# def add(a, b, c, *args):
#     print(a+b+c)
#     print(*args)
#     print(args)
#     sum= a+b+c
#     for i in args:
#         sum+= i
#     return sum
# print(add(1,2,3,4,5,6,7,8,9,10))

# def kwargs_wala_func(a,b, **kwargs):\
#     print(a,b)
#     print(kwargs)
#     print(*kwargs)
#     print(kwargs['m'])
#     print(kwargs['n'])
# kwargs_wala_func(1,2, m= 'xyz', n= 'abc')


# def adderr(a, *args, **kwargs):
#     print(a)
#     print(args)
#     print(kwargs) 
# adderr(2, 3, 4, 5, 45, name_1 = 'tushar', name_2 = 'Khitoliya')

# li= [1,2,3,4,5, 'lovish', 'Bansal']
# print(li[::-1])