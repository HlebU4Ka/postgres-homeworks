-- Напишите запросы, которые выводят следующую информацию:
-- 1. заказы, доставленные в страны France, Germany, Spain (таблица orders, колонка ship_country)
select *
from orders
where ship_country in ('France', 'Germany', 'Spain')

-- 2. уникальные города и страны, куда отправлялись заказы, отсортировать по странам и городам (таблица orders, колонки ship_country, ship_city)
select DISTINCT ship_city, ship_country
from orders

-- 3. сколько дней в среднем уходит на доставку товара в Германию (таблица orders, колонки order_date, shipped_date, ship_country)
select avg(shipped_date - order_date) as average_delivery_days
from orders
where ship_country = 'Germany'

-- 4. минимальную и максимальную цену среди продуктов, не снятых с продажи (таблица products, колонки unit_price, discontinued не равно 1)
SELECT MIN(unit_price) AS min_price, MAX(unit_price) AS max_price
FROM products
WHERE discontinued <> 1;

-- 5. минимальную и максимальную цену среди продуктов, не снятых с продажи и которых имеется не меньше 20 (таблица products, колонки unit_price, units_in_stock, discontinued не равно 1)
select min(unit_price) as min_price, max(unit_price) as max_price

from products
where discontinued <> 1 and units_in_stock >= 20