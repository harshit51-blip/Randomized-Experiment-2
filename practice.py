import random as r

lst = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
n = len(lst)
pert = r.choice(lst)
print(pert)
ind = lst.index(pert)
ifactor = 2
lst1 = [n * (ifactor/pow(2, abs(ind-lst.index(n))+1)) for n in lst]
print(lst1)
