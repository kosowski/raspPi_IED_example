import socket   #for sockets
import sys  #for exit
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()
 
host = 'localhost';
port = 8888;
 

msg = 'ola k ase'
 
try :
    #Set the whole string
    s.sendto(msg, (host, port))
    
except socket.error as msg:
    print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
