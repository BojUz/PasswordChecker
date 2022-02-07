# from typing_extensions import ParamSpecArgs
# import sys
# sys.setrecursionlimit(15000)
# from math import e
from datetime import datetime
startTime = datetime.now()
startLetter = 48
LastLetter = 57
#gornite promenlivi slujat za tova da se opredeli ot koi do koi simvol shte se proverqa parolata
#v momenta e nastroeno da probva samo s chisla za po burzo testvane
parola = input("Input pasword to test(curently only numbers): ")
parr=[None]*16
poziciq=0
outputi =""
print(parr)
while (True):
    asciiCOde=False
    if(parr[poziciq]==None):
        # asciiCOde=48
        parr[poziciq]=startLetter
    elif(parr[poziciq]<=LastLetter):
        # asciiCOde = parr[poziciq]
        # asciiCOde+=1
        parr[poziciq]+=1
        if(parr[poziciq]>LastLetter):
            asciiCOde=True
            parr[poziciq]=LastLetter
        # else:
        #     parr[poziciq]=asciiCOde
    if(asciiCOde==True):
        if(poziciq<15):
            start = poziciq
            for i in range(start,16):
                if(parr[poziciq]==LastLetter):
                    parr[i]=startLetter
                    poziciq+=1
                else:
                    break
            if(parr[poziciq]==None):
                parr[poziciq]=startLetter           
            else:
                parr[poziciq]=parr[poziciq]+1         
            # for i in range(poziciq-1,-1,-1):
            #     parr[i]=48
        poziciq=0

    if(poziciq==15):
        if(asciiCOde==True):
            print("Time for completion: ")
            print(datetime.now() - startTime)
            break
    for i in parr:
        if(i!=None):
            outputi+=chr(i)
        else:
            break
    print(outputi)
    #printa e samo za naglednost bez nego programata e dosta po burza
    if(outputi==parola):
        print(outputi)
        print("PASSWORD WAS CRACKED!!!")
        print("Time for completion: ")
        print(datetime.now() - startTime)
        break
    outputi=""