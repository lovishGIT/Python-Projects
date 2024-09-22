import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('func/Fish.csv')
print(df.head())

# sns.displot(df['Weight'])
# sns.displot(df['Weight'], hist= False)

# sns.lineplot(x= df['Species'], y= df['Height'], data= df, linestyle= '--')
# plt.show()

# sns.scatterplot(x= df['Height'], y= df['Weight'], data= df, markers='*')
# plt.show()

# sns.barplot(x= df['Species'], y= df['Weight'], data= df)
# plt.show()

# countplot only for categorical
# sns.countplot( x= df.iloc[:, 1], data=df)
# sns.countplot( x=df['Species'], data= df)
# plt.show()

# sns.boxplot(x= df['Species'], y= df['Weight'], data=df)
# plt.show()

# sns.violinplot(x= df['Species'], y= df['Weight'], data=df)
# plt.show()

# D= df.iloc[:,1:]
# Matrix= D.corr()

# print(Matrix)

# sns.heatmap(Matrix)
# plt.show()

# sns.heatmap(Matrix, annot=True, cmap= 'tab20', linecolor= 'yellow', linewidths=2) # likha ayega via annot,,, cmap is set of colours
# plt.show()


# sns.pairplot(df)
# plt.show()

# sns.distplot(df['Weight'], hist= False)
# plt.show()

# print(df['Height'].mean().round())
# print(df['Height'].median().round())

