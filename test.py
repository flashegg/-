#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#文件备份脚本
#定义一个旧文件和新文件，循环写入内容
def powercp(path):
    File = open(path,'r')
    Nowfile = open('/root/passwd_bak','a')
    while True:
        data = File.read()
        if not data:
            break
        Nowfile.write(data)
    File.close()
    Nowfile.close()

powercp('/root/passwd')





#创建文件或目录
#调用os模块
import os
def cjfile(path):
    os.mknod(path)

def cjdir(path):
    os.mkdir(path)




#常见模块
#位置参数的应用
import sys
print(sys.argv[1])

#返回1-10随机数
import random
print(random.randrange(1,10))

#重命名文件
import os
print(os.rename())

#删除指定文件
print(os.remove())

#判断目录是否存在
print(os.path.isdir())






#不同包之间模块导入及使用方法
import pack.hehe
pack.hehe.fun('12a')






#8位数密码生成器
import random,string
pwd = ''
sj = string.ascii_letters + string.digits
for i in range(8):
    pwd += random.choice(sj)
print(pwd)







#菜单
x = ''
caidan = """---------------------------
1、开始
2、退出
---------------------------"""

while not x:
    print('请选择菜单内容：')
    x = input((caidan))
    if x == '1':
        print('ok')
    elif x == '2':
        print('end')
