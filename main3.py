import streamlit as st
import time

# 앱 제목
st.title("키보드 반응 속도 테스트")

# 설명
st.write("초록색 버튼이 나타나면 'K' 버튼을 최대한 빠르게 눌러주세요. 이 과정을 5번 진행하고, 총 시간이 3초 이하이면 S등급, 3초 초과 4초 이하이면 A등급, 5초 초과이면 '유감이네요'라고 말합니다.")

# 카운트다운 타이머와 키 입력을 측정하는 함수
def measure_speed():
    input_times = []  # 키보드를 누른 시간 기록
    total_time = 0  # 총 시간
    attempts = 5  # 테스트 횟수

    # 5번의 테스트 진행
    for i in range(attempts):
        st.write(f"테스트 {i+1}/{attempts} 시작!")

        # 초록색 버튼 표시
        button = st.button("초록색 버튼", key=f"button_{i}")
        if button:
            start_time = time.time()  # 버튼 클릭 시 시작 시간 기록
            st.write("지금 'K' 버튼을 눌러주세요!")
            # 사용자가 'K'를 입력할 때까지 기다림
            while True:
                user_input = st.text_input(f"여기서 'K'를 입력하세요.", key=f"input_{i}")
                if user_input.lower() == 'k':
                    end_time = time.time()  # 'K'를 입력한 시간 기록
                    input_times.append(end_time - start_time)  # 눌린 시간 기록
                    total_time += end_time - start_time  # 총 시간에 더하기
                    st.write(f"반응 시간: {end_time - start_time:.3f}초")
                    break

    return input_times, total_time

# 키보드 반응 속도 측정
if st.button("테스트 시작"):
    input_times, total_time = measure_speed()

    # 평균 반응 시간 및 총 시간 계산
    average_time = total_time / len(input_times)
    
    # 등급 평가
    if total_time <= 3:
        st.write("S 등급! 훌륭한 속도입니다!")
    elif total_time <= 4:
        st.write("A 등급! 좋습니다!")
    else:
        st.write("유감이네요... 좀 더 연습해보세요.")

    st.write(f"총 소요 시간: {total_time:.3f}초")
    st.write(f"평균 반응 시간: {average_time:.3f}초")
