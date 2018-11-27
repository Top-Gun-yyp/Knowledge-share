from demo.extends.father import *
from demo.extends.teacher import *
class son(father,teacher):
    def __init__(self,name,age,grade):
        self.name = name
        self.__age = age
        self.grade = grade
    def getSonAge(self):
        return self.__age
if __name__ =='__main__':
    s = son('hh',12,'大学')
    #s.printName()
    #s.printGrade()
    # 外部不能访问了
   # print(s.age)
    # 只有内部可以访问
    print(s.getSonAge())
