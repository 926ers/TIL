# SCALING RELATIONSHIP ON LEARNING MATHEMATICAL REASONING WITH LARGE LANGUAGE MODELS

### Rejection sampling
***
#### 주어진 확률 분포에서 효율적으로 샘플을 생성하기 위해 이용되는 알고리즘
#### - 주어진 확률 분포 p의 확률 밀도 함수를 알고 있어야한다.
#### - 그러나 p에서 직접 샘플을 생성하는 것은 매우 어렵거나 불가능하다.

![image](https://github.com/sondonghup/paper_searcher/assets/42092560/13e0fd5d-9ad5-4195-ba71-fb42f17133ef)

#### 쉽게 샘플을 생성할 수 있는 q에서 샘플들을 생성한 뒤에 이샘플들의 분포가 p를 따르도록 수정하는 것
#### 이때 쉽게 샘플을 생성할 수 있도록 임의로 설정한 q를 제안 분포라고한다.

![image](https://github.com/sondonghup/paper_searcher/assets/42092560/520c2373-ef88-48ed-b15f-92412c5b17aa)

#### x0 샘플에서 [0, Mq(x0)]사이의 uniform distribution에서 u를 생성하여 

![image](https://github.com/sondonghup/paper_searcher/assets/42092560/178070ad-25ab-429b-bdcf-819d03c69eed)

#### A에 있으면 rejection B에 있으면 샘플로 이용한다.