r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

A = []
B = []

print("Enter elements of Matrix A:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)

print("Enter elements of Matrix B:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    B.append(row)
C = [[0 for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        C[i][j] = A[i][j] + B[i][j]

print("Result Matrix:")
for i in range(r):
    for j in range(c):
        print(C[i][j], end=" ")
    print()
