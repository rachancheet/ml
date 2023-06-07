import math
import numpy as np
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


def func_min_j(data ,min_x, min_y, max_x, max_y):
    output = open("output.txt", "w")

    # w = mod[max_y - min_y, max_x-min_x]
#    b= [max_y,-max_y]
    min_x = int(min_x)
    min_y = int(min_y)
    max_x = int(max_x)
    max_y = int(max_y)

    max_slope = int(math.ceil((abs((max_y - min_y)/(max_x-min_x)))))
    min_j = 10000000
    per_w = data[0,0]
    per_b = data[0,1]

    # plt_j=np.array([max_slope*2,3], dtype=
    # print(min_x, min_y, max_x, max_y,max_slope)
    for w in range(-max_slope,max_slope+1):
        for b in range(-max_y,max_y):
            j=0
            for gh in data:
                j += abs(w*gh[0]+b - gh[1]) 
                if j > min_j:
                    break
            # print(f"w:{w}b:{b}j:{j}\n--------------------------------\n")
            # output.write(f"w:{w}  b:{b}  j:{j}\n--------------------------------\n")
            if j<min_j:
                min_j = j
                per_w=w
                per_b =b
        # print(w)        
        
                
    # print(f"w:{per_w}  b:{per_b}  min_j:{min_j}\n--------------------------------\n")
    # output.write(f"min_j :: {min_j}")
    # output.close()
    return min_j,per_w,per_b


def predict_graph(data,w,b):
    j= np.zeros([data.shape[0],2])
    k=0
    for d in data:
        j[k] = [d[0],w*d[0]+b]
        k+=1
    return j

def binary_min_j(data ,min_x, min_y, max_x, max_y):
    output = open("output.txt", "w")

    # w = mod[max_y - min_y, max_x-min_x]
#    b= [max_y,-max_y]
    min_x = int(min_x)
    min_y = int(min_y)
    max_x = int(max_x)
    max_y = int(max_y)

    max_slope = int(math.ceil((abs((max_y - min_y)/(max_x-min_x)))))
    min_j = 100000000000
    per_w = data[0,0]
    per_b = data[0,1]

    e_w=max_slope
    s_w = -max_slope
    e_b= max_y
    s_b = -max_y
    while (s_w<e_w):
        m_w = (e_w +s_w)/2
        j = 0
        min_b_j = 10000000000
        while (s_b<e_b):
            j_b =0
            m_b=(s_b+e_b)/2
            for d in data:
                j_b += abs(m_w*d[0]+m_b - d[1])
            # print(f"w:{w}b:{b}j:{j}\n--------------------------------\n")
    #         output.write(f"w:{w}  b:{b}  j:{j}\n--------------------------------\n")
            if j_b<min_b_j:
                min_b_j = j_b
                per_b = m_b
                e_b = m_b
                print("m_b :: ",m_b)
            else :
                print("ok")
                s_b = m_b+1
        for d in data:
                j += abs(m_w*d[0]+per_b - d[1])
#         print(j,":::",min_j)
        if j<min_j:
            print("m_w :: ",m_w)
            min_j = j
            per_w = m_w
            e_w = m_w
            
        else : 
            s_w = m_w+1

    print(f"w:{per_w}  b:{per_b}  min_j:{min_j}\n--------------------------------\n")



    # plt_j=np.array([max_slope*2,3], dtype=
    # print(min_x, min_y, max_x, max_y,max_slope)
    # for w in range(-max_slope,max_slope+1):
    #     for b in range(-max_y,max_y):
    #         j=0
    #         for gh in data:
    #             j += abs(w*gh[0]+b - gh[1]) 
    #             if j > min_j:
    #                 break
    #         print(f"w:{w}b:{b}j:{j}\n--------------------------------\n")
    #         output.write(f"w:{w}  b:{b}  j:{j}\n--------------------------------\n")
    #         if j<min_j:
    #             min_j = j
    #             per_w=w
    #             per_b =b
    # print(min_x, min_y, max_x, max_y,max_slope)
    # output.write(f"min_j :: {min_j}")
    # output.close()
    return min_j,per_w,per_b
