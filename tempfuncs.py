
def add_temp_creds(new_user,new_pass):
    file=open("tempcred.txt","a")
    file.write(new_user+" "+new_pass+" 0"+"\n")
    
def temp_cred_checker(new_user, new_pass):
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

def buyer_checker(buyer):
    flag=0
    u_file=open("users.txt","r")
    u_list=u_file.readlines()
    for user in u_list:
        user=user.split()
        if(user[0]==buyer):
            flag=1
            break;
    return flag