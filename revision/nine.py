st= "Supervised learning algorithms build a mathematical model of a set of data that contains both the inputs and the desired outputs.The data is known as training data, and consists of a set of training examples. Each training example has one or more inputs and the desired output, also known as a supervisory signal. In the mathematical model, each training example is represented by an array or vector, sometimes called a feature vector, and the training data is represented by a matrix. Through iterative optimization of an objective function, supervised learning algorithms learn a function that can be used to predict the output associated with new inputs. An optimal function allows the algorithm to correctly determine the output for inputs that were not a part of the training data. An algorithm that improves the accuracy of its outputs or predictions over time is said to have learned to perform that task"

file= open('nine.txt','w')

for i in range(len(st)):
    # print(len(st))  
    n= int(input('Enter the num: '))
    part_st= st[i:i+n]
    file.write(part_st)
    i= i+n
    if i>=len(st):
        break
    