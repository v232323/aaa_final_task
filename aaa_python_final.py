from random import randint
import time
import click

MARGHERICA_RECIPE = {
    'tomato sauce': 1,
    'mozzarella': 1,
    'tomatoes': 1,
}
PEPPERONI_RECIPE = {
    'tomato sauce': 1,
    'mozzarella': 1,
    'pepperoni': 1,
}
HAWAIIAN_RECIPE = {
    'tomato sauce': 1,
    'mozzarella': 1,
    'chicken': 1,
    'pineapples': 1,
}
MENU = {
    'MARGHERICA 🧀': MARGHERICA_RECIPE,
    'PEPPERONI 🍕': PEPPERONI_RECIPE,
    'HAWAIIAN 🍍': HAWAIIAN_RECIPE,
}


def make_xl_recipe(ingr):
    """
    Функция делает из рецепта пиццы рецепт большой пиццы, умножая ингридиенты на два
    """
    xl_recipe = ingr.copy()
    for key in xl_recipe:
        xl_recipe[key] *= 2
    return xl_recipe


class Pizza():
    """
     Класс пицца, от которого будут наследоваться все прочие пиццы
    """
    def __init__(self, ingr: dict = {}, size: str = 'L'):
        if size.upper() in ('L', 'XL'):
            self.size = size.upper()
        else:
            raise ValueError(f'Size {size} is not available')
        if size == 'L':
            self.ingr = ingr
        elif size == 'XL':  # если пицца большая, то рецепт удваивается
            self.ingr = make_xl_recipe(ingr)

    def dict(self):
        """
        Функция возвращает рецепт пиццы ввиде словаря
        """
        return self.ingr

    def __eq__(self, other):
        """
        Проверяет пиццы на равенство. Пиццы равны, если у них полностью равные рецепты
        """
        return self.ingr == other.ingr


class Margherita(Pizza):
    def __init__(self, ingr: dict = MARGHERICA_RECIPE, size: str = 'L'):
        super().__init__(ingr, size)


class Pepperoni(Pizza):
    def __init__(self, ingr: dict = PEPPERONI_RECIPE, size: str = 'L'):
        super().__init__(ingr, size)


class Hawaiian(Pizza):
    def __init__(self, ingr: dict = HAWAIIAN_RECIPE, size: str = 'L'):
        super().__init__(ingr, size)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery_flg', default=False, is_flag=True)
@click.option('--big_flg', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery_flg: bool, big_flg: bool):
    """Готовит и доставляет пиццу"""
    if big_flg:
        size = 'XL'
    else:
        size = 'L'
    if pizza == 'pepperoni':
        order_pizza = Pepperoni(size=size)
    elif pizza == 'margherita':
        order_pizza = Margherita(size=size)
    elif pizza == 'hawaiian':
        order_pizza = Hawaiian(size=size)
    bake(order_pizza)
    if delivery_flg:
        delivery(order_pizza)
    else:
        pickup(order_pizza)


@cli.command()
def menu():
    """Выводит меню"""
    for pizza in MENU:
        ing_str = ', '.join(list(MENU[pizza].keys()))
        print(f'{pizza}: {ing_str}')


def log(tag: str = None):
    """
    Универсальный (можно с параметром, а можно без) декоратор
    Печатает время выполнения функции
    При запуске с параметром tag использует его для более красивого вывода
    """
    def outer_wrapper(func):
        def inner_wrapper(pizza: Pizza):
            start_time = time.time()
            func(pizza)
            finish_time = time.time() - start_time
            if tag is None:
                print(f'{func.__name__} - {finish_time}c!')
            else:
                print(tag.format(finish_time))

        return inner_wrapper

    return outer_wrapper


@log('🍳 Приготовили за {}с!')
def bake(pizza: Pizza):
    """Готовит пиццу"""
    time.sleep(randint(1, 5))


@log('🛵 Доставили за {}с!')
def delivery(pizza: Pizza):
    """Доставляет пиццу"""
    time.sleep(randint(1, 5))


@log('🏡 Забрали за {}с!')
def pickup(pizza: Pizza):
    """Самовывоз"""
    time.sleep(randint(1, 5))


if __name__ == '__main__':
    cli()
