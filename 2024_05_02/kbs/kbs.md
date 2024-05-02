# Spring Expression Language



서버의 포트 번호로 카프카 토픽 어노테이션을 만들려니까 상수가 아니여서 안된데요

찾아보니 spel있어요



런타임에서 객체에 대한 쿼리와 조작(querying and manipulating)을 지원하는 강력한 표현 언어이다.



## 연산자

SpEL 표현식은 `#` 기호로 시작하며 중괄호로 묶어서 표현 `#{표현식}`

속성 값을 참조할 때는 `$` 기호와 중괄호로 묶어서 표현 `${property.name}`

아래와 같이 속성 값 참조는 표현식 안에서 사용이 가능하다.

```
#{${someProperty} + 2}
```





기본적인 관계, 논리 연산자 또한 지원한다.

```
@Value("#{1 == 1}") // true
private boolean equal;
```

조건부 연산자, 정규 표현식,리스트  맵 객체 참조 가능

```
@Value("#{'100' matches '\\d+'}") // true
private boolean validNumericStringResult
@Value("#{some.property != null ? some.perperty : 'default'}")
private String ternary;

@Value("#{membersHolder.membersAge['devwithpug']}") // 24
private Integer age;


```


