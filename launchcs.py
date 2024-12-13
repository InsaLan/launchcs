#!/usr/bin/python3
from subprocess import run as runCommand
import pathlib
import argparse

INSTANCES_PATH = "/home/cs-servers/msm.d/cs2"

def main() -> None:
    arguments = initializeParser()
    args = arguments.parse_args()
    action = args.action
    numberOfServer = args.numberOfServer
    servers = getServerList()
    runningServers = getRunningServers(servers)
    stoppedServers = [server for server in servers if runningServers == [] or server not in runningServers]
    match action:
        case "start":
            if numberOfServer > len(stoppedServers):
                print(f"Can't launch this much servers, {len(servers)} are found and {len(runningServers)} are running!")
                return
            elif numberOfServer == 0:
                print("Please specify the number of server to start")
                return
            for server,_ in zip(stoppedServers, range(numberOfServer)):
                launchServer(server)
            print("Start successfully !")
        case "stop":
            if numberOfServer > len(runningServers):
                print(f"Can't stop launch this much servers, {len(runningServers)} are running out of the {len(servers)} found")
                return
            elif numberOfServer == 0:
                print("Please specify the number of server to stop")
                return
            for server,_ in zip(reversed(runningServers), range(numberOfServer)):
                closeServer(server)
            print("Stop successfully !")
        case "list":
            print("Servers found:")
            for server in servers:
                print(f" - {server} {'(running)' if server in runningServers else '(stopped)'}")
        case _:
            print("Invalid action, please use 'start' or 'stop', here is the help:")
            arguments.print_help()

def initializeParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="launchcs" ,description="Launch or stop a number of CS2 servers", usage="%(prog)s action numberOfServer")
    parser.add_argument("action", type=str, choices=["start", "stop", "list"], help="The action to perform, either 'start', 'stop', or 'list'")
    parser.add_argument("numberOfServer", type=int, nargs='?', default=0, help="The number of server to start or stop")
    return parser

def getServerList() -> list[str]:
    return [f.name[5:] for f in sorted(pathlib.Path(INSTANCES_PATH).iterdir(), key=lambda f: (len(f.name), f.name)) if f.is_dir() and f.name.startswith("inst")]

def launchServer(server: str) -> None:
    runCommand(f"cs2-server @{server} start", shell=True)

def closeServer(server: str) -> None:
    runCommand(f"cs2-server @{server} stop", shell=True)

def getRunningServers(serverList: list[str]) -> list[str]:
    return [server for server in serverList if b"STOPPED" not in runCommand(f"cs2-server @{server} status", shell=True, capture_output=True).stdout]

if __name__ == "__main__":
    main()
