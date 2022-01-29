
'''n=int(input()) # Number of test cases
m=2
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split()[:m])))
    print(len(arr[i]))'''

    


#print(arr)


#a=int(input())
#b=int(input())

def GCD(a,b):
    if (a>=0 and b>=0):

        if (a==0 and b==0):
            return 0
        elif(a==0 and b!=0):
            return b
        elif (b==0 and a!=0):
            return a
        elif (a>0 and b>0):
            if (a>b):
                a,b=a,b
            elif (a<b):
                a,b=b,a
    else:
        for i in range(1,2+1):
            if (a%i == 0 and b%i == 0):
                gcd=i*gcd
                print(gcd)

        

print(GCD(60,36))

'''if (a>0 and b>0):
    if(a==0 and b>0):
        print(b)
    elif (b==0 and a>0):
        print(a)
    else:
        for i in range(1,len(arr)+1):
            if (a%i==0 and b%i==0):
                gcd=i*i '''


'''def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 36 
num2 = 60

print("The H.C.F. is", compute_hcf(num1, num2))'''



import numpy as np
num1=60
num2=12

GCD=print(np.gcd(num1,num2))