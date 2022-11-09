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
        favorite_jacket=findMax(Users.jacket)#找到最喜爱的上衣类型,0为亮色长袖、1为暗色长袖、2为亮色短袖、3为暗色长袖
        favorite_pants=findMax(Users.pants)#找到最喜欢的下衣类型，0为亮色长裤、1为暗色长裤、2为亮色短裤、3为暗色短裤
        #根据最喜爱的上衣选择
        if favorite_jacket==0:
            file1=open('00//whitejacket.jpg')
        elif favorite_jacket==1:
            file1=open('01//blackjacket.jpg')
        elif favorite_jacket==2:
            file1=open('02//whitets.jpg')
        else:
            file1=open('03//blackts.jpg')
            # 根据最喜爱的下衣选择
            if favorite_pants == 0:
                file2 = open('10//whitepant.jpg')
            elif favorite_pants == 1:
                file2 = open('11//blackpants.jpg')
            elif favorite_pants == 2:
                file2 = open('12//whiteshorts.jpg')
            else:
                file2 = open('13//blackshorts.jpg')
        return [file1,file2]#返回推荐的上衣和下衣









