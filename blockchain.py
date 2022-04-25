import datetime
import hashlib

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
        plot = x[0]+" "+x[1]+" "+x[2]+"\n"
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
            blockdets.append(blockfiledets[1:-3])
            blockdets.append(blockfiledets[-3])
            blockdets.append(blockfiledets[-2])
            blockdets.append(blockfiledets[-1]) 
            newblock = block(blockdets)
            self.blocks.append(newblock)

class block:
    def __init__(self, blockdets):
        if len(blockdets) == 2:
            self.blockno = blockdets[0]
            self.txn_det = blockdets[1]
            self.timestamp = datetime.datetime.now()
            self.hash = self.hash()
            
            if(self.blockno == 1):
                self.prevhash = "0"*64
            else:
                self.prevhash = new_blockchain.blocks[-1].hash
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