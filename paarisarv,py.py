arv1 = int(input("Sisestage esimene arv:"))
arv2 = int(input("Sisestage teine arv:"))
print("Nende kahe arvu vahele jäävad paarisarvud on:")

if arv1 < arv2:
    vahearv = arv1 +1
    suuremarv = arv2
    
elif arv2 < arv1:
    vahearv = arv2 +1
    suuremarv = arv1
    
while vahearv < suuremarv:
    if vahearv / 2 == vahearv // 2:
        print(vahearv)
    vahearv = vahearv + 1
        
