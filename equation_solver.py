def compute_solns(temp):
    A=temp
    result=[0]
    result.insert(1,A)
    for _ in range(len(A)-2):
        
        n=len(A)-1
        a1=A[1][1]
        for j in range(1,n+2):
            A[1][j]/=a1
        
        temp=[0]
        
        for i in range(2,n+1):
            a1=A[i][1]
            #print(a1)
            temp.append([0])
            for j in range(1,n+2):
                A[i][j]=A[i][j]/a1-A[1][j]
                if j!=1:
                    temp[i-1].append(A[i][j])
        #print(A)
        A=temp
        result.insert(1,temp)
    return result


X=[0,[0,1,1,2],[0,1,-1,2]]
Y=[0,[0,1,1,2,9],[0,2,4,-3,1],[0,3,6,-5,0]]
y=[0,[0,1,1,2,9],[0,2,4,-3,1],[0,3,6,-5,0]]
Z=[0,[0,1,-3.50,-8.5],[0,1,-3.66,-9]]
Q=[0,[0,3,-2,5,4],[0,11,-3,7,8],[0,2,8,9,7]]
P=[0,[0,1,1,2],[0,1,-1,2]]
S=[0,[0,4,11,5],[0,6,8,9]]
W=[0,[0,6,-3,2,5,6],[0,9,8,4,3,-2],[0,3,5,-8,-2,11],[0,16,14,-8,3,0]]
#print(Z)
#for i in compute_solns(Y):
    #print(i)
#print(compute_solns(compute_solns(Y)))


def get_variable(A):
    
    X=[]
    n=len(A)-1
    for i in range(1,n+1):
        lhs=0
        for j in range(2,i+1):
            lhs+=A[i][1][j]*X[j-2]
        rhs=A[i][1][i+1]
        x=(rhs-lhs)/A[i][1][1]
        X.insert(0,x)
        
    print(X)
    
#get_variable(compute_solns(W))


print("Enter no. of variables/equations: ")
n=int(input())
I=[0]
for i in range(n):
    print("Enter coefficients of %rth equation separated by a space"%(i+1))
    print("Format: 3x+5y-7z=16 , Input: 3 5 -7 16")
    print()
    I.append([0]+list(map(int,input().split())))
    print(I)
get_variable(compute_solns(I))

