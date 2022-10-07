with recursive cte as(
    select 0 as num
    union all
    select num+1 from cte
    where num<23
)
select num,if(count1 is null,0,count1) as count
from cte
    left join (
        select hour(datetime) as hour,count(hour(datetime)) as count1
        from animal_outs 
        group by hour(datetime) 
        order by hour(datetime)
    ) as t1
    on cte.num=t1.hour


# # IF(NAME IS NULL,"No name",NAME)
# select * from animal_outs