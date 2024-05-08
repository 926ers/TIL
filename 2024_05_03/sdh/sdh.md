# KAN: Kolmogorov-Arnold Networks

기존 MLP(Multi Layer Perceptrons)의 대안입니다. 처음 Kolmogorov-Arnold 표현정리와 MLP는 거의 동시기에 발명되었습니다.
<br>
<br>
연산에서의 이점과 한번 학습을 하고 나서 그 과정을 살펴보기위한 또는 그런 행위를 하기 힘든 MLP에 반해 시각적으로 판단을 할 수 있다고 합니다.
<br>
MLP는 예를들어 RELU(wieght * x + b)와 같이 node에 활성함수를 적용합니다.
<br>
KAN은 RELU * x + b 처럼 edge에 활성함수를 적용합니다. (여기서는 활성함수를 RELU로 예시를 들었지만 사실은 매개변수화 된 학습가능한 일변량 함수 입니다.)
<br>
<br>
그럼 배개변수화 되어 학습가능한 일변량 함수를 어떻게 역전파 할 것인가? -> 어떤 복잡한 함수도 근사를 할 수 있다는 UAT로 뒷받침 한다.
<br>
UAT (Universal Approximation Theorem)은 정의역 X으로의 실수를 치역으로 갖는 연속적인 함수들의 집합이 존재한다고 하자. 그러면 R->R인 연속적인 함수들의 집합에 시그마(활성함수, 비다항식인)가 존재한다고 하고
n, m은 자연수이고, K는 n-dim 실수에 속하는 작은 범위(근사할 범위), 입실론은 아주 작은 양수이다.
그러면 근사시키려는 범위인 K내에서 실제함수 f와 선형결합으로 이루어진 함수인 근사함수 g의 오차가 앞의 입실론보다 작도록 근사 할 수 있다는 내용입니다.
<br>
<br>

관련 1차 코드

```
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt


# 임의의 연속함수 설정 (R->R)
def true_function(x):
    return torch.sin(x) + torch.cos(2 * x)

# 훈련 데이터 생성
x_train = torch.linspace(0, 2 * np.pi, 100)
y_train = true_function(x_train)

# 신경망 모델 정의
class UniversalApproximator(nn.Module):
    def __init__(self):
        super(UniversalApproximator, self).__init__()
        self.hidden = nn.Linear(1, 50)  # 은닉 레이어
        self.output = nn.Linear(50, 1)  # 출력 레이어

    def forward(self, x):
        x = torch.relu(self.hidden(x))  # ReLU 활성화 함수
        x = self.output(x)
        return x

# 모델 생성
model = UniversalApproximator()

# Loss function & Optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Train
num_epochs = 10000
for epoch in range(num_epochs):
    optimizer.zero_grad()
    outputs = model(x_train.unsqueeze(1))
    loss = criterion(outputs, y_train.unsqueeze(1))
    loss.backward()
    optimizer.step()

# Visualization
x_test = torch.linspace(0, 2 * np.pi, 1000)
with torch.no_grad():
    y_pred = model(x_test.unsqueeze(1))

plt.figure(figsize=(10, 6))
plt.plot(x_train, y_train, label='True Function')
plt.plot(x_test, y_pred, label='Approximation')
plt.legend()
plt.title('Universal Approximation with PyTorch')
plt.show()
```

[출처 : https://velog.io/@jenesoolee/Universal-Approximation-Theorem]

RELU의 조합만으로도 비선형 함수를 만들 수 있듯이 근사가 가능하다는 말인것 같습니다.
<br>
<br>
성능은 1/100 파라미터 수 대비 100배의 정확도(mse에서 100배 차이 난다는 뜻)를 보여준다고 합니다.

![summary](C:\Users\bosung\Desktop\TIL\2024_05_03\sdh\summary.png)