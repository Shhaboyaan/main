from abc import ABC, abstractmethod
import math

"""1. Գրել Animal ծնող class՝ eat() և sleep() մեթոդներով:
   - Այս մեթոդներից յուրաքանչյուրը պետք է վերադարձնի համապատասխան հաղորդագրություն, երբ կանչ է արվում։
   - eat()-ը պետք է վերադարձնի "Animal is eating..." հաղորդագրությունը
   - sleep()-ը պետք է վերադարձնի "Animal is sleeping..." հաղորդագրությունը
   Ծրագիրը պետք է ներառի նաև երկու ժառանգ class-ներ, որոնք ժառանգում են Animal class-ը՝ Bird և Fish:
   Այս class-ները Animal class-ից պետք է ժառանգեն sleep() մեթոդը, բայց նաև պետք է ներառեն իրենց մեթոդները՝ ներկայացնելու համար կենդանիներին բնորոշ վարքագիծը:
   - Bird class-ում, փոփոխեք eat() մեթոդը՝ "Bird is pecking at its food..." հաղորդագրությունը վերադարձնելու համար։
   - Բացի այդ, ներառեք fly() մեթոդը, որը վերադարձնում է "Bird is flying..." հաղորդագրությունը:
   - Fish class-ում ներառեք swim() մեթոդը, որը վերադարձնում է "Fish is swimming..." հաղորդագրությունը:
2․ Գրել Shape abstract class, որը․
   - կունենա __init__(), perimetr(), area() աբստրակտ մեթոդներ։
   Գրել Circle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի շրջանագծի շառավիղը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտը ճիշտ մուտքագրված լինի (պետք է լինի դրական թիվ),
   - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները շրջանագծի համար։
   Գրել Rectangle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի ուղղանկյան լայնությունը և երկարությունը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն (պետք է լինեն դրական թվեր),
   - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները ուղղանկյան համար։
   Գրել Triangle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի
     -- կամ եռանկյան երեք կողմերը,
     -- կամ մեկ կողմը և բարձրությունը,
     -- կամ երկու կողմերը և այդ կողմերի կազմած անկյունը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն,
   - կվերախմբագրի Shape class-ի perimetr() մեթոդը եռանկյան համար,
   - եռանկյան մակերեսը կհաշվի 3 տարբերակով, կախված մուտքագրված պարամետրերից․
     1) S = (p * (p - a) * (p - b) * (p - c)) ^ 0.5   , որտեղ a, b, c - եռանկյան կողմերն են, p - եռանկյան կիսապարագիծը,
     2) S = a * h / 2                                 , որտեղ a - եռանկյան կողմը, h = եռանկյան բարձրությունը,
     3) S = a * b * sin(alpha) / 2                    , որտեղ a, b - եռանկյան կողմերն են, alpha - եռանկյան a և b կողմերի կազմած անկյունը։"""


# # Task 1
#
# class Animal:
#     @staticmethod
#     def eat():
#         return "Animal is eating..."
#     @staticmethod
#     def sleep():
#         return "Animal is sleeping..."
# class Bird(Animal):
#     @staticmethod
#     def eat():
#         return "Bird is pecking at its food..."
#     @staticmethod
#     def fly():
#         return "Bird is flying..."
# class Fish(Animal):
#     @staticmethod
#     def swim():
#         return "Fish is swimming..."
#
# animal = Animal
# animal1 = Bird
# animal2 = Fish
# print(animal.eat())
# print(animal1.eat())
# print(animal1.fly())
# print(animal1.sleep())
# print(animal2.eat())
# print(animal2.sleep())

# Task 2

# class Shape(ABC):
#     @abstractmethod
#     def __init__(self):
#         raise Exception
#
#     @abstractmethod
#     def perimetr(self):
#         raise Exception
#
#     @abstractmethod
#     def area(self):
#         raise Exception
#
#
# class Circle(Shape):
#     def __init__(self, r):
#         if r <= 0:
#             raise Exception('Error,try again')
#         else:
#             self.r = r
#
#     def perimetr(self):
#         return 2 * math.pi * self.r
#
#     def area(self):
#         return math.pi * self.r ** 2
#
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         if length <= 0 or width <= 0:
#             raise Exception('Error,try again')
#         else:
#             self.l = length
#             self.w = width
#     def perimetr(self):
#         return 2 * (self.l + self.w)
#     def area(self):
#         return self.l * self.w
#
# class Triangle(Shape):
#     def __init__(self,*args,flag=0):
#         self.flag = flag
#         if len(args) == 3 and isinstance(args[2],float):
#             self.a, self.b, self.angle= args
#             self.angle = int(self.angle)
#             self.flag = 3
#         elif len(args) == 2 and isinstance(args[0] and args[1] , (int, float)):
#           self.base, self.height = args
#           self.flag = 2
#         elif len(args) == 3 and isinstance(args[2],int) :
#            if args[0] + args[1] <= args[2] or args[0] + args[2] <= args[1] or args[1] + args[2] <= args[0]:
#                raise ValueError('Impossible triangle')
#            self.a, self.b, self.c = args
#            self.flag = 1
#
#
#     def perimetr(self):
#         if self.flag == 1:
#             a,b,c = self.a, self.b, self.c
#             return a + b + c
#         elif self.flag == 2:
#             return"Not enough info for perimetr"
#
#         elif self.flag == 3:
#             a,b,angle = self.a, self.b, math.radians(self.angle)
#             c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle))
#             return a + b + c
#     def area(self):
#         if self.flag == 1:
#             a,b,c = self.a, self.b, self.c
#             p = (a + b + c) / 2
#             p = int(p)
#             S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#             return S
#         elif self.flag == 2:
#             a = self.base
#             h = self.height
#             S = a * h / 2
#             return S
#         elif self.flag == 3:
#             a,b,angle = self.a, self.b,self.angle
#             S = (a * b * math.sin(math.radians(angle))) / 2
#             return S
#
# tri = Triangle(3,4,5) # for angle use float to differentiate from side
# print(tri.perimetr())
# print(tri.area())
