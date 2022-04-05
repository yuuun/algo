### https://programmers.co.kr/learn/courses/30/lessons/59409

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, 
    CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' or SEX_UPON_INTAKE LIKE '%Spayed%'
    THEN 'O'
    ELSE 'X'
    END 중서화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID