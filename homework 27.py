import math
"""1․ Գրել Triangle class, որը․
   - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
     եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
   - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
   - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
   - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
   - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն),
   - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը ուղղանկյուն եռանկյուն է, թե ոչ,
   - կունենա մեթոդ, որը կգտնի եռանկյան անկյունները,
   - կարող եք գրել նաև այլ մեթոդներ, որոնց միջոցով կստանաք տրված եռանկյան վերաբերյալ այլ ինֆորմացիա
     (օրինակ՝ ներգծած և արտագծած շրջանագծերի շառավղերը և այլն)․ բանաձևերը կարող եք գտնել համացանցում։
"""


# class Triangle:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#         if not a + b > c:
#             print("Error,try again")
#         elif not a + c > b:
#             print("Error,try again")
#         elif not c + b > a:
#             print("Error,try again")
#
#     def __str__(self):
#         return f"a={self.a},b={self.b},c={self.c}"
#     def perimeter(self):
#         print(self.a + self.b + self.c)
#     def area(self):
#         p = (self.a + self.b + self.c) / 2
#         print((p * ((p - self.a) * (p - self.b) * (p - self.c))) ** 0.5)
#     def shape(self):
#         if self.a == self.b and self.a == self.c and self.b == self.c:
#             print('Shape is equilateral')
#         elif self.a != self.b and self.a != self.c and self.c != self.b:
#             print('Shape is scalene')
#         else:
#             print('Shape is isosceles')
#
#     def right_angle(self):
#         if ((self.a ** 2) + (self.b ** 2)) == (self.c ** 2) or ((self.a ** 2) + (self.c ** 2)) == (self.b ** 2) or ((self.c ** 2) + (self.b ** 2)) == (self.a ** 2):
#             print('This is right-angle triangle')
#         else:
#             print('This is not right-angle triangle')
#     def angles(self):
#         angle_a = math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c))
#         angle_b = math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))
#         angle_c = math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b))
#         angle_a_degree = round(math.degrees(angle_a),1)
#         angle_b_degree = round(math.degrees(angle_b),1)
#         angle_c_degree = round(math.degrees(angle_c),1)
#         print(f'1st angle:{angle_a_degree}|2nd angle:{angle_b_degree}|3rd angle:{angle_c_degree}')
#
#
# tri = Triangle(a=3,b=4,c=5)
# print(tri)
# tri.perimeter()
# tri.area()
# tri.shape()
# tri.right_angle()
# tri.angles()
