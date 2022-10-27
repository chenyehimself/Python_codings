number = int(input()）
date = []
cow = []
milk = []
for i in range(number):
    day, change = map(int, input().split())
    date.append(day)
    cow.append(input("name: "))
    milk.append(change)
bessiemilk = 7
elsiemilk = 7
mildredmilk = 7
bessieon = True
elsieon = True
mildredon = True
dayadjust = 0
for current in range(1, 101):
    for i in range(number):
        if date[i] == current:
            if cow[i] == "Bessie":
                bessiemilk += milk[i]
            if cow[i] == "Elsie":
                elsiemilk += milk[i]
            if cow[i] == "Mildred":
                mildredmilk += milk[i]
            highestmilk = max(mildredmilk, bessiemilk, elsiemilk)
            bessieonnext = (bessiemilk == highestmilk)
            elsieonnext = (elsiemilk == highestmilk)
            mildredonnext = (mildredmilk == highestmilk)
            if bessieonnext == True or elsieonnext == True or mildredmilk == True:
                dayadjust += 1
                bessieon = bessieonnext
                elsieon = elsieonnext
                mildredon = mildredonnext
print(dayadjust)
print("\n")


