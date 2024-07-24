import streamlit as st

st.title("Sum of no's in string")
a=st.text_input(label="Input String")
if st.button(label="submit"):
    try:
        sum=0
        for i in a:
            if i.isnumeric():
                sum+=int(i)
        st.info(sum)
    except ValueError:
         st.write("Please enter a valid String")