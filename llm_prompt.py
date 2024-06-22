import ollama

def load_model(my_message):
    response = ollama.chat(
        model="llama3",
        messages=my_message
    )
    return response["message"]["content"]

def generate_response(user_message: str, chat_history: list=[]):
    system_msg = "You are a Chatbot assistant"
    my_message = [{"role": "system", "content": system_msg}]
    
    for chat in chat_history:
        my_message.append({"role": chat["name"], "content": chat["msg"]})
    my_message.append({"role": "user", "content": user_message})
    
    response = load_model(my_message)
    return response