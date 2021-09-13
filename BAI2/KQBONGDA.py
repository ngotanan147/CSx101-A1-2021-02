
team1 = []
team2 = []
for i in range(6):
    x, y, z = map(int, input().split())
    if (i > 2):
        team2.append([x, y, z])
    else:
        team1.append([x, y, z])


def printWinner(lst):
    point1 = 0
    diff1 = 0
    goal1 = 0
    fair1 = 0
    for item in lst:
        if (int(item[0]) > int(item[1])):
            point1 += 3
        if (int(item[0]) == int(item[1])):
            point1 += 1
        diff1 += item[0] - item[1]
        goal1 += item[0]
        fair1 += item[2]
    print(point1, diff1, goal1, fair1)


def solve(t1, t2):
    point1 = 0
    diff1 = 0
    goal1 = 0
    fair1 = 0
    for item in t1:
        if (int(item[0]) > int(item[1])):
            point1 += 3
        if (int(item[0]) == int(item[1])):
            point1 += 1
        diff1 += item[0] - item[1]
        goal1 += item[0]
        fair1 += item[2]

    point2 = 0
    diff2 = 0
    goal2 = 0
    fair2 = 0
    for item in t2:
        if (int(item[0]) > int(item[1])):
            point2 += 3
        if (int(item[0]) == int(item[1])):
            point2 += 1
        diff2 += item[0] - item[1]
        goal2 += item[0]
        fair2 += item[2]

    if (point1 > point2):
        printWinner(t1)
    else:
        if (point1 < point2):
            printWinner(t2)
        else:
            if (diff1 > diff2):
                printWinner(t1)
            else:
                if (diff1 < diff2):
                    printWinner(t2)
                else:
                    if (goal1 > goal2):
                        printWinner(t1)
                    else:
                        if (goal1 < goal2):
                            printWinner(t2)
                        else:
                            if (fair1 < fair2):
                                printWinner(t1)
                            else:
                                if (fair1 > fair2):
                                    printWinner(t2)
                                else:
                                    printWinner(t1)


solve(team1, team2)

# lst = [[0, 0, 7],
#        [9, 0, 0],
#        [7, 6, 1]]
# lst2 = [
#     [7, 7, 7],
#     [2, 1, 2],
#     [1, 0, 2]]
# lst1 = []
# lst1.append(diff(lst))
# print(lst1)
# print(diff(lst))
# print(goal(lst))
# print(fairPoint(lst))
