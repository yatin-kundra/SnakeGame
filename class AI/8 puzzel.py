# BFS
import copy
q = []
visited = []
h_list = []

def mini(h_list):
    mini = 10
    index = 0
    for i in range(len(h_list)):
        if mini>h_list[i]:
            mini = h_list[i]
        return index

def display(s):
    for i in s:
        print(i)
    print("-----------------------------------")

def emptybox(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 0:
                return ([i, j])

def distance(state, goal):      # heuristics
    simi = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == goal[i][j]:
                simi+=1
    return 9-simi




def up(s):
    pos = emptybox(s)
    i = pos[0]
    j = pos[1]

    if i > 0:
        s[i][j] = s[i - 1][j]
        s[i - 1][j] = 0
    return s


def down(s):
    pos = emptybox(s)
    i = pos[0]
    j = pos[1]

    if i < len(s)-1:
        s[i][j] = s[i + 1][j]
        s[i + 1][j] = 0
    return s


def left(s):
    pos = emptybox(s)
    i = pos[0]
    j = pos[1]

    if j>0:
        s[i][j] = s[i][j - 1]
        s[i][j - 1] = 0
    return s


def right(s):
    pos = emptybox(s)
    i = pos[0]
    j = pos[1]

    if j < len(s)-1:
        s[i][j] = s[i][j + 1]
        s[i][j + 1] = 0
    return s


def compare(s, r):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[j] == r[j]:
                continue
            else:
                return 0
    return 1

def search(s, g):
    global q
    global visited
    global h_list
    if compare(s, g):
        print("found")
        visited.append(s)
        exit()
    while(1):
        initial = copy.deepcopy(s)
        u = up(initial)
        h_list.append(distance(u, g))
        # display(initial)
        if initial == g:
            print("found")
            # print(len(visited))
            exit()
        else:
            if u not in visited and u not in q:
                q.append(u)

        initial = copy.deepcopy(s)
        d = down(initial)
        h_list.append(distance(d, g))
        # display(initial)
        if initial == g:
            print("found")
            # print(len(visited))
            exit()
        else:
            if d not in visited and d not in q:
                q.append(d)

        initial = copy.deepcopy(s)
        l = left(initial)
        h_list.append(distance(l, g))
        # display(initial)
        if initial == g:
            print("found")
            # print(len(visited))
            exit()
        else:
            if l not in visited and l not in q:
                q.append(l)
        initial = copy.deepcopy(s)
        ri = right(initial)
        h_list.append(distance(ri, g))
        # display(initial)
        if initial == g:
            print("found")
            # print(len(visited))
            # print(initial)
            exit()
        else:
            if ri not in visited and ri not in q:
                q.append(ri)

        if len(q) > 0:
            s = q[0]
            del q[0]
            print(s)
        else:
            print("goal state not possible.")
            exit()









def main():
    start = [[1, 2, 3],
             [8, 0, 4],
             [7, 6, 5]]

    goal = [[2, 8, 1],
            [0, 4, 3],
            [7, 6, 5]]



    # initial = copy.deepcopy(start)  # this is used to compare to the initial setting

    #    print(compare(start, goal))

    # print(initial)
    # pos = emptybox(initial)
    # u = up(pos, initial)
    # print(u)
    #
    # l = left(pos, initial)
    # print(l)
    #
    # d = down(pos, initial)
    # print(d)
    #
    # r = right(pos, initial)
    # print(r)
    #
    # print(start)


    # print(distance(start, goal))
    search(start, goal)



if __name__ == "__main__":
    main()