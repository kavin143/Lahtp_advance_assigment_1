import socket
import pyfiglet


# The pyfiglet is used for asscii banners prints
ascii_banner = pyfiglet.figlet_format("TCP SERVER")
print(ascii_banner)

HOST = "" # Empty Host "" it will receive any interface like wifi,Ethernet etc.. 
PORT = 8898

# To create an Socket connection
# when we use with statement it atoumaticaly close the socket connection we dont want to close (s.CLOSE())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # To Bind the HOST And PORT
    s.bind((HOST, PORT))

    # TO Listen the connection 
    s.listen()

    print("========= TCP Server ===========\n")
    print(f"[*] Listening on port {PORT}...")

    # To accept the connection
    # addr it store the IP address and PORT 
    conn, addr = s.accept()
    
    #  TO print the Connected device detials like IP and PORT
    print(f"[+] Connected device -> IP: {addr[0]} | PORT: {addr[1]}\n")

    with conn:

        while True:
            # Receive the data from Client
            data = conn.recv(1024)

            # if data is not available to break
            if not data:
                break
            
            # To send the Message to client 
            server_msg=b"Message was received"
            conn.sendall(server_msg)
            
            # Print the client detials 
            print("-"*50)    
            print(f"Message from {addr[0]} and the client Message is :{data.decode()}")
