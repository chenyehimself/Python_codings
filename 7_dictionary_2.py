print("这是一款从百度上摘抄的流行词词典程序，欢迎您的使用！")
slang_dictionary = {"摆烂":"摆烂是一种正常的表达。有些人摆烂是因为实在是“烂”的不行了，属于真实写照。往往摆烂背后，常常是一种无奈的过稀碎的生活。"}
slang_dictionary["yyds"] = "永远的神"
slang_dictionary["芭比Q了"] = "完蛋了"
slang_dictionary["破防"] = "突破心理防线"
slang_dictionary["躺平"] = "躺平，网络流行词，指无论对方做出什么反应，你内心都毫无波澜，对此不会有任何反应或者反抗，表示顺从心理。"
slang_dictionary["内卷"] = "内卷，网络流行语，原指一类文化模式达到了某种最终的形态以后，既没有办法稳定下来，也没有办法转变为新的形态，而只能不断地在内部变得更加复杂的现象。"
slang_dictionary["元宇宙"] = "元宇宙（Metaverse）是利用科技手段进行链接与创造的，与现实世界映射与交互的虚拟世界，具备新型社会体系的数字生活空间。"
slang_dictionary["emo"] = "忧郁了"
slang_dictionary["寄"] = "完蛋了，近似于\"芭比Q了\""
query = input("请输入你想要查询的流行词: ")
if query in slang_dictionary:
    print(query + "的意思是")
    print(slang_dictionary[query])
else:
    print("非常抱歉，您所查询的流行词词条当前词典并未收录。")
    print("当前本流行词词典共收录词条" + str(len(slang_dictionary)) + "条。")
print("感谢您的使用！")



