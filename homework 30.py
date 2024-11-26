
"""1․ Գրել MyShows class, որը․
   - __init__ ում կստանա
     -- սերիալի անունը (պետք է լինի տեքստ),
     -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ),
     -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
     -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
     -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
     -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
   - բոլոր ատրիբուտները կլինեն private,
   - կունենա getter բոլոր ատրիբուտների համար,
   - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
   - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
   - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
   - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։"""



class MyShows:
    def __init__(self,name,platform,ep1,mainheroes:list,rate=None,epnum=1):
        if not (isinstance(name,str) or isinstance(platform,str) or isinstance(ep1,int) or isinstance(epnum,int) or  isinstance(mainheroes,list) or isinstance(rate,int)  ) :
            raise Exception("Invalid info")
        if  rate < 1 or rate > 10:
            raise Exception("Invalid info")
        self.__name = name
        self.__platform = platform
        self.__ep1 = ep1
        self.__mainheroes = mainheroes
        self.__rate = rate
        self.__epnum = epnum

    def __str__(self):
        return (f"Name:{self.__name}\n"
                f"Platform:{self.__platform}\n"
                f"1st episode date:{self.__ep1}\n"
                f"Mainheroes:{self.__mainheroes}\n"
                f"Overall rating:{self.__rate}\n"
                f"Episode Number:{self.__epnum}")
    @property
    def all(self):
        return self.__name,self.__platform,self.__ep1,self.__mainheroes,self.__rate,self.__epnum
    @property
    def epnumber(self):
        return f"Episode Number:{self.__epnum}"
    @property
    def rating(self):
        return f"Overall rating:{self.__rate}"
    @epnumber.setter
    def epnumber(self,epnum):
        self.__epnum = epnum
    @rating.setter
    def rating(self,rate):
        self.__rate = rate
    @rating.deleter
    def rating(self):
        new_rating = input('New rating: ')
        self.__rate = new_rating
    def new_mainheroes_add(self,new_chars):
        if not isinstance(new_chars, list):
            raise Exception
        return self.__mainheroes.extend(new_chars)
    def new_mainheroes_remove(self, remove_chars):
        if not isinstance(remove_chars, list):
            raise Exception
        new = [item for item in self.__mainheroes if item not in remove_chars]
        self.__mainheroes = new
        return self.__mainheroes

first = MyShows('You','Netflix',2018,['Joe Goldberg','Love Quinn','Ellie Alves'])
# print(first)
# print(first.all)
# first.epnumber = 2
# print(first.epnumber)
# del first.rating
# first.new_mainheroes_add(["Theo Engler","Peach Salinger"])
# first.new_mainheroes_remove(['Ellie Alves','Love Quinn'])
# print(first)
