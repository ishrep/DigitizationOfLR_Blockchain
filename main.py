## initial (from to plotno)
## mempool (from to plotno)
## plot (plotno owner size)
## user (username password level)
## tempcred (username password 1 new_username new_password)
## tempinit (from to(temp_user) plot)
## userdet(new user details) (username aadhar name addr)
## userdetail(old user details) (username aadhar name addr)0

import datetime
import random
import hashlib
from tempfuncs import *
#from flask import Flask

class newuser:
    def __init__(self,details):
        self.username = details[0]
        self.password = details[1]
    
    def verify(self):
        while(True):
            self.user1 = input("Enter username: ")
            f11=open("users.txt","r")
            f=f11.readline()
            flag=0
            while(f!=''):
                f=f.split()
                if(f[0]==self.user1):
                    flag=1
                    break;
                f=f11.readline()
            if(flag):
                print("user already exists")
            else:
                self.pass1 = input("Enter password: ")
                self.level = 1
                break
        ff=open("userdet.txt","a")
        self.aadhar = input("Enter Aadhar number: ")
        self.name = input("Enter name: ")
        self.address = input("Enter Address: ")
        ff.write(self.user1+" "+self.aadhar+" "+self.name+" "+self.address + "\n")
        f=open("tempcred.txt","r")
        f1=f.readline()
        while(f1!=''):
            f1=f1.split()
            if(f1[0]==self.username):
                f.seek(0)
                te=f.readlines()
                te.remove(f1[0]+" "+f1[1]+" 0"+"\n")
                te.append(f1[0]+" "+f1[1]+" 1 "+self.user1+" "+self.pass1+"\n")
                f.close()
                f = open("tempcred.txt","w")
                f.writelines(te)
                f.close()
                break;
            f1=f.readline()


class user:
    def __init__(self,details):
        self.username = details[0]
        self.password = details[1]
        self.plots = self.getplots(details[0])

    def sell(self):
        plotno = input("Enter plot no: ")
        flag=0
        buyer=""
        plotexist = 0
        for plot in self.plots:
            if plot.plotno == plotno:
                newbuyer = input("Is he a new buyer: ")
                if newbuyer == "0":
                    buyer=input("Enter buyer ID: ")
                    if (buyer_checker(buyer)):
                        file = open("initial.txt","a")
                        file.write(self.username+" "+buyer+" "+plotno+"\n")
                    else:
                        print("No such user")
                    # add buyer_checker()
                    # create_transaction()
                else:
                    while True:
                        new_user = str(random.random())
                        new_pass = str(random.random())
                        #Checking temp creds
                        flag = temp_cred_checker(new_user, new_pass)
                        if(flag==0):
                            add_temp_creds(new_user, new_pass)
                            buyer = new_user
                            print("Temp username",new_user)
                            print("Temp password",new_pass)
                            break;
                    f3 = open("tempinit.txt","a")
                    f3.write(self.username+" "+buyer+" "+plotno+"\n")
                plotexist = 1
                break
        if plotexist ==0 :
               print("No such plot")
    
    def buy(self):
        f5=open("initial.txt","r")
        f6=f5.readline()
        flag=0
        while(f6!=''):
            f6=f6.split()
            if(f6[1]==self.username):
                flag=1
                print("Approve Plot from",f6[0],"against plot no",f6[2])
                inp = int(input("Choice: "))
                if(inp):
                    f5.seek(0)
                    te=f5.readlines()
                    te.remove(f6[0]+" "+f6[1]+" "+f6[2]+"\n")
                    f5.close()
                    f15=open("mempool.txt","a")
                    f15.write(f6[0]+" "+f6[1]+" "+f6[2]+"\n")
                    f5=open("initial.txt","w")
                    f5.writelines(te)
                    f5.close()
                    f5=open("initial.txt","r")
                else:
                    f5.seek(0)
                    te=f5.readlines()
                    te.remove(f6[0]+" "+f6[1]+" "+f6[2]+"\n")
                    f5.close()
                    f5=open("initial.txt","w")
                    f5.writelines(te)
                    f5.close()
                    f5=open("initial.txt","r")
            f6=f5.readline()
        if(flag==0):
            print("No plot to buy!!")
        
    def getplots(self,uname):
        file = open("plot.txt", "r")
        details = file.readline()
        plots = list()

        while details!= '':
            details = details.split()
            if(uname == details[1]):
                newplot = propertydets(details)
                plots.append(newplot)
            details = file.readline()
        
        return plots
    
    def display(self):
        print("username: ",self.username,"plots: ", self.plots)
    

