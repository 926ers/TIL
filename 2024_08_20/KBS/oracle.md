# oracle 시작

`sqlplus '/as sysdba'`

`select username from dba_users;`

```sql
su root
su - oracle
lsnrctl start
sqlplus
aaa
qweqwe11
```

비밀번호 변경

`alter user $(유저) identified by $(새 비밀번호)`

윈도우 방화벽 

**Ping해제방법**
"핵심 네트워킹 진단 - ICMP Echo Request (ICMPv4-In)" 규칙사용으로 체크

**db 확인 **

`    select name from v$database`

https://joshua-memories.tistory.com/25

listener.ora

```
SID_LIST_LISTENER =
  (SID_LIST =
    (SID_DESC =
      (SID_NAME = cdb1)
      (ORACLE_HOME = /u01/app/oracle/product/19.3.0/dbhome_1)
    )
  )

LISTENER =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = 127.0.0.1)(PORT = 1521))
    )
  )
```

포트와 연결된 상대 정보 확인

`netstat -tn`

telnet open 127.0.0.1 1521 -> 리스너 확인

sid 대소문자 구분

오라클 리스너 파라미터

큐사이즈 (default 17) 성능 형상 비례하진 않는다

서버(리스너 수)

로드 밸런싱

리스너 로그

# 오라클 db

데이터 베이스 확인

`SELECT NAME FROM V$DATABASE;`

테이블 조회

SELECT TABLE_NAME FROM DBA_TABLE;

다른 행 조회 LEAD, LAG

LAG(average_salary) OVER (ORDER BY DEPARTMENT_ID)

# 리눅스에서 실행하기

## java

```bash
#!/bin/bash
java -version
yum install -y java-11-openjdk-devel.x86_64

javac Main.java
java Main
```

## python

```bash
#!/bin/bash
python3 --version

python3 main.py
```

## C

```bash
#!/bin/bash
gcc -c main.c
gcc -o main.out main.o
./main.out
```

오라클 아키텍쳐