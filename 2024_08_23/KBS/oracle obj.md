1. limit   WHERE ROWNUM BETWEEN 0 AND 10;

2. group by -> mysql 이랑 다른점
   - group by 에 선택 되지 않은 컬럼을 포함 가능
   - 복수의 값중 하나  임의 선택
   - 오라클은 group by에 포함되지 않은 컬럼을 select 불가
   
3. having

4. 실행순서

5. join

6. 시퀀스 nextval

7. 현재시간

8. 날짜 포멧 변환

9. 컬럼명이 예약어일때 `"컬럼명"`

10. 커밋 안한것도 읽어지는 데요?
    1. 세션 내부에서 읽을때 -> 생각해보니 커밋 안되도 읽어져야하는거 같다
    2. `commit` 을 하자
    
11. insert_all  constraint primary key -> select union all을 쓰자

12. ansi vs oracle

    https://devscb.com/post/246/





할일

---

### 계정

계정 생성

- https://viera.tistory.com/9

권한 부여

- 권한 집합?
- 롤?

---

### 테이블

테이블 생성

인덱스

- 자동 스크립트
- 카디널리티 높다 == 중복도가 낮다
  - 성별로 index -> 테이블 50% 스캔
- 실행계획
- 인덱스 조회시 주의 사항
  - https://jojoldu.tistory.com/243
  - https://dev-jy.tistory.com/59
  - https://m.blog.naver.com/mincoln419/222624805212
- SGA 데이터 버퍼 캐시? -> 재시작(풀스캔은 버퍼캐시로 가지 않는다)
- 버퍼캐시 히트: https://diary90.tistory.com/111
- 왜 시간이 비슷한가 실행계획 -> 풀스캔 중인데요? table access full
- 인덱스 rowid로 테이블을 엑세스하는 과정은 적지않은 비용
- index range scan  cost > table full scan cost가 되는 지점 : 인덱스 손익 분기전
- 양이 많아서 그렇다
  - full scan 은 항상 코스트가 일정 테이블 데이터 비율과 상관있는게 아닐까
  - `SELECT count(*) from emp e where e.employee_id <= $범위;`
    - 1: unique scan
    - 10000: range scan
    - 20000: fast full scan
- 힌트로 강제로 쓸수 있다-> 무조건 하진 않는다

View

- 뷰자체는 인덱스 적용x
- 기존 테이블의 인덱스가 적용 (테이블 별로 다르게 적용)
- 일부 데이터 제거 불가
- 원본 데이터 수정시 뷰 조회 데이터도 수정됨

synonym

- public/ private -> 권한을 가진 모든 스키마에서/ 시노님을 생성한 스키마
- 생성 삭제
- 테이블, 함수, 프로시저 등 객체도 가능

data type

Each value manipulated by Oracle Database has a **data type**.

-- docs.oracle

- 오라클 DB에서 조작되는 모든 값들은 data type이 있다
- 고정된 속성
- 테이블 컬럼, 함수의  모든 arguments 는 data type을 지정해야한다
- 같은 data type 일때 연산 -> date string 비교는 translate후 진행되는것



