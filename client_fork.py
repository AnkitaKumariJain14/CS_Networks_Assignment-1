import socket
import os
import random
import time

class Client_fork:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_connection()
    def server_connection(self):
        self.host = socket.gethostname()
        self.port = 12345
        try:
            self.sock.connect((self.host,self.port))
        except socket.error as e:
            print(str(e))
        self.main()

    def new_conn(self):
        self.sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def main(self):
            server_file = 'war.txt'
            #server_file = input('Enter File Name to be fetched from server: ') #inputs file to be fetched
            server_file_size = os.path.getsize(server_file)
            self.sock.send(server_file.encode())
            i = str(random.randint(1,20))
            confirm = self.sock.recv(32)
            if confirm.decode() == "file-doesnt-exist": 
                print("File doesnt exist on server") #Prints error if file doesnt exist
                  
            else: 
                write_file_name = 'From-server_'+i+server_file # Name for the client file
                if os.path.exists(write_file_name): 
                    os.remove(write_file_name) #removes file if already exists
                
                with open(write_file_name, 'wb') as file:
                    start_time = time.time()
                    while True:
                        data = self.sock.recv(1024)

                        if not data:
                            break
                        file.write(data) #Writes file from server
                    end_time = time.time()
                print(server_file, 'Succesfully Downloaded')
                print("\nFile transfer Complete.Total time: ", end_time - start_time, "s")
                print("Throughput:", (server_file_size)/((end_time-start_time)*(10**6)), "MBps")

            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
                #cont = input("Do you want to continue (y/n)?")
                #if(cont == 'y'):
                #    self.new_conn()
                #else:
                  #break

client = Client_fork()