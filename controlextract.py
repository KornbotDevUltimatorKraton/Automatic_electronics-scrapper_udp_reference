import os
import socket
import psycopg2 # Getting the database function to save the json file in the cloud 
import pickle # using the pickle to dump list data in array list 
import subprocess
from flask import Flask,render_template,url_for,redirect # Getting the flask 

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = "127.0.0.1"


username = str(subprocess.check_output("uname -a",shell=True)) # Get the the username of the computer reading from the client computer 
Getusername = username.split("-")[0].split(" ")[1]  #Get the username
HOME_PATH = "/home/"+str(Getusername)+"/Automaticsoftware/"
EXTRACT  = "/home/"+str(Getusername)+"/Automaticsoftware/tempolarydocextract" #Tempolary read the file extraction from the pdf specification function
PATHMAIN = "/home/"+str(Getusername)+"/Automaticsoftware/ComponentDoc"   # Getting the document page 
CONFIG   = "/home/"+str(Getusername)+"/Automaticsoftware/Configuresearch" # Config file
TI_product  = "/home/"+str(Getusername)+"/Automaticsoftware/TI_product"
NXP_product = "/home/"+str(Getusername)+"/Automaticsoftware/NXP_product"
ST_product = "/home/"+str(Getusername)+"/Automaticsoftware/ST_product"

TI_motor_drive  = "/home/"+str(Getusername)+"/Automaticsoftware/TIpro/TI_motordriver"
TI_bms  = "/home/"+str(Getusername)+"/Automaticsoftware/TIpro/TI_BMS"
TI_sensor  = "/home/"+str(Getusername)+"/Automaticsoftware/TIpro/TI_sensor"

NXP_interfaces = "/home/"+str(Getusername)+"/Automaticsoftware/NXPpro/NXP_interface"
NXP_multiplexer = "/home/"+str(Getusername)+"/Automaticsoftware/NXPpro/NXP_multiplexer"

ST_motordriver = "/home/"+str(Getusername)+"/Automaticsoftware/STpro/ST_motordriver"
ST_sensor =  "/home/"+str(Getusername)+"/Automaticsoftware/STpro/ST_sensor"
ST_microcontroller  =  "/home/"+str(Getusername)+"/Automaticsoftware/STpro/ST_mcus"

directcreate = ['tempolarydocextract','ComponentDoc','Configuresearch','TI_product','NXP_product','ST_product'] #list of the directory to create file
print("Create directory and give permission.....")

DATABASE_URL = "postgres://deblnijnzpwins:0b338cb6d067f909fa72de09359f40e8a3089c76a216192a3ae1355c58d71f5e@ec2-3-229-127-203.compute-1.amazonaws.com:5432/d43p77fjhmtuf2"
Host = "ec2-3-229-127-203.compute-1.amazonaws.com"
Database = "d43p77fjhmtuf2"
Password = "0b338cb6d067f909fa72de09359f40e8a3089c76a216192a3ae1355c58d71f5e"
Port = "5432"
list_path = ['TI_product','NXP_product','ST_product']
list_subpath = ['TI_motor_drive','TI_bms','TI_sensor','NXP_interfaces','NXP_multiplexer','ST_motordriver','ST_sensor','ST_microcontroller']
dict_manufacture = {'TI':'TI_product','NXP':'NXP_product','ST':'ST_product'}
dict_menudoct = {'TI_product':'TI_comdoc','NXP_product':'NXP_comdoc','ST_product':'ST_comdoc'} #component doct


data_com = list(dict_menudoct)[0]

listcomponents = dict_menudoct.get(data_com)
PATH_GEN = HOME_PATH + data_com +"/"+list_subpath[0]
while True:     
     listdirec  = os.listdir(PATH_GEN)
     message = pickle.dumps(listdirec)
     sock.sendto(message,(address,5050))   
