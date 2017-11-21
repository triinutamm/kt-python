list1 = [11, 15, 6, 13, 13, 25, 32, 11, 20, 5, 31, 16, 32, 29, 11, 13, 3, 29, 28, 24]
list2 = [5, 19, 16, 4, 12, 7, 2, 28, 34, 29, 29, 36, 6, 8, 24, 18, 31, 7, 1, 7]

# 1. ühisosa
print("esimeses ja teises listis kattub number")
for number in list1:
    a = number
    for number2 in list2:
        if a == number2:
            print(number2)

# 2.Suurim number
a = max(list1)
b = max(list2)
print("Kahe listi suurim number on:", max(a, b))

# 3.Väikesim number
c = min(list1)
d = min(list2)
print("Kahe listi väikseim number on:", min(c, d))

# 4.Listide keskmised
def keskmised(listinimi):    
    e = 0
    for number in listinimi:
        f = number
        g = e+f
        e = g
    keskmine = e / len(listinimi)
    print(keskmine)
    return keskmine
print("Esimese listi keskmine on:")
x = keskmised(list1)
print("Teise listi keskmine on:")
y = keskmised(list2)
listidekeskmised = (x + y)/2
print("Kahe listi keskmine on:",listidekeskmised)



