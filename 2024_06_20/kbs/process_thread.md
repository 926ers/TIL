### process

실행중인 프로그램

운영체제러 부터 시스템 자원을 할당받는 작업의 단위

stack 메게변수 지역변수등 임시적인 자료

heap 동적으로 할당되는 메모리

data 전역 변수(static)

text 프로그램의 코드

### thread

프로세스 내에서 실행되는 흐름의 다누이

text, data, heap 영역을 공유

별도의 stack 영역을 가짐

컨텍스트 스위칭 비용이 적음

자원을 공유하는 만큼 충돌 주의

멀티 프로세스

프로세스간 통신(IPC)

자식 프로세스 문제가 다른 프로세스에 영향 X



### PCB (Process Control Block)

- PCB 는 운영체제가 프로세스를 표현한 자료구조이다. 특정 프로세스에 대한 정보를 갖고 있다. 각 프로세스가 생성될때마다 고유의 PCB가 생성되고, 프로세스가 완료되면 PCB 는 제거된다. 프로세스 간 문맥교환이 일어나면서, 프로세스는 진행하던 작업들을 PCB에 저장하고, 이후에 자신의 순서가 왔을 때 이어서 처리한다.
  - OS 가 관리상 사용하는 정보
    - Process state, Process ID
    - scheduling information, pritoiry
  - CPU 수행 관련 하드웨어 값
    - Program counter, registers
  - 메모리 관련
    - Codㄷ, Data, Stack, Heap ..
  - 파일 관련
    - open file descriptors
