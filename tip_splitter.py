import streamlit as st

st.set_page_config(
    page_title="Bill Splitter",
    page_icon="💸",
    layout="centered"
)

st.title("💸 Bill Splitter")
st.write("Easily Split Bill and Calculate tip with Friends!")

amount=st.number_input("Enter Total Bill Amount: ",min_value=0.0)
tip =st.slider("Tip-Percentage:",0,30)
person =st.number_input("Number of People: ", min_value=1)

tip_amount= (amount * tip / 100)
total= amount+tip_amount
pay=total/person




col1 ,col2, col3 =st.columns(3)

with col1:
    st.metric("Tip Amount:", f"{tip_amount:.2f}")

with col2:
    st.metric("Total Amount:", f"{total:.2f}")

with col3:
    st.metric("Each Pay:", f"{pay:.2f}")

