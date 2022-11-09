import os
def findMax(list):#寻找列表最大值所在的序号
    max=0
    index=0
    for a in range(len(list)):
        if max<list[a]:
            max=list[a]
            index=a
    return index
class Users:#定义用户类
    def __init__(self):
        Users.sex='LGBT'
        Users.jacket=[0,0,0,0]#用户上衣喜好度列表，依次为亮色长袖、暗色长袖、亮色短袖、暗色长袖
        Users.pants=[0,0,0,0]#用户下衣喜好度列表，依次为亮色长裤、暗色长裤、亮色短裤、暗色短裤
    def plusjacket(self,index):#上衣喜好度+1
        Users.jacket[index]=Users.jacket[index]+1
    def minusjacket(self,index):#上衣喜好度-1
        Users.jacket[index]=Users.jacket[index]-1
    def pluspants(self,index):#下衣喜好度+1
        Users.pants[index]=Users.pants[index]+1
    def minuspants(self,index):#下衣服喜好度-1
        Users.pants[index]=Users.pants[index]-1
    def recommend(self):#根据属性推荐穿搭的方法
        favorite_jacket=findMax(Users.jacket)#找到最喜爱的上衣类型
        favorite_pants=findMax(Users.pants)#找到最喜欢的下衣类型
        file=open('C:\\Users\\hua31\\Desktop\\softwarepractice\\repository507\\clothes\\example.jpg')
        return file#返回推荐的图片




