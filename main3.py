import streamlit as st
import pandas as pd
import plotly.graph_objects as go  # Plotly 그래프 객체 사용

# 앱 제목
st.title("국가별 사망률, 출산율, 노인 비율 시각화 앱")

# 사이드바: 데이터 입력 옵션
st.sidebar.header("데이터 입력 옵션")
data_input_method = st.sidebar.selectbox(
    "데이터 입력 방법을 선택하세요",
    ("샘플 데이터 사용", "CSV 파일 업로드")
)

# 데이터 준비
if data_input_method == "샘플 데이터 사용":
    # 샘플 데이터 생성
    countries = ["한국", "미국", "일본", "독일", "프랑스", "중국", "인도", "브라질", "호주", "캐나다"]
    mortality_rates = [5.2, 8.7, 10.5, 11.1, 9.8, 7.6, 6.2, 6.9, 6.3, 7.8]  # 사망률 (%)
    birth_rates = [0.9, 1.6, 1.2, 1.4, 1.9, 1.7, 2.3, 2.1, 1.8, 1.5]  # 출산율 (출생아 수)
    elderly_ratios = [16.5, 12.9, 29.1, 22.3, 20.1, 10.6, 8.2, 9.3, 13.4, 14.8]  # 노인 비율 (%)

    data = pd.DataFrame({
        "Country": countries,
        "Mortality Rate (%)": mortality_rates,
        "Birth Rate (per 1000)": birth_rates,
        "Elderly Ratio (%)": elderly_ratios
    })

elif data_input_method == "CSV 파일 업로드":
    uploaded_file = st.sidebar.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
    else:
        st.warning("CSV 파일을 업로드하세요.")
        st.stop()

# 데이터 미리보기
st.subheader("데이터 미리보기")
st.dataframe(data)

# 그래프 시각화
st.subheader("국가별 사망률, 출산율, 노인 비율")

# Plotly 그래프 생성
fig = go.Figure()

# 사망률
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["Mortality Rate (%)"],
    name="사망률 (%)",
    marker=dict(color="red")
))

# 출산율
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["Birth Rate (per 1000)"],
    name="출산율 (출생아 수)",
    marker=dict(color="blue")
))

# 노인 비율
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["Elderly Ratio (%)"],
    name="노인 비율 (%)",
    marker=dict(color="green")
))

# 레이아웃 설정
fig.update_layout(
    title="국가별 사망률, 출산율, 노인 비율 비교",
    xaxis_title="국가",
    yaxis_title="비율 / 값",
    barmode="group",  # 그룹형 막대 그래프
    xaxis_tickangle=-45  # x축 레이블 회전
)

# Streamlit에 그래프 표시
st.plotly_chart(fig)

# 추가 분석
st.subheader("추가 분석")
highest_mortality = data.loc[data["Mortality Rate (%)"].idxmax()]
highest_birth_rate = data.loc[data["Birth Rate (per 1000)"].idxmax()]
highest_elderly_ratio = data.loc[data["Elderly Ratio (%)"].idxmax()]

st.write(f"**사망률이 가장 높은 국가**: {highest_mortality['Country']} ({highest_mortality['Mortality Rate (%)']}%)")
st.write(f"**출산율이 가장 높은 국가**: {highest_birth_rate['Country']} ({highest_birth_rate['Birth Rate (per 1000)']})")
st.write(f"**노인 비율이 가장 높은 국가**: {highest_elderly_ratio['Country']} ({highest_elderly_ratio['Elderly Ratio (%)']}%)")

# 사용자 의견 요청
st.write("### 인사이트")
st.text_area("데이터를 보고 얻은 인사이트를 기록하세요.", placeholder="예: 특정 국가의 출산율이 낮은 이유는...")

st.write("앱을 사용해주셔서 감사합니다!")
