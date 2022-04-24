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