'''#01
n = int(input())
pos = list(map(int,input().split()))
cowid = list(map(int,input().split()))
perm = []
for i in range(len(pos)):
    perm.append(int(int(pos[i])-1))
final = []
for i in range(n):
    final.append(perm[perm[perm[i]]])
for i in range(n):
    print(cowid[final[i]])
#02
n = int(input())
l = list(map(int,input().split()))
map = int(split)
for i in range(n):
    l.append(cowid[final[i+1]])
    str()
'''

'''def RecCountDown(n):
    if n == 0 :
        return n
    else:
        if n > 0:
            print(n)
            return (RecCountDown(n - 1))
        if n < 0:
            print(n)
            return (RecCountDown(n + 1))
print(RecCountDown(3))'''

'''
def RecReverseString(n):
    if len(n) == 0:
        return ""
    else:
        return n[-1] + RecReverseString(n[:-1])

print(RecReverseString("abcde"))
'''

'''def primecheck(m,f):
    f = m-1
    if f == 2:
        return f
    elif m%f != 0:
        return primecheck(m,f-1)
    elif m%f ==0 :
        return f

    if f == 2:
        print("Integer m is no prime.")
    if f != 2:
        print("Integer m is prime.")

print(primecheck(3,3))'''

