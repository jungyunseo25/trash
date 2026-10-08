# Streamlit 로또 번호 생성기

Streamlit을 활용하여 1부터 45까지의 숫자 중 중복 없이 6개의 로또 번호를 랜덤으로 추첨하는 웹 애플리케이션입니다.

## 주요 기능

* **랜덤 번호 추출**: 1~45 범위 내 중복 없는 6개 숫자 생성 및 오름차순 정렬
* **최대 5세트 기록**: [로또번호 생성] 버튼을 누를 때마다 최근 생성된 번호 세트를 최대 5개까지 화면에 표시
* **로또 공 색상 적용**: 실제 로또 공 색상 규격을 적용하여 시각적 직관성 제공
  * 1~10번: 노란색
  * 11~20번: 파란색
  * 21~30번: 빨간색
  * 31~40번: 보라/회색
  * 41~45번: 초록색
* **기록 초기화**: [초기화] 버튼으로 생성된 세트 목록 리셋

## 실행 방법

### 1. 가상환경 설정 (선택 사항)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2. 패키지 설치

`requirements.txt` 파일에 정의된 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

### 3. Streamlit 앱 실행

```bash
streamlit run app.py
```

*(기본 파일명이 `app.py`가 아닌 경우 해당 파이썬 파일명으로 변경하여 실행하세요.)*

## 프로젝트 구조

```
.
├── app.py           # Streamlit 로또 번호 생성기 메인 코드
├── requirements.txt # 필요 라이브러리 목록
└── README.md        # 프로젝트 설명 문서
```