# oracle , mysql과 다른점 + 쿼리

- limit: WHERE ROWNUM BETWEEN 0 AND 10;

- group by 
  
  - mysql:group by 에 선택 되지 않은 컬럼을 포함 가능
  - 복수의 값중 하나 임의 선택 -> 실행계획중 가장 코스트가 낮은것
  - 오라클은 group by에 포함되지 않은 컬럼을 select 불가

- 실행순서

- 시퀀스 다음값: nextval

- 현재시간 : `sysdate`

- 날짜 포멧 변환
  
  ```
  SELECT 
  TO_CHAR(SYSDATE, 'YYYY-MM-DD'), --현재날짜 /
  TO_CHAR(SYSDATE, 'YYYY-MM-DD'), --현재날짜 -
  TO_CHAR(SYSDATE, 'YYYY'), --현재년도
  TO_CHAR(SYSDATE, 'MM'), --현재 월
  TO_CHAR(SYSDATE, 'DD'), --현재 일
  TO_CHAR(SYSDATE, 'DAY'), --현재 요일
  TO_CHAR(SYSDATE, 'HH24:MI:SS'), --현재시간 포맷 (24시간)
  TO_CHAR(SYSDATE, 'HH:MI:SS') --현재시간 포맷 (12시간)
  FROM
  DUAL
  ```

- 컬럼명이 예약어일때 `"컬럼명"`

- 대소문자 구분X

---

다중 입력

```sql
insert all
    into talbe(...) values(...)
```

```sql
insert into talbe(...)
select ... from dual union all
select ... from dual union all
selct ... from dual;
```

union all 이 더빨라요

index 설정을 해도 속도가 개선되지 않는다면? 실행계획을 보자 

dbeaver: `ctrl + shift + E`

카디널리티가 높은 순으로 index가 항상 정답은 아닐수 있다!
