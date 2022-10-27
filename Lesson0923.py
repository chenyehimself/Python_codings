n = int(input())
cowlist = []
for i in range(n):
    c = int(input())
    cowlist.append(c)
cowlist1 = sorted(cowlist)
dist = []
for ii in range(1, n):
    distance = cowlist1[ii] - cowlist1[ii - 1]
    dist.append(distance)
right = [True]
for iii in range(1, len(dist)):
    if dist[iii] < dist[iii - 1]:
        right.append(True)
    else:
        right.append(False)
right.append(False)
result = 0
j = 0
if n <= 3:
    result = 1
else:
    while j < n:
        rcount = 0
        while right[j] == True:
            j += 1
            rcount += 1

        lcount = 0
        while j < n and right[j] == False:
            j += 1
            lcount += 1

        if rcount > 1 and lcount > 1:
            result += 2
        else:
            result += 1
print(result)

'''f= open('promote.in', 'r')
list0 = list(map(int,f.readline().split()))
list1 = list(map(int,f.readline().split()))
list2 = list(map(int,f.readline().split()))
list3 = list(map(int,f.readline().split()))
'''
'''list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list3 = list(map(int,input().split()))
listnum = []
for i in range(2):
    listnum.append(list1[i])
for i in range(2):
    listnum.append(list2[i])
for i in range(2):
    listnum.append(list2[i])
print(listnum)
'''