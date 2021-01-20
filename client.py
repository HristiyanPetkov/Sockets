import socket

reconnect= ''

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 6732))
    
    while True:
    
        info = input("What do you want information about: weather, time or airquality: ")
        s.send(bytes(info, 'utf-8'))   
        
        return_info = s.recv(1024).decode('utf-8')
        
        print("Server:", return_info)

        if return_info == 'N/A':
            s.close()
            break
            
    print("Disconnected from server!")
    
    reconnect = input("Do you want to reconnect(y/n): ")
    
    if reconnect == 'n':
        break
