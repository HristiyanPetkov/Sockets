import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("34.77.60.185", 8080))
    
info = input("Enter 'time', 'weather' or 'airquality': ")
s.send(pickle.dumps(info))

return_info = s.recv(1024)
return_info = pickle.loads(pickle.loads(return_info))

s.close()

print(return_info)
