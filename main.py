import ollama
import streamlit as st

st.title("LLAMA3 ChatBot")

def generate_response(user_message):
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": user_message}]
    )
    return response["message"]["content"]


user_msg = st.chat_input("Enter your message here", key="user_input")
if user_msg:
    with st.chat_message("user"):
        st.write(user_msg)

response=generate_response(user_msg)

if response:
    with st.chat_message("assistant"):
        assistant_response_area = st.empty()
        assistant_response_area.write(response)