class admin:
    def __init__(self,details):
        self.username = details[0]
        self.password = details[1]

    def verifyuser(self):
        f=open("tempcred.txt","r")
        flag=1
        f1=f.readline()
        while(f1!=''):
            f1=f1.split()
            if(f1[2]=="1"):
                flag=0
                g=open("userdet.txt","r")
                g1=g.readline()
                while(g1!=''):
                    g1=g1.split()
                    if(f1[3]==g1[0]):
                        print(g1[0],g1[1],g1[2],g1[3])
                        print("Approve details")
                        n= int(input("Enter chice: "))
                        h=open("tempinit.txt","r")
                        h1=h.readline()
                        while(h1!=''):
                            h1=h1.split()
                            if(f1[0]==h1[1]):
                                if(n):
                                    h.seek(0)
                                    he=h.readlines()
                                    he.remove(h1[0]+" "+h1[1]+" "+h1[2]+"\n")
                                    h.close()
                                    g.seek(0)
                                    te=g.readlines()
                                    te.remove(g1[0]+" "+g1[1]+" "+g1[2]+" "+g1[3]+"\n")
                                    g.close()
                                    f.seek(0)
                                    fe=f.readlines()
                                    fe.remove(f1[0]+" "+f1[1]+" "+f1[2]+" "+f1[3]+" "+f1[4]+"\n")
                                    f.close()
                                    f15=open("userdetail.txt","a")
                                    f15.write(g1[0]+" "+g1[1]+" "+g1[2]+" "+g1[3]+"\n")
                                    f16=open("users.txt","a")
                                    f16.write(f1[3]+" "+f1[4]+" "+f1[2]+"\n")
                                    f17=open("initial.txt","a")
                                    f17.write(h1[0]+" "+f1[3]+" "+h1[2]+"\n")
                                    h=open("tempinit.txt","w")
                                    h.writelines(he)
                                    h.close()
                                    g=open("userdet.txt","w")
                                    g.writelines(te)
                                    g.close()
                                    f=open("tempcred.txt","w")
                                    f.writelines(fe)
                                    f.close()
                                    f=open("tempcred.txt","r")
                                    g=open("userdet.txt","r")
                                    h=open("tempinit.txt","r")
                                else:
                                    h.seek(0)
                                    he=h.readlines()
                                    he.remove(h1[0]+" "+h1[1]+" "+h1[2]+"\n")
                                    h.close()
                                    g.seek(0)
                                    te=g.readlines()
                                    te.remove(g1[0]+" "+g1[1]+" "+g1[2]+" "+g1[3]+"\n")
                                    g.close()
                                    f.seek(0)
                                    fe=f.readlines()
                                    fe.remove(f1[0]+" "+f1[1]+" "+f1[2]+" "+f1[3]+" "+f1[4]+"\n")
                                    f.close()
                                    h=open("tempinit.txt","w")
                                    h.writelines(he)
                                    h.close()
                                    g=open("userdet.txt","w")
                                    g.writelines(te)
                                    g.close()
                                    f=open("tempcred.txt","w")
                                    f.writelines(fe)
                                    f=open("tempcred.txt","r")
                                    g=open("userdet.txt","r")
                                    h=open("tempinit.txt","r")
                            h1=h.readline()
                    g1=g.readline()
            f1=f.readline()
        if(flag):
            print("Nothing to verify")

        

class propertydets:
    def __init__ (self, details):
        self.plotno = details[0]
        self.sqft = details[2]
        self.owner = details[1]

