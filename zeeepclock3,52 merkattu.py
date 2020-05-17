#kirjastot
import sys
import datetime
import os
from tkinter import *
import time
import threading
from time import sleep
from zeep import Client, Settings
#napit testaus tarpeeseen
try:
    from gpiozero import Button as Btton
    print("Napit")
    ab=Btton(18)
    bb=Btton(19)
    cb=Btton(20)
    db=Btton(21)
    eb=Btton(22)
    napit=True
except:
    print("Ei nappeja")
    napit=False
    ab=None
    bb=None
    cb=None
    db=None
    eb=None

#muuttujien määritys
settings = Settings(strict=False, xml_huge_tree=True)

jouk={}
joukn=[]
jouki=[]

lajit={}
lajitn=[]
lajiti=[]
#verkko yhteyden tekemimen
try:
    
    client = Client("http://taitaja9.gradia.fi/julkaistu5/Service1.svc?wsdl", settings=settings)
    print("Yhteys saatu")
    result = client.service.lajit();
    
    result2 = client.service.joukkueet();
    #print(result2)
    for i in range(len(result2._value_1._value_1) ):
        jouk[result2._value_1._value_1[i]["Table"]["Joukkue"]]=result2._value_1._value_1[i]["Table"]["Id"]
    #joukn=list(jouk.keys())
    joukn=list(("Mikromekaanikot","NeJaNe","Golden magic", "Foxtrot","Jöröjukat","Bluefox","Norpat","KYK8b","Konnat","Lennin enkelit","Friends Without Benefits","ESA","Jasun Mussukat","Sepät","Lumiukot","Välkyt"))
    jouki=list(jouk.values())
    
    for i in range(len(result._value_1._value_1) ):
        lajit[result._value_1._value_1[i]["Table"]["Nimi"]]=result._value_1._value_1[i]["Table"]["Id"]
    lajitn=list(lajit.keys())
    lajiti=list(lajit.values())
    yhteys=True
    
except:
    print("Ei yhteyttä")
    joukn=("Mikromekaanikot","NeJaNe","Golden magic", "Foxtrot","Jöröjukat","Bluefox","Norpat","KYK8b","Konnat","Lennin enkelit","Friends Without Benefits","ESA","Jasun Mussukat","Sepät","Lumiukot","Välkyt")
    for i in range(len( joukn)):
        jouki.append(i)
    for i in range(len( joukn)):
        jouk[joukn[i]]=jouki[i]
    lajiti=("laji1","laji2","laji3")
    for i in range(len( lajiti)):
        lajitn.append(i)
    for i in range(len( lajiti)):
        lajit[lajiti[i]]=lajitn[i]
    yhteys=False

#Muutujien määritys kelloille
#laskinten arvo
a=0
b=0
c=0
d=0
#onko laskin päällä
ar=False
br=False
cr=False
dr=False
er=False
#Onko kierros mennyt redundantti
kiert=False
#Onko Laskin tallettanut
at=False
bt=False
ct=False
dt=False
kier=0
ate=datetime.datetime.now().strftime("%H:%M:%S")


#Päivitys 
def tick():
    global a
    global b
    global c
    global d
    clock1.config(text=a)
    clock2.config(text=b)
    clock3.config(text=c)
    clock4.config(text=d)
    clock4.after(100,tick)


#ajastimien määritys
def t1():
    global a,ar,ab,variable1,variable5,at
    if napit==True:
        while ar == True and not ab.is_pressed and not a >=900:
            if ar == True:
                a+=1
            sleep(1)
        if not a<=1 and ab.is_pressed and at==False:
            at=True
            muistiin(variable1,variable5,a)
            
    elif napit==False:
        while ar == True and not a >=900 and nap1v.get()==0:
            if ar == True:
                a+=1
            sleep(1)
        if not a<=1 and nap1v.get()==1 and at==False:
            at=True
            muistiin(variable1,variable5,a)

def t2():
    global b,br,bb,variable2,variable5,bt
    if napit==True:
        while br == True and not bb.is_pressed and not b >=900:
            if br == True:
                b+=1
            sleep(1)
        if not b<=1 and bb.is_pressed and bt==False:
            bt=True
            muistiin(variable2,variable5,b)

    elif napit==False:
        while br == True and nap2v.get()==0 and not b >=900:
            if br == True:
                b+=1
            sleep(1)
        if not b<=1 and nap2v.get()==1 and bt==False:
            bt=True
            muistiin(variable2,variable5,b)

