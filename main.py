import streamlit as st 
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text 

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("cold emailing agent")
    url_input = st.text_input("Enter the URL of the job listing:" , value="https://careers.nike.com/data-analyst/job/R-51792")
    submit_button = st.button("Generate Email")
    
    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio() 
            jobs = llm.extract_jobs(data) 
            for job in jobs: #if one webpage have many jobs 
                skills = job.get("skills",[])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job,links) 
                st.write(email.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    llm = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Emailing Agent", page_icon="📧")
    create_streamlit_app(llm, portfolio, clean_text)
    
    