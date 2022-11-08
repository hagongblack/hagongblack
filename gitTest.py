import socket

UDP_IP = "172.20.202.22"
UDP_PORT = 65022
MESSAGE = b"Hello, Im 172.20.1.68\n"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))