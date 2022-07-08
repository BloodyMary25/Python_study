# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел Бокс ТВ целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} денег нет, но вы держитесь!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def to_take_cat(self, cat):
        self.cat = cat
        self.cat.house = self.house
        cprint(' {} подобрал очередного кота  на улице и забрал домой'.format(self.name), color='cyan')

    def to_buy_rybov(self):
        if self.house.money >= 50:
            self.house.food_for_cat += 50
            self.house.money -= 50
            cprint('{} купил вискаса'.format(self.name), color='blue')
        else:
            cprint('Кот голоден, сердит, мстительно поглядывает в твои тапки!', color='magenta')

    def clear_house(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint(' убрал дом, готов к новым делам', color='magenta')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.house.food < 10:
            self.shopping()
        elif self.fullness < 25:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.food_for_cat <= 10:
            self.to_buy_rybov()
        elif self.house.dirt >= 100 and self.fullness >= 20:
            self.clear_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.food_for_cat = 0
        self.dirt = 0

    def __str__(self):
        return f'В доме человеческой еды осталось {self.food}, кошачей еды осталось {self.food_for_cat}, ' \
               f'денег осталось {self.money}, дом грязный на {self.dirt} баллов' # а вот тут пришлось попробовать с f строками


class Cat:

    def __init__(self, name):
        self.fullness = 50
        self.house = None
        self.name = name

    def __str__(self):
        return f'Сытость кота {self.name} составляет {self.fullness}'

    def sleep(self):
        self.fullness -= 10
        cprint(f'Котик {self.name} поспал!', color='blue')

    def eat(self):
        if self.house.food_for_cat >= 10:
            self.fullness += 20
            self.house.food_for_cat -= 10
            cprint(f'Котик {self.name} обожролся!', color='green')
        else:
            cprint(f'Нет еды для кота {self.name}', color='red')

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint(f'Котик {self.name} снова нашкодил!', color='grey')

    def act(self):
        if self.fullness < 0:
            cprint('Вот и помер кот {}...'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.tear_wallpaper()


cats = [
    Cat(name='Юрген'),
    Cat(name='Пушистый засранец'),
    Cat(name='Рыжая бестия '),
    Cat(name='Котя'),

]

people = Man(name='Харальд')
my_house = House()

people.go_to_the_house(house=my_house)
for cat in cats:
    people.to_take_cat(cat=cat)
# citizen.pick_up_cat(cat=my_cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    people.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    print(people)
    for cat in cats:
        print(cat)
    # print(my_cat)
    print(my_house)
