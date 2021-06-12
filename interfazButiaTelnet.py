from telnetlib import Telnet

def connect(HOST,PORT):
    tn = Telnet(HOST,PORT)
    return tn
pass

def mover(tn,direccion,estado):
    if direccion == 2:
        tn.write(b'CALL motors setvel2mtr 1 100 0 100')
        estado = 1
    elif direccion == 3:
        tn.write(b'CALL motors setvel2mtr 0 100 1 100')
        estado = 1
    elif direccion == 0:
        if estado == 0:
            tn.write(b'CALL motors setvel2mtr 0 100 0 100')
            estado = 1
        elif estado == 1:
            tn.write(b'CALL motors setvel2mtr 0 0 0 0')
            estado = 0
pass