import streamlit as st
from streamlit_chat import message
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.memory import ConversationBufferMemory
from pydantic import BaseModel, Field
import re

#clé OpenAI
api_key = "sk-proj-_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Modèle LLM GPT-4
llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0,
    openai_api_key=api_key
)

# Mémoire
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Prompt Darija
chat_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        """Nta chatbot dyal l9anoun f lmaghrib. Jawb b darija maghribia fa9at. 
        Ma t9drch tjawb b anglais ou fransawi ou fos7a.
        Jawb 3la sou2al f l9anoun lmaghribi (contrat, wiratha, khdma, etc). 
        Ila ma kaynach 3la9a b l9anoun, gol: 'Smah lia, ana nqdr njawb ghir 3la lmasail l9anounia.'"""
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{user_input}"),
])

# Chaîne LLM
llm_chain = LLMChain(llm=llm, prompt=chat_template, memory=memory, verbose=False)

# Interface Streamlit
st.set_page_config(page_title="Chatbot L9anoun b Darija 🇲🇦", layout="centered")
st.title("⚖️ Chatbot Dyal L9anoun b Darija 🇲🇦")
st.markdown("🟢 Ktoub sou2al dyalek hna:")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("", key="input_field")

if user_input:
    st.session_state.chat_history.append(("🧑", user_input))

    raw_answer = llm_chain.run(user_input)

    darija_lines = [
    line.strip() for line in raw_answer.split("\n")
    if not re.match(r"^[A-Z][a-z]", line.strip()) and not line.lower().startswith("the ")]
    darija_answer = "\n".join(darija_lines).strip()
    if not darija_answer:
        darija_answer = "Smah lia, ana nqdr njawb ghir 3la lmasail l9anounia b darija lmaghribia."

    st.session_state.chat_history.append(("🤖", darija_answer))

# Affichage conversation
for i, (speaker, msg) in enumerate(st.session_state.chat_history):
    is_user = speaker == "🧑"
    message(msg, is_user=is_user, key=f"{speaker}_{i}")
