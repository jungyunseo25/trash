import random
import streamlit as st

# 앱 제목 설정
st.title("🎲 로또 번호 생성기")


# 번호에 따른 로또 공 색상(배경색) 반환 함수
def get_ball_color(num):
    if num <= 10:
        return "#fbc02d"  # 노란색
    elif num <= 20:
        return "#1e88e5"  # 파란색
    elif num <= 30:
        return "#e53935"  # 빨간색
    elif num <= 40:
        return "#8e24aa"  # 보라/회색 계열
    else:
        return "#43a047"  # 초록색


# 세션 상태에 번호 세트 목록 저장 공간 생성 (최대 5개 관리용)
if "lotto_sets" not in st.session_state:
    st.session_state.lotto_sets = []

# 버튼 영역 (생성 / 초기화)
col1, col2 = st.columns([2, 1])

with col1:
    # [로또번호 생성] 버튼 클릭 시
    if st.button("🎰 로또번호 생성"):
        # 1~45 사이 중복 없는 6개 번호 추출 후 정렬
        new_set = sorted(random.sample(range(1, 46), 6))
        # 생성된 세트를 목록 맨 앞에 추가
        st.session_state.lotto_sets.insert(0, new_set)
        # 최대 5개 유지 (5개 넘어가면 가장 오래된 항목 삭제)
        if len(st.session_state.lotto_sets) > 5:
            st.session_state.lotto_sets.pop()

with col2:
    # [초기화] 버튼 클릭 시 기록 삭제
    if st.button("🔄 초기화"):
        st.session_state.lotto_sets = []
        st.rerun()

st.divider()

# 저장된 로또 번호 세트 화면에 출력 (최대 5개)
if st.session_state.lotto_sets:
    st.subheader(f"최근 생성된 번호 (총 {len(st.session_state.lotto_sets)}/5세트)")

    for idx, lotto in enumerate(st.session_state.lotto_sets, start=1):
        st.markdown(f"**{idx}회차 생성 번호**")

        # 번호 6개를 공 모양 HTML/CSS로 변환하여 출력
        balls_html = ""
        for num in lotto:
            bg_color = get_ball_color(num)
            balls_html += f"""
            <div style="
                display: inline-flex;
                justify-content: center;
                align-items: center;
                width: 45px;
                height: 45px;
                border-radius: 50%;
                background-color: {bg_color};
                color: white;
                font-weight: bold;
                font-size: 18px;
                margin-right: 8px;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
            ">{num}</div>
            """

        st.markdown(f"<div style='display: flex; margin-bottom: 15px;'>{balls_html}</div>", unsafe_allow_html=True)
else:
    st.info("상단의 [로또번호 생성] 버튼을 눌러 번호를 추출해보세요!")