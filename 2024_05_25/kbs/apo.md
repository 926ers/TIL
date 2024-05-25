# AOP

관점 지향프로그래밍


객체 지향 프로그래밍 패러다임을 보완하는 기술로 메소드나 객체의 기능을 핵심 관심사와 공통 관심사로 나누어 프로그래밍하는것


반복적으로 사용하는 코드를 하나로 묶어서 모듈화하여 재사용성과 유지 보수성을 높일 수 있떠

## Spring AOP 이해하기

---

### 1. 주요 용어 이해하기

| **용어**         | **설명**                                                         |
| -------------- | -------------------------------------------------------------- |
| **Aspect**     | - 공통적인 기능들을 모듈화 한것을 의미합니다.                                     |
| **Target**     | - Aspect가 적용될 대상을 의미하며 메소드, 클래스 등이 이에 해당 됩니다.                  |
| **Join point** | - Aspect가 적용될 수 있는 시점을 의미하며 메소드 실행 전, 후 등이 될 수 있습니다.           |
| **Advice**     | - Aspect의 기능을 정의한 것으로 메서드의 실행 전, 후, 예외 처리 발생 시 실행되는 코드를 의미합니다. |
| **Point cut**  | - Advice를 적용할 메소드의 범위를 지정하는 것을 의미합니다.                          |

---

### 2. 주요 어노테이션

| **메서드**             | **설명**                                      |
| ------------------- | ------------------------------------------- |
| **@Aspect**         | 해당 클래스를 Aspect로 사용하겠다는 것을 명시합니다.            |
| **@Before**         | 대상 “메서드”가 실행되기 전에 Advice를 실행합니다.            |
| **@AfterReturning** | 대상 “메서드”가 정상적으로 실행되고 반환된 후에 Advice를 실행합니다.  |
| **@AfterThrowing**  | 대상 “메서드에서 예외가 발생”했을 때 Advice를 실행합니다.        |
| **@After**          | 대상 “메서드”가 실행된 후에 Advice를 실행합니다.             |
| **@Around**         | 대상 “메서드” 실행 전, 후 또는 예외 발생 시에 Advice를 실행합니다. |

---

### 사용 예시

로그 출력



1.  build.gradle 의존성 추가

`implementation 'org.springframework.boot:spring-boot-starter-aop'`

2. `@aspect` 어노테이션이 있는 `LoggingAspect` 클래스 생성

```java
@Aspect
@Component
@Slf4j
public class LoggingAspect {  

    @Before("execution(* pomdol.controller.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {}

    @After("execution(* pomdol.controller.*.*(..))")
    public void logAfter(JoinPoint joinPoint) {}

    @AfterReturning(pointcut = "execution(* pomdol.controller.*.*(..))", returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {}

    @AfterThrowing(pointcut = "execution(* pomdol.controller.*.*(..))", throwing = "e")
    public void logAfterThrowing(JoinPoint joinPoint, Throwable e) {}

    @Around("execution(* pomdol.controller.*.*(..))")
    public void logAround(ProceedingJoinPoint joinPoint) throws Throwable {
        //before
        Object result = joinPoint.proceed();
        //after
    }

}
```

패키지내의 모든 클래스 모든 메소드를 대상으로 할수도 있지만 하나만 선택가능

gpt code

```java
@Around("execution(* pomdol.controller.*.*(..))")
public void logAround(ProceedingJoinPoint joinPoint) throws Throwable {
    System.out.println("Method " + joinPoint.getSignature().getName() + " is called on " + joinPoint.getTarget().getClass().getName());
    long start = System.currentTimeMillis();

    Object result = joinPoint.proceed(); // 메소드 실행

    long elapsedTime = System.currentTimeMillis() - start;
    System.out.println("Method " + joinPoint.getSignature().getName() + " execution time: " + elapsedTime + " milliseconds.");

    // return result if needed, or modify the result if necessary
}
```

```java
        Object[] args = joinPoint.getArgs();
        Long projectId = (Long) args[0];
        Long categoryId = (Long) args[1];
        Long userId = (Long) args[3];

        CardDto cardDto = (CardDto) joinPoint.proceed(); //형변환 필요
        Long cardId = cardDto.getId();
        String cardTitle = cardDto.getTitle();
```

대상 메소드의 인자나 리턴값을 받을 수 있다



스프링 AOP는 인터페이스(interface), 프록시(proxy),  런타임(runtime) 기반이다. 라는데요