class blockchain:
    def __init__(self):
        blockchaindet = open("blockdet.txt","r+")
        self.height = int(blockchaindet.read())
        self.blocks = list()
        for x in range(self.height):
            blockfile = open("block"+str(x+1)+".txt","r")
            blockfiledets = blockfile.readlines()
            blockdets = list()
            blockdets.append(blockfiledets[0])
            blockdets.append(blockfiledets[1:-3])
            blockdets.append(blockfiledets[-3])
            blockdets.append(blockfiledets[-2])
            blockdets.append(blockfiledets[-1]) 
            newblock = block(blockdets)
            self.blocks.append(newblock)
            

    def mine(self):
        file = open("mempool.txt","r+")
        transaction = file.readline()
        transactions = list()
        flag=1
        while(transaction != ''):
            flag=0
            transactionlist = transaction.split()
            plotfile = open("plot.txt","r+")
            plotdet = plotfile.readline()
            while(plotdet != ''):
                plotdetlist = plotdet.split()
                if(plotdetlist[0] == transactionlist[2] and plotdetlist[1] == transactionlist[0]):
                    plotfile.seek(0)
                    allplotdet = plotfile.readlines()
                    allplotdet.remove(plotdet)
                    allplotdet.append(plotdetlist[0]+" "+ transactionlist[1]+" "+ plotdetlist[2]+"\n")
                    plotfile.seek(0)
                    plotfile.truncate(0)
                    plotfile.writelines(allplotdet)
                    transactions.append(transaction)
                    records = open("record.txt","a")
                    records.write(str(datetime.datetime.now())+" "+transactionlist[0]+ " " + transactionlist[1]+ " "+ transactionlist[2]+ " " + plotdetlist[2]+"\n")
                    records.close()
                    break
                plotdet = plotfile.readline()
            plotfile.close()
            transaction = file.readline()
        if(flag):
            print("No transaction to mine")
        file.seek(0)
        file.truncate(0)
        file.close()
        blockdets = [self.height +1,transactions]
        newblock = block(blockdets)
        self.blocks.append(newblock)
        self.height+=1

class block:
    def __init__(self, blockdets):
        if len(blockdets) == 2:
            self.blockno = blockdets[0]
            self.txn_det = blockdets[1]
            self.timestamp = datetime.datetime.now()
            
            if(self.blockno == 1):
                self.prevhash = "0"*64
            else:
                self.prevhash = new_blockchain.blocks[-1].hash
            records = open("record.txt","a")
            records.writelines(self.txn_det)
            records.close()
            self.hash = self.hash()
            file = open("block"+str(self.blockno)+".txt","w")
            file.write(str(self.blockno)+"\n")
            file.writelines(self.txn_det)
            file.write(str(self.timestamp)+"\n")
            file.write(str(self.prevhash)+"\n")
            file.write(self.hash)
            blockchainfile = open("blockdet.txt","w")
            blockchainfile.write(str(self.blockno))

        elif len(blockdets) == 5:
            self.blockno = int(blockdets[0])
            self.txn_det = blockdets[1]
            self.timestamp = blockdets[2]
            self.prevhash = blockdets[3]
            self.hash = blockdets[4]

    def hash(self):
        file = open("record.txt","r")
        FileContent = str(file.readlines())
        FileContent = FileContent.encode()
        FileContent = hashlib.sha256(FileContent)
        return FileContent.hexdigest()

## login for existing user
def login():
    uname, password = input("Enter your username & password: ").split()
    file = open("users.txt", "r")
    details = file.readline()
    
    while details!= '':
        details = details.split()
        if(uname == details[0] and password == details[1]):
            return details
        details = file.readline()
    
    print("Incorrect Credentials!!")
    return 0
## login for new user    
def login_temp():
    uname, password = input("Enter your username & password: ").split()
    file = open("tempcred.txt", "r")
    details = file.readline()
    
    while details!= '':
        details = details.split()
        if(uname == details[0] and password == details[1]):
            return details
        details = file.readline()
    
    print("Incorrect Credentials!!")
    return 0

app = Flask(__name__)
new_blockchain = blockchain()
@app.route('/login',methods =["GET", "POST"])
## main starts
def login():
    while(True):
        print("1. Login\n2. Exit")
        i = int(input("Enter Choice: "))
        if(i):
            n=int(input("Are you a new user: "))
            if(n):
                details =login_temp()
                if details != 0:
                    new_user = newuser(details)
                    new_user.verify()
                    print("Registered for verification, It will take 2-3 days to get verified.\nThank you")
            else:
                details = login()
                if details != 0:  
                    if details[2] == '1':
                        curr_user = user(details)
                        curr_user.display()
                        while True:
                            print("1. Sell\n2. Buy\n3. log out")
                            choice = input("Enter choice: ")
                            if choice == "1":
                                curr_user.sell()
                            elif choice == "2":
                                curr_user.buy()
                            elif choice == "3":
                                break
                            else:
                                print("Enter correct choice")
                    elif details[2] =='2':
                        curr_admin = admin(details)
                        while True:
                            print("1.verifyuser\n2. Mine\n3. log out")
                            choice = input("Enter Choice: ")
                            if choice == "1":
                                curr_admin.verifyuser()
                            elif choice == "2":

                                new_blockchain.mine()
                            elif choice == "3":
                                break
                            else:
                                print("Enter correct choice")
        elif(1==2):
            break
        else:
            print("Enter correct choice!!")

app.run()    
    
