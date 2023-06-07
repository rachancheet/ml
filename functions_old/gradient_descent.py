import pandas as pd
import numpy as np
from functions_old.linear_regression import *
import matplotlib.pyplot as pl


def min__j(data,w,b):
    j= 0
    for d in data:
        j+=(w*d[0]+b-d[1])**2
    ghj = (2*data.shape[0])
    return j/ghj


def gradient(data, w, b):
    j_i = 0
    j_j = 0
    m = data.shape[0]
    for d in data:
        k= w*d[0] +b -d[1]
        j_i += k*d[0]
        j_j += k
        if k > 100000000000000:
            break
    grad = [1/m * j_i, 1/m * j_j]
    return grad





def gradient_descent(data,w,b):
    dist = 0.000006
    hist =[]
    count =0
    for i in range(50000):
        count +=1
        dj_dw,dj_db =  gradient(data,w,b)

        w = w-(dist*dj_dw)
        b = b-(dist*dj_db)

        # printing
        if i%10==0:
            print(w,b,"-------------------------------- j: ",min__j(data,w,b))
            pass
        # automatic convergence check
        hist.append([w,b])
        p =False
        if len(hist)%5==0:
            diff =[]
            for k in range(4):
                diff.append([abs(hist[k][0]-hist[k+1][0]),abs(hist[k][1]-hist[k+1][1])])
            for j in diff:
                # print("--------------------------------",diff)
                if j[0]<0.00005 and j[1]<0.00005:
                    p=True
                else:
                    p=False
                    break
            hist = []
            diff = []
        if p==True:
            print("breaks",count)
            break
    return w,b





def graph(data,predict):
    pl.scatter(data[:,0],data[:,1])
    pl.plot(predict[:, 0], predict[:, 1], color='red')
    pl.show()


if __name__ == "__main__":
    w,b = gradient_descent(data2,0,0)
    print(w, b)
    predict2 = predict_graph(data2, w, b)