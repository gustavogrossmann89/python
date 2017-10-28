import socket
import struct
import binascii

OP_COOLER = (0x6E)
OP_LED = (0x6F)
OP_SENSOR = (0x22)
RESPONSE = (0x28)

HOST = '' # all interfaces
UDP_PORT = 8802
UDP_IP = "2804:7f4:3b80:c6e8:212:4b00:f28:c303"

#LIGA OS LEDS
#MESSAGE = struct.pack('>BB',OP_LED,1)
#DESLIGA OS LEDS
#MESSAGE = struct.pack('>BB',OP_LED,0)

#LIGA O COOLER
#MESSAGE = struct.pack('>BB',OP_COOLER,1)
#DESLIGA O COOLER
MESSAGE = struct.pack('>BB',OP_COOLER,0)

#SOLICITA O ESTADO DO SENSOR DE LUMINOSIDADE
#MESSAGE = struct.pack('>B',OP_SENSOR)

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
print 'Packed Value   :', binascii.hexlify(MESSAGE)

#PACOTES IPV6
sock = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
sock.bind((HOST,UDP_PORT))
sock.sendto(MESSAGE,(UDP_IP,UDP_PORT))

if binascii.hexlify(MESSAGE) == "22":
    while True:
        data, addr = sock.recvfrom(1024) #buffer size is 1024 bytes
        print "received message: ",binascii.hexlify(data), " from: [" , addr[0].strip()," ]: ",addr[1]
        
        dados = struct.unpack_from(">B",data,0)
        if dados[0] == RESPONSE:
            print "Recebeu RESPONSE"
            resposta = struct.unpack_from("<i",data,1)
            print "Valor do sensor de luminosidade: ", resposta[0]
            break
            pass
