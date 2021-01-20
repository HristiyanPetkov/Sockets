import socket
from time import time, ctime

t = time()
real_time = ctime(t)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6732))
s.listen(10)

while True:

    c, address = s.accept()
    print("Socket running, connection from", address)
    
    while True:
        
        received_Data = c.recv(1024).decode('utf-8')

        if received_Data == 'weather':
        
            c.send(bytes('windy',"utf-8"))
            
        elif received_Data == 'time':
        
            c.send(bytes(real_time, 'utf-8'))
            
        elif received_Data == 'airquality':
        
            c.send(bytes('realy bad', 'utf-8')) 
            
        else: 
        
            c.send(bytes('N/A', 'utf-8'))
            c.close()
            break