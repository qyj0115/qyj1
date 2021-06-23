from pymysql import *
lj=connect(user="root",password="123456",port=3306,
           database="qinyajing",host="localhost",charset="utf8")
yb=lj.cursor()
def main():
    for i in range(10000,10002):
        b=str(i)
        a=("hh_"+b)
        sql = """
            insert into title(name) values(%s)
        """
        try:
            yb.execute(sql,a)
            lj.commit()
        except Exception as e:
            print(f"错误为{e}")
        finally:
            print(f"成功了{yb.rowcount}次")
a=main()
yb.close()
lj.close()

#一、使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，
# 该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典
# 示例：假设向程序提供以下输入:8
# 则输出为:
# {1:1，2:4，3:9，4:16，5:25，6:36，,7:49，8:64}
# n=int(input("请输入一个正整数n："))
# a={}
# for i in range(1,n+1):
#     a[i]=i*i
# print(a)

# 二、编写一个程序，该程序接受控制台以逗号分隔的数字序列，并生成包含每个数字的列表和元组。
# 假设向程序提供以下输入:
# 34岁,67年,55岁,33岁,12日,98年则输出为:['34'， '67'， '55'， '33'， '12'， '98']
# ('34'， '67'， '55'， '33'， '12'， '98')
# import re
# n=input("请输入以逗号分隔的数字序列：")
# a=[]
# c=n.split(",")
# for i in c:
#     d= re.findall("\d+",i)
#     a.append(str(d)[2:-2])
# b=tuple(a)
# print(a,b)

# 三、使用列表推导来对列表中的每个奇数。 该列表由一系列逗号分隔的数字输入
# 假设为程序提供了以下输入：
# 1,2,3,4,5,6,7,8,9
# 然后，输出应该是：
# 1,3,5,7,9
# n=input("请输入数字：")
# k=n.split(",")
# print(k)
# a=[i for i in k if int(i)%2!=0]
# print(",".join(a))

# 四、标题：找出符合要求的字符串子串 时间限制：1秒 内存限制：262144K 语言：不限
# 给定两个字符串，从字符串2中找出字符串1中的所有字去符，重并按照ASCII值从小到大排序
# 输入字符串1:长度不超过1024
# 输入字符串2:长度不超过1000000
# 字符串范围满足ASCII编码要求，按照ASCII的值由小到大排序。
# 示例：
# 输入：
# fach
# bbaaccedfg
# 输出：
# acf

# n1=input("请输入字符串1：")
# n2=input("请输入字符串2：")
# a="".join(sorted(set(n1)&set(n2)))
# print(a)