def t3():
    global c,cr,cb,variable3,variable5,ct
    if napit==True:
        while cr == True and not cb.is_pressed and not c >=900:
            if cr == True:
                c+=1
            sleep(1)
        if not c<=1 and cb.is_pressed and ct==False:
            ct=True
            muistiin(variable3,variable5,c)
            
    elif napit==False:
        while cr == True and nap3v.get()==0 and not c >=900:
            if cr == True:
                c+=1
            sleep(1)
        if not c<=1 and nap3v.get()==1 and ct==False:
            ct=True
            muistiin(variable3,variable5,c)
    

def t4():
    global d,dr,db,variable4,variable5,dt
    if napit==True:
        while dr == True and not db.is_pressed and not d >=900:
            if dr == True:
                d+=1
            sleep(1)
        if not d<=1 and db.is_pressed and dt==False:
            dt=True
            muistiin(variable4,variable5,d)
            
    elif napit==False:
        while dr == True and nap4v.get()==0 and not d >=900:
            if dr == True:
                d+=1
            sleep(1)
        if not d<=1 and nap4v.get()==1 and dt==False:
            dt=True
            muistiin(variable4,variable5,d)
        


#Talletuksen määritys
def muistiin(joukid,lajid,aikaaa):
    
    if chkvar2.get()==1:
        koe ={"joukkueid": str(jouk[joukid.get()]),"lajiID" : str(lajit[lajid.get()]),"aika": str(aikaaa)}
        tulo = str(client.service.Lisaatulos(koe))
        print(tulo)
    else:
        print("ei tallennettu verkkoon")
    if chkvar1.get()==1:
        on=open("tulokset.txt","a+")
        on.write("\n")
#        on.write("kierros: "+str(kiervar.get())+"\n")
        try:
            print(joukid.get())
        except:
            print("joukid ei")
        try:
            print(lajid.get())
        except:
            print("joukid ei")
        
        on.write(str("Joukkue"+":"+str(joukid.get())+","+"Laji" +":"+ str(lajid.get())+"\n"))
        on.write(str("joukkueid"+":"+str(jouk[joukid.get()])+","+"lajiID" +":"+ str(lajit[lajid.get()])+","+"aika"+":"+ str(aikaaa))+"\n")
        on.close
    else:
        print("ei tallennettu tiedostoon")
    
    
#laskinten säikeiden aloitus
def lask():
    p1 = threading.Thread(target = t1)
    p2 = threading.Thread(target = t2)
    p3 = threading.Thread(target = t3)
    p4 = threading.Thread(target = t4)
        
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    



#Konsoliin -||- verkkoon laitosta
def tulos(joukid,lajid,aikaaa):
    koe ={"joukkueid": str(joukid),"lajiID" : str(lajd),"aika": str(aikaaa)}
    tulo = str(client.service.Lisaatulos(koe))
    print(tulo)
    
#konsoliin valikkojen valintojen tiedon syöttö
def tyo(x):
    print ("value is", lajit[x.get()])
def tyo2(x):
    print ("value is", jouk[x.get()])    
#vahingossa kaksin kerroin??
def tyo(x):
    print(x.get())
    print ("value is", lajit[x.get()])
def tyo2(x):
    print(x.get())
    print ("value is", jouk[x.get()])
#rajoittaa syöttökentän kokoa
def raj(syo):
    if len(syo.get()) > 0:
        syo.set(syo.get()[-1])
#kokonäyttö tilan vaihtaja
def taysi():
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))
#Redundantti kierros valinta tiedostolle
def tiekie():
    if chkvar1.get()==1:
        
        kr.grid(row=2,column=7,sticky=S)
        kierrossyo.grid(row=3,column=7)
    elif chkvar1.get()==0:
        kr.grid_forget()
        kierrossyo.grid_forget()
    
#pää pyöritys palanen
def main():
    global a,b,c,d,ar,br,cr,dr,kier,kiert
	#Lopettaa laskimet
    kiert=not kiert
    ar=not ar
    br=not br
    cr=not cr
    dr=not dr
    #odottaa 1 sekunnin varmistamaan että laskimet ovat sammuneet
	sleep(1)
    if kiert == True:
        kier+=1
		#osa koodista joka olisi laittanut tiedostoon merkkauksen kierroksesta
		#mui=open("tulokset.txt","a+")
        #mui.write("Kierros: "+str(kier)+"\r\n")
        #mui.close
        duttontxt.set("Pysäytä")
        
		lask()
        
    else:
        duttontxt.set("Aloita")
    
    
#Uusii kaikki laskurien arvot jotta 
def reset():
    global a,b,c,d,ar,br,cr,dr,kier,kiert,redo,at,bt,ct,dt
    duttontxt.set("Aloita")
    kiert=False
    ar=False
    br=False
    cr=False
    dr=False
    sleep(1)
    a=0
    b=0
    c=0
    d=0
    at=False
    bt=False
    ct=False
    dt=False
    

