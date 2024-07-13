1. SQL도 재귀가 된다는 사실

```
-- https://school.programmers.co.kr/learn/courses/30/lessons/301651
WITH RECURSIVE GENERATION AS (
    SELECT 
        ID,
        1 AS GEN,
        PARENT_ID
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL

    UNION ALL

    SELECT e.ID, g.GEN + 1 as GEN, e.PARENT_ID
    FROM ECOLI_DATA e
    INNER JOIN GENERATION g ON e.PARENT_ID = g.ID
)

SELECT 
COUNT(*) AS COUNT,
g1.gen AS GENERATION
from GENERATION g1 left join GENERATION g2 ON g1.ID = g2.PARENT_ID
WHERE g2.ID IS NULL
GROUP BY g1.gen
```

2. with  문

공통 테이블 표현(Common Table Expression, CTE)

특정 SQL 문 내에서 임시 결과 집합을 정의할 수 있는 기능

동일한 서브쿼리를 여러 번 사용해야 할 때 유용

복잡한 SQL 쿼리의 가독성과 관리성을 향상

with 문은 한번만 쓸수 있다

```
-- https://school.programmers.co.kr/learn/courses/30/lessons/293261
WITH MAX_TABLE AS
(
    SELECT MAX(LENGTH) AS LENGTH, FISH_TYPE
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)

SELECT 
(select id from FISH_INFO i where i.FISH_TYPE = MAX_TABLE.FISH_TYPE AND i.LENGTH = MAX_TABLE.LENGTH) as ID,
n.FISH_NAME,
MAX_TABLE.LENGTH
FROM MAX_TABLE
LEFT JOIN FISH_NAME_INFO n ON MAX_TABLE.FISH_TYPE = n.FISH_TYPE 
ORDER BY ID
```



3. 서브 쿼리 내에 서브 쿼리 중첩 가능

```

--https://school.programmers.co.kr/learn/courses/30/lessons/301650

SELECT ID FROM ECOLI_DATA WHERE PARENT_ID IN
    (SELECT ID FROM ECOLI_DATA WHERE PARENT_ID IN
        (SELECT ID FROM ECOLI_DATA WHERE PARENT_ID IS NULL))
    ORDER BY ID
```

부모의 부모의 부모가 없는 경우 -> 3세대만 출력하는 코드





;
