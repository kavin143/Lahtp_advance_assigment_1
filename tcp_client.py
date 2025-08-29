import socket
import pyfiglet


# The pyfiglet is used for asscii banners prints
ascii_banner = pyfiglet.figlet_format("TCP CLIENT")
print(ascii_banner)

HOST = "localhost"
PORT = 8898

# Function for TCP Server
def tcp_server(HOST,PORT):
    
    # To create an Socket connection
    # when we use with statement it atoumaticaly close the socket connection we dont want to close (s.CLOSE())
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        # TO connect to the HOST and PORT
        s.connect((HOST,PORT))

        # To Get the input
        print("========= TCP Cleint ===========\n")
        print("You Need send to the Message Press (1)")
        print("You need to exit Press (2)")
        choice=int(input("Enter the Choice : "))

        while True:
        
            if choice == 1:
                # TCP Messaging 
                client_msg=input("Enter the Message : ")
                print("If you need to quit type => (exit)")
                
                # Exit form the tcp server

                if client_msg.lower() == "exit":
                    print("Thank You For visting Us :)")
                    break
                # To send client Message to the server
                s.sendall(client_msg.encode())
                # To Receive the data from tcp server
                data=s.recv(1024)

                print(f"[Server]: {data.decode()}")
                print("="*50)
            # To exit form the tcp client server
            elif choice == 2:
                print("Thank You For visting Us :)")
                break

if __name__ == "__main__":
    tcp_server(HOST,PORT)