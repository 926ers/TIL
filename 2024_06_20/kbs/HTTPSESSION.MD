### httpservletRequest와 http session

| HttpSession                                                           | HttpServletRequest                                           |
| --------------------------------------------------------------------- | ------------------------------------------------------------ |
| 생성 : Client 최초 접속 시<br/>제거 : Client 접속 종료 시<br/>Client가 접속 중인 동안에만 존재 | 생성 : Client가 요청 시<br>삭제 : Server가 응답 시<br>Request 중인 동안에만 존재 |

httpsession은 sevlet container에서 만든다

로그인시 session의 유지시간을 설정해 인가인증에 사용

클라이언트에겐 session id 를 담아 주자

로그아웃시 invalidate() 메소드로 세션을 무력화하자

key-value 형식으로 저장

```
스프링에선 세션을 주입해야 할 때, 내부적으로 Servlet Container에게 Session을 달라고 한다.

위의 login 메소드가 호출될때 즉시 세션이 요청 / 생성되고

Tomcat의 경우 이 SessionID를 JSESSIONID라는 키의 쿠키로 생성/전달한다.
```






