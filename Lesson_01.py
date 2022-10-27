#Classwork_01
def timeCal(x):
    print(x//3600, (x-(x//3600)*60)//60, x-(x//3600)*3600-(x-(x//3600)*60)//60*60, sep=":")
timeCal(3400)
print("\n")
#Homework_01
def Calculation1(a,b):
    return(a+b,a-b)
res = Calculation1(40,10)
print(res)
print("\n")
"""
input1 = str(input("Please enter your name:"))
input2 = str(input("and your salary(if default,type nothing): "))
if input2 == "" or input2 == " ":
    input2 = 9000

print("Name: ",input1,"Salary:",input2)
#这个代码我也测试了 确实是可行的 虽然不能达到题目要求但是我觉得这种互动也挺有意思的也更真实 我就保留在注释里面了
"""
#Homework_02 #default应该这么使用
def show_employee( name, salary = 9000 ):
    print("Name:", name, "Salary:", salary)
show_employee("Ben","12000")
show_employee("Jessa")
print("\n")

#Homework_03
#Method_01
def reverse_num(a):
    #a should be a 3-digit number
    #Original number: a//100,(a%100)//10,a%10
    print((a%10)*100+((a%100)//10)*10+a//100)
reverse_num(628)
reverse_num(123)
print("\n")
#Method_02
def reverse_num2(a):
    print(a-99*(a//100)+99*(a%10))
reverse_num2(628)
reverse_num2(123)








