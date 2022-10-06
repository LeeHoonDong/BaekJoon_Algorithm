select fp.product_id,fp.product_name,fp.price*filter.amount as total_sales
from food_product as fp
    join (
        SELECT PRODUCT_ID, sum(AMOUNT) as amount
        FROM FOOD_ORDER
        WHERE DATE_FORMAT(PRODUCE_DATE, "%Y/%m") = "2022/05"
        group by product_id
    ) as filter
    on fp.product_id=filter.product_id
order by total_sales desc