from keygen import *
msg = "ishanrishabh7yashdany"
pubkey = getPublicKey("ishan")
privkey = getPrivateKey("ishan")
msg = msg.encode()
signature = rsa.sign(msg,privkey,'SHA-256')
print(signature)
file = open('text.bin',"wb")
file.write(signature)
file.close()
signature = b''
file = open('text.bin','rb')
signatures = file.readlines()
for x in signatures:
    signature = b''.join([signature, x])
print(signature)
print(verify(msg,signature,pubkey))