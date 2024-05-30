# STOMP EVENTS

다음은 Spring의 ApplicationListener 인터페이스를 구현하여 수신할 수 있는 여러 ApplicationContext 이벤트에 대한 설명입니다:

**BrokerAvailabilityEvent**: 브로커가 사용 가능해지거나 사용 불가능해질 때 발생합니다. "단순" 브로커는 애플리케이션이 시작되면 즉시 사용 가능해지며 애플리케이션이 실행되는 동안 계속해서 사용 가능합니다. 반면, STOMP "broker relay"는 전체 기능을 갖춘 브로커와의 연결을 잃을 수 있습니다(예: 브로커가 재시작되는 경우). 브로커 릴레이는 재연결 로직을 가지고 있으며 브로커가 다시 사용할 수 있게 되면 "시스템" 연결을 다시 설정합니다. 이 이벤트는 연결 상태가 연결됨에서 끊김으로 또는 그 반대로 변경될 때마다 발생합니다. SimpMessagingTemplate을 사용하는 구성 요소는 이 이벤트를 구독하고 브로커가 사용 가능하지 않을 때 메시지를 보내지 않도록 해야 합니다. 어쨌든 메시지를 보낼 때 MessageDeliveryException을 처리할 준비가 되어 있어야 합니다.

**SessionConnectEvent**: 새로운 STOMP CONNECT가 수신되어 새로운 클라이언트 세션이 시작될 때 발생합니다. 이 이벤트는 연결을 나타내는 메시지를 포함하며, 세션 ID, 사용자 정보(있는 경우) 및 클라이언트가 보낸 모든 사용자 정의 헤더를 포함합니다. 클라이언트 세션을 추적하는 데 유용합니다. 이 이벤트를 구독하는 구성 요소는 포함된 메시지를 SimpMessageHeaderAccessor 또는 StompMessageHeaderAccessor로 래핑할 수 있습니다.

**SessionConnectedEvent**: SessionConnectEvent 직후에 브로커가 CONNECT에 응답하여 STOMP CONNECTED 프레임을 보낼 때 발생합니다. 이 시점에서 STOMP 세션은 완전히 설정된 것으로 간주될 수 있습니다.

**SessionSubscribeEvent**: 새로운 STOMP SUBSCRIBE가 수신될 때 발생합니다.

**SessionUnsubscribeEvent**: 새로운 STOMP UNSUBSCRIBE가 수신될 때 발생합니다.

**SessionDisconnectEvent**: STOMP 세션이 종료될 때 발생합니다. DISCONNECT는 클라이언트에서 전송했거나 WebSocket 세션이 닫힐 때 자동으로 생성될 수 있습니다. **일부 경우에는 세션당 이 이벤트가 여러 번 발생할 수 있습니다.** 구성 요소는 여러 차례의 연결 해제 이벤트에 대해 무상관(idempotent)하도록 해야 합니다.





### 오늘의 억울한 점

`SessionConnectedEvent`는 `SessionConnectEvent`와 다르게 직접적으로 헤더 값을 제공하지 않습니다. `SessionConnectedEvent`는 STOMP 연결이 완전히 설정되었음을 나타내지만, 해당 이벤트 객체 자체는 기본적으로 헤더 정보를 포함하지 않습니다. 반면, `SessionConnectEvent`는 클라이언트의 CONNECT 메시지를 포함하여 세션 ID, 사용자 정보 및 커스텀 헤더 등을 제공합니다.


하지만? 로그를 찍으면 헤더값이 찍히긴 한다.
