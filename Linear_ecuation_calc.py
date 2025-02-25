from math import gcd
from functools import reduce
fin = open("input.txt","r")
A = fin.readlines()
linii_de_0 = 0

term_liberi = list(map(int, A[-1].strip().split()))
A.pop()

m = len(A)
for i in range(0, m):
    A[i] = list(map(int, A[i].strip().split()))

for i in range(0, m):
    A[i].append(term_liberi[i])

n = len(A[0])
print(f"m: {m}     n: {n}")
def print_mat():
    for line in A:
        print("|", end = " ")
        for el in line[:-1-linii_de_0]:
            print(el, end = " ")
        print("|", end = " ")
        for el in line[-1-linii_de_0:]:
            print(el, end = " ")
        print("|")
    print()

def sub(who, byWho, multiplier=1):
    for i in range(0,n):
        A[who][i] -= multiplier * A[byWho][i]

def swap_col(j1,j2):
    for i in range(0,m):
        A[i][j1],A[i][j2] = A[i][j2],A[i][j1]

def swap_line(line1,line2):
    A[line1],A[line2]=A[line2],A[line1]

print_mat()

### CALCULUL ECUATIEI LINIARE ###

for j in range(0,n):
    if j >= m:
        break

    # FACEM 1 PE PIVOTUL i j
    if A[j][j] != 1:
        for i in range(j+1,m):
            if A[i][j] != 0 and A[j][j] % A[i][j] != 0:
                print(A[j][j], A[i][j])
                while A[j][j] != 1:
                    if A[j][j] > A[i][j]:
                        sub(j,i)
                    elif A[j][j] < A[i][j]:
                        sub(i,j)
                    else: 
                        print(f"SUNT EGALE {A[j][j]} si {A[i][j]}")
                        break
    # FACEM 0 SUB PIVOTUL i j
    if A[j][j] == 1:
        for i in range(j+1,m):
            sub(i,j,A[i][j])

# VEDEM CATE LINII DE 0 AVEM

i = 0
while i < m-linii_de_0:
    if max(A[i]) == min(A[i]) == 0:
        swap_line(i,m-1-linii_de_0)
        linii_de_0 += 1
        i -= 1
    i += 1
m -= linii_de_0 # taiem liniile de 0

# MUTAM DUPA EGAL NEC. SECUNDARE
for i in range(m):
    for j in range(n-2,n-2-linii_de_0,-1):
        A[i][j] *= -1

# FACEM 0 DEASUPRA PIVOTILOR

for i in range(m-1,-1,-1):
    if A[i][i] != 1:
        print(f"EROARE: NU ESTE 1 PE PIVOTUL [{i},{i}]")
    for j in range(i-1,-1,-1):
        sub(j,i,A[j][i])

print(linii_de_0)

print_mat()
