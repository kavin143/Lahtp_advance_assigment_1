# import a socket package
import pyfiglet
import socket as s
import sys
import threading
from datetime import datetime

""" The pyfiglet is used for asscii banners prints it gives

 ____   ___  ____ _____     ____   ____    _    _   _ _   _ _____ ____          ______   __  _  __    ___     _____ _   _
|  _ \ / _ \|  _ \_   _|   / ___| / ___|  / \  | \ | | \ | | ____|  _ \       | __ ) \ / / | |/ /   / \ \   / /_ _| \ | |
| |_) | | | | |_) || |     \___ \| |     / _ \ |  \| |  \| |  _| | |_) |      |  _ \\ V /  | ' /   / _ \ \ / / | ||  \| |
|  __/| |_| |  _ < | |      ___) | |___ / ___ \| |\  | |\  | |___|  _ <       | |_) || |   | . \  / ___ \ V /  | || |\  |
|_|    \___/|_| \_\|_|     |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\      |____/ |_|   |_|\_\/_/   \_\_/  |___|_| \_|

""" 
ascii_banner = pyfiglet.figlet_format("PORT SCANNER BY KAVIN")
print(ascii_banner)
print("="*50)

# Function for Scaning a Port for Target IP
def scan_port(target,port,results):
    
    try:
            # To create an Socket
            sock=s.socket(s.AF_INET,s.SOCK_STREAM)
            sock.settimeout(1) # 1 second timeout
            # print("the connection created ")
        
            # print("List of ports:",port)

            # to Attempt a Connection for Target Ip and Port 
            result=sock.connect_ex((target,port))
            # print("The Result is :",result)

            
            if result == 0 :
                # To Append the port are Open
                results.append(port)
            
            sock.close()

    except sock.error as err: 
        print (f"socket creation is failed {err}")


# Function for make a Port Scanner as a multi threading port Scanner 
def threads_for_port_Scanning(target_ip,port_start,port_end):
    
    print(f"The target IP Address is : {target_ip}")
    print(f"Start Port : {port_start}")
    print(f"End Port   : {port_end}")

    
    open_ports=[]
    threads =[]

    for port in range(port_start,port_end + 1):
        thread=threading.Thread(target=scan_port,args=(target_ip,port,open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
    print("="*50)
    print(f"Scanning completed at: {datetime.now()}")
    print(f"Open ports: {sorted(open_ports)}")
    return sorted(open_ports)



if __name__ == "__main__":
   
    Domain=input("Enter your Target Domain :")

    print("****************Enter the Port Range*****************")
    port_start=int(input("Enter the Start Port :"))
    port_end=int(input("Enter the End Port :"))


    try:
        # To get a target Domain name to convert into IP  
        Target_IP=s.gethostbyname(Domain)
    
    except s.gaierror:
        print("The Ping Has not work")
        sys.exit()

    threads_for_port_Scanning(Target_IP,port_start,port_end)



