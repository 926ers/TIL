# mysql 모니터링



### general log

```
# general_log 기능을 비활성화
MariaDB [mysql]> set global general_log = OFF;

# general_log가 mysql DB의 general_log TABLE에 log 기록
MariaDB [mysql]> set global log_output = 'TABLE';

# general_log가 /rdsdbdata/log/general/mysql-general.log 위치에 FILE로 기록
MariaDB [mysql]> set global log_output = 'FILE';

# general_log가 TABLE과 FILE에 둘다 기록
MariaDB [mysql]> set global log_output = 'TABLE,FILE';

# general_log 기능을 활성화
MariaDB [mysql]> set global general_log = ON;
```

전체 쿼리 로그를 확인

너무 로그가 쌓이면 안좋으니 몇일 단위로 삭제나 일정 퍼센트이상 차지하면 가장 오래된 로그를 삭제하자



### slow query log

```sql
[mysqld]
slow_query_log = 1
slow_query_log_file = /path/to/your/slow-query.log
long_query_time = 2
```

2 초 초과하는 쿼리를 로그에 기록



```
# Time: 2024-07-29T10:15:32.123456Z
# User@Host: user_name[user_name] @ host_name [ip_address]
# Thread_id: 12345  Schema: database_name  QC_hit: No
# Query_time: 3.456789  Lock_time: 0.000123  Rows_sent: 10  Rows_examined: 100
SET timestamp=1627545332;
SELECT * FROM large_table WHERE column = 'value';
```

- **Time:** 쿼리가 실행된 시간.
- **User@Host:** 쿼리를 실행한 사용자와 호스트 정보.
- **Thread_id:** MySQL 스레드 ID.
- **Schema:** 쿼리가 실행된 데이터베이스 스키마.
- **QC_hit:** 쿼리 캐시 히트 여부.
- **Query_time:** 쿼리 실행 시간(초).
- **Lock_time:** 테이블 잠금에 걸린 시간(초).
- **Rows_sent:** 클라이언트로 전송된 행 수.
- **Rows_examined:** 쿼리 실행 중에 검사된 행 수.
- **SET timestamp:** 쿼리가 실행된 시간을 UNIX 타임스탬프로 표시.
- **쿼리문:** 실제 실행된 SQL 쿼리.

### performance schema

낮은 수준에서 MySQL 서버 실행을 모니터링하는 기능

• 시스템 변수 설정.

my.cnf(서버 환경 구성 파일)에 다음 사항을 추가합니다. 기본값은 ON입니다.

```
[mysqld]
performance_schema=ON

```

### show status

`SHOW STATUS` 명령어는 MySQL 서버의 상태 변수와 통계 정보를 제공

`SHOW GLOBAL STATUS; SHOW SESSION STATUS;`

- `SHOW GLOBAL STATUS`: MySQL 서버 전체에 대한 통계와 상태 정보를 표시합니다.
- `SHOW SESSION STATUS`: 현재 세션에 대한 통계와 상태 정보를 표시합니다.

자주 사용되는 상태 변수들은 다음과 같습니다:

- `Connections`: MySQL 서버에 대한 연결 수.
- `Uptime`: 서버가 시작된 이후 경과 시간(초).
- `Slow_queries`: 슬로우 쿼리로 기록된 쿼리 수.
- `Questions`: 클라이언트가 서버에 보낸 쿼리 수.
- `Innodb_buffer_pool_reads`: InnoDB 버퍼 풀에서 읽지 못한 페이지를 디스크에서 읽은 횟수.
- `Innodb_buffer_pool_read_requests`: InnoDB 버퍼 풀에서 읽기 요청 횟수.

-  **Bytes_received / Bytes_sent**  

Bytes_sent가 높다면 이 서버는 읽기위주 작업(select) 

Bytes_received 가 높다면 이 서버는 쓰기 위주작업(insert 등) 서버임을 알 수 있다.

위의 Questions,Uptime과 함께 응용해보면 1개 쿼리당 평균 Byte, 시간당 처리Byte등을 계산 할 수 있어 

네트워크 트래픽등의 계산(예상 트래픽을 초과하는 쿼리가 있는지 등)에 유효하게 사용될 수 있다.

[show status를 통한 MySQL 상태 분석하기 &#124; CEnA](https://cena.co.kr/show-status%EB%A5%BC-%ED%86%B5%ED%95%9C-mysql-%EC%83%81%ED%83%9C-%EB%B6%84%EC%84%9D%ED%95%98%EA%B8%B0/)

출처: [[MySQL] Performance Schema 소개 및 사용방법](https://myinfrabox.tistory.com/194) [MyInfraBox:티스토리]
