"""1․ Գրել BankUser class, որը․
   - __init__() -ում կընդունի մարդու անունը, ազգանունը, տարիքը, հաշվեհամարը, գումարը հաշվեհամարի վրա, գաղտնաբառը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ են մուտքագրված՝
     -- անունը և ազգանունը - տառերից բաղկացած,
     -- տարիքը - բնական թիվ,
     -- հաշվեհամարը - 16 թվանշանից բաղկացած (xxxx xxxx xxxx xxxx կամ xxxxxxxxxxxxxxxx ֆորմատով),
     -- գումարը - դրական թիվ,
     -- գաղտնաբառը - ամենաքիչը 8 սիմվոլից բաղկացած տեքստ,
   - անունը, ազգանունը և տարիքը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի պաշտպանված,
   - հաշվեհամարը, գումարը և գաղտնաբառը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի արգելված,
   - կունենա մեթոդ, որը կվերադարձնի մարդու անունը, ազգանունը և տարիքը,
   - կունենա մեթոդ, որը կվերադարձնի հաշվեհամարը և գումարը, բայց միայն ճիշտ գաղտնաբառ հավաքելուց հետո,
   - կունենա մեթոդ, որը կավելացնի գումար հաշվին,
   - կունենա մեթոդ, որը կհանի գումար հաշվից, հաշվի առեք, որ գումարը բացասական չի կարող լինել,
   - 3 անգամ սխալ գաղտնաբառ հավաքելուց հետո տվյալ user-ի համար հասանելիությունը class-ի ամբողջ ֆունկցիոնալությանը կլինի արգելված,
   - կունենա մեթոդ, որի միջոցով կվերականգնվի հասանելիությունը անունը, ազգանունը և հաշվեհամարի վերջին 4 թվանշանները մուտքագրելուց հետո։"""


class BankUser:
    @classmethod
    def card_numbers(cls, nums):
        if  nums.isdigit() and len(nums) == 16:
            return True
        else:
         sp = nums.split(' ')
         s = ''
         sp1 = s.join(sp)
         for i in sp:
             if len(i) != 4:
                 raise Exception
         if len(sp1) > 16 or len(sp1) < 16:
             raise Exception
         if not sp1.isdigit():
             raise Exception
         else:
            return True

    def __init__(self, name: str, surname: str, age: int, card: str, password, money: int = 0):
        if name.isalpha() and surname.isalpha() and age > 0 and self.card_numbers(card) and money >= 0 and len(password) >= 8:
            self._name = name
            self._surname = surname
            self._age = age
            self.__card = card
            self.__money = money
            self.__password = password
        else:
            raise Exception

    def __str__(self):
        return f'Name:{self._name} | Surname:{self._surname} | Age:{self._age}'

    def validate(self, pass_2):

        if pass_2 == self.__password:
            return f'account number։ {self.__card} | money: {self.__money}'
        else:
            return 'Wrong password'

    def add(self, amount):
        self.__money += amount
        return f'Was: {self.__money - amount}, now: {self.__money}'

    def ext(self, amount):
        if (self.__money - amount) >= 0:
            self.__money -= amount
            return f"Before: {self.__money + amount}, now: {self.__money}"
        else:
            return f'Not enough amount of money,right now you have: {self.__money} '


bank = BankUser('Aram', 'Manukyan', 19, '1231 2414 2444 4242', '12345678')
print(bank)
print(bank.validate('12345678'))
print(bank.add(10))
print(bank.add(100))
print(bank.ext(50))
print(bank.ext(50))
print(bank.ext(50))
print(bank.add(40))
