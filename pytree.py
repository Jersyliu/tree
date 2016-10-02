#! / usr / bin / env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
import os
import string


def DFS(dirt, path, result, unicodedic):
    if not os.path.isdir(dirt):
        return
    result[1] += 1
    result[2] -= 1
    listdir = os.listdir(dirt)
    temp = []
    for i in listdir:
        if i[0] != ".":
            temp.append(i)
    listdir = sorted(temp, key=func)
    count = len(listdir)
    result[2] += count
    newpath = "{}{}".format(path, (unicodedic["nextLevel2"] if count == 1 else unicodedic["nextLevel1"]))
    for (i, filename) in enumerate(listdir):
        newdirt = dirt + " / " + filename
        if filename[0] == ".":
            result[2] -= 1
            continue
        if i == count - 1:
            result[0] = "{}{}".format(result[0], (path + unicodedic["theLast"] + filename + "\n"))
            DFS(newdirt, path + "    ", result, unicodedic)
        else:
            result[0] = "{}{}".format(result[0], (path + unicodedic["notTheLast"] + filename + "\n"))
            DFS(newdirt, newpath, result, unicodedic)
    return


def func(x):
    x = x.lower()
    if x[0] in string.ascii_lowercase:
        return x.lower()
    else:
        for (i, key) in enumerate(x):
            if key in string.ascii_lowercase:
                return x[i:]
if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append(".")
    unicodedic = {"notTheLast": "├── ", "theLast": "└── ", "nextLevel1": "│   ", "nextLevel2": "    "}
    result = [sys.argv[1] + "\n", - 1, 1]
    path = ""
    DFS(sys.argv[1], path, result, unicodedic)
    print(result[0])
    print(str(result[1]) + " directories, " + str(result[2]) + " files")
