# SQL INJECTION

3즐요약

데이터 베이스와 연동된 웹 애플리케이션에서 공격자가 입력이 가능한 폼에 조작된 질의문을 삽입하여 데이터베이스 정보를 열람또는 조작 할수있는 취약점

parameter binding을 쓰자

서버의 에러를 사용자에게 노출시키지 말자

`` select * from USERS where name = input1 and password = input2`

` select * from USERS where name = 'test' and password = '1123' or '1' = '1'`

`select * from USERS where name = '' or '1' = '1' -- and password = '1123' or '1' = '1'`

`select * from USERS where name = 'test'; drop table users; # and password '1123' or '1' = '1'`

parameter binding을 사용하면 문자열을 확인하면서 바꿔준다

`'1123' or '1' = '1'` -> `'''1123'' or ''1'' =''1'''`

**query string 사용 XXX***


