#1
'''
n = int(input())
temp_list = []
long_list=[]
for i in range(n):
    a,b,c = map(int,input().split())
    tmp_list = [a,b,c]
    long_list.append(tmp_list)

list_origin = [1,2,3]
list_guess = []

for i in range(n):
    list_origin[long_list[i][0]-1],list_origin[long_list[i][1]-1] = list_origin[long_list[i][1]-1],list_origin[long_list[i][0]-1]
    list_guess.append(list_origin[long_list[i][2]-1])

print(max(list_guess.count(1),list_guess.count(2),list_guess.count(3)))
'''
#2

n = int(input())
list1 = list(map(int,input().split()))
k = 0
list1.append(0)
print(len(list1))
#print(list1)
for i in reversed(range(n)):
    if list1[i]>list1[i-1]:
        pass
    else:
        k = i
        break
print(k)
list_interval = []

for i in range(n):
    if list1[0]<list1[k-i]:
        list1.insert(i+k,list1[0])
        del list1[0]
        list_interval.append(i+k-1)
        print("check0")
        #print(list1)
    else:
        for i in range(len(list1)-k):
            if list1[0]<list1[i+k]:
                list1.insert(i + k, list1[0])
                del list1[0]
                list_interval.append(i+k-1)
                print("check1")
            elif list1[n-1]>list1[0]>list1[n-2]:
                list1.insert(n-1,list1[0])
                del list1[0]
                list_interval.append(n-2)
                print("check2")

            if list1[0]>list1[n-1] and list1[0]>list1[n]:
                list1.insert(n, list1[0])
                del list1[0]
                list_interval.append(n-1)
                print("check3")


for i in range(len(list_interval)):
    print(list_interval[i],end = " ")






