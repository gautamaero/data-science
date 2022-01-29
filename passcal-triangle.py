'''from math import factorial as fct
print(fct.5)

n=int(input())


for i in range(n):
    for j in range(n-i+1):
        print(end=" ")

        past=fct(i)/(fct((i-j))*fct(j),end=" ") 



from math import factorial as fct
# input n
n = int(input())
arr=[]
for i in range(n):
    for j in range(n-i+1):
 
        # for left spacing
        #print(end=" ")
 
        for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
            #arr.append((fct(i)//(fct(j)*fct(i-j))))
            print(fct(i)//(fct(j)*fct(i-j)), end=" ")
 
    # for new line
    print()  '''


from math import factorial as fct

n=int(input())

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(fct(i)/(fct(j)*fct(i-j)), end=" ")

