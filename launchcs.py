#!/usr/bin/python
from os import popen as runCommand
from time import sleep

SERVER_NUMBER = 17

def init() -> None:
    """
    Try opening the serverlist.txt file to read the list of running servers.
    Then launch the menu passing it the file content.
    When exiting the menu, write the list of running servers to the file.
    """
    print("Welcome to the CS2 server launcher!")
    runningServers = []
    try:
        runningServersFile = open("serverlist.txt", "r")
        for line in runningServersFile.readlines():
            try:
                num = int(line)
                runningServers.append(num)
            except ValueError:
                print("Invalid server list file. Discarding...")
    except FileNotFoundError:
        print("Server list file not found. Discarding...")
    
    menu(runningServers)
    
    with open("serverlist.txt", "w") as runningServersFile:
        for server in runningServers:
            runningServersFile.write(f"{server}\n")

def menu(runningServers: list[int]) -> None:
    """
    The main menu, where the user can choose to launch, terminate or exit the program.
    Args:
        runningServers (list[int]): The list of running servers.
    """
    while True:
        print("############################")
        print("# CS2 Server Launcher Menu #")
        print("############################")
        print("1. Launch n instances of CS")
        print("2. Terminate all instances of CS in the server list")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            launch(runningServers)
            sleep(2)
        elif choice == '2':
            terminate(runningServers)
            sleep(2)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

def launch(runningServers: list[int]) -> None:
    """
    Launch n instances of the CS2 server.
    Args:
        runningServers (list[int]): The list of running servers.
    """
    try:
        n = int(input(f"Enter the number of instances to launch (available: {SERVER_NUMBER - len(runningServers)}): "))
    except ValueError:
        print("Invalid input. Try again.")
        launch(runningServers)
        return
    
    i = 0
    while i <= n-1:
        if i >= SERVER_NUMBER:
            print("Maximum number of servers reached.")
            break
        if i not in runningServers:
            runCommand(f"cs2-server @server{i} start")
            runningServers.append(i)
        else:
            n+=1
        i += 1

def terminate(runningServers: list[int]) -> None:
    """
    Terminate all instances in the server list file.
    Args:
        runningServers (list[int]): The list of running servers.
    """
    for server in runningServers:
        runCommand(f"cs2-server@server{server} stop")
        runningServers.remove(server)

if __name__ == "__main__":
    init()
