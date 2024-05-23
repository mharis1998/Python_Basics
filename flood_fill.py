import numpy as np

matrix=np.array([[1,1,1],
                 [1,1,0],
                 [1,0,1]
                 ])

#print(matrix)
add=lambda x:2 if x==1 else x
#print(add(0))

def toggle(num):
    if num==1:
        num=2
    else:
        num=num


def flood_fill(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j]==1:
                if i+1<=2 and j+1<=2 and j>=0 and i>=0:
                    mat[i+1][j]=add(mat[i+1][j])
                    mat[i][j]=add(mat[i][j])
                    mat[i-1][j]=add(mat[i-1][j])
                    mat[i][j+1]=add(mat[i][j+1])
                    mat[i][j-1]=add(mat[i][j-1])
    return mat

mat=flood_fill(matrix)
print(mat)