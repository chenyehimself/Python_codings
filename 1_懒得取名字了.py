print("hi")
print("\n")
#print加上+可以将字符串连接 但是中间是没有空格的
print("I" + " Love" + " You" )
print("\n")
print("He said \"let\'s go!\"")
#在 字符串 里的引号前放一个 反斜杠 表示里面的引号单纯就是引号 是内容的一部分
print("\n")
#反斜杠叫做转义符 只要字符串里面有反斜杠 和后面的符号一起读 产生特殊的意思
#\n 表示换行
print("Hello!\nHi!")
print("\n")
# 三引号的使用 大段的引用中换行将被默认为文本内容的换行
print("""Dear Delores
When I think of you, 
I am reminded of the beautiful plains in Iowa. 
The distance between us is breaking my spirit. 
My time and experiences without you are meaningless to me. 
Falling in love with you was the easiest thing I have ever done. 
Nothing matters to me but you. 
And every day I am alive, I am aware of this. 
I love you the day I met you. 
I love you today. And I will love you the rest of my life.
""")
print("\n")

#变量 先取名字 不能有空格 和数字开头 且不能用引号包裹（赋值操作）
My_idol ="Kevin Durant"
print(My_idol +" yyds")
#变量的重新赋值有顺序
My_love = "IU"
My_ex = My_love
My_love = "鞠婧祎"
print("I love "+My_love)
print("\n")
#变量的存储&便于替换
greet= "哈罗亲爱的"
greet_Chinese=greet
greet_English="Yo what\'s up "
print(greet_English +"Andrew")
print(greet_English +"Jackie")
print("\n")
print(greet_Chinese +"Andrew")
print(greet_Chinese +"Jackie")
#变量大小写是敏感的 不要占用函数的命名 关键字python自己会提示成彩色的
print("\n")
#数学运算 乘方：** 例如 二的三次方：2**3
#导入math函数库（默认有的叫做内置函数）
import math
#去python官网看各个函数的基本使用方法
math.log2(8)#运算完了需要打印
print(math.log2(8))
print("\n")
#或者用变量赋值
result = math.log2(8)
print(result)
print("\n")
#写一个一元二次求根计算器
import math
a=1
b=9
c=20
print((-b + math.sqrt(b**2-4*a*c))/(2*a)) #sqrt表示根号
print((-b - math.sqrt(b**2-4*a*c))/(2*a))
print("\n")
#代码的好处：可以看出整个公式 可以改变变量的值 可以中间变量分步骤
#很多行自动加/取消井号变成注释：command+/
#三引号中间大段的注释

'''
计算字符串的长度：len函数 空格数字等都会占据长度 完整的转义符被计算成一个长度
字符串后跟上方括号 然后再方括号里面放索引 就能提取该索引位置的字符 从0开始数
整数：int 浮点数：float
布尔类型bool 真True 假False
空值类型Nonetype None 完全没有值 如My_Wife=None
当不确定对象类型的时候用type函数返回该对象的类型
'''

# 对字符串求长度
s="hello my love"
print(len(s))
print("\n")

# 通过索引获取单个字符（从0开始）
print(s[0])#结果为H
print(s[len(s)-1])
print(s[9]+s[10]+s[11]+s[12])
print("\n")

# 布尔类型 True要大写 不加引号
b1 = True
b2 = False

# 空值类型
n = None

# type函数
print(type(s))
print(type(b1))
print(type(b2))
print(type(n))
print(type(1.5))
print(type(2))






