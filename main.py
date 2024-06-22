import ollama
import streamlit as st

st.title("Moron ChatBot")

def generate_response(user_message: str, chat_history: list=[]):
    system_msg=("You are a Chatbot assistant")       #give role to Chatbot 
    my_message = [{"role": "system", "content": system_msg}]
    
    for chat in chat_history:                        #Append history in message 
        my_message.append({"role": chat["name"], "content": chat["msg"]})
                                                     #Append the latest question in message
    my_message.append({"role": "user", "content": user_message})
    
    response = ollama.chat(                          #define model&input for response 
        model="llama3",
        messages=my_message
        )

    return response["message"]["content"]

def main():

    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []

    user_message = st.chat_input("Enter your message here", key="user_input")
    if user_message:
        for chat in st.session_state.chat_log:          #first display chat history
            with st.chat_message(chat["name"]):
                st.write(chat["msg"])
    
        with st.chat_message("user"):                  #display latest user message
            st.write(user_message)

    response=generate_response(user_message, chat_history=st.session_state.chat_log)

    if response:
        with st.chat_message("assistant"):
            assistant_response_area = st.empty()
            assistant_response_area.write(response)   # at bottom show LLM response
        
        #add latest message and response to chat history 
        st.session_state.chat_log.append({"name": "user", "msg": user_message})
        st.session_state.chat_log.append({"name": "assistant", "msg": response})

if __name__ == "__main__":
    main()
