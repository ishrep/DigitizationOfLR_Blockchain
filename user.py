import random
def login(accessLevel, username, password):
    if accessLevel == 1 or accessLevel == 2:
        file = open("users.txt", "r")
    elif accessLevel == 0:
        file=open("tempcred.txt","r")
        
    details = file.readline()
    
    while details!= '':
        details = details.split()
        if (username == details[0] and password == details[1] and accessLevel == int(details[2])):
            return details
        details = file.readline()
        
    return 0

class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class alreadyuser(user):
    def __init__(self,username,password):
        user.__init__(self,username, password)
    def temp_cred_checker(self,new_user, new_pass):
        flag = 0
        file=open("tempcred.txt","r")
        f=file.readline()
        while(f!=''):
            f=f.split()
            if(f[0]==new_user):
                flag=1
                break;
            f=file.readline()
        return flag
    def add_temp_creds(self,new_user,new_pass):
        file=open("tempcred.txt","a")
        file.write(new_user+" "+new_pass+" 1"+"\n")
    def getuser(self):
        while True:
            new_user = str(random.randint(1000000,9999999))
            new_pass = str(random.randint(1000000,9999999))
            ls = [new_user, new_pass]
            #Checking temp creds
            flag = self.temp_cred_checker(new_user, new_pass)
            if(flag==0):
                self.add_temp_creds(new_user, new_pass)
                buyer = new_user
                break;
            ls.clear()
        f3 = open("tempinit.txt","a")
        f3.write(self.username+" "+buyer+" v\n")
        return ls
    def getpart_txns(self):
        file=open("initial.txt","r")
        part_txns = list()
        part_txn = file.readline()
        while(part_txn!= ''):
            part_txn = part_txn.split()
            if(part_txn[7]=="1"):
                if(part_txn[1] == self.username):
                    part_txns.append(part_txn)
            part_txn = file.readline()
        return part_txns
    def getplot(self):
        file=open("plot.txt","r")
        part_txns = list()
        part_txn = file.readline()
        while(part_txn!= ''):
            part_txn = part_txn.split()
            if(part_txn[1]==self.username):
                part_txns.append(part_txn)
            part_txn = file.readline()
        return part_txns
    def getverify_txns(self):
        file=open("initial.txt","r")
        part_txns = list()
        part_txn = file.readline()
        while(part_txn!= ''):
            part_txn = part_txn.split()
            if(part_txn[7]=="0"):
                if((part_txn[3] == self.username and part_txn[4] == "1") or (part_txn[5] == self.username and part_txn[6] == "1") or (part_txn[8] == self.username and part_txn[9] == "1") or (part_txn[10] == self.username and part_txn[11] == "1")):
                    part_txns.append(part_txn)
            part_txn = file.readline()
        return part_txns

class admin(user):
    def __init__(self,username,password):
        user.__init__(self,username, password)

class newuser(user):
    def __init__(self,username,password):
        user.__init__(self,username, password)