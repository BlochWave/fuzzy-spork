import time
start = time.time()
def euler67():
    f = open('p067_triangle.txt','r')
    data = []
    for line in f:
        data.append([int(j) for j in line.strip('\n').split(' ')])
    
    for i in range(-1,-len(data),-1):
        for j in range(len(data[i-1])):
            data[i-1][j] = data[i-1][j] + max(data[i][j],data[i][j+1])
    return data[0][0]

print euler67(), time.time() - start