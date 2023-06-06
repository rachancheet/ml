import numpy as np
import pandas as pd
import matplotlib.pyplot as pl



def min__j(x_data,y_data,w,b):
    j= 0
    for i in range(x_data.shape[0]):
        j+=(np.dot(x_data[i],w)+b- (y_data[i]))**2
    ghj = (2*x_data.shape[0])
    return j/ghj


def gradient(x_data,y_data, w, b):
    j_i = np.zeros(w.shape[0])
    j_j = 0
    m = x_data.shape[0]
    for i in range(x_data.shape[0]):
        k = (np.dot(x_data[i],w)+b- (y_data[i]))
        for gb in range(w.shape[0]): 
            j_i[gb] += (k*x_data[i][gb])
        
        j_j += k
     
    grad = [1/m * j_i, 1/m * j_j]
    return grad





def gradient_descent(x_data,y_data,w,b):
    dist = 0.00000000006
    hist =[]
    count =0
    for i in range(50000):
        count +=1
        dj_dw,dj_db =  gradient(x_data,y_data,w,b)

    
        w = w-(dist*dj_dw)
        b = b-(dist*dj_db)

        if i%10==0:
            print(w,b,"-------------------------------- j: ",min__j(x_data,y_data,w,b),"dj_dw: ",dj_dw,"dj_db: ",dj_db)
      
    return w,b




def predict_graph(x_data,w,b):
    # pred = np.zeros([x_data.shape[0],])
    pred = np.zeros([x_data.shape[0]])
    for i in range(x_data.shape[0]):
        pred[i] = np.dot(x_data[i],w) +b
    return pred

def show_predictions(x_test,y_test,per_w,per_b):
    print(per_w,per_b)
    pred = predict_graph(x_test,per_w,per_b)
    print(" Limit","Rating","Cards","Age","Education")
    for i in range(x_test.shape[0]):
        print(x_test[i],"       ",round(pred[i],3),y_test[i]) 



def accuracy(x_test,y_test,w,b,):
    pred = predict_graph(x_test,w,b)
    t =np.sum(y_test)
    k = np.sum(pred)
    error = abs(k-t)/t 
    error *= 100
    return error


