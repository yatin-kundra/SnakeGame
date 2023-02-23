import copy
visited = []
q_queue = []

def enqueue(node):
    global visited
    global q_queue
    if node not in visited and node not in q_queue:
        q_queue.append(node)

def dequeue():
    global q_queue
    if len(q_queue) > 0:
        s = q_queue[0]
        s.append(visited)
        del q_queue[0]
        print(s)
        return s

    else:
        print("goal does not exist.")


def min_index():
    global h_list
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

def position_of_0(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 0:
                return ([i, j])

def heuristic(state, goal):      # heuristics
    simi = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == goal[i][j]:
                simi+=1
    return 9-simi

def up(s):
    pos = position_of_0(s)
    i = pos[0]
    j = pos[1]

    if i > 0:
        s[i][j] = s[i - 1][j]
        s[i - 1][j] = 0
    return s

def down(s):
    pos = position_of_0(s)
    i = pos[0]
    j = pos[1]

    if i < 2:
        s[i][j] = s[i + 1][j]
        s[i + 1][j] = 0
    return s

def left(s):
    pos = position_of_0(s)
    i = pos[0]
    j = pos[1]

    if j>0:
        s[i][j] = s[i][j - 1]
        s[i][j - 1] = 0
    return s

def right(s):
    pos = position_of_0(s)
    i = pos[0]
    j = pos[1]

    if j < len(s)-1:
        s[i][j] = s[i][j + 1]
        s[i][j + 1] = 0
    return s


def compare(s, g):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[j] == g[j]:
                continue
            else:
                return 0
    return 1

def search(s, g):
    global q_queue
    global visited
    # global h_list
    if compare(s, g):
        print("found")
        visited.append(s)
        exit()
    while(1):
        initial = copy.deepcopy(s)
        u = up(initial)

        if initial == g:
            print("found")
            exit()
        else:
            enqueue(u)

        initial = copy.deepcopy(s)
        d = down(initial)

        if initial == g:
            print("found")
            exit()
        else:
            enqueue(d)

        initial = copy.deepcopy(s)
        l = left(initial)
        if initial == g:
            print("found")
            exit()
        else:
            enqueue(l)
        initial = copy.deepcopy(s)
        r = right(initial)
        if initial == g:
            print("found")
            exit()
        else:
            enqueue(r)

        dequeue()



def main():
    start = [[1, 2, 3],
             [8, 0, 4],
             [7, 6, 5]]

    goal = [[2, 8, 1],
            [0, 4, 3],
            [7, 6, 5]]
    # print(type(start))
    search(start, goal)



if __name__ == "__main__":
    main()