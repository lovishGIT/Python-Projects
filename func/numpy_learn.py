import numpy as np

# a= np.array([1,
#              2,
#              5,
#              3,
#              4,
#              6]) 
# always arranged like this

# print(type(a))
# print(a.shape) # (6, )

# a= np.array([[1,2,3,4],[5,6]]) # error
# a= np.array([[1,2,3,4],[5,6,7,8]]) # (2,4)
# print(a.shape)

# a= np.zeros(3,3) # error
# a= np.zeros((3,3))
# print(a)

# print(np.eye(3,3))

# print(np.random.random((3,3)))

# print(np.full((3,3), 5))

# a= np.random.random((6,6))
# print(a)
# print("-------------------")
# print(a[:4])
# print("-------------------")
# print(a[ :4, 3]) # (0 to 4)rows 3rd column
# print("-------------------")
# print(a[:4, :5]) # (0 to 4)rows (0 to 5)column

# x= np.array([[1,2],
#             [3,4]])
# print(x)
# y= np.array([[5,6], 
#             [7,8]])
# print(y)
# print("-------------------")
# print(x/y)

# print(np.add(x,y))
# print("-------------------")
# print(np.subtract(x,y))
# print("-------------------")
# print(np.multiply(x,y))
# print("-------------------")
# print(np.divide(x,y))
# print("-------------------")

# print(np.sqrt(155))
# print("-------------------")

# print(np.matmul(x,y))
# print("-------------------")
# print(np.dot(x,y))
# print("-------------------")
# print(x@y)
# print("-------------------")
# print(x.dot(y))
# print("-------------------")

# print(np.sum(x, axis= 0)) # Column wise
# print(np.sum(x, axis= 1)) # Row wise

# a= np.stack((x,y),axis= 1) # ROW WISE
# X ki row 1 -- Y ki row 1
# X ki row 2 -- Y ki row 2
# print(a)

# a= np.random.random((4,3))
# print(a)

# print(a.reshape(3,4))
# print(a.reshape(((6,-1)))) # 6rows columns jitne bhi

# print(a.reshape((-1,4))) # 4 columns row jitne bhi

# c= np.array(range(0,10))
# c= np.arange(10)
# print(c)

# c= np.random.random((3,4))
# print(c)
# np.random.shuffle(c)
# print(c)

# print(np.random.rand(2,4))
# print(np.random.randint(2,5)) # 1 element in between 2,5 
# print(np.random.randint(2,5, 2)) # 2 elements in between 2,5
# print(np.random.randint(2,5, size=2)) # same

# arr= np.random.randint(2,5, (5,3))
# print(arr)
# arr= np.random.randint(2,5, 5)
# print(arr)
# print(np.random.choice(arr))


# arr= np.random.randint(2,5, (5,3))
# print(arr)
# print(np.min(arr)) #smallest ele
# print(np.min(arr, axis=0)) # comparison column wise printing smallest in column
# print(np.min(arr, axis=1)) # ulta i.e row wise

# print("------------------")
# print(np.sum(arr, axis=0))
# print(np.sum(arr, axis=1))

# a= np.array([
#     [1,2,3,4],
#     [5,6,7,8], 
# ])

# print(np.mean(a))
# print(np.mean(a, axis=0))
# print(np.mean(a, axis=1))

# print(np.mean(a))
# print(np.median(a))
# print(np.average(a))

# average means sum krke divide by number of ele's
# mean means phele ascending me sort fr mean
# median means phele ascending mein sort when ele are odd -> middle ele , when ele are even middle two ka sum div by 2 

# standard deviation
# c= np.array([
#     [1,2,3,4],
#     [5,6,7,8], 
# ])
# u= np.mean(c)
# std= np.sqrt( np.mean( abs(c-u) ** 2 ) )

# print(std)

# print(std**2)
# print(np.var(c)) # standard deviation ** 2 hai but abs nahi liya