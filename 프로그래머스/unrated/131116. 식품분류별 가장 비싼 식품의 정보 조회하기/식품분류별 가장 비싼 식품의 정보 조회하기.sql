-- 코드를 입력하세요
select category,price as MAX_PRICE, product_name
from food_product
where (category,price) in (
    SELECT category,max(price)
    from food_product
    group by category
    having category in ('식용유','과자','국','김치')
)
order by price desc


#과자 1950
#국 2900
#김치	19000
#식용유	8950