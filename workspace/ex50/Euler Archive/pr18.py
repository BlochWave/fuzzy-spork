# Maximum path, sum I
# Problem 18

triangle = [
# j= 0   1  2   3   4  ...
    (75,),  # i = 0
    (95, 64,),  # i = 1
    (17, 47, 82,),  # i = 2
    (18, 35, 87, 10,),  # i = 3
    (20, 4, 82, 47, 65,),  # i = 4
    (19, 1, 23, 75, 3, 34,),  # i = 5
    (88, 2, 77, 73, 7, 63, 67,),  # i = 6
    (99, 65, 4, 28, 6, 16, 70, 92,),  # i = 7
    (41, 41, 26, 56, 83, 40, 80, 70, 33,),  # i = 8
    (41, 48, 72, 33, 47, 32, 37, 16, 94, 29,),  # i = 9
    (53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,),  # i = 10
    (70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,),  # i = 11
    (91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,),  # i = 12
    (63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,),  # i = 13
    (4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23,),  # i = 14
    ]
previous_row = (triangle[0][0]+triangle[1][0],triangle[0][0]+triangle[1][1]);

for i in range(2,len(triangle)):
    current_row = [];
    for j in range(len(triangle[i])):
        if j == 0:
            current_row.append(triangle[i][j] + previous_row[j]);
        elif j == len(triangle[i])-1:
            current_row.append(triangle[i][j] + previous_row[j-1]);
        else:
            current_row.append(max(previous_row[j],previous_row[j-1])+triangle[i][j]);
    previous_row = current_row;    

print max(previous_row);