#määrittää ohejelman ikkunan ja kutsuu kaikki muut ohjelman osat
if __name__ == "__main__":
#Ikkunan luonnin aloitus
    root=Tk()
	
   # ax=root.winfo_screenheight()
   # ay=root.winfo_screenwidth() 
   # root.geometry(str(ay)+"x"+str(ax)) 
   
   #"Tiimit" teksti
    Label(root,text="Tiimit: ").grid(row=0)
    #tiimi 1
    variable1 = StringVar(root)
    variable1.set(joukn[0])    
    w1 = OptionMenu(root, variable1, *joukn, command=lambda x: tyo2(variable1))
    w1.grid(row=0,column=1)
    #tiimi 2
    variable2 = StringVar(root)
    variable2.set(joukn[0])   
    w2 = OptionMenu(root, variable2, *joukn, command=lambda x: tyo2(variable2))
    w2.grid(row=0,column=2)
    #tiimi 3
    variable3 = StringVar(root)
    variable3.set(joukn[0])   
    w3 = OptionMenu(root, variable3, *joukn, command=lambda x: tyo2(variable3))
    w3.grid(row=0,column=3)
    #tiimi 4
    variable4 = StringVar(root)
    variable4.set(joukn[0]) 
    w4 = OptionMenu(root, variable4, *joukn, command=lambda x: tyo2(variable4))
    w4.grid(row=0,column=4)
    #lajilistan sijoitus
    Label(root,text="Laji:").grid(row=0,column=7,sticky=E)
    variable5 = StringVar(root)
    #Lajilistan luominen
    if yhteys ==True:
        variable5.set(lajitn[12])   
        w5 = OptionMenu(root, variable5, *lajitn, command=lambda x: tyo(variable5))
    elif yhteys==False:
        variable5.set(lajiti[0]) 
        w5 = OptionMenu(root, variable5, *lajiti, command=lambda x: tyo(variable5))
    w5.grid(row=0,column=8)
    #laskuri 1
    clock1=Label(root, font = ("comic sans", 20,"bold") )
    clock1.grid( row=2, column=1)
	#laskuri 2
    clock2=Label(root, font = ("comic sans", 20,"bold") ) 
    clock2.grid( row=2, column=2)
    #laskuri ...
	clock3=Label(root, font = ("comic sans", 20,"bold") )
    clock3.grid( row=2, column=3)
    #laskuri 4
	clock4=Label(root, font = ("comic sans", 20,"bold") )
    clock4.grid( row=2, column=4)
	#Laskurin aloitus/pysäytys nappi
    duttontxt =StringVar()
    duttontxt.set("Aloita")
    dutton = Button(root,textvariable=duttontxt,command=lambda : main())
    dutton.grid(row=4,column=3,sticky=W)

    #full = Button(root,text ="naytonkoko",command=lambda : taysi())
    #full.grid(row=0,column=8)

#kierros?
    kr=Label(root,text="Kierros", font=("comic sans",8))
    kiervar = StringVar() 
    kiervar.set("1")
    kierrossyo = Entry(root, width = 1, textvariable = kiervar)
    kiervar.trace("w", lambda *args: raj(kiervar))

#Laskurin uusinta nappi
    duttore = Button(root,text ="Uusi",command=lambda : reset())
    duttore.grid(row=4,column=7)
    
	#tallennus valinta
    Label(root,text="Tallennus").grid(row=2,column=8)
	#tiedostoon tallentamisen valinta
    chkvar1=IntVar()
    chk1=Checkbutton(root,text="Tiedostoon", variable=chkvar1)
    chk1.grid(row=3,column=8)
    chkvar1.set(1)
	#Verkkoon tallentamisen valinta
    if yhteys==True:
        chkvar2=IntVar(value=1)
        chk2=Checkbutton(root,text="Verkkoon", variable=chkvar2)
        chk2.grid(row=4,column=8)
    else:
        chkvar2=IntVar()

	#chkvar1.trace("w", lambda *args: tiekie())
    
	#Jossei nappeja ole saatavilla korvataan ne ohjelman ikkunaan valintaruuduilla
	if napit==False:
        nap1v=IntVar(value=1)
        nap1=Checkbutton(root, variable=nap1v)
        nap1.grid(row=3,column=1)
        
        nap2v=IntVar(value=1)
        nap2=Checkbutton(root, variable=nap2v)
        nap2.grid(row=3,column=2)
    
        nap3v=IntVar(value=1)
        nap3=Checkbutton(root, variable=nap3v)
        nap3.grid(row=3,column=3)
        
        nap4v=IntVar(value=1)
        nap4=Checkbutton(root, variable=nap4v)
        nap4.grid(row=3,column=4)
    
	
    tick()
    root.mainloop()




    
