# 01
'''import sys
sys.stdin = open('herding.in', 'r')
sys.stdout = open('herding.out', 'w')
'''
a,b,c = map(int,input().split())
R2 = max(b-a,c-b)-1
if c == a+2:
  R1 = 0
elif b == a+2 or c == b+2:
  R1 = 1
else:
  R1 = 2

print(R1)
print(R2)

#02
