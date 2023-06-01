# trying to write my own linear regression algorithm
# input np array with x and y values
import numpy as np 
import math

def range_w_b(data):
    min_x = data[0,0]
    min_y = data[0,1]
    max_y = data[0,1]
    max_x = data[0,0]
    for i in data:
        x = i[0]
        y = i[1]
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:  
            min_y = y
        if y > max_y:
            max_y = y
    return min_x, min_y, max_x, max_y
        
def    min_j(data ,min_x, min_y, max_x, max_y):
    # w = mod[max_y - min_y, max_x-min_x]
#    b= [max_y,-max_y]
    min_x = int(min_x)
    min_y = int(min_y)
    max_x = int(max_x)
    max_y = int(max_y)

    max_slope = int(math.ceil((abs((max_y - min_y)/(max_x-min_x)))))
    min_j = data[0,1] 
    per_w = data[0,0]
    per_b = data[0,1]

    # plt_j=np.array([max_slope*2,3], dtype=
    # print(min_x, min_y, max_x, max_y,max_slope)
    for w in range(-max_slope,max_slope+1):
        for b in range(-max_y,max_y):
            for gh in data:
                j= abs(w*gh[0]+b - gh[1]) 
                # print(w,b,j,"\n--------------------------------\n")
                if j<min_j:
                    min_j = j
                    per_w=w
                    per_b =b
    # print(min_x, min_y, max_x, max_y,max_slope)
    return min_j,per_w,per_b

def fun_j(data,w,b):
    j= np.array([max_x-min_x,2])
    for d in data:
        j = np.append(j,[d[0],abs(w*d[0]+b - d[1])])
    return j


data = np.random.randint(0,30,[20,2])
# print(data[1,1])
min_x, min_y, max_x, max_y = range_w_b(data)
# print(type(min_x))
min_j,per_w,per_b = min_j(data , min_x, min_y, max_x, max_y)
error_plt = fun_j(data,per_w,per_b)
print(error_plt)
import matplotlib.pyplot as plt
plt.scatter(data[:,0],data[:,1])
plt.plot()

plt.show()
