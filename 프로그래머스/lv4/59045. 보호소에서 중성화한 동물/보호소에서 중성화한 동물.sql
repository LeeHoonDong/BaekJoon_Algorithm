-- 코드를 입력하세요
SELECT animal_ins.animal_id,animal_ins.animal_type,animal_ins.name
from animal_ins
    join animal_outs
    on animal_ins.animal_id=animal_outs.animal_id
where animal_ins.sex_upon_intake!=animal_outs.sex_upon_outcome
order by animal_id