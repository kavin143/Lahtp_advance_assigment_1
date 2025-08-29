import socket
import threading
import pyfiglet

# The pyfiglet is used for asscii banners prints
ascii_banner = pyfiglet.figlet_format("CHAT APPLICATION SERVER BY KAVIN")
print(ascii_banner)

HOST = "" # Empty Host "" it will receive any interface like wifi,Ethernet etc.. 
PORT = 8898

connections = {}  # {conn: nickname}

# Function for Handle the Clients 
def handle_client(conn, addr):

    conn.send("Connected Successfully! Use 'join' to register.\n".encode())
    # TO store th user name 
    nickname = None

    while True:

        try:
            # To recive the message 
            msg = conn.recv(1024).decode().strip()
            if not msg:
                break
            
            # To join the chat room  using join command 
            if msg == "join":
                conn.send("Enter Your Nickname :) : ".encode())

                nickname = conn.recv(1024).decode().strip()
                connections[conn] = nickname
                
                # TO Broadcast the message 
                broadcast(f"{nickname} joined the chat!", conn)
            
            # To start The message using msg command 

            elif msg == "msg":
                
                # if the user Not register means to intimate the Must To Register for this if statement use \
                if not nickname:
                    conn.send("Excuse You Must be Register please Type the (join) to join with Us:)\n".encode())
                    continue

                conn.send("Type your message: ".encode())
                # To get the message 
                message = conn.recv(1024).decode().strip()
                broadcast(f"{nickname}: {message}", conn)

            # Quit command is use to leave the chat
            elif msg == "quit":
                if nickname:
                    broadcast(f"{nickname} left the chat.", conn)
                conn.send("You left the chat.\n".encode())
                break
            
            else:
                conn.send("Invalid command! Use: join, msg, quit\n".encode())

        except:
            break

    if conn in connections:
        del connections[conn]
    conn.close()
    print(f"Connection closed: {addr}")

# Function for broadcast the message 
def broadcast(message, sender_conn):
    for client in connections:
        if client != sender_conn:
            try:
                client.send((message + "\n").encode())
            except:
                client.close()
                del connections[client]

# Function for start the server
def start_server(HOST, PORT):
    
    # To create an Socket connection
    # when we use with statement it atoumaticaly close the socket connection we dont want to close (s.CLOSE())

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        # To Bind the HOST And PORT
        s.bind((HOST, PORT))

        # TO Listen the connection
        s.listen()
        
        print(f"Server started on {HOST}:{PORT}")
        
        while True:
            
            # To accept the connection
            # addr it store the IP address and PORT 
            conn, addr = s.accept()
            print(f"Connected new Device => IP: {addr[0]} | PORT: {addr[1]}")
            
            # Threading for multiple user can message in the chat room
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()


if __name__ == "__main__":
    start_server(HOST, PORT)
