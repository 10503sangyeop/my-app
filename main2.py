import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Streamlit 앱 제목
st.title("기온 상승과 이상기후 및 자연재해 시각화")

# 사이드바를 통해 데이터 선택
st.sidebar.header("데이터 옵션")
data_source = st.sidebar.selectbox(
    "데이터를 선택하세요",
    ("샘플 데이터 사용", "CSV 파일 업로드")
)

# 데이터 준비
if data_source == "샘플 데이터 사용":
    # 샘플 데이터 생성
    years = np.arange(2000, 2025)
    temp_rise = np.random.uniform(0.1, 1.0, len(years)).cumsum()  # 누적 기온 상승
    extreme_weather = np.random.randint(10, 50, len(years))  # 이상기후 발생 빈도
    disaster_freq = np.random.randint(5, 30, len(years))  # 자연재해 발생 빈도
    disaster_scale = np.random.uniform(1.0, 10.0, len(years))  # 자연재해 발생 규모

    data = pd.DataFrame({
        "Year": years,
        "Temperature Rise (°C)": temp_rise,
        "Extreme Weather Frequency": extreme_weather,
        "Disaster Frequency": disaster_freq,
        "Disaster Scale": disaster_scale
    })
else:
    # CSV 파일 업로드
    uploaded_file = st.sidebar.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
    else:
        st.warning("CSV 파일을 업로드하세요.")
        st.stop()

# 데이터 확인
st.subheader("데이터 미리보기")
st.dataframe(data)

# 그래프 생성
st.subheader("데이터 시각화")

# 기온 상승 그래프
st.write("### 기온 상승 (°C)")
fig, ax = plt.subplots()
ax.plot(data["Year"], data["Temperature Rise (°C)"], color='orange', marker='o', label="기온 상승")
ax.set_xlabel("Year")
ax.set_ylabel("Temperature Rise (°C)")
ax.set_title("기온 상승")
ax.legend()
st.pyplot(fig)

# 이상기후 발생 빈도 그래프
st.write("### 이상기후 발생 빈도")
fig, ax = plt.subplots()
ax.bar(data["Year"], data["Extreme Weather Frequency"], color='blue', label="이상기후 발생 빈도")
ax.set_xlabel("Year")
ax.set_ylabel("Frequency")
ax.set_title("이상기후 발생 빈도")
ax.legend()
st.pyplot(fig)

# 자연재해 발생 빈도 및 규모 그래프
st.write("### 자연재해 발생 빈도와 규모")
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel("Year")
ax1.set_ylabel("Disaster Frequency", color=color)
ax1.bar(data["Year"], data["Disaster Frequency"], color=color, alpha=0.6, label="발생 빈도")
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel("Disaster Scale", color=color)
ax2.plot(data["Year"], data["Disaster Scale"], color=color, marker='o', label="발생 규모")
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
st.pyplot(fig)

st.write("데이터를 분석하고, 변화 추이를 확인해보세요!")

