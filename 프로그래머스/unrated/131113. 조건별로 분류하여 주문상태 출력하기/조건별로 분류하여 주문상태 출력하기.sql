-- 코드를 입력하세요
SELECT ORDER_ID,PRODUCT_ID, OUT_DATE,
case when out_date is null then "출고미정"
when datediff(out_date,'2022-05-01') >0 then "출고대기"
when datediff(out_date,'2022-05-01') <=0 then "출고완료"
end as 출고여부
from food_order
order by order_id