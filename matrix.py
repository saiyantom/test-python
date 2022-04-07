# Matrix Addition

mata=[[2,6,9,10],[7,0,3,7],[8,4,5,6]]
matb=[[1,4,9,5],[2,5,8,6],[3,7,6,1]]
matc=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for row in range (len(mata)):
    for col in range (len(mata[row])):
        matc[row][col] = mata[row][col] + matb[row][col]

print(matc)
