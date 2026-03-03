#!/usr/bin/python3
from subprocess import run

def getDedServer():
    dedLine = []
    serverList = run("/home/cs-servers/launchcs/launchcs.py list", shell=True, capture_output=True).stdout.decode("utf-8")
    for line in serverList.split("\n"):
        if "stopped" in line:
            dedLine.append(line)
    ded = []
    for dedServer in dedLine:
        serverString = dedServer.split()[1]
        ded.append(serverString)
    return ded

def rebootDed():
    dedServers = getDedServer()
    for server in getDedServer():
        run(f"cs2-server @{server} start", shell=True)

rebootDed()
