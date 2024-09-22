import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x1= np.arange(10)
# y1= 2*x1 + 13
# plt.plot(x1,y1)
# plt.show()

# x2= np.arange(10)
# y2= 2*(x2*x2) + 12
# plt.plot(x2,y2)
# plt.show()

# x3= np.arange(10)
# y3= 2*(x3*x3) + 12

# plt.plot(x3,y3, color = 'green', marker='x', linestyle= '--', label= 'Graph')

# marker='x' :- Marking at points like 0 1 2 3 4 5 6 i.e where x is integer
# marker='y' :- Marking at points like 0 1 2 3 4 5 6 i.e where y is integer

# Linestyle:-  ValueError: '-+-' is not a valid value for ls; supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted

# plt.xlabel('Time')
# plt.ylabel('Velocity')
# plt.title('Velocity vs Time Graph')
# plt.legend() # Makes Label visible

# plt.show()


# plt.figure(figsize=(5,5))
# plt.bar(x3,y3, color = 'green', label= 'Graph')
# plt.legend()
# plt.show()


# BAR GRAPH

# x= np.array([0,1,2])
# plt.bar( x, [10, 15, 20], width= 0.5, label="Blue Data" )
# plt.bar( x + 0.5, [20, 15, 10], width= 0.5, color="green", label="Green Data" )

# plt.xlim(-1, 5) # x axis kha se kha vary kregi
# plt.ylim(0, 30) # y axis kha se kha tak vary

# plt.xlabel('sales')
# plt.ylabel('Time')
# plt.title('Bar Plot')

# plt.legend()
# plt.show()

# sub= ['Maths', 'Physics', 'Chemistry', 'Biology']
# x= np.random.randint(50, 100, 4)
# plt.pie(x, labels=sub, explode=[0, 0.1, 0.2, 0.3], shadow= True, autopct= "%.2f") 
# # explode for gaps # shadow for 3d print # autopct is giving percentage
# plt.show()

# x_gausian= np.random.randn(1000)
# sigma= 5
# mean= 60

# x_shifted_gausian_1= x_gausian * sigma + mean
# x_shifted_gausian_2= x_gausian * 7 + 70

# print(x_gausian, x_shifted_gausian_1, x_shifted_gausian_2)

# x_shifted_gausian_1 = x_shifted_gausian_1.round(decimals=1) # decimals means jitne decimals chahiye
# x_shifted_gausian_2 = x_shifted_gausian_2.round( decimals=0)

# print(x_gausian, x_shifted_gausian_1, x_shifted_gausian_2)

# plt.hist(x_shifted_gausian_1, color="pink")
# plt.hist(x_shifted_gausian_2, color="orange", alpha=0.1) # alpha is transparency

# plt.show()


# data= pd.read_csv('func/Fish.csv')
# print(data.head())

# print(data['Species'].unique())

# plt.hist(data['Weight'])
# plt.show()

# sns.displot(data['Weight'])
# sns.displot(data['Weight'], hist= False)


# plt.plot( data['Weight'], data['Length1'] ) #Line plot

# plt.plot( data.iloc[:, 1], data.iloc[:, 2] ) #Line plot for continous graph
# plt.scatter( data.iloc[:, 1], data.iloc[:, 2] ) #scatter plot for discrete values

# plt.show()

# plt.bar(data.iloc[:, 0], data.iloc[:, 1])


# plt.bar(data['Species'],data['Length1'])
# plt.bar(data['Species'],data['Weight'])
# plt.show()

#This will overlap because weight graph is smaller

# plt.bar(data['Species'],data['Weight'])
# plt.bar(data['Species'],data['Length1'])
# plt.show()

#This will not overlap

# plt.hist(data['Width'])
# plt.hist(data[''])

# data.hist()
# plt.tight_layout()

# print(data.iloc[:, 1].mean()," ", data.iloc[:, 1].median())
# print(data.iloc[:, 2].mean()," ", data.iloc[:, 2].median())
# print(data.iloc[:, 3].mean()," ", data.iloc[:, 3].median())
# print(data.iloc[:, 4].mean()," ", data.iloc[:, 4].median())
# print(data.iloc[:, 5].mean()," ", data.iloc[:, 5].median())
# print(data.iloc[:, 6].mean()," ", data.iloc[:, 6].median())
# plt.show()



# labels= data['Species'].unique()

# x= list( data['Species'].value_counts() )
# print(x)

# plt.pie( x, labels= labels)
# plt.show()


# data= pd.read_csv('func/Titanic-Dataset.csv')
# print(data.head())

# print(data.isnull().sum())


# mean= data['Age'].mean()
# data['Age'].fillna(mean)

# print(data)

# plt.plot(data.iloc[:, 1], data.iloc[:, 9])
# plt.scatter(data.iloc[:, 1], data.iloc[:, 9])

# labels= data['Sex'].unique()
# x= data['Sex'].value_counts()

# print(x)

# plt.pie(x, labels= labels)

# plt.show()

# x= Input Feature
# y= Target Variable

# data= pd.read_csv('func/Fish.csv')
# print(data.head())

# plt.bar(data['Length1'], data['Species'])
# plt.show()

# HISTOGRAM OF LENGTH2 PARAMETER
# plt.hist(data['Length1'])
# plt.show()

# plt.subplot(211)
# plt.scatter(data.iloc[:, 1], data.iloc[:, 2])
# plt.scatter(data.iloc[:, 2], data[:, 3])
# plt.grid()



# -------------------------------

# data= pd.read_csv('func/Titanic-Dataset.csv')
data= pd.read_csv('func/netflix_titles.csv')
# print(data.head())

# data['Embarked']= data['Embarked'].fillna('Nan')
# print(data.isnull().sum())

# label= data['Embarked'].unique()
# values= data['Embarked'].value_counts()

# print(label, values)

# plt.pie(values, labels=label)
# plt.show()


data= data.drop(columns= ['show_id', 'director','description', 'cast'])
# print(data.head())

# print(data.isnull().sum())
# print("-------------------")
# print(data['rating'].value_counts().idxmax())

# data['rating']= data['rating'].fillna(data['rating'].value_counts().idxmax())

# print(data.isnull().sum())
# print(data.head())

# y= data['rating'].value_counts()
# x= data['rating'].unique()

# plt.bar( x, y )
# plt.xticks()
# plt.show()

# data['date_added']= pd.to_datetime(data['date_added'].str.strip(), format= "%B %d, %Y")

# print(data.head())

# data['month']= data['date_added'].dt.month()
# data['year']= data['date_added'].dt.year()
# data['day']= data['date_added'].dt.date()

# print(data.head())

# data['country']= data['country'].fillna(data['country'].value_counts().idxmax())

# a= data['country'].unique()
# b= data['country'].value_counts()

# print(a,b)

# plt.plot(a, b)
# plt.show()
# This gets ploted but we cant understand anything

# country= data['country'].str.split(",",expand= True)
# print(country)

