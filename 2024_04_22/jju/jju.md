# 0422

- ## HTML 태그
  
  ```HTML
  <ol type="1|a|A|i|I" start="정수">
    <li>아메리카노</li>
    <li>카페라떼</li>
    <li>핫초코</li>
  </ol>
  
  <ul>
    <li>아메리카노</li>
    <li>카페라떼</li>
    <li>핫초코</li>
  </ul>
  ```
  
  - ol : 순서가 중요한 목록(숫자, 알파벳, 로마자로 순서 표기). -> 기본적으로 1에서 시작.
  - ul : 순서가 중요하지 않은 목록(점으로 표기)
    - li : ol 또는 ul의 하위항목으로 존재하는 아이템.
  
  ```HTML
  <dl>
    <dt>호박</dt>
    <dd>- 박과의 한해살이 덩굴성 채소</dd>
    <dt>상추</dt>
    <dd>- 국화과의 한해살이 또는 두해살이풀</dd>
  </dl>
  ```
  
  - dl : 용어와 설명을 리스트 형식으로 정의.
    - dt : 용어.
    - dd : 용어의 설명.
    - dt 여러개 배치 후 하나의 dd로도 설명 가능.
    - div로 각각의 용어에 대한 정의로 묶을 수도 있음.(기능상 의미는 없지만 CSS 편의성).
    - 무분별한 dl 사용 주의점. (참고 : https://aoa.gitbook.io/skymimo/aoa-2019/tips-2/dl-dt-dd-.)
  
  ```HTML
  <p><dfn>W3C</dfn>는 월드 와이드 웹(WWW)을 위한 표준을 제정하고 관리하는 중립적인 기관입니다.</p>
  ```
  
  - 문장 또는 맥락에서 정의하고 있는 요소를 나타냄.
  - dl의 직계 자손이 될 수 없음.
  
  ```HTML
  <table>
    <thead>
        <tr>
            <th>출장비 내역</th>
            <th>금액</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>교통비</td>
            <td>45000</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td>총 합계</td>
            <td>103000</td>
        </tr>
    </tfoot>
  </table>
  
  <table>
    <colgroup span="2" style="background-color: lightpink"></colgroup>
    <tr>
        <th>학번</th>
        <th>이름</th>
        <th>학과</th>
    </tr>
    <tr>
        <td>2006123456</td>
        <td>홍길동</td>
        <td>전자공학과</td>
    </tr>
  </table>
  ```
  
  - 테이블 정의[행(row) &rarr;, 열(column)&darr;].
    1. 테이블 기본 태그.
       - caption : 표의 제목, 반드시 table태그 바로 다음 위치(스크린 리더는 읽을 수 있으나 화면에 보이지 않게 처리).
       - tr : 행을 만드는 태크.
         - td : tr로 지정한 행에 셀을 만듦.
         - th : 제목 행에 셀을 만듦.
    2. 테이블 그룹핑 태그.
       - thead : 제목 셀 그룹, 테이블 내 한 번만 사용.
       - tbody : 테이블 본문 행.
       - tfoot : 소계, 합계 등의 정보, 테이블 내 한 번만 사용.
       - colgroup : 하나 이상의 열을 그룹으로 묶을 때 사용(스타일 지정, caption 태그 보다는 뒤, thead보다는 앞, span속성으로 묶을 수 있음).
       - col : 지정한 열 스타일 적용 가능(span속성으로 묶을 수 있음).
       - colgroup으로 전체 적용해 놓은 것을 col로 개별지정해서 덮을 수 있는 것 같음.
       - 보통 CSS 사용.
    3. 테이블 그룹핑 태그.
       - thead : 제목 셀 그룹, 테이블 내 한 번만 사용.
       - tbody : 테이블 본문 행.
       - tfoot : 소계, 합계 등의 정보, 테이블 내 한 번만 사용.
    4. 셀 병합 속성.
       - rowspan : 행, 가로로 읽음 -> 세로로 병합.
       - colspan : 열, 세로로 읽음 -> 가로로 병합(ex. colspan="2" = 위에서 가로로 두 칸을 합치고 아래로 읽을거야).
  
  ```HTML
  <img src="/examples/images/img_monalisa.png" alt="모나리자">
  ```
  
  - 이미지 정의(문서에 직접 넣은 것이 아닌, 문서에 이미지를 링크).
  - src : 경로(웹 문서 파일 기준).
  - alt : 이미지 없을 때 텍스트로 대체.
  - HTML5 에서는 align, border, hspace, vspace 지원 안함.
  
  ```HTML
  <object data="/examples/media/sample.mp4" height="180" width="288">
    현재 사용 중인 브라우저는 object 요소를 지원하지 않습니다!
  </object>
  ```
  
  - 외부소스의 종류에 따라 문서처리 방식 변경 가능한 임베디드 객체 정의.
  - body 내에만 존재 가능.
  - object를 지원하지 않을 경우를 위해 태그사이에 텍스트 넣을 수 있음.
  - data, type 둘 중 한 속성은 명시.
  - CLSID 값을 명시하여 지정 된 ActiveX를 사용하여 프로그램이 없어도 재생가능.
  
  ```HTML
  <embed src="/examples/media/sample.pdf">
  ```
  
  - audio, video, object를 지원하지 않을 대 사용. src 명시.
  - HTML5에서 audio, video가 추가 되었기 때문에 주로 pdf등의 다른 웹문서 추가에 사용.
  - 컴퓨터에 해당 미디어 파일 재생 프로그램이 없을 경우 실행 안됨(기본 설정 플러그인을 사용).
  
  ```HTML
  <a href="http://www.tcpschool.com">티씨피스쿨 사이트로 이동!</a>
  ```
  
  - 페이지를 다른 페이지로 연결하는 하이퍼링크 정의.
  - href속성 필수.
  - 태그사이에 img태그 또는 텍스트를 넣을 수 있음.
  - target 속성을 \_blank로 하면 새 창에서 링크를 띄움.
  
  ```HTML
  <form action="/examples/media/action_target.php">
    이름 : <input type="text" name="st_name"><br>
    학번 : <input type="text" name="st_id"><br>
    학과 : <input type="text" name="department"><br>
    <input type="submit">
  </form>
  
  <form action="/examples/media/action_target.php" method="get">
    <fieldset>
        <legend>학사 관리 로그인</legend>
        이름 : <input type="text" name="st_name"><br>
        학번 : <input type="text" name="st_id"><br>
        학과 : <input type="text" name="department"><br>
        <button type="submit">제출하기</button>
    </fieldset>
  </form>
  
  <form action="/examples/media/action_target.php" method="get">
    여러분의 나이대를 골라보세요.<br>
    <input type="radio" name="ages" id="teen" value="teenage">
    <label for="teen">10대</label><br>
    <input type="radio" name="ages" id="twenty" value="twenties">
    <label for="twenty">20대</label><br>
    <input type="submit">
  </form>
  ```
  
  - 사용자로부터 입력을 받을 수 있는 HTML 입력 폼.
    - fieldset : 폼 요소 중 연관 된 것들을 묶는 것(요소 주변으로 박스 생성).
    - legend : caption 정의.
    - label : 폼 요소에 붙히는 라벨.
      - label 태그 안에 폼 요소 넣기.
      - 폼 요소에 id 속성으로 이름을 정해주고, label에 for 속성으로 해당 값 지정.
  - input 태그의 type 속성.
    - text : 한 줄 짜리 일반 텍스트.
    - password : 비밀번호 입력 필드.
      - size : input 요소의 너비를 문자 수 단위로.
      - value : 초기값 value를 지정.
      - maxlength : 최대 문자 수 제한.
    - search : 검색 입력 필드.
    - url : 웹 주소 입력 필드.
    - email : 이메일 입력 필드.
    - tel : 전화번호 입력 필드.
    - checkbox : 항목을 2개 이상 선택 시.
    - radio : 항목을 한 개만 선택 시.
      - name : 버튼의 이름(분류가 같다면 하나만 선택 가능).
      - value : 선택한 값.
      - checked : 초기 선택 되어 있는 값.
      - name = value의 형태로 서버로 전송.
    - number : 스핀박스에서 숫자 선택.
    - range : 슬라이드 막대를 움직여 숫자 입력.
      - min : 최솟값.
      - max : 최대값.
      - step : 숫자 간격(default : 1, 소수점 입력하려면 따로 적어 줘야 함).
      - value : 초기 표기값.
      - placeholder : 유저에게 보여주는 기본값 예시.
    - date : 달력에서 날짜 골라서 yyyy-mm-dd 형식으로 표기.
    - month : 달력에서 월 선택 yyyy-mm 으로 표기.
    - week : 달력에서 주 선택 1월 첫째 주에서 몇 번째 주 인지 yyyy, oo번째 주 로 표기.
    - time : 폼에서 시간 입력 할 수 있도록 함.
      - min : 최솟값.
      - max : 최대값.(min max 값을 어겨도 선택은 되는데 폼 제출이 안됨).
      - step : 숫자 간격(default : 1, 소수점 입력하려면 따로 적어 줘야 함).
      - value : 초기 표기값.
    - datetime-local : 날짜 + 시간
    - submit : input에 입력한 값을 서버로 전송.
      - value : 버튼에 보일 값.
    - reset : input에 입력한 값을 지움.
    - image : submit 버튼과 같은 이미지.
      - src : 이미지경로.
      - alt : 대체 텍스트.
    - button : 버튼 자체의 기능은 없고, js 실행시 사용.
      - value : 버튼 표시값.
      - button과 input의 차이는? : input은 스스로 닫는 태그이지만 button은 아님 -> 사이에 이미지 등을 넣기 수월함.
    - file : 사진 또는 문서 첨부 시 사용.
    - hidden : 화면의 폼에는 보이지 않음. 입력이 끝나면 폼과 함께 서버로 전송(ex. 유저가 변경해서는 안되는 값).
      - name : 이름.
      - value : 서버로 전송 할 값.
