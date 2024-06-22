
import streamlit as st
from chat_history import load_chat_session,list_saved_session,save_chat_session,display_chat_history
from llm_prompt import generate_response 

st.title("Moron ChatBot")

def main():
    st.sidebar.title("Save/Load Chat Session")

    # Display saved sessions in the sidebar
    saved_sessions = list_saved_session()
    selected_session = st.sidebar.selectbox("Select a session to load", [""] + saved_sessions, index=0)
    
    if selected_session:
        chat_log = load_chat_session(selected_session)
        if chat_log:
            display_chat_history(chat_log)

    session_name = st.sidebar.text_input("Enter title:", key="session_name")
    
    if st.sidebar.button("Save Chat"):
        if session_name:
            saved_sessions = save_chat_session(session_name, st.session_state.chat_log)  # Update saved_sessions
            st.sidebar.success(f"Session saved!")
        else:
            st.sidebar.error("Please enter a name to save the chat.")

    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []

  

    user_message = st.chat_input("Enter your message here", key="user_input")
    if user_message:
        
        for chat in st.session_state.chat_log:
            with st.chat_message(chat["name"]):
                st.write(chat["msg"])

        with st.chat_message("user"):
            st.write(user_message)

        with st.spinner("Loading answer..."):
            response = generate_response(user_message, chat_history=st.session_state.chat_log)
            if response:
                    with st.chat_message("assistant"):
                        assistant_msg = response
                        assistant_response_area = st.empty()
                        assistant_response_area.write(assistant_msg)

            st.session_state.chat_log.append({"name": "user", "msg": user_message})
            st.session_state.chat_log.append({"name": "assistant", "msg": response})
        


if __name__ == "__main__":
    main()
