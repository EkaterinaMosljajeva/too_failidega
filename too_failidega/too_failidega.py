from moodul import *
laused=[] 

while True:
    v=int(input("1-loeme failist\n2-salvestamine failisse\n3-Tekst helisse"))
    if v==1:
        laused=loe_failist("laused.txt")
        for line in laused:
            print(line)
    elif v==2:
        line=input("Lisa lause: ")
        laused.append(line)
        kirjuta_failisse("laused.txt",laused)
    elif v==3:
        for line in laused:
            text=text+" "+line
        #text : kõik elemendis järjendis
        ind=int(input("Number: "))
        heli(laused[ind],'et')
