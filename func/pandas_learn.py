# accuracy percision

# import os
import numpy as np
import pandas as pd

# print(np.random.randint(2,5))
# user_definned = {
#     'Marks_A': np.random.randint(50, 100, 5),
#     'Marks_B': np.random.randint(50, 100, 5),
#     'Marks_C': np.random.randint(50, 100, 5),
#     'Marks_D': np.random.randint(50, 100, 5),
# }

# print(type(user_definned))



# data = pd.read_csv('func\Data.csv') # copy relative path krke krna hai
# data = pd.read_csv('func/Titanic-Dataset.csv') 


# print(data)
# os.path.join(os.getcwd(), 'data.csv')
# print(data)

# print(data.head())
# print(data.shape)


# categorizing the data
# FILLING Nan Values

# We should not fill values which is more, to reduce time and effort.
# Moreover the filled data will give us more error.

# print( data.isnull() )
# print( data.isnull().sum() )

#Cabin is 687

# print(data.head().isnull().sum())

# datashape= data.shape
# print(datashape)


# y= mx+c               m,c to make straight line. two parameters 
# y= kuch formula.....  m1, m2, c to make straight line. three parameters 


# shifted gaussion= ( gaussian * σ ) + mean(μ)


# mean_age= data['Age'].mean()
# median_age= data['Age'].median()

# print(mean_age)


# Embared is data of S, C, Q like characters

# mean_embarked= data['Embarked'].unique()
# print(mean_embarked)

# max_value_embarked= data['Embarked'].value_counts().idxmax()
# print(max_value_embarked)


# mean_age= data['Age'].mean(skipna= True)
# median_age= data['Age'].median(skipna= False)
# max_emb= data['Embarked'].value_counts().idxmax()

# data['Age'].fillna(mean_age)
# data['Embarked'].fillna(max_emb)

# data['Company'] = np.where((data['SibSp'] + data['Parch'] > 0 ),1 ,0 )
# data= data.drop(columns= ['Parch','SibSp'])
# # print(data)


# train= pd.get_dummies(data, columns= ['Embarked', 'Sex'])
# train['Embarked_C']= np.where((train['Embarked_C'] == True),1 ,0)  # train nhi likha data likhdiya waah
# print(train.head())

# print(data.head())

# data= data.sort_values(by= ['Maxpulse']) # sorting values
# print(data.head())


# data= data.groupby(by= ['Pulse', 'Maxpulse']) # making groups
# print(data.head())

df= pd.read_csv('func/Fish.csv')
data= pd.read_csv('func/Data.csv')

# print(pd.concat([df.head(), data], axis= 1))

# print(df.columns)

