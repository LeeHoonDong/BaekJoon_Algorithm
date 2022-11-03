-- 코드를 입력하세요
# SELECT ORDER_ID,PRODUCT_ID, DATE_FORMAT(out_date,'%Y/%m/%d') as OUT_DATE,
# case when out_date is null then "출고미정"
# when datediff(out_date,'2022-05-01') >0 then "출고대기"
# when datediff(out_date,'2022-05-01') <=0 then "출고완료"
# end as 출고여부
# from food_order
# order by order_id

SELECT ORDER_ID,PRODUCT_ID,DATE_FORMAT(OUT_DATE,'%Y-%m-%d') AS OUT_DATE,
CASE
WHEN OUT_DATE IS NULL THEN "출고미정"
WHEN DATEDIFF(OUT_DATE,'2022/05/01')>0 THEN "출고대기"
WHEN DATEDIFF(OUT_DATE,'2022/05/01')<=0 THEN "출고완료"
END AS "출고여부"
FROM FOOD_ORDER
ORDER BY ORDER_ID