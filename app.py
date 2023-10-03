import os

import streamlit as st
from langchain.llms import OpenAI

#Remove this line while working locally to access Codespace secret
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

apikey = os.environ['OPENAI_API_KEY']

#App framework
st.title('🦜🔗 LangChain LLM App')
prompt = st.text_input('Plug in your prompt here')

#llms
llm = OpenAI(openai_api_key=apikey, temperature=0.9)

#Show stuff to the screen if there's a prompt
if prompt:
    response = llm(prompt)
    st.write(response)