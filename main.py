# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

all_data = []
dict = dict()
start = {}
node_visited = []
node_reach = []
node_updated = []
def read_data():
    fr = open("data.txt", "r") # 设置文件对象
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split(',')
        newline = [0, 0, 0]
        newline[0] = (int(listFromLine[0]))
        newline[1] = (int(listFromLine[1]))
        newline[2] = (float(listFromLine[2]))
        all_data.append(newline)
    fr.close()

def dijkstra():
    while (bool(dict)):
        min_dis = min(zip(dict.values(), dict.keys()))
        node = min_dis[1]
        if node not in node_visited: #Node not visited
                for d in all_data:
                    if d[0] == node:     #Find this node
                        if d[1] in dict.keys():
                            res1 = float(dict[node])
                            res2 = float(d[2])
                            #if d[1] ==99:
                            #print(node,min_dis[0],res1 + res2)
                            if float(dict[d[1]]) > res1 + res2:   #New distance smaller
                                dict[d[1]] = res1 + res2
                                node_updated.append(d[1])
                            else:
                                continue

        del dict[node]
        start[node]= min_dis[0]
        node_visited.append(node)

def main():
    read_data()
    for item in all_data:
        if item[0] == 0:
            dict[int(item[1])]=item[2]
    node_reach.append(item[0])
    for i in range(1,99):
        if i in dict.keys():
            continue
        if i not in dict.keys():
            dict[i] = float("inf")
    node_visited.append(0)
    dijkstra()
    print('Distance between 0 and 99 is ' + str(start[99]))

if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
