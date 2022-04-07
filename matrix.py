# Matrix Addition
mata=[[2,6,9],[7,0,3],[8,4,5]]
matb=[[1,4,9],[2,5,8],[3,7,6]]
matb=[[0,0,0],[0,0,0],[0,0,0]]

for row in range (len(mata)):
    for col in range (len(mata[row])):
        matc[row][col] = mata[row][col] + matb[row][col]

print(matc)
