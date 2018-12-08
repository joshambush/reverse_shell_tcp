# python2
# Make sure to run server before client
"""
Creater: Josh Ambush aka J Slump
Email: ambushslump5435@gmail.com
"""
import socket

def main():
    port = 5000 # could be any port
    host = '0.0.0.0' # all IP addresses on the local machine

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("[!] Waiting for connection to be established...")

    conn, addr = server_socket.accept()
    print("[$] Connected to " + str(addr) + " on port "+str(port)+ " | [*]Successful")

    while True:
        try:
            request = raw_input(str(addr) + ">")
            if(len(request.split()) != 0):
                conn.send(request)
            else:
                continue
        except(EOFError):
            print("command is invalid")
            continue
        if(request == "stop()"):
            break
        data = conn.recv(1024)
        print(data + '\n')
    conn.close()
if __name__ == "__main__":
    main()
