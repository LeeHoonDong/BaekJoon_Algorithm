-- 코드를 입력하세요
SELECT animal_id,name, date_format(datetime,"%Y-%m-%d") as 날짜
FROM ANIMAL_INS
ORDER BY animal_id