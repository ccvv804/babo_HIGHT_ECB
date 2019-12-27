import ctypes
import io
import sys
import platform

def decrypt(fff):          
    if platform.system() == 'Windows':
        Highttest = ctypes.cdll.LoadLibrary("./KISA_HIGHT_ECB.dll")
    elif platform.system() == 'Linux':
        Highttest = ctypes.cdll.LoadLibrary("./KISA_HIGHT_ECB.so")
    Highttest.HIGHT_Decrypt.restype = ctypes.c_byte
    zerodata11=bytes(136)
    zerodata1=bytes(8)
    keyfile=open('key.hex',"rb")
    keydata=keyfile.read()
    keyfile.close
    hightfunc1 = Highttest.HIGHT_KeySched(keydata, 16, zerodata11)
    global fff_out
    fff_out = b''
    c=0
    a=1
    b=1
    d=0
    zzokzzokyaong=io.BytesIO(fff)
    while True:
        fileobj=zzokzzokyaong.seek(0+c)
        #print(c)
        eht=fileobj=zzokzzokyaong.read(8)
        #print(eht)
        if eht == b'' :
            print('read end')
            break
        outdata = eht
        hightfunc2 = Highttest.HIGHT_Decrypt(zerodata11, outdata)     
        fff_out = fff_out+outdata
        c=c+8
        a=a+1
        
def encrypt(fff):            
    if platform.system() == 'Windows':
        Highttest = ctypes.cdll.LoadLibrary("./KISA_HIGHT_ECB.dll")
    elif platform.system() == 'Linux':
        Highttest = ctypes.cdll.LoadLibrary("./KISA_HIGHT_ECB.so")
    Highttest.HIGHT_Encrypt.restype = ctypes.c_byte
    zerodata11=bytes(136)
    zerodata1=bytes(8)
    keyfile=open('key.hex',"rb")
    keydata=keyfile.read()
    keyfile.close
    hightfunc1 = Highttest.HIGHT_KeySched(keydata, 16, zerodata11)
    global xff_out
    xff_out = b''
    c=0
    a=1
    b=1
    d=0
    zzokzzokyaong=io.BytesIO(fff)
    while True:
        fileobj=zzokzzokyaong.seek(0+c)
        #print(c)
        eht=fileobj=zzokzzokyaong.read(8)
        #print(eht)
        if eht == b'' :
            print('read end')
            break
        outdata = eht
        hightfunc2 = Highttest.HIGHT_Encrypt(zerodata11, outdata)     
        xff_out = xff_out+outdata
        c=c+8
        a=a+1        

def encrypt_load(r):
    ppp=open(r,"rb")
    pppfxfx = ppp.read()
    ppp.seek(0)
    pppp=ppp.read()
    ppp.close

    encrypt(pppp)

    www=open('e'+r,"wb")
    www.write(xff_out)
    www.close
    
def decrypt_load(r):
    ppp=open(r,"rb")
    pppfxfx = ppp.read()
    ppp.seek(0)
    pppp=ppp.read()
    ppp.close

    decrypt(pppp)

    www=open('d'+r,"wb")
    www.write(fff_out)
    www.close
    
r1=sys.argv[1]
r2=sys.argv[2]

if r2 == 'e' :
    encrypt_load(r1)
elif r2 == 'd' :
    decrypt_load(r1)