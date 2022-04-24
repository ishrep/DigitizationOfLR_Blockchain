from flask import Flask, request, render_template, redirect, url_for
from user import *
  
app = Flask(__name__)   
  
username = ''
password = ''
global signedin 
signedin = 0

@app.route('/', methods = ['GET','POST'])
def usertype():
    if request.method == "POST":
        type = request.form.get("usertype")
        if(type == "user"):
            return redirect(url_for("userlogin"))
        elif type == "newuser":
            return redirect(url_for("newuser"))
        elif type == "admin":
            return redirect(url_for("admin"))

    return render_template("login.htm")
    

  
@app.route('/userlogin', methods =["GET", "POST"])
def userlogin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password") 
        details = login( 1, username, password)
        if(details!= 0):
            global signedin
            signedin =1
            global userobj
            userobj = alreadyuser(details[0],details[1])
            return redirect(url_for("usermenu"))

    return render_template("alreadyuser.htm")

@app.route('/newuser', methods =["GET", "POST"])
def newuserlogin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password") 
        details = login( 0, username, password)
        if(details!= 0):
            global signedin
            signedin =1
            global userobj
            userobj = newuser(details[0],details[1])
            return redirect(url_for("newusermenu"))

    return render_template("newuser.htm")

@app.route('/admin', methods =["GET", "POST"])
def adminlogin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password") 
        details = login( 0, username, password)
        if(details!= 0):
            global signedin
            signedin =1
            global userobj
            userobj = admin(details)
            return redirect(url_for("newusermenu"))

    return render_template("admin.htm")

@app.route('/usermenu', methods =["GET", "POST"])
def usermenu():
    if signedin == 0:
        return redirect('/')
    if request.method == "POST":
        x = request.form.get("userAction")
        if(x == "buy"):
            return redirect(url_for("buypage"))
        elif x == "sell":
            return redirect(url_for("sellpage"))
        elif x == "display":
            return redirect(url_for("displayplotpage"))
        elif x == "verify":
            return redirect(url_for("verifypage"))
        elif x == "logout":
            return redirect(url_for("admin"))

    return render_template("usermenu.htm")

@app.route('/buypage', methods =["GET", "POST"])
def buypage():
    if signedin == 0:
        return redirect('/')
    if request.method == "POST":
        part_txn=userobj.getpart_txns()
        type = request.form.get("verify")
        pno = request.form.get("plotnum")
        present_txn=""
        for txn1 in part_txn:
            
            if(txn1[2]==pno):
                present_txn= txn1[0]
                for x in range(1,len(txn1)):
                    present_txn = present_txn + " " + txn1[x]
                present_txn = present_txn + "\n"
                break
        if(present_txn==""):
            return redirect(url_for('buypage'))
        if type=="accept":
            wt1 = request.form.get("witness1")
            wt2 = request.form.get("witness2")
            file = open("initial.txt","r")
            ini_ls = file.readlines()
            ini_ls.remove(present_txn)
            p_txn=present_txn.split()
            ini_ls.append(p_txn[0]+" "+p_txn[1]+" "+p_txn[2]+" "+p_txn[3]+" "+p_txn[4]+" "+p_txn[5]+" "+p_txn[6]+" 0 "+wt1+" 1 "+wt2+" 1\n")
            file.close()
            file = open("initial.txt","w")
            file.writelines(ini_ls)
            file.close()
        elif type=="deny":
            file = open("initial.txt","r")
            ini_ls = file.readlines()
            ini_ls.remove(present_txn)
            file.close()
            file = open("initial.txt","w")
            file.writelines(ini_ls)
            file.close()
        return redirect(url_for("usermenu"))
    return render_template("buypage.htm", content = userobj.getpart_txns())
    
@app.route('/verifypage', methods =["GET", "POST"])
def verifypage():
    if signedin == 0:
        return redirect('/')
    if request.method == "POST":
        part_txn=userobj.getverify_txns()
        pno = request.form.get("plotnum")
        type = request.form.get("verify")
        present_txn=""
        for txn1 in part_txn:
            if(txn1[2]==pno):
                present_txn= txn1[0]
                for x in range(1,len(txn1)):
                    present_txn = present_txn + " " + txn1[x]
                present_txn = present_txn + "\n"
                break
        if(present_txn==""):
            return redirect(url_for("usermenu"))
        if(type=="accept"):
            file = open("initial.txt","r")
            ini_ls = file.readlines()
            ini_ls.remove(present_txn)
            p_txn=present_txn.split()
            if p_txn[3]==userobj.username:
                ini_ls.append(p_txn[0]+" "+p_txn[1]+" "+p_txn[2]+" "+p_txn[3]+" 0 "+p_txn[5]+" "+p_txn[6]+" "+p_txn[7]+" "+p_txn[8]+" "+p_txn[9]+" "+p_txn[10]+" "+p_txn[11]+"\n")
            elif p_txn[5]==userobj.username:
                ini_ls.append(p_txn[0]+" "+p_txn[1]+" "+p_txn[2]+" "+p_txn[3]+" "+p_txn[4]+" "+p_txn[5]+" 0 "+p_txn[7]+" "+p_txn[8]+" "+p_txn[9]+" "+p_txn[10]+" "+p_txn[11]+"\n")
            elif p_txn[8]==userobj.username:
                ini_ls.append(p_txn[0]+" "+p_txn[1]+" "+p_txn[2]+" "+p_txn[3]+" "+p_txn[4]+" "+p_txn[5]+" "+p_txn[6]+" "+p_txn[7]+" "+p_txn[8]+" 0 "+p_txn[10]+" "+p_txn[11]+"\n")
            elif p_txn[10]==userobj.username:
                ini_ls.append(p_txn[0]+" "+p_txn[1]+" "+p_txn[2]+" "+p_txn[3]+" "+p_txn[4]+" "+p_txn[5]+" "+p_txn[6]+" "+p_txn[7]+" "+p_txn[8]+" "+p_txn[9]+" "+p_txn[10]+" 0\n")
            file.close()
            file = open("initial.txt","w")
            file.writelines(ini_ls)
            file.close()
            file = open("initial.txt","r")
            ls = file.readlines()
            for txn in ls:
                txn1=txn.split()
                if(txn1[2]==pno):
                    present_txn=txn
                    break
            p_txn=present_txn.split()
            if(p_txn[4]=="0" and p_txn[6]=="0" and p_txn[9]=="0" and p_txn[11]=="0"):
                ls.remove(present_txn)
                file.close()
                file = open("initial.txt","w")
                file.writelines(ls)
                file.close()
                file = open("mempool.txt","a")
                file.write(present_txn)
                file.close()


        elif(type=="deny"):
            file = open("initial.txt","r")
            ini_ls = file.readlines()
            ini_ls.remove(present_txn)
            file.close()
            file = open("initial.txt","w")
            file.writelines(ini_ls)
            file.close()
        return redirect(url_for("usermenu"))
    return render_template("verifypage.htm", content = userobj.getverify_txns())

if __name__=='__main__':
   app.run(debug = True)