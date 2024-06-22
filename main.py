import streamlit as st
from chat_history import save_chat_session,load_chat_session,display_saved_sessions, display_chat_history
from llm_prompt import generate_response
st.title("Moron ChatBot")


def main():
    st.sidebar.title("Session Manager")

    # Display saved sessions in the sidebar
    saved_sessions = display_chat_history()
    selected_session = st.sidebar.selectbox("Select a session to load", [""] + saved_sessions, index=0)
    
    if selected_session:
        chat_log = load_chat_session(selected_session)
        if chat_log:
            display_chat_history(chat_log)

    session_name = st.sidebar.text_input("Enter title:", key="session_name")
    
    if st.sidebar.button("Save Chat"):
        if session_name:
            save_chat_session(session_name, st.session_state.chat_log)
        else:
            st.sidebar.error("Please enter a name to save the chat.")

    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []

    user_message = st.chat_input("Enter your message here", key="user_input")
    if user_message:
        st.session_state.chat_log.append({"name": "user", "msg": user_message})
        
        response = generate_response(user_message, chat_history=st.session_state.chat_log)
    
        if response:
            st.session_state.chat_log.append({"name": "assistant", "msg": response})
        
        display_chat_history(st.session_state.chat_log)

if __name__ == "__main__":
    main()
