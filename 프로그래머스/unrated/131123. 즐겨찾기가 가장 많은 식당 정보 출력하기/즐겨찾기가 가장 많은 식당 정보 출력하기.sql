# -- 코드를 입력하세요

select food_type,rest_id,rest_name,favorites
from rest_info
where (food_type,favorites) in (select food_type,max(favorites)
from rest_info
group by food_type)
order by food_type desc

# select food_type,max(favorites)
# from rest_info
# group by food_type

#분식 151 00008 애플우스
#양식 102 00003	따띠따띠뜨
#일식 230 00004 스시사카우스
#중식 20
#한식 734 00001 은돼지식당