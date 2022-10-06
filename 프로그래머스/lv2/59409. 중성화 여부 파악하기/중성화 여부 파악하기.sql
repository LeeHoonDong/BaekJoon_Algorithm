-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
    CASE
    WHEN (SEX_upon_intake like "%Neutered%" or sex_upon_intake like "%spayed%") then 'O'
    else 'X'
    end as 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID