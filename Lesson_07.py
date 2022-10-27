#Lesson_07
'''sample_dic = {'a': 100, 'b': 200, 'c': 300}
for i in sample_dic:
    if sample_dic[i]==200:
        print("200 present in a dict")
        break
print("\n")'''

#真题1
R,S=map(int,input().split())
M,N,Q,P=map(int,input().split())
A1=0
A2=0
B1=R
B2=S
gate = 0
for i in range(1000):
    A1 = M + A1
    A2 = N + A2
    B1 = B1 - P
    B2 = B2 - Q
    if A1 == B1 and A2 == B2:
        gate += 1
        print(i+1)
        break
    else:
        pass
if gate == 0:
    print(-1)
print("\n")

#真题2
N = int(input())
listC = list(map(int,input().split()))
listA = list(map(int,input().split()))
for i in range(N-1):
    if listA[i]+listA[i+1] <= listC[i+1]:
        listA[i + 1] = listA[i] + listA[i + 1]
        listA[i] = 0
    if listA[i]+listA[i+1] > listC[i+1]:
        listA[i] = listA[i] + listA[i + 1] - listC[i + 1]
        listA[i+1] = listC[i+1]
for i in listA:
    print(i, end=" ")
print("")
print("\n")

#练习
c1,m1 = map(int,input().split())
c2,m2 = map(int,input().split())
c3,m3 = map(int,input().split())
listc = [c1,c2,c3]
listm = [m1,m2,m3]
for i in range(33):
    if listm[0] + listm[1] <= listc[1]:
        listm[1] = listm[0] + listm[1]
        listm[0] = 0
    if listm[0] + listm[1] > listc[1]:
        listm[0] = listm[0] + listm[1] - listc[1]
        listm[1] = listc[1]

    if listm[1] + listm[2] <= listc[2]:
        listm[2] = listm[1] + listm[2]
        listm[1] = 0
    if listm[1] + listm[2] > listc[2]:
        listm[1] = listm[1] + listm[2] - listc[2]
        listm[2] = listc[2]

    if listm[2] + listm[0] <= listc[0]:
        listm[0] = listm[2] + listm[0]
        listm[2] = 0
    if listm[2] + listm[0] > listc[0]:
        listm[2] = listm[2] + listm[0] - listc[0]
        listm[0] = listc[0]
if listm[0] + listm[1] <= listc[1]:
    listm[1] = listm[0] + listm[1]
    listm[0] = 0
if listm[0] + listm[1] > listc[1]:
    listm[0] = listm[0] + listm[1] - listc[1]
    listm[1] = listc[1]
for i in listm:
    print(i)
for i in range(m):
print("\n")








