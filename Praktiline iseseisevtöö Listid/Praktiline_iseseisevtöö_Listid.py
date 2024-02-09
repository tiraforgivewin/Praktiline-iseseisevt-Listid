from string import *
#1
#vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
#konsonanti="qwrtpsdfghjklzxcvbnm"
#markid=punctuation
#v=k=m=t=0
#tekst=input("Sisesta sõna vöi lause: ").lower()
#tekst_list=list(tekst)
#    if sümbol in vokaali:
#        v+=1
#    elif sümbol in konsonanti:
#        k+=1
#    elif sümbol in markid:
#        m+=1
#    elif sümbol==" ":
#        t+=1
#print("Vokaali:",v,"\nKonsonanti:",k)
#print("Kirjuvahemärgid:",m)
#print("Tühikud:",t)


#2
nimed=[]
for i in range(5):
    nimi=(input("Sisesta nimi: "))
    nimed.append(nimi)
print("Loetelu oli: ",nimed)
nimed.sort()
print("Loetelu sorteeritud: ",nimed)
for n in range(len(nimed)):
    print(n+1,".",nimed[n],sep="")
print("VImasena oli lisatud: ",nimi)

uued_nimi=[]
for nimi in nimed:
    if nimi not in uued_nimi:
        uued_nimi.append(nimi)
print(uued_nimi)



