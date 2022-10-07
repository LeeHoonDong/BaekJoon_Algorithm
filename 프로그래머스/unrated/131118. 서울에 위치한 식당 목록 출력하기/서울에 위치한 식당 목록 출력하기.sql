-- 코드를 입력하세요
select rest_info.rest_id,rest_name,food_type,favorites,address,score
from rest_info
    join (
        select rest_id,round(avg(review_score),2) as score
        from rest_review
        group by rest_id
    ) as rr
    on rest_info.rest_id=rr.rest_id
where address like "서울%"
order by score desc, favorites desc




# 00001	5.00
# 00004	4.29
# 00018	4.00
# 00013	4.00
# 00024	4.67
# 00002	4.50
# 00003	4.00