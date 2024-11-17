import math
"""1․ Գրել ֆունկցիա, որը․
   - որպես արգումենտ կընդունի շրջանագծի շառավիղը (r) և սեկտորի անկյունը (alpha) ռադիաններով արտահայտված,
   - կհաշվի և կտպի համապատասխան շառավղով և անկյունով սեկտորի մակերեսը,
   - բանաձևը՝ S = (pi * r ** 2) * alpha / 360, բանաձևի մեջ alpha-ն արտահայտված է աստիճաններով։
2․ Գրել ֆունկցիա, որը․
   - կստանա արգումենտ արաբական բնական թիվ (0-ից մեծ),
   - կվերադրձնի այդ թիվը հռոմեական տեսքով,
   հռոմեական թվերի համարժեքները՝ I-1, V-5, X-10, L-50, C-100, D-500, M-1000,
   օրինակ՝ 15 -> XV,
           72 -> LXXII
           9 -> IX:
3․ Գրել ֆունկցիա, որը․
   - տրված բառերի list-ը կֆիլտրի այնպես, որ կթողի միայն ամենաերկար բառերը
     (այսինքն՝ կգտնի ամենաերկար բառի երկարությունը և լիստում կթողնի միայն այդ երկարության բառերը),
   օրինակ՝ input = ["aba", "aa", "z", "ad", "vcd", "aba"]
           output = ["aba", "vcd", "aba"],

           input = ["aba", "aa", "z", "advc", "vcd", "aba"]
           output = ["advc"],
4. Գնահատեք Ձեր գրած կոդերը Big O notation-ի միջոցով։
"""

# Task 1 | O(n)
# def area(r,alpha):     
#     S = (math.pi * r ** 2) * math.degrees(alpha) / 360
#     print(f'Area = {S}')
# area(5,1)

# Task 2 | O(n)
# d = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,'I':1}
# num = int(input("Enter the arabic number: "))
# romanian = str()
#
# for i,j in d.items():d
#     while num >= j:
#         romanian += i
#         num -= j
# print(romanian)


# Task 3 | O(n)
# lst = ["aba", "aa", "z", "ad", "vcd", "aba"]
# max_inlst = max(lst,key=len)
# changed = []
# for i in lst:
#     if len(i) == len(max_inlst):
#         changed.append(i)
# print(changed)

# 2nd list
# lst = ["aba", "aa", "z", "advc", "vcd", "aba"]
# max_inlst = max(lst,key=len)
# changed = []
# for i in lst:
#     if len(i) == len(max_inlst):
#         changed.append(i)
# print(changed)
