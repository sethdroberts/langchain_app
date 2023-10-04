import os

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

#Remove this line while working locally to access Codespace secret
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

apikey = os.environ['OPENAI_API_KEY']

#App framework
st.title('🦜🔗 YouTube Script Generator')
prompt = st.text_input('Plug in your prompt here')

#Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = "write me a youtube video title about {topic}"
) 

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'],
    template = "write me a youtube video script based on this title TITLE: {title}, but also while leveraging this wikipedia research: {wikipedia_research}"
) 

#Memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

#llms
llm = OpenAI(openai_api_key=apikey, temperature=0.9, max_tokens=1024)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

wiki=WikipediaAPIWrapper()

#Show stuff to the screen if there's a prompt
if prompt:
    title=title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    wiki_sources = wiki.load(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)
    
    st.write(title)
    st.write(script)

   # with st.expander('Title History'):
    #    st.info(title_memory.buffer)

    #with st.expander('Script History'):
     #   st.info(script_memory.buffer)

    st.divider()
    st.subheader("Wikipedia Sources:")
    for i in wiki_sources:
        with st.expander(i.metadata['title']):
            st.info(i.metadata['summary'])
            st.info(i.metadata['source'])
       
    