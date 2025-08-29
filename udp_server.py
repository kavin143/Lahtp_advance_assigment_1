import socket
import pyfiglet

# The pyfiglet is used for asscii banners prints
ascii_banner = pyfiglet.figlet_format("UDP SERVER")
print(ascii_banner)

HOST = "" # Empty Host "" it will receive any interface like wifi,Ethernet etc.. 
PORT = 8898

# To create an Socket connection
# when we use with statement it atoumaticaly close the socket connection we dont want to close (s.CLOSE())
# IN UDP we use the SOCK_DGRAM
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    # To Bond the HOST And PORT
    s.bind((HOST,PORT))

    print("========= UDP Server ===========\n")
    print(f"[*] Listening on port {PORT}...")

    while True:
        
        # In UDP we Receive the data from using recvform() 
        data,addr=s.recvfrom(1024)
        if not data:
            break
        
        server_msg=b"Message was received"
        s.sendto(server_msg)
   
        # print The  client detials 
        print("-"*50)    
        print(f"Message from {addr[0]} and the client Message is :{data.decode()}")
