# st= "Lovish"
# print(st.isalpha()) #Means Lovish string has no special chars like space comma etc

# st= "Lovish"
# print(st.find("L"))
# print(str.reverse)

# st= "Lovish"
# print(st[:])
# print(st[0:3])
# print(st[:-1])
# print(st[::-1])

#all about list

# append insert pop  remove sorted

# b= [1,2,5,23,523,1]
# print(sorted(b))
# print(sorted(b, reverse = True))

# def sort_them(li, reverse= False):
#     if(reverse):
#         for i in range(0,len(li)):
#             max= i
#             for j in range(i+1,len(li)):
#                 if(li[max] < li[j]):
#                     max= j
#             temp= li[max]
#             li[max]= li[i]
#             li[i]= temp
#     else:
#         for i in range(0,len(li)):
#             min= i
#             for j in range(i+1,len(li)):
#                 if(li[min] > li[j]):
#                     min= j
#             temp= li[min]
#             li[min]= li[i]
#             li[i]= temp
#     return li

# li= [1,5,2,3,0]
# sort_them(li)
# print(li)
# sort_them(li,reverse= True)
# print(li)

# li= [1,3,5,0,2]
# print(list(reversed(li)))

# tup= (1,2,5,3,7)
# print(len(tup))
# tup= list(tup)
# tup.append(20)
# tup= tuple(tup)
# print(tup)

# print(sorted(tup))
# print(tuple(reversed(tup)))

# dictionary= {
#     'a': 0,
#     'b': 1,
#     'c': '2',
#     'd': {
#         'phela mtlb': 'pata nhi',
#         'doosra mtlb': 'vo bhi nhi pta',
#         'teesra mtlb': 'apna kaam krna laude',
#     },
# }

# print(dictionary['d'])

# for i in dictionary.items():
#     print(i)

# print(dictionary.items())

# dictionary['e']= 4
# print(dictionary['d']['phela mtlb'])

# input_dictionary= {
#     input("key: "): input("value: "),
#     input("key: "): input("value: "),
#     # input("key: "): input("value: "),
#     # input("key: "): input("value: "),
#     # input("key: "): input("value: "),
# }

# print(input_dictionary.keys)

