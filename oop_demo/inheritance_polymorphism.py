#!/usr/bin/env python 
# coding:utf-8
# @Time :11/12/18 08:30

"""
    📋 --->>> 控制台输出（ter）
    🤔 --->>> 解析（thi）
    📢 --->>> 说明（exp）
    🌰 --->>> 例子（exa)
    ------>>> 分割线(sep)

    materials:
        # Python 类的继承和多态
        1. https://www.cnblogs.com/feeland/p/4419121.html

"""


# # 1. 继承父类的属性和方法
#
# class Person:
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#
#     def get_title(self):
#         return "name is {} and sex is {}".format(self.name, self.sex)
#
#
# class Child(Person):
#     pass
#
#
# May = Child("May", "male")
#
# print(May.name, May.sex)
# print(May.get_title())
#
# # 📢：
# #   python2中，父类的超类object不可以省略，即：class Person(object)

# -------------------------------------------- 分割线 --------------------------------------------

# # 2. 继承
# # 实例化用isinstance检测、issubclass检测类的继承
#
# class Person(object):
#     pass
#
#
# class Child(Person):
#     pass
#
#
# May = Child()
# Peter = Person()
#
# print(isinstance(May, Child))       # True
# print(isinstance(May, Person))      # True
# print(isinstance(Peter, Person))    # True
# print(isinstance(Peter, Child))     # False
# print(isinstance(Child, Person))    # False
# print(issubclass(Child, Person))    # True

# -------------------------------------------- 分割线 --------------------------------------------

# # 3. 多态
#
# class Person(object):
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#
#     def print_title(self):
#         if self.sex == "male":
#             print("man")
#         elif self.sex == "female":
#             print("woman")
#
#
# class Child(Person):
#
#     def print_title(self):
#         if self.sex == "male":
#             print("boy")
#         elif self.sex == "female":
#             print("girl")
#
#
# May = Child("May", "female")
#
# print(May.print_title())
#
# # 子类可以继承父类方法，相应的如果对其中的功能有特定需求，如上实例，则可以定义一个同名方法，覆盖父类的方法。
# # 这样做的好处是：
# #   调用方：不关注细节只管调用
# # 著名的“开闭原则”：
# #   1. 对拓展开放：允许子类重写父类同名方法函数
# #   2. 对修改封闭：不重写，直接继承父类方法函数

# -------------------------------------------- 分割线 --------------------------------------------

# # 3. 子类重写构造函数
#
# class Person(object):
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#
#
# # class Child(Person):
# #     def __init__(self, name, sex, father, mother):
# #         self.name = name
# #         self.sex = sex
# #         self.father = father
# #         self.mother = mother
# #
# #
# # May = Child("May", "female", "Tom", "Juily")
# # print(May.name, May.sex, May.father, May.mother)
#
# # 📢：
# #   如果父类有很多属性，子类只需要对特定的几个属性进行修改，那么像上面那样写就太繁琐了，因此可以用以下的方式👇（人生苦短）
#
# class Child_Better(Person):
#     def __init__(self, name, sex, father, mother):
#         Person.__init__(self, name, sex)  # 写法一
#         # super().__init__(name, sex)     # 写法二
#         self.mother = mother
#         self.father = father
#
#
# May = Child_Better("May", "female", "Tom", "Juily")
# print(May.name, May.sex, May.father, May.mother)


# -------------------------------------------- 分割线 --------------------------------------------

# 4. 多重继承（爷爷-父亲-儿子）

# class Person(object):
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#
#     def print_title(self):
#         if self.sex == "male":
#             print("man")
#         elif self.sex == "female":
#             print("woman")
#
#
# # class Child(Person):
# #     pass
# #
# #
# # class Baby(Child):
# #     pass
# #
# #
# # May = Baby("May", "female")
# #
# # May.print_title()
#
#
# class Child(Person):
#
#     def print_title(self):
#         if self.sex == "male":
#             print("boy")
#         elif self.sex == "female":
#             print("girl")
#
#
# class Baby(Child):
#     pass
#
#
# May = Baby("May", "female")
#
# May.print_title()


