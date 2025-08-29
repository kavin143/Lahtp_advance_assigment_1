import socket
import threading
import pyfiglet

# To create an Socket connection
# when we use with statement it atoumaticaly close the socket connection we dont want to close (s.CLOSE())

ascii_banner = pyfiglet.figlet_format("CHAT APPLICATION CLIENT BY KAVIN")
print(ascii_banner)

HOST = "127.0.0.1"
PORT = 8898

# Function for Receving message from the server 
def receive_message(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print(msg)
        except:
            break

# Fucntion ofr  start the Client to chat 
def start_client(HOST, PORT):

    # To create an Socket connection
    # when we use with statement it atoumaticaly close the socket connection we dont want to close (s.CLOSE())

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_client:
        sock_client.connect((HOST, PORT))
       
        # Threading for multiple user can message in the chat room
        threading.Thread(target=receive_message, args=(sock_client,), daemon=True).start()

        print("========== Chat Application ===========")
        print("Connected to the chat server!")
        print("Commands:\n1. join\n2. msg\n3. quit")

        # To get the users messages 
        while True:
            msg = input("")
            sock_client.send(msg.encode())
            if msg.strip() == "quit":
                break

if __name__ == "__main__":
    start_client(HOST, PORT)
