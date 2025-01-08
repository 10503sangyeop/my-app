import streamlit as st
import time

# 앱 제목
st.title("키보드 반응 속도 측정 게임")

# 설명
st.write("초록색 화면이 나타날 때 'k' 버튼을 가능한 빨리 누르세요.")
st.write("이 과정을 5번 진행한 후, 당신의 반응 속도를 평가합니다.")

# 결과 초기화
if 'reaction_times' not in st.session_state:
    st.session_state.reaction_times = []

# 반응 시간 측정
def measure_reaction_time():
    # 초록색 화면 표시
    st.markdown(
        """
        <div style="background-color: green; height: 200px;">
        </div>
        """, unsafe_allow_html=True
    )

    # 사용자가 'k' 버튼을 누를 때까지 대기
    start_time = time.time()
    while True:
        if st.session_state.key_pressed == 'k':
            reaction_time = time.time() - start_time
            st.session_state.reaction_times.append(reaction_time)
            break

# 키보드 입력을 추적하는 함수
def on_key_event(key):
    st.session_state.key_pressed = key

# 키보드 입력 이벤트 핸들링
st.text_input("여기에 아무거나 입력해보세요", key="key", on_change=on_key_event)

# 반응 시간 측정을 5번 진행
if len(st.session_state.reaction_times) < 5:
    if st.button("시작"):
        measure_reaction_time()
        st.write(f"반응 시간: {st.session_state.reaction_times[-1]:.4f} 초")

else:
    # 5번 측정 후 결과 출력
    total_time = sum(st.session_state.reaction_times)
    st.write(f"총 소요 시간: {total_time:.4f} 초")
    
    if total_time <= 3:
        st.write("**등급: S**")
    elif total_time <= 4:
        st.write("**등급: A**")
    else:
        st.write("**유감이네요!**")
        st.write("반응 속도를 향상시키기 위해 연습을 계속해보세요!")
    
    # 다시 시작 버튼을 보여줌
    if st.button("다시 시작"):
        st.session_state.reaction_times = []
