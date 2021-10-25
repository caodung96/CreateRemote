from tkinter import * 

def run(namefile,no):
    fileObject = open("vps.txt", "r")
    data = fileObject.read().replace(" ","").split('\n')  
    name=namefile
    namedis='view'
    pw='123'
    top='<?xml version="1.0" encoding="utf-8"?>\n<RDCMan schemaVersion="1">\n<version>\n2.7\n</version>\n<file>\n'
    mid='<properties><name>\n'+namefile+'\n</name>\n<expanded>\nTrue\n</expanded>\n<comment />\n<logonCredentials inherit="FromParent" />\n<connectionSettings inherit="FromParent" />\n<gatewaySettings inherit="FromParent" />\n<remoteDesktop inherit="FromParent" />\n<localResources inherit="FromParent" />\n<securitySettings inherit="FromParent" />\n<displaySettings inherit="FromParent" />\n\n</properties>\n'
    bot='</file>\n</RDCMan>'
    i=0
    j=1
    k=no
    sever=''
    for vps in data:
        namedis=str(k)+'-'+str(i%4+1)
        if vps.count('|')==1:
            sever = sever+'<server><name>'+vps.split('|')[0]+'</name><displayName>'+namedis+'</displayName><comment /><logonCredentials inherit="None"><userName>Administrator</userName><domain>'+vps.split('|')[0]+'</domain><password storeAsClearText="True">'+vps.split('|')[1].replace("&","&amp;")+'</password></logonCredentials><connectionSettings inherit="FromParent" /><gatewaySettings inherit="FromParent" /><remoteDesktop inherit="FromParent" /><localResources inherit="FromParent" /><securitySettings inherit="FromParent" /><displaySettings inherit="FromParent" /></server>'
        i+=1
        j+=1
        if i%4 == 0:
            k+=1
        

    f = open(name+".rdg", "w")
    f.write(top+mid+sever+bot)
    f.close()


from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Name File')
        self.lbl2=Label(win, text='Start no ')
        self.lbl3=Label(win, text='Status')
        self.lbl4=Label(win, text='')

        self.t1=Entry()
        self.t2=Entry()
        self.btn1 = Button(win, text='Add')
        self.lbl1.place(x=10, y=20)
        self.t1.place(x=100, y=20)
        self.lbl2.place(x=10, y=70)
        self.t2.place(x=100, y=70)
        self.b1=Button(win, text='Create', command=self.add)
        self.b1.place(x=120, y=170)
        self.lbl3.place(x=10, y=120)
        self.lbl4.place(x=100, y=120)
    def add(self):
        name=self.t1.get()
        no=self.t2.get()
        if name and no:
            run(name,int(no))
            self.lbl4.config(text="Done..!") 
        else :
            self.lbl4.config(text="Pls, input name and no.") 

window=Tk()
mywin=MyWindow(window)
window.resizable(0,0)
window.title('Tool Remote')
window.geometry("270x200")
window.mainloop()



