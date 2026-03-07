#!/usr/bin/env python3
from subprocess import run
from datetime import datetime

LAUNCHCS_CMD = "/home/cs-servers/scripts/launchcs.py"
CS2_SERVER_CMD = "/home/cs-servers/.local/bin/cs2-server"

def getDedServer():
    dedLine = []
    process = run(f"{LAUNCHCS_CMD} list", shell=True, capture_output=True)

    stdout_str = process.stdout.decode("utf-8")
    stderr_str = process.stderr.decode("utf-8")

    if stderr_str:
        print(f"ERROR launchcs.py : {stderr_str}")

    for line in stdout_str.split("\n"):
        if "stopped" in line:
            dedLine.append(line)

    ded = []
    for dedServer in dedLine:
        try:
            serverString = dedServer.split()[1]
            ded.append(serverString)
        except IndexError:
            pass
    return ded

def rebootDed():
    servers = getDedServer()

    for server in servers:
        process = run(f"{CS2_SERVER_CMD} @{server} start", shell=True, capture_output=True)
        print(f"[{datetime.now()}] - Revived {server}")

rebootDed()
