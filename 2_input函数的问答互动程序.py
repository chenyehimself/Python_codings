input("给用户的提示")
#用变量去获取input函数返回的值
user_age = input("请输入您的年龄: ")
print("知道了，你今年" + user_age + "岁了！" )
#使用int函数将默认为字符串的input值变成整数的形式 如int("666")就变成了整数666
#使用str函数讲整数变成字符串的形式
#开始实践
#BMI指数计算器
user_weight = float(input("请输入您的体重（单位：kg）： "))
user_height = float(input("请输入您的身高（单位： m）： "))
user_BMI = user_weight/(user_height)**2
print("您的BMI值为"+str(user_BMI))#将数字转换为字符串




