import json
import os
import streamlit as st

def save_chat_session(session_name, chat_log):
    chat_session = {
        "name": session_name,
        "chat_log": chat_log
    }
    # Ensure the directory exists
    os.makedirs("chat_session", exist_ok=True)
    # Save chat session to a JSON file
    with open(os.path.join("chat_session", f"{session_name}.json"), "w") as f:
        json.dump(chat_session, f)
        
    # Return updated list of saved sessions
    return list_saved_session()

def load_chat_session(session_name):
    # Load chat session from a JSON file
    file_path = os.path.join("chat_session", f"{session_name}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            chat_session = json.load(f)
        st.session_state.chat_log = chat_session["chat_log"]
        
        return chat_session["chat_log"]
    else:
        st.sidebar.error(f"No chat session found with the name '{session_name}'")
        return []

def list_saved_session():
    # Ensure the directory exists
    os.makedirs("chat_session", exist_ok=True)
    sessions = [f.replace('.json', '') for f in os.listdir("chat_session") if f.endswith('.json')]
    return sessions

def display_chat_history(chat_history):
    for chat in chat_history:
        with st.chat_message(chat["name"]):
            st.write(chat["msg"])

