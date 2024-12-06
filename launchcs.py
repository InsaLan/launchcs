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
        case "run":
            if numberOfServer > len(stoppedServers):
                print(f"Can't launch this much servers, {len(servers)} are found and {len(runningServers)} are running!")
                return
            for server,_ in zip(stoppedServers, range(numberOfServer)):
                launchServer(server)
            print("Run successfully !")
        case "stop":
            if numberOfServer > len(runningServers):
                print(f"Can't stop launch this much servers, {len(runningServers)} are running out of the {len(servers)} found")
                return
            for server,_ in zip(runningServers, range(numberOfServer)):
                closeServer(server)
            print("Stop successfully !")
        case _:
            print("Invalid action, please use 'run' or 'stop', here is the help:")
            arguments.print_help()

def initializeParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="Launch CS Servers" ,description="Launch or stop a number of CS2 servers", usage="%(prog)s action numberOfServer")
    parser.add_argument("action", type=str, help="The action to perform, either 'run' or 'stop'")
    parser.add_argument("numberOfServer", type=int, help="The number of server to run or stop")
    return parser

def getServerList() -> list[str]:
    return [f.name[5:] for f in pathlib.Path(INSTANCES_PATH).iterdir() if f.is_dir() and f.name.startswith("inst")]

def launchServer(server: str) -> None:
    runCommand(f"cs2-server @{server} start", shell=True)

def closeServer(server: str) -> None:
    runCommand(f"cs2-server @{server} stop", shell=True)

def getRunningServers(serverList: list[str]) -> list[str]:
    return [server for server in serverList if b"STOPPED" not in runCommand(f"cs2-server @{server} status", shell=True, capture_output=True).stdout]

if __name__ == "__main__":
    #main()
    test()
