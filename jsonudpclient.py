import json 
import socket 
import pickle
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ("127.0.0.1",5080) 
sock.bind(address)
while True: 
      data,addr = sock.recvfrom(1024)
      received  = pickle.loads(data)
      message = json.loads(received)
      #print(received,type(received),addr)
      print(message,type(message),addr)   