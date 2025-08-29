import socket
import pyfiglet

# The pyfiglet is used for asscii banners prints

ascii_banner = pyfiglet.figlet_format("BANNER GRABBER BY KAVIN")
print(ascii_banner)
print("="*100)

# Function for grab the banner 
def banner_grab(target_ip,port,host):

    try:
        # To create an Socket connection
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((target_ip,port))

        # This the syntax for get the banner
        # GET to send the get request HTTP/1.1 version
        # \r\n\r\n to break the server connection after get the request 
        request=f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
        sock.sendall(request.encode('utf-8'))

        while True:
            # TO receive the BANNER :
            banner=sock.recv(1024).decode(errors="ignore")
                # print(f"{banner}")

            if len(banner) == 0:
                break

            # To print the Banner
            print("=== Banner Grabbed ===")
            print(f"{banner.strip()}")
    except:
        pass



if __name__ == "__main__":
    # To get the Input form user 
    while True:

        print("\n=== Banner Grabber ===")
        print("You Want Grab the IP Press : (1)")
        print("You Want TO Exit Press : (2)")

        choice=int(input("Enter the Choice :"))

        if choice == 1:

            host=input("\tEnter the Domain Name :")
            port=int(input("\tEnter the Port NUmber :"))
            
            # convert the Domain Name into IP Address 
            target_ip=socket.gethostbyname(host)

        elif choice == 2:

            print("Thank You For visting Us :)")
            break

        # pass the input to banner_grab funtion
        banner_grab(target_ip,port,host)