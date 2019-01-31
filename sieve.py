def sieve(n):
    from math import sqrt
    A=range(2,n+1)
    i=0
    while A[i]<sqrt(n):
        k=0
        while (A[i])**2+k*A[i]<n:
            if (A[i])**2+k*A[i] in A:
                A.remove((A[i])**2+k*A[i]) 
            k=k+1
        i=i+1
    return(A)
