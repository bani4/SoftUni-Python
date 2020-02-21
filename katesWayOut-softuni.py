maze = []
empty_spaces = []
Kate_posX = -1
Kate_posY = -1
count_spaces = 0
number_lines = int(input())
for i in range(number_lines):
    data = input()
    maze.append(list(data))
    for j in range(len(data)):
        if data[j] == ' ':
            empty_spaces.append([i, j])
        if data[j] == 'k':
            Kate_posX = i
            Kate_posY = j

count_spaces = len(empty_spaces)


def find_neighbours(sp1, sp2):
    neighbours = []
    for i in sp1:
        n1 = [i[0] - 1, i[1]]
        n2 = [i[0] + 1, i[1]]
        n3 = [i[0], i[1] - 1]
        n4 = [i[0], i[1] + 1]
        if n1 not in neighbours:
            neighbours.append(n1)
        if n2 not in neighbours:
            neighbours.append(n2)
        if n3 not in neighbours:
            neighbours.append(n3)
        if n4 not in neighbours:
            neighbours.append(n4)
    neighbours_to_be_removed = []
    for i in neighbours:
        if i not in sp2:
            neighbours_to_be_removed.append(i)
        else:
            sp2.remove(i)
    for t in neighbours_to_be_removed:
        neighbours.remove(t)
    sp1[::] = neighbours


def set_number_neighbour(n, sp3, sp4):
    for i in sp3:
        sp4[i[0]][i[1]] = n


nei = [[Kate_posX, Kate_posY]]
for i in range(count_spaces):
    find_neighbours(nei, empty_spaces)
    set_number_neighbour(i + 1, nei, maze)
steps = []
way_out = False
r = 0
c = 0
while r != len(maze) - 1 or c != len(maze[0]) - 1:
    if type(maze[r][c]) is int:
        way_out = True
        steps.append(maze[r][c])
    if maze[r][c] == 'k':
        way_out = True
        steps.append(0)
    if r == 0 or r == len(maze) - 1:
        if c == len(maze[0]) - 1:
            if r != len(maze) - 1:
                r += 1
            c = 0
        else:
            c += 1
    else:
        if c == len(maze[0]) - 1:
            r += 1
            c = 0
        else:
            c = len(maze[0]) - 1

if way_out:
    print(f'Kate got out in {min(steps) + 1} moves')
else:
    print('Kate cannot get out')