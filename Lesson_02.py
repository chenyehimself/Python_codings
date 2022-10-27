#Classwork

#01
def distance(x1,y1,x2,y2):
    result_1 = ((x2-x1)**2+(y2-y1)**2)**0.5
    return result_1
radius = distance(1,1,5,5) #需要是具体的值
def area_circle(radius):
    result_2 = 3.14*(radius**2)
    return result_2
final_result = area_circle(radius)
print(final_result)
#function call需要删掉缩进
print("\n")

#02
def seq3np1(n):
    while n != 1:
        print(int(n), end = ",")
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
    else:
        print(int(n), end = ".")
seq3np1(3)
print("\n")

#03
#for else连用
'''
for i in range(5):
    a = int(input("Enter 0 to end the loop, you have 5 chances in total: "))
    if a == 0:
        print("break will run, and else will not run")
        break
else:
    print("you missed all 5 chances, else will run. Loop ends now")
'''

#Homework

#Functions
#01 Find max of three numbers
a = int(input("please enter the value for a:"))
b = int(input("please enter the value for b:"))
c = int(input("please enter the value for c:"))
def find_max(a,b,c):
    if a > b and a > c:
        result = a
        return result
    elif b > a and b > c:
        result = b
        return result
    elif c > a and c > b:
        result = c
        return result
print(find_max(a,b,c))
#这个题目我不是非常明白，我按照自己输入abc的值让电脑判断做了
print("\n")
#02 Check divisibility
m = int(input("please enter the value for m:"))
n = int(input("please enter the value for n:"))
def divisibility(m, n):
    if n > m:
        print("invalid value for m and n")
    if n == 0:
        print("The case is not defined for n=0.")
    elif m%n == 0:
        return True
    else:
        return False
print(divisibility(m,n))
print("\n")

#Condition
#01
print("your gesture should be chosen from only rock, paper or scissors.")
player_1 = input("Player 1, please enter your gesture: ")
player_2 = input("Player 2, please enter your gesture: ")
if player_1 == "rock" and player_2 == "rock":
    print("tie")
elif player_1 == "rock" and player_2 == "scissors":
    print("Player_1 wins.")
elif player_1 == "rock" and player_2 == "paper":
    print("Player_2 wins.")
elif player_1 == "paper" and player_2 == "paper":
    print("tie")
elif player_1 == "paper" and player_2 == "rock":
    print("Player_1 wins.")
elif player_1 == "paper" and player_2 == "scissors":
    print("Player_2 wins.")
elif player_1 == "scissors" and player_2 == "scissors":
    print("tie")
elif player_1 == "scissors" and player_2 == "paper":
    print("Player_1 wins.")
elif player_1 == "scissors" and player_2 == "rock":
    print("Player_2 wins.")







