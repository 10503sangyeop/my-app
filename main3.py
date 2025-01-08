import streamlit as st
import pandas as pd
import plotly.express as px  # Plotly 사용

# 앱 제목
st.title("국가별 사망률 시각화 앱")

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
    mortality_rates = [5.2, 8.7, 10.5, 11.1, 9.8, 7.6, 6.2, 6.9, 6.3, 7.8]  # 가상의 사망률 데이터
    data = pd.DataFrame({"Country": countries, "Mortality Rate (%)": mortality_rates})

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
st.subheader("국가별 사망률 그래프")
fig = px.bar(
    data,
    x="Country",
    y="Mortality Rate (%)",
    title="국가별 사망률",
    labels={"Mortality Rate (%)": "사망률 (%)", "Country": "국가"},
    color="Mortality Rate (%)",  # 색상으로 사망률 표시
    color_continuous_scale="Blues"
)
fig.update_layout(xaxis_tickangle=-45)  # x축 레이블 회전
st.plotly_chart(fig)

# 추가 분석
st.subheader("추가 분석")
highest_mortality = data.loc[data["Mortality Rate (%)"].idxmax()]
lowest_mortality = data.loc[data["Mortality Rate (%)"].idxmin()]

st.write(f"**사망률이 가장 높은 국가**: {highest_mortality['Country']} ({highest_mortality['Mortality Rate (%)']}%)")
st.write(f"**사망률이 가장 낮은 국가**: {lowest_mortality['Country']} ({lowest_mortality['Mortality Rate (%)']}%)")

# 사용자 의견 요청
st.write("### 인사이트")
st.text_area("데이터를 보고 얻은 인사이트를 기록하세요.", placeholder="예: 특정 국가의 사망률이 높은 이유는...")

st.write("앱을 사용해주셔서 감사합니다!")
