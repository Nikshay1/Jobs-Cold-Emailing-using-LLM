import os 
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

class Chain : 
    def __init__(self): 
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name = "llama-3.3-70b-versatile")
    
    def extract_jobs(self,cleaned_text) : 
        prompt_extract = ChatPromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}

        ### INSTRUCTIONS:
        - The provided text is from a job listing on a company's careers page.
        - Extract relevant job details and return a structured JSON object with the following keys:
          - "company" (string): The company name.
          - "location" (string): The job location.
          - "role" (string): The job title.
          - "experience" (string): Required years of experience.
          - "skills" (list of strings): A list of required skills.
          - "job_description"(string) : the job description  
        - Ensure the JSON is valid, properly formatted, and contains only the necessary details.
        - Do NOT include any introductory text, explanations, or additional commentary.
        - ### DO NOT INCLUDE A PREAMBLE OR ANY OTHER TEXT EXCEPT THE JSON FILE --- REALLY IMPORTANTTT!!!

        ### OUTPUT FORMAT (Strict JSON):
        {{
          "company": "Example Corp",
          "location": "123 Example St, City, Country",
          "role": "Software Engineer",
          "experience": "3 years",
          "skills": ["Python", "Machine Learning", "AWS"] ,
          "job_description" : ""
        }}
        """
        )
        chain_extract = prompt_extract | self.llm 
        res = chain_extract.invoke(
        {"page_data" : cleaned_text}
        )
        try: 
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException(
                "context too big , unable to parse jobs"
            )
        return res if isinstance(res, list) else [res]
    
    
    def write_mail(self, job, links): 
        prompt_email = ChatPromptTemplate.from_template(
            """
            ### JOB DESCRIPTION :
            {job_description} 

            ### INSTRUCTION : 
            You are Nikshay Yadav, a second-year Computer Science student at Delhi Technological University. 
            Your graduation year is 2027. Your current CGPA is 7.65. 
            Your job is to write a cold email to the client regarding the job mentioned above, describing your capability to fulfill their needs. 
            Also, add the most relevant ones from the following links to showcase my portfolio: {link_list} 
            Remember, you are Nikshay Yadav, a 2nd-year Computer Science student at Delhi Technological University.

            ### DO NOT PROVIDE A PREAMBLE OR ANY OTHER TEXT OTHER THAN THE EMAIL --- REALLY IMPORTANT!!!

            ### EMAIL (NO PREAMBLE):
            """
        )  # <- This closing parenthesis was missing

        chain_email = prompt_email | self.llm  # Now correctly placed
        res = chain_email.invoke(
            {
                "job_description": str(job),
                "link_list": links
            }
        )

        return res

            

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY")) # Print the API key to verify it's loaded correctly 