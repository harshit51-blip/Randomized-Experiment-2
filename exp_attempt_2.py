import random as r
import math as m
import msvcrt
import matplotlib.pyplot as plt
import statistics


def perturbation(lst,ind,ifactor,precision):
    lst1 = [round(_ + (ifactor/(pow(2, abs(ind-lst.index(_))+1))),precision) for _ in lst]
    return lst1

def diff(lst):
    minimum = min(lst)
    maximum = max(lst)
    diff = maximum - minimum
    return diff

def central_tendency(l):
    arith_mean = statistics.mean(l)
    
    return round(arith_mean,4)
    

def plotting(x_list, y_list, ytitle):
    plt.plot(x_list, y_list)
    plt.title('Graph')
    plt.grid(True, which = 'both')
    plt.xlabel('Iterations')
    plt.ylabel(ytitle)
    plt.show()
    

n = int(input("number of particles: "))
iteration = int(input("number of iterations: "))
lst_X = []
precision = 4
counter = 1
x_plot = []
y_plot = []
arm = []

for _ in range(n):
    while True:
        ele = round(r.uniform(-10000,10000+1), precision)
        if ele not in lst_X:
            lst_X.append(ele)    
            break

lst_X.sort()

lst_V = [round(m.sin(x), precision) for x in lst_X]

arm.append(central_tendency(lst_V))


V_d = diff(lst_V)
x_plot.append(counter)
y_plot.append(V_d)

for E in range(iteration-1):
        
    #lst_V = [round(m.sin(x) ,precision) for x in lst_X]

    some_list = [1,2,3,4]
    random_num = r.randint(1,101)
    
    if random_num in some_list:
        ifactor = r.randint(-50,51)
        pert = r.choice(lst_V)
        ind = lst_V.index(pert)
        
        lst_V = perturbation(lst_V,ind,ifactor,precision)
        print(counter)
        
    '''V_d = diff(lst_V)
    x_plot.append(counter)
    y_plot.append(V_d)'''
    
    for e in range(len(lst_V)):
        y = round(r.uniform(lst_V[e]-4,lst_V[e]+5), precision)
        lst_X[e]  = round(lst_X[e],precision) + y
        lst_V[e] = round(m.sin(lst_X[e]) + y, precision)

    counter+=1

    arm.append(central_tendency(lst_V))

    V_d = diff(lst_V)
    x_plot.append(counter)
    y_plot.append(V_d)

    #counter+=1

plotting(x_plot, arm, ytitle = 'mean')

  
dV_d = []
for d in range(len(y_plot)-1):
    diff_d = -(y_plot[d] - y_plot[d+1])
    dV_d.append(diff_d)


plotting(x_plot, y_plot, ytitle = 'V_d')

number = list(range(iteration-1))
plotting(number, dV_d, ytitle = 'dV_d')


char = msvcrt.getch()



        



        
    
