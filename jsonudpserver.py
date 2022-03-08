import socket
import json 
import pickle
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
address = "127.0.0.1"
dict_info = {'Hello':'test test'} # dictionary data 
jsondata = json.dumps(dict_info)
message = pickle.dumps(jsondata)
sock.sendto(message,(address,5080)) # Sending the json data into the udp  
