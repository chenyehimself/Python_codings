#01
list0 = list(map(int,input().split()))
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list3 = list(map(int,input().split()))

print(list3[1]-list3[0])

print(list2[1]+list3[1]-list2[0]-list3[0])

print(list2[1]+list3[1]+list1[1]-list2[0]-list3[0]-list1[0])

#02
N,K=map(int,input().split())
sentence = input().split()
position = 0
for word in sentence:
    if position == 0:
        print(word,end="")
        position = len(word)
    else:
        position += len(word)
        if position > K:
            print("")
            print(word,end="")
            position = len(word)
        else:
            print(" "+word, end="")

#03
grid = []
for i in range(10):
    row = list(input())
    grid.append(row)
#print(grid)

#创建空的坐标列表
listBc=[]
listRc=[]
listLc=[]
listLd=[]


#获取坐标填入列表
for i in range(10):
    for j in range(10):
        if str(grid[i][j])=="B":
            listBc.append(i+1)
            listBc.append(j+1)
            #print(i+1,j+1)

for i in range(10):
    for j in range(10):
        if str(grid[i][j])=="R":
            listRc.append(i+1)
            listRc.append(j+1)
            #print(i+1,j+1)

for i in range(10):
    for j in range(10):
        if str(grid[i][j])=="L":
            listLc.append(i+1)
            listLc.append(j+1)
            #print(i+1,j+1)

#计算：两个special_case 三点共水平线 三点共竖直线 再加一个common_case
if listLc[0]==listRc[0]==listBc[0]:
    print(abs(listBc[1]-listLc[1])-1+2)
if listLc[1]==listRc[1]==listBc[1]:
    print(abs(listBc[0] - listLc[0]) - 1 + 2)
else:
    print(abs(listLc[0]-listBc[0])+abs(listBc[1]-listLc[1])-1)
if listLc[0]==listRc[0]==listBc[0] and listRc[0]>listBc[0]>listLc[0]:
    print(listBc[0]-listLc[0]-1)
if listLc[0]==listRc[0]==listBc[0] and listRc[0]>listLc[0]>listBc[0]:
    print(listLc[0]-listBc[0]-1)
if listLc[1]==listRc[1]==listBc[1] and listRc[1]>listBc[1]>listLc[1]:
    print(listBc[1]-listLc[1]-1)
if listLc[1]==listRc[1]==listBc[1] and listRc[1]>listLc[1]>listBc[1]:
    print(listLc[1]-listBc[1]-1)






            














'''N,K=map(int,input().split())
sentence = input().split()
position = 0
for word in sentence:
    if position == 0:
        print(word,end="")
        position = len(word)
    else:
        position += len(word)
        if position > K:
            print("")
            print(word,end="")
            position = len(word)
        else:
            print(" "+word, end="")
'''






