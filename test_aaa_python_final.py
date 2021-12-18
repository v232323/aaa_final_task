import pytest
import aaa_python_final
from unittest.mock import patch
import time

def test_make_xl_recipe():
    assert aaa_python_final.make_xl_recipe({
        'tomato sauce': 1,
        'mozzarella': 1,
        'chicken': 1,
        'pineapples': 1,
        }) == {
            'tomato sauce': 2,
            'mozzarella': 2,
            'chicken': 2,
            'pineapples': 2,
        }


def test_pizza_class_dict_method():
    pz = aaa_python_final.Pizza(ingr = {'tomato sauce': 1, 'mozzarella': 1})
    assert pz.dict() == {'tomato sauce': 1, 'mozzarella': 1}


def test_pizza_class_ex_method():
    pz1 = aaa_python_final.Pizza(ingr={'tomato sauce': 1, 'mozzarella': 1})
    pz2 = aaa_python_final.Pizza(ingr={'tomato sauce': 1, 'mozzarella': 1})
    assert pz1 == pz2


def test_bake():
    mar = aaa_python_final.Margherita()
    with patch.object(time, 'sleep') as sleep:
        aaa_python_final.bake(mar)
        sleep.assert_called_once()


def test_delivery():
    mar = aaa_python_final.Margherita()
    with patch.object(time, 'sleep') as sleep:
        aaa_python_final.delivery(mar)
        sleep.assert_called_once()


def test_pickup():
    mar = aaa_python_final.Margherita()
    with patch.object(time, 'sleep') as sleep:
        aaa_python_final.pickup(mar)
        sleep.assert_called_once()