# SQL MAPPER JDBC ORM

-> 영속성과 관련

-> 데이터를 생성한 프로그램이 종료되더라도 사라지지 않느 데이터특성

![](jdbc%20sql%20mapper%20orm_assets/2024-07-15-16-00-18-image.png)

![](jdbc%20sql%20mapper%20orm_assets/2024-07-15-16-00-28-image.png)

자바에서 db에 접근하기 위해 만든 api

여러 드라이버를 제공하기 때문에 어떤 데이버베이스든 동일한 로직으로 접속 가능

순서

JDBC 드라이버 로드

DB 연결

statement 생성

결과 리턴

연결 종료

![](jdbc%20sql%20mapper%20orm_assets/2024-07-15-16-02-50-image.png)

단점

- 직접 작성해야 하는 코드가 많음

- 커넥션관리

- DB별 예외 처리 필요

-> SQL MAPPER 등장

**Statement 클래스**

- SQL 구문을 실행하는 역할

- 스스로는 SQL 구문 이해 못함(구문해석 X) -> 전달역할

- SQL 관리 O + 연결 정보 X

### SQL MAPPER

SQL 매퍼는 SQL 쿼리와 객체 간의 매핑을 처리하는 도구로, 개발자가 직접 작성한 SQL 쿼리를 사용하여 데이터베이스와 상호작용할 수 있게 해주는 프레임 워크

dbms에 종속적

- mybatis
  
  - SQL을 xml 파일에 작성해 놓고 코드와 SQL을 분리하는 방식
  
  - 코드 복잡성 감소

- spring jdbc
  
  - datasource를 통해 커넥션을 위한 설정들을 관리
  
  - 예외처리 간단
  
  - RowMapper -> 결과값을 한 행씩 읽어 자바 객체로 변환



### ORM

객체지향적으로 구현된 모델을 RDBMS 모델로 맞추기 힘들어 나왔따

객체의 필드가 추가된다면?

객체를 가진 필드가 생긴다면?



패러다임 불일치

OOP -> 추상화 상속 캡슐화ㅏ 다형성 의존성

RDBMS -> 데이터 중심의 구조

설계 원칙이 다르게 때문에 사용 방법과 표현방시에 차이가 있다

-> 객체와 DB 테이블을 매핑하면 데이터를 객체화 



장점

객체간의 관계를 바탕으로 SQL을 자동 생성하고 메서드를 통해 조작

유지보수 쉽다

필드 수정시 엔티티만 수정

복잡한 경우 직접 추가 필요 (JPQL)

JPA, Hibernate, SPRING DATA JPA


