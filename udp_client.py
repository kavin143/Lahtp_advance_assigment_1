import socket
import pyfiglet

# The pyfiglet is used for asscii banners prints
ascii_banner = pyfiglet.figlet_format("TCP CLIENT")
print(ascii_banner)

HOST = "localhost"
PORT = 8898
# Function for UDP Server
def udp_client(HOST,PORT):

    # To create an Socket connection
    # when we use with statement it atoumaticaly close the socket connection we dont want to close (s.CLOSE())
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:

        print("========= UDP Cleint ===========\n")
        print("You Need send to the Message Press (1)")
        print("You need to exit Press (2)")

        # To Get the input
        choice=int(input("Enter the Choice : "))

        while True:
            if choice == 1:

                # UDP Message 
                client_msg=input("Enter the Message :")
                print("If you need to quit type => (exit)")

                # Exit form the UDP server
                if client_msg.lower() == "exit":
                    print("Thank You For visting Us :)")
                    break

                # In UDP sendto use to send Message to server 
                s.sendto(client_msg.encode(),HOST,PORT)

                # To receive the message 
                server_msg,=s.recvfrom(1024)
                print(f"[Server] : {server_msg.decode()}")
                print("="*50)

            # TO Exit form the client 
            elif choice == 2:
                print("Thank You For visting Us :)")
                break


if __name__ == "__main__":
    udp_client(HOST,PORT)