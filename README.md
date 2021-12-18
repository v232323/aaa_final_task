
**Для запуска из командной строки:**

Показать меню:
```
python aaa_python_final.py menu
```

Заказать пиццу pepperoni или margherita или hawaiian:
```
python aaa_python_final.py order pepperoni
```
Заказать пиццу с доставкой. Нужно использовать --delivery_flg:
```
python aaa_python_final.py order pepperoni --delivery_flg   
```
Заказать большую пиццу с доставкой. Нужно использовать --big_flg:
```
python aaa_python_final.py order pepperoni --delivery_flg --big_flg
```


**Тесты:**

```
coverage run -m pytest test_aaa_python_final.py
```
Отчет по покрытию тестами. Покрыто 71% кода:
```
 coverage report -m aaa_python_final.py
```
Отчет в html:
```
coverage html
```
