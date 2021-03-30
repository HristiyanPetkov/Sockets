import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 8080))
    
info = input("What do you want information about(weather, time or airquality): ")
s.send(pickle.dumps(info))

return_info = s.recv(1024)
return_info = pickle.loads(pickle.loads(return_info))

s.close()

print("Here is the information:", "\n", return_info)
