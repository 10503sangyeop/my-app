import streamlit as st
import random



st.title('나의 첫 번째 앱')
st.write('안녕하세요, 저는 상엽 입니다')
st.write('저의 이메일 주소는 sy2008.kim@gmail.com 입니다')


import streamlit as st

st.button("Reset", type="primary")
if st.button("난수 생성"):
    st.write("random.randint(1,100)")
else:
    st.write("Goodbye")
  
