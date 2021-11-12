import os
import socket

class Server_fork:
 def __init__(self):
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_accept()

 def connection_accept(self):
        host = socket.gethostname()
        port = 12345
        i=1
        try:
           self.s.bind((host,port))
        except socket.error as e:
           print(str(e))
        print('Waiting for a connection')
        self.s.listen(10)
        
        while i<=10:
          c, addr=self.s.accept()
          child_pid=os.fork()
          if child_pid==0:
                print("\nConnection Successful with client " + str(i) + str(addr) + "\n")
                self.handle_client(c, addr, i)
                break
          else:
                i+=1
 def handle_client(self,connection, addr, i):
        data=connection.recv(32).decode()
        if not os.path.exists(data): #checks if file exists
          connection.send("file-doesnt-exist".encode()) #sends a "File doesnt exist" message to client 
          print("File does not exist") # Prints msg at server end
        else:
          connection.send("file-exists".encode()) # Sends a File exists message 
          print('Sending',data) 
          if data != '':
            file = open(data,'rb')
            data = file.read(1024)
            while data:
                connection.send(data) #Sends data to Client 
                data = file.read(1024) 

            connection.shutdown(socket.SHUT_RDWR) # Used to close the connection but still allows server to listen
            connection.close() #Used to close the socket 
        
server = Server_fork()
