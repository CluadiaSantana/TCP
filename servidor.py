import socket
import os
import nacl.utils

class randomPynacl():
    def __init__(self, bytes):
        self._bytes = bytes
        self._buf= nacl.utils.random(self._bytes)
    
    def changeBits(self,bytes):
        self._bytes = bytes
    
    def Random(self):
        self._buf= nacl.utils.random(self._bytes)

    def PrintRandom(self):
        for number in self._buf:
            print(f'{hex(number)[2:]}',end = " ")
    
    def strRandom(self):
        random=''
        for number in self._buf:
            random+= hex(number)[2:]
            random+=" "
        return random

# se crea el socket para el servidor
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#se pone el host de mi localhost y el port 5500 (es el que tengo configurado)
host="127.0.0.1"
port=5500
#se le asigna al servidor el host y el puerto
serversocket.bind((host,port))
#se configura para que empiece a escuchar
serversocket.listen(3)
print(f'El servidor esta escuchando en {host} puerto {port}')
#se crea el cliente para verificar que funcione y se conecta al servidor
clientso = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientso.connect((host,port))
#se crea el random que se mandara
random=randomPynacl(256)
random=random.strRandom()
while True: #siempre se estara escuchando
    # se aceptan conexiones del exterior
    (clientsocket, address) = serversocket.accept()
    print(f'Se ha conectado con el cliente {address}')
    #una vez conectado el cliente y el servidor se envia el random
    clientsocket.sendall(random.encode())
    print(f'Se ha enviado: \n{random}')
    print('\n---------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    while True:
        #se verifica que se reciba el random
        recived=clientso.recv(1024)
        print(f'Se ha recibido: \n{recived}')
