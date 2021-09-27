#0移动至末尾
list_merge = [2, 0, 0, 2]
def zero_to_end():
    global list_merge
    for index in range(-1 , -len(list_merge) -1 , -1):
        if list_merge[index] == 0:
            del list_merge[index]
            list_merge.append(0)

#相同元素合并
def merge():
    zero_to_end()
    for index in range(len(list_merge) - 1):
        if list_merge[index] == list_merge[index + 1]:
            list_merge[index] += list_merge[index + 1]
            del list_merge[index + 1]
            list_merge.append(0)

map = [
    [2, 4, 4, 2],
    [2, 4, 4, 2],
    [0, 4, 2, 0],
    [2, 0, 2, 0]
]

def move_left():
    global list_merge
    for line in map:        
        list_merge = line
        merge()

def move_right():
    global list_merge
    for line in map:        
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge

def square_matrix_tranpose(matrix):
    for c in range(len(matrix) - 1):
        for r in range(c + 1, len(matrix)):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

def move_up():
    global list_merge
    global map
    square_matrix_tranpose(map)
    move_left()
    square_matrix_tranpose(map)

def move_down():
    global list_merge
    global map
    square_matrix_tranpose(map)
    move_right()
    square_matrix_tranpose(map)

# print(map)
# move_down()
# print(map)