from telnetlib import Telnet

def connect(HOST,PORT):
    tn = Telnet(HOST,PORT)
    return tn
pass
estado = 0
def mover(tn,direccion):
    global estado
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

def mover2(tn,direccion):
    if direccion == 2:
        tn.write(b'CALL motors setvel2mtr 1 100 0 100')
    elif direccion == 3:
        tn.write(b'CALL motors setvel2mtr 0 100 1 100')
    elif direccion == 0:
        tn.write(b'CALL motors setvel2mtr 0 0 0 0')
    elif direccion == 1: 
        tn.write(b'CALL motors setvel2mtr 0 100 0 100')
pass

def test(tn):
    tn.write(b'CALL motors testMotors')