def NAND (A, B):
    return not(A and B)

def NOT(A):
    return NAND(A,A)

def AND(A, B):
    return NOT(NAND(A, B))

def OR(A, B):
    return NAND(NOT(A), NOT(B))

environments = [(0 ,0) ,(0 ,1) ,(1 ,0) ,(1 ,1) ]

for env in environments :
    print ( env , AND (* env ) , OR (* env ) )