import os
from dotenv import load_dotenv
import streamlit as st
from pypdf import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_classic.chains.question_answering import load_qa_chain

def main():
    load_dotenv()
    
    # Ensure GOOGLE_API_KEY is in your .env file
    if not os.getenv("GOOGLE_API_KEY"):
        st.error("Please set your GOOGLE_API_KEY in the .env file")
        return

    st.set_page_config(page_title="Ask your PDF (Gemini Edition)")
    st.header("Ask your PDF 💬")
    
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    
    if pdf is not None:
      pdf_reader = PdfReader(pdf)
      text = ""
      for page in pdf_reader.pages:
        text += page.extract_text()
        
      text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
      )
      chunks = text_splitter.split_text(text)
      
      # 1. NEW: Gemini Embeddings
      # 'text-embedding-004' is the modern 2026 standard for Gemini
      embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
      
      with st.spinner("Creating vector space..."):
          knowledge_base = FAISS.from_texts(chunks, embeddings)
      
      user_question = st.text_input("Ask a question about your PDF:")
      
      if user_question:
        docs = knowledge_base.similarity_search(user_question)
        
        # 2. NEW: Gemini Chat Model
        # Gemini 3 Flash is fast and usually falls under the free tier
        llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.3)
        
        chain = load_qa_chain(llm, chain_type="stuff")
        
        # Note: get_openai_callback() only works for OpenAI. 
        # For Gemini, we simply run the chain.
        with st.spinner("Gemini is thinking..."):
            response = chain.run(input_documents=docs, question=user_question)
           
        st.write(response)

if __name__ == '__main__':
    main()
