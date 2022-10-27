#计算BMI指数的计算器
user_gender = input("请输入您的性别： ")
if user_gender == "男":
    Salutation = "先生您好"
else:
    Salutation = "女士您好"
print("\n")

user_weight = float(input("请输入您的体重（单位：kg）： "))
user_height = float(input("请输入您的身高（单位： m）： "))
user_BMI = user_weight/(user_height)**2
print("您的BMI值为"+str(user_BMI))#将数字转换为字符串

if user_BMI <= 18.5:
    print(Salutation + ", 此BMI值属于偏瘦范围。")
elif 18.5 < user_BMI <= 25:
    print(Salutation + ", 此BMI值属于正常范围。")
elif 25 < user_BMI <= 30:
    print(Salutation + ", 此BMI值属于偏胖范围。")
elif user_BMI > 30:#也可以说 else：
    print(Salutation + ", 此BMI值属于肥胖范围。")



