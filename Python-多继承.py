# 如果不同的父类中存在同名的方法，子类对象在调用方法时，会调用哪一个父类中的方法呢
# 是按照__mro__的输出结果从左至右的顺序查找的


# super().__init__相对于类名.__init__，在单继承上用法基本无差
# super方法能保证每个父类的方法只会执行一次，而使用类名的方法会导致方法被执行多次
class Parent(object):

    def __init__(self, name, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):

    def __init__(self, name, age, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1的init结束被调用')


class Son2(Parent):

    def __init__(self, name, gender, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2的init结束被调用')


class Grandson(Son1, Son2):

    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        # 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍
        # 而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
        # super(Grandson, self).__init__(name, age, gender) 效果和下面的一样
        super().__init__(name, age, gender)
        print('Grandson的init结束被调用')


# method resolution order
print(Grandson.__mro__)  #搜索顺序

gs = Grandson('grandson', 12, '男')

print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)

'''结果如下：
(<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
Grandson的init开始被调用
Son1的init开始被调用
Son2的init开始被调用
parent的init开始被调用
parent的init结束被调用
Son2的init结束被调用
Son1的init结束被调用
Grandson的init结束被调用
姓名： grandson
年龄： 12
性别： 男
'''
