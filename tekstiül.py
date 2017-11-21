tekst = open("kttekst.txt", "r")
lines = tekst.read().split(' ')
print("Tekstifailis on " , len(lines) , " sõna")
sõna_arv = 0
for word in lines:
    if len(word) < 5:
        sõna_arv += 1
        
print("Selles tekstis on: ", sõna_arv, " sõna väiksemad kui viis tähte")


tekst.close()
