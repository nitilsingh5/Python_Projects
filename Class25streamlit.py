import streamlit as st
from PIL import Image
image=Image.open('download.jpg')
st.image(image,caption='Welcome to Nitil')
st.title('Loan Calculator')
st.header('Nitil Bank of India')
x=st.number_input('Enter Your amount')
y=st.number_input('Enter your salary')
if y>50000:
    st.write('Congratulation Your loan is approved')
    st.balloons()

else:
    st.write('Your loan is not approved')

st.radio('Are you a Govt. emp',options=['Yes','No'])
st.checkbox('Do you have a credit card')
st.sidebar.header('Schemes')
st.sidebar.markdown('This is schemes')