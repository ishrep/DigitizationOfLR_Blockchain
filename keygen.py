import rsa
import hashlib
from os.path import exists

def generateKeys(username):
    
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('publicKey/'+username+'.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('privateKey/'+username+'.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def getPrivateKey(username):
    file_exists = exists('privateKey/'+ username + '.pem')
    if file_exists == False:
        generateKeys(username)
    with open('privateKey/'+ username + '.pem', 'rb') as p:
        PrivateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return PrivateKey

def getPublicKey(username):
    with open('publicKey/'+username+'.pem', 'rb') as p:
        PublicKey = rsa.PublicKey.load_pkcs1(p.read())
    return PublicKey

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode(encoding = 'utf8')
    except:
        return False

def signmsg(msg, key):
    msg = hashlib.sha256(msg.encode()).hexdigest
    msg = str(msg)
    msg = msg.encode(encoding = 'utf8')
    return rsa.encrypt(msg, key)

def verifysign(msg,signature, key):
    msg = hashlib.sha256(msg.encode()).hexdigest
    msg = str(msg)
    return rsa.decrypt(signature, key)

def verify(message, signature, key):
    return rsa.verify(message, signature, key)
