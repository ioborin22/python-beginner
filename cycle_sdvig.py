A = [1, 2, 3, 4, 5]
tmp = A[0]
N = len(A)
for k in range(N-1):
    A[k] = A[k+1]
A[N-1] = tmp

print(A)