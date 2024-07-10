# TOMCAT

1. 스프링부트는 내장 서블릿 컨테이너인 Tomcat을 이용합니다.

```properties
# application.yml (적어놓은 값은 default)
server:
  tomcat:
    threads:
      max: 200 # 생성할 수 있는 thread의 총 개수
      min-spare: 10 # 항상 활성화 되어있는(idle) thread의 개수
    max-connections: 8192 # 수립가능한 connection의 총 개수
    accept-count: 100 # 작업큐의 사이즈
    connection-timeout: 20000 # timeout 판단 기준 시간, 20초
  port: 8080 # 서버를 띄울 포트번호
```

default 값은 autoConfiuration에서 정의한 디폴트 값을 주입



스프링부트 2.5.4 기준으로 9.0.52버전의 Tomcat을 내장

톰캣 8.5부터 Non blocking io connector 채택

9.0에서는 Bio -> deprecate



2. Tomcat은 다중 요청을 처리하기 위해서, 부팅할 때 스레드의 컬렉션인 Thread Pool을 생성합니다.
   
   - Tomcat 3.2 이전에는 쓰레드를 생성
   
   - 쓰레드 생성 제거는 많은 자원 소모
   
   - 쓰레드 풀 등장
   
   - 첫 작업이 들어오면, core size만큼의 스레드를 생성
   
   - 유저 요청(Connection, Server socket에서 accept한 소캣 객체)이 들어올 때마다 작업 큐(queue)에 담아둡니다.
   
   - core size의 스레드 중, 유휴상태(idle)인 스레드가 있다면 작업 큐에서 작업을 꺼내 스레드에 작업을 할당하여 작업을 처리합니다.
   
   - 만약 유휴상태인 스레드가 없다면, 작업은 작업 큐에서 대기
   
   - 작업 큐가 꽉 찬다면, 스레드를 새로 생성
   
   - 반복하다 스레드 최대 사이즈 에 도달하고 작업큐도 꽉 차게 되면, 추가 요청에 대해선 connection-refused 오류를 반환
   
   - 태스크가 완료되면 스레드는 다시 유휴상태로 돌아갑니다
   
   -  작업큐가 비어있고 core size이상의 스레드가 생성되어있다면 스레드를 destory합니다.

3. 유저 요청(HttpServletRequest)가 들어오면 Thread Pool에서 하나씩 Thread를 할당합니다. 해당 Thread에서 스프링부트에서 작성한 Dispatcher Servlet을 거쳐 유저 요청을 처리합니다.
   
   - 

4. 작업을 모두 수행하고 나면 스레드는 스레드풀로 반환됩니다.





# 스프링 부트 전체적인 흐름

![](https://velog.velcdn.com/images/ejung803/post/f97cbbcd-8f4c-440f-83d5-1c41987db16b/image.png)

최종 결과를 톰캣에게 전달

json 응답은 view, view resolver 사용X

`HttpMessageConverter`가 객체를 JSON으로 변환하여 응답

![](https://velog.velcdn.com/images/rudwhd515/post/86a4cb74-eb89-4e6b-9ff7-e3f75d80879c/image.png)

- # Tomcat의 동작 원리
  
  1. Tomcat이 WS (Web Server)로 부터 동적 (dynamic) 페이지 요청을 받게 된다.
  
  2. Servlet Container는 HttpServletRequest와 HttpServletResponse 객체를 생성한다.
  
  3. Servlet Container의 address space에 요청된 페이지에 해당하는 Servlet이 load되어 있는지 확인한다.
     
     3-1. load되어 있지 않다면, Serlvet 객체를 생성하고, `init()` 메서드를 실행한다.
     
     > Servlet은 Servlet Container에 load된 뒤에 바로 소멸하지 않고, 자신에게 들어오는 요청에 계속 응답하게 된다. -> `init()` 메서드는 Servlet 객체 생성 후 한 번만 실행
  
  4. Servlet Container는 새로운 Thread를 생성해 Servlet의 `service()` 메서드를 실행한다. (HttpServletRequest, HttpServletResponse 객체를 파라미터로 넘김)
     
     4-1. `service()` 메서드 내부에서 `doGet()` or `doPost()`메서드가 실행된다.
  
  5. Servlet Container는 응답 결과인 response를 HttpResponse로 변환해 WS로 넘겨주게 된다.
  
  6. Servlet Container는 HttpServletRequest, HttpServletResponse 객체를 소멸한다.
  
  7. Thread를 종료한다.





서블릿은 다음과 같은 상황에서 소멸할 수 있습니다:

1. **컨테이너 종료**: 서블릿 컨테이너(예: 톰캣)가 종료될 때, 컨테이너 내의 모든 서블릿 인스턴스도 함께 소멸됩니다.

2. **서블릿 컨텍스트 초기화**: 서블릿 컨텍스트가 초기화되면, 컨텍스트에 속한 모든 서블릿 인스턴스도 소멸될 수 있습니다. 이는 보통 웹 애플리케이션이 리로드(reload)될 때 발생합니다.

3. **서블릿 초기화 매개변수 변경**: 서블릿의 초기화 매개변수가 변경되어 해당 서블릿을 다시 초기화해야 할 경우, 기존 서블릿 인스턴스는 소멸되고 새로운 인스턴스가 생성될 수 있습니다.

4. **서블릿 컨테이너에 의한 소멸**: 서블릿 컨테이너가 서블릿 인스턴스의 메모리 관리를 위해 필요에 따라 서블릿을 소멸시킬 수 있습니다. 이는 특히 서블릿 인스턴스가 오랫동안 사용되지 않거나, 메모리 부족 상황에서 발생할 수 있습니다.
