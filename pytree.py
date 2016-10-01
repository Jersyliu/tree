#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
import subprocess
import sys
import os

def DFS(dirt,path,result,unicodedic):
	if os.path.isdir(dirt) == False:
		return
	result[1] += 1
	result[2] -= 1
	listdir = os.listdir(dirt)
	listdir.sort()
	count = len(listdir)
	result[2] += count
	newpath = path + (unicodedic["nextLevel2"] if count == 1 else unicodedic["nextLevel1"])
	for (i,filename) in enumerate(listdir):
		newdirt = dirt+"/"+filename
		if filename[0] == ".":
			result[2] -= 1
			continue
		if i == count-1:
			result[0] += (path+unicodedic["theLast"]+filename+"\n")
			DFS(newdirt, path+"    ", result, unicodedic)
		else:
			result[0] += (path+unicodedic["notTheLast"]+filename+"\n")
			DFS(newdirt, newpath, result, unicodedic)
	return

if __name__ == '__main__':
	#argv = ["python","."]
	
	if len(sys.argv) == 1:
		sys.argv.append(".")
	unicodedic = {"notTheLast":u"\u251c\u2500\u2500 ", "theLast":u"\u2514\u2500\u2500 ", "nextLevel1":u"\u2502   ", "nextLevel2":"    " }
	result = [sys.argv[1]+"\n",-1,1]
	path = ""
	DFS(sys.argv[1], path,result, unicodedic)
	print (str(result[0]))
	print (str(result[1])+" directories, "+str(result[2])+" files")
