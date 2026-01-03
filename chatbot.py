from python-dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

#load the env variable
load_dotenv()

#streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered"
)
st.title("💬 GEN AI Chatbot")


#initiate chat history
#chat_history = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#llm intiate
llm =ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature =0.0,
)

#input box
user_prompt = st.chat_input("Ask chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content" : user_prompt})

    response = llm.invoke(
        input = [{"role": "system", "content" : "You are a helpful assistent"}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content" : assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)



# USER query --> display user query --> save query to chat_history --> send the chat_history to llm --> get response from llm -->
#--> save reponse in chat_history --> display llm response

