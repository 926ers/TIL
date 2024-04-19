## 외로운 곰곰이는 친구가 있어요

https://www.acmicpc.net/problem/26073

```py
def get_gcd(x, y):
    while y != 0:
        t = x%y
        x, y = y, t
    return abs(x)

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    gcd = arr[1]
    for i in arr[2:]:
        gcd = get_gcd(gcd, i)

    if x%gcd or y%gcd:
        print("Gave up")
    else:
        print("Ta-da")
```

x, y에서 arr[1:]의 값들을 빼서 0,0이 될수있어야한다

`1<= N <= 10000`에 x,y도 최대 100000이여서 queue나 배열로는 안되요

arr[1:]의 값들로 만들수 있는 좌표 -> arr[1:]의 최대 공약수의 배수들

따라서 최대공약수로 x,y 가 나눠지는지 확인하면 된다



#### 알퐁스 도데 책읽었어요

별, 풍차 방앗간 편지, 마지막 수업 등등




