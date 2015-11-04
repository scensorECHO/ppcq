#Python PsTools Tool

import subprocess, os, sys

pspath = "C:\\Users\\Carrio\\Documents\\PsTools"
psinfo = pspath+"\\PsInfo.exe"
psexec = pspath+"\\PsExec.exe"
pslogd = pspath+"\\PsLoggedOn.exe"

pclist = []

with open('pcsheet.csv','r') as s:
	for p in s.readlines():
		print(p)
		pclist.append(p.strip().split(',')[0])

print(pclist)

infofile="C:\\Users\\Carrio\\Desktop\\ppstt\\info.txt"

log = []

with open(infofile,'w') as info:
	for pc in pclist:
		try:
			log.append(subprocess.check_output([psinfo,"\\\\"+pc]))
		except:
			print("Stupid calledprocesserrors")
	for line in log:
		info.write("%s\n" % line)
