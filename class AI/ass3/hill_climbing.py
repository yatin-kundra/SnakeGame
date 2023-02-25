import copy
visited = []
q_queue = []
Heuristic_value = []


def min_index():
    global Heuristic_value
    mini = 10
    index = 0
    for i in range(len(Heuristic_value)):
        if mini > Heuristic_value[i]:
            mini = Heuristic_value[i]
            index = i
    return index


def enqueue(node):
    global visited
    global q_queue
    if node not in visited and node not in q_queue:
        q_queue.append(node)



def dequeue():
    global q_queue, Heuristic_value
    if len(q_queue) > 0:
        mini = 0
        mini = min_index()
        s = q_queue[mini]
        visited.append(s)
        # del q_queue[mini]
        # del Heuristic_value[mini]
        q_queue = []
        Heuristic_value = []
        # print(s)
        return s

    else:
        print("goal does not exist.")


def display(s):
    for i in s:
        print(i)
    print("-----------------------------------")


def position_of_0(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 0:
                return [i, j]


def heuristic(state, goal):      # heuristics
    simi = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == goal[i][j]:
                simi += 1
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

    if j > 0:
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


def search(s,g):
    global Heuristic_value
    count = 1
    if compare(s,g):
        print("Found")
        exit()

    while 1:
        initial = copy.deepcopy(s)
        u = up(initial)

        count += 1
        if initial == g:
            display(u)
            print("Found")
            print(count)
            exit()

        else:
            enqueue(u)
            if u in q_queue:
                Heuristic_value.append(heuristic(u, g))

        initial = copy.deepcopy(s)
        d = down(initial)

        count += 1
        if initial == g:
            display(d)
            print("Found")
            print(count)
            exit()


        else:
            enqueue(d)
            if d in q_queue:
                Heuristic_value.append(heuristic(d, g))

        initial = copy.deepcopy(s)
        l = left(initial)

        count += 1
        if initial == g:
            display(l)
            print("Found")
            print(count)
            exit()

        else:
            enqueue(l)
            if l in q_queue:
                Heuristic_value.append(heuristic(l, g))

        initial = copy.deepcopy(s)
        r = right(initial)

        count += 1
        if initial == g:
            display(r)
            print("Found")
            print(count)
            exit()

        else:
            enqueue(r)
            if r in q_queue:
                Heuristic_value.append(heuristic(r, g))

        s = dequeue()




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