import datetime
import hashlib
import math

def check_initial(pno):
    file = open("initial.txt", "r")
    txn2 = file.readline()
    while txn2 !='':
        txn2 = txn2.split()
        if(txn2[2] == pno):
            return True
        txn2 = file.readline()
    return False

def check_tempinit(pno):
    file = open("initial.txt", "r")
    txn = file.readline()
    while txn !='':
        txn = txn.split()
        if(txn[2] == pno):
            return True
        txn = file.readline()
    return False

def get_plots():
    file = open("plot.txt","r")
    plot = file.readline()
    plots = list()
    while(plot!=""):
        plot = plot.split()
        plots.append(plot)
        plot = file.readline()
    return plots

def add_plots(plots):
    file = open("plot.txt","w")
    for x in plots:
        plot = x[0]+" "+x[1]+" "+x[2]+" "+ x[3]+" "+ x[4]+" "+ x[5]+" "+ x[6]+" "+ x[7]+"\n"
        file.write(plot)

def get_transactions():
    file = open("mempool.txt","r")
    txn_dets = file.readline()
    transactions = list()
    while(txn_dets !=""):
        txn_dets = txn_dets.split()
        transactions.append(txn_dets)
        txn_dets = file.readline()
    return transactions

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
            blockdets.append(blockfiledets[1:-4])
            blockdets.append(blockfiledets[-4])
            blockdets.append(blockfiledets[-3])
            blockdets.append(blockfiledets[-2]) 
            blockdets.append(blockfiledets[-1]) 
            newblock = block(blockdets)
            self.blocks.append(newblock)
    def __str__(self):
        a = ""
        for block in self.blocks:
            a = a + str(block)
        return a

def calculate_merkle(height, transchecked, ceilheight, transactions):
    if height == ceilheight:
        hashcode = hashlib.sha256(transactions[transchecked].encode()).hexdigest()
        return hashcode, transchecked +1
    hashcodeleft = ""
    hashcoderight = ""
    if transchecked < len(transactions):
        hashcodeleft,transchecked = calculate_merkle(height + 1, transchecked, ceilheight, transactions)
    if transchecked < len(transactions):
        hashcoderight,transchecked = calculate_merkle(height + 1, transchecked, ceilheight, transactions)
    hashcode = hashcodeleft+hashcoderight
    hashcode = hashlib.sha256(hashcode.encode()).hexdigest()
    return hashcode, transchecked


class block:
    def __init__(self, blockdets):
        if len(blockdets) == 3:
            self.blockno = blockdets[0]
            self.txn_det = blockdets[1]
            self.timestamp = datetime.datetime.now()
            if(self.blockno == 1):
                self.prevhash = "0"*64
            else:
                self.prevhash = blockdets[2].blocks[-1].currhash
            records = open("record.txt","a")
            records.writelines(self.txn_det)
            height = math.log(len(self.txn_det))
            height = height/0.301
            height = int(math.ceil(height))
            self.merkle,transchecked = calculate_merkle(0, 0,height,self.txn_det)
            records.close()
            self.currhash = self.hash()
            file = open("block"+str(self.blockno)+".txt","w")
            file.write(str(self.blockno)+"\n")
            file.writelines(self.txn_det)
            file.write(str(self.timestamp)+"\n")
            file.write(str(self.prevhash)+"\n")
            file.write(self.currhash+"\n")
            file.write(self.merkle)
            blockchainfile = open("blockdet.txt","w")
            blockchainfile.write(str(self.blockno))

        elif len(blockdets) == 6:
            self.blockno = int(blockdets[0])
            self.txn_det = blockdets[1]
            self.timestamp = blockdets[2]
            self.prevhash = blockdets[3]
            self.currhash = blockdets[4]
            self.merkle = blockdets[5]

    def __str__(self):
        a = "Block Height: "+str(self.blockno) + "<br>Timestamp: " + str(self.timestamp) +"<br>Current Hash: " + self.currhash + "<br>Previous Hash: "+ self.prevhash + "<br>Merkle Root:" + self.merkle + "<br>"
        for x in self.txn_det:
            a= a+ x + "<br>"
        return a + "<br>"

    def hash(self):
        file = open("record.txt","r")
        FileContent = str(file.readlines())
        FileContent = FileContent.encode()
        FileContent = hashlib.sha256(FileContent)
        return FileContent.hexdigest()