'''def check(number):
    gate = True
    j = 2
    for j in range(2,number):
        if number % j == 0:
            gate = True
        if gate:
            return "是质数"
        else:
            return "不是质数"
for n in range(0,39+1):
    m = n ** 2 + n +41
    print('n为'+str(n)+"时"+str(m)+check(m))

'''
while i > 0:
    if 4**i+2%3==0:
    i += 1
    print(int(i))
