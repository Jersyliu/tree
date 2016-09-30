#!/usr/bin/env python3
import subprocess
import sys
import os
'''
def DFS(dirt, path, unicode, hasSibling):
	if os.path.isdir(dirt) == False:
		return ""
	result = ""
	listdir = os.listdir(dirt)
	#print (listdir)
	count = len(listdir)
	for (i,file) in enumerate(listdir):
		if file[0] == ".":
			continue
		if i == count-1:
			result += 
		if os.path.isdir(dirt+"/"+file):
			if i == count-1:
				result += DFS()
			result += (path+unicode["notTheLast"]+file+"\n")
			if path == "" or path[-4:] == "    " :
				result += DFS(dirt+"/"+file, path+unicode["nextLevel1"], unicode)
			else:
				result += DFS(dirt+"/"+file, path+unicode["nextLevel2"], unicode)
		else:
			if i == count-1:
				result += (path+unicode["theLast"]+file+"\n")
			else:
				result += (path+unicode["notTheLast"]+file+"\n")
	return result
	'''

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
	argv = ["python","."]
	unicodedic = {"notTheLast":u"\u251c\u2500\u2500 ", "theLast":u"\u2514\u2500\u2500 ", "nextLevel1":u"\u2502   ", "nextLevel2":"    " }
	result = [argv[1]+"\n",-1,1]
	path = ""
	DFS(argv[1], path,result, unicodedic)
	print (result[0])
	print (str(result[1])+" directories, "+str(result[2])+" files")
	
	
