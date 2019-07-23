# a='https://docs.qq.com/blankpage/DUUpWQldMSkJFeUNQ'
# xieyi=a.split('://')[0]
# print(xieyi)
# a=a.split('://')[1]
# print(a)
# yuming=a[:a.find('/')]
# print(yuming)
# uri=a[a.find('/'):]
# print(uri)
#
# #[ ]列表
# #a.append 新增单个值，b.extend 放元祖，列表，字典都可以，print a+b
# a=[0]
# a.append(1)
# a.append('dan')
# print(a)
# b=[2,3,4,5,'hu',9,8,99,66,7,8,10]
# print(a+b)
# #extend 合并两个表，在最后一个
# a.extend(b)
# print(a)
# #pop 删除第几位的字符
# a.pop(2)
# print(a)
# # #pop（）默认删除列表的最后一个元素
# # a.pop()
# # print(a)
# # #清空一个列表
# # a=[]
# # print(a)
# # a.clear()
# # print(a)
# #改
# #根据下表修改某个元素的值
# a[0]=0
# a[1]=4
# #等价
# a[0],a[1]= 0,4
# print(a)
# #查
# #根据下表查询某个元素
# print(a[0])
# print(a[1])
# #遍历（借助循环 ）
# for i in a:
#     print(i)
# #截取
# #截取部分数据
# print(a[1:3])
# #倒叙
# print(a[::-1])
# #隔一个取一个
# print(a[::-2])
# #成员判断
# if (66 in a):
#     print("存在列表中")
# else:
#     print("不存在列表中")
# #列表和元组的区别
# #1，元组只有一个数据的时候，后边必须带一个逗号，列表就不需要、
# b=[1]
# a=(1,)
# #2,元组中的数据不可修改
# #a[0]=2
# #print(a)
# c=(1,2,3)
# d=(4,5,6)
# #元组合并
# print(c+d)
# print(c)
# print(d)
# #截取
# print(c[1:])
# print(c[::-1])
# print(c[::2])
# #截取长度
# print(len(c))


# 字典的特性1，字典中的key是唯一的，创建时如果同一个键被赋值两次，后一个值会被记住
# 字典中新增一对数据
# a ={}
# a['姓名']='胡丹'
# print(a)
# #改
# a['姓名']='zahg'
# print(a)
# #删pop参数只能为key
# #a.pop('姓名')
# #del a[姓名]
# print(a)
# #清空字典
# a.clear()
# print(a)
# #查
# #根据key查看value
# print(a["姓名"])
# #遍历字典（借助循环）
# for key  in a:
# print(a[key])
# 字典合并
# c={'姓名':'hudan'}
# # d={'性别':'女'}
# # print(dict(c,**d))
# #
# # #两个字典合并，生成一个新字典
# # print(dict(c,**d))
# # print(c)
# # print(d)
# 成员判断（key）
# if("性别" in c):
#     print('存在字典中')
# [''D1'', ''H1'', ''H10'', ''H7'', ''S1'', ''S7]
# ["C9", "D6", "D9", "H13", "H9", "S7"]
# ["C2", "D13", "D2", "H2", "H9", "S13"]

def juge_3_2(a):
    # 第一步：统一符号  对字符串的处理，用replace（）
    # a=input()
    a=a.replace("''",'"')
    # 第二步：去掉中括号 字符串截取  [::]
    a=a[2:-2]
    # print(a)
    # 第三步：变成list  字符串切片  .split（） 新建一个list变量
    b=a.split('" , "')
    # print(b)
    # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
    d={}
    for i in b:
        c=i[1:]
    # 第五步：统计相同的数字个数  用字典去统计
        if c in d:
            d[c]=d[c]+1
        else:
            d[c]=1
    # print(d)
    # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
    m=1#key对应的数值有3的，如果没有则为m=0
    n=1#key对应的数值有3的，如果没有则为n=0
    for e in d:
        if(d[e]==3):
            m=1
        if(d[e]==2):
            n=1
    if(m==1 and n==1):
        print('这把三带二带飞')
    else:
        print('要王炸何用')



# juge_3_2()

with open("D:\\softwaredata\\biancheng\\1906dandan\\demo\\day04\\dan.txt") as f:
 d = f.readline()
 for d in f:
     d = d.replace('\n',"")
     print(d)
     juge_3_2(d)






