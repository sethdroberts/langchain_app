import os

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = process.env.{OPENAI_API_KEY}


#App framework
st.title('🦜🔗 YouTube GPT Creator')
prompt = st.text_input('Plug in your prompt here')