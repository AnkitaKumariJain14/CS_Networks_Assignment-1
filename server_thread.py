import os
import socket
import threading
#import tqdm

class Server_Thread:
 def __init__(self):
    self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # AF_INET Specifies IPv4 address and SOCK_STREAM specifies TCP communication
    self.connection_accept()


 def connection_accept(self):
    ip = socket.gethostname()
    port = 12345  
    Threadcount = 0
    try:
        self.sock.bind((ip,port))
    except socket.error as e:
        print(str(e))
    print('Waiting for a connection')
    self.sock.listen(10) #queue capacity is 10

    while True:
            connection,addr = self.sock.accept()
            print('Connected to:' + addr[0] + ":" + str(addr[1]))  # Connected to IP addr: Port
            Threadcount +=1
            threading.Thread(target=self.handle_client,args=(connection,addr,Threadcount)).start()
            print('Thread Number:' + str(Threadcount)) 
    self.sock.close()

 def handle_client(self,connection,addr,i):
            data = connection.recv(32).decode() #32 bytes buffer size #Used to input file name needed for download
            size1 = os.path.getsize(data)
            if not os.path.exists(data): #checks if file exists
                connection.send("file-doesnt-exist".encode()) #sends a "File doesnt exist" message to client 
                print("File does not exist") # Prints msg at server end
            else:  
                connection.send("file-exists".encode()) # Sends a File exists message 
                #progress = tqdm.tqdm(range(int(size1)), f"Sending {data}", unit="B", unit_scale=True, unit_divisor=1024)
                print('Sending',data) 
                if data != '':
                    file = open(data,'rb')
                    data = file.read(1024)
                    while data:
                        connection.send(data) #Sends data to Client 
                        data = file.read(1024) 
                        #progress.update(len(data))
                    print("File Sent")
                    connection.shutdown(socket.SHUT_RDWR) # Used to close the connection but still allows server to listen
                    connection.close() #Used to close the socket 


server = Server_Thread()
