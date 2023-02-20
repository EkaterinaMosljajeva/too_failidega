def loe_failist(fail:str)->list:
    """Faili lugemine faili nime järgi
    """
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def kirjuta_failisse(fail:str,jarjend:list):
    """
    """
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

from gtts import gTTS
import os

def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")
