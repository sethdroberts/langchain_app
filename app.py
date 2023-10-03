import os

import streamlit as st
from langchain.llms import OpenAI

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