- [Oracle Built-in Data Types](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Data-Types.html#GUID-7B72E154-677A-4342-A1EA-C74C1EA928E6)
- [ANSI, DB2, and SQL/DS Data Types](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Data-Types.html#GUID-0BC16006-32F1-42B1-B45E-F27A494963FF)
- [User-Defined Types](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Data-Types.html#GUID-7CF27C66-9908-4C02-9401-06C2F2C4021C)
- [Oracle-Supplied Types](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Data-Types.html#GUID-B3300D21-4598-4AE5-AA95-451E9F1040ED)
- [Data Type Comparison Rules](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Data-Type-Comparison-Rules.html#GUID-1563C817-86BF-430B-99AB-322EE2E29187)
- [Data Conversion](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Data-Type-Comparison-Rules.html#GUID-6DB331B5-0F34-4215-9A20-16AEA9D7FF4B)
- data type은 scalar 와 nonscalar
  - scalar: 단일 타입
    - number, varchar2, char, ...
  - nonscalar: 복합적 데이터 표현
    - table, record, ref cursor, ...->...? 공부 필요
- external data type들은 internal 타입과 다르다
  - 오라클이 변환해줌
  - https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpcc/datatypes-and-host-variables.html#LNPCC3158

- oracle_built_in_datatypes;

  - character

    ```
    { CHAR [ (size [ BYTE | CHAR ]) ]
    | VARCHAR2 (size [ BYTE | CHAR ])
    | NCHAR [ (size) ]
    | NVARCHAR2 (size)
    }
    ```

    

  - number

    ```
    { NUMBER [ (precision [, scale ]) ] 
    | FLOAT [ (precision) ]
    | BINARY_FLOAT
    | BINARY_DOUBLE
    }
    ```

    - 자리수와 정밀도
    - 정밀도
    - 32비트 부동 소수점
    - 64비트 부동 소수점

    

  - long_ raw

    ```
    { LONG | LONG RAW | RAW (size) }
    ```

    - 긴 문자열, 바이너리저장, 가변 길이의 바이너리 저장
    - 한로우에 한개만 가능!

  - datetime

    ```
    { DATE
    | TIMESTAMP [ (fractional_seconds_precision) ]
         [ WITH [ LOCAL ] TIME ZONE ]
    | INTERVAL YEAR [ (year_precision) ] TO MONTH
    | INTERVAL DAY [ (day_precision) ] TO SECOND
         [ (fractional_seconds_precision) ]
    }
    ```

    

  - large_object

    ```
    { BLOB | CLOB | NCLOB | BFILE }
    ```

    이진 대용량 객체, 대용량 문자 데이터, 국제화 문자데이터(4GB), 데이터 베이스 외부에 저장된 파일에 대한 참조

    lob 제약사항

    http://www.gurubee.net/lecture/1841

  - row_id

  - ```
    { ROWID | UROWID [ (size) ] }
    ```

  - 로우 id 와 원격 접속 row id

- ansi_support_datatypes;

- ```
  { CHARACTER [VARYING] (size)
  | { CHAR | NCHAR } VARYING (size)
  | VARCHAR (size)
  | NATIONAL { CHARACTER | CHAR }
       [VARYING] (size)
  | { NUMERIC | DECIMAL | DEC }
       [ (precision [, scale ]) ]
  | { INTEGER | INT | SMALLINT }
  | FLOAT [ (size) ]
  | DOUBLE PRECISION
  | REAL
  }
  ```

  - varying 좀 신기

- user_defined_datatypes;

  - oracle built in datatype이나 다른 user defined datatypes를 사용

- oracle_supplied_types;

  - xml,
  - spartial  (공간)
  - any types



# desc -> sql statment X  sql*plus command!

---

### pl/sql

sql을 확장한 절차적 언어

여러 sql을 하나의 블록으로 구성하여 sql을 제어할수 잇음(tcl X)

EXCEPTION 종류

- https://e-una.tistory.com/17
- others

fuction

- 디비버에선 function 컴파일에 문제가 있는거 아닐까 -> sql developer는 잘됨
  - 줄바꿈이 잘 입력이 안됨
  - 스키마-> 유저 -> 프로시저에 어떻게 저장됬는지 보자
- 반환 O

procedure

- 파라미터: IN OUT
- for

- if
- CURSOR
  - https://logical-code.tistory.com/53?category=724583
  - OPEN 하면 CLOSE도

package

- 함수와 프로시저 등을 묶어둔 객체
- 관리하기 쉽다?

trigger

- 하나의 트랜잭션 -> 롤백? 트리거안에서 세이브 포인트 롤백 커밋불가
  - 별도의 트랜잭션을 만들어면 되지만 데드락 발생 가능

sequence

- 트랜잭션X

- ```sql
  CREATE SEQUENCE WDRL_SEQ --시퀀스이름 WDRL_SEQ
  INCREMENT BY 1 --증감숫자 1
  START WITH 1 --시작숫자 1
  MINVALUE 1 --최소값 1
  MAXVALUE 9999999999 --최대값 
  NOCYCLE --순한하지않음
  NOCACHE; --메모리에 시퀀스값 미리할당 cache 30; 30개 캐시(미리 생성)
  ```

- ```sqlite
  SELECT WDRL_SEQ.CURRVAL FROM DUAL;
  ```

- currval는 nextval 실행후 사용되므로 동시에 호출하면 같다
- 디비버로 시퀀스를 보면 GENERATE BY DEFAULT 는CACHE 20으로 되어있다

`SELECT  employee_id_seq.currval, employee_id_seq.nextval FROM dual;`