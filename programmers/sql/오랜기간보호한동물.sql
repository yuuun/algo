-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A LEFT OUTER JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.DATETIME IS NOT NULL
ORDER BY B.DATETIME - A.DATETIME DESC
LIMIT 2

select ai.animal_id, ai.name
from animal_ins ai left outer join animal_outs ao
on ai.animal_id = ao.animal_id
order by ao.datetime - ai.datetime desc
limit 2