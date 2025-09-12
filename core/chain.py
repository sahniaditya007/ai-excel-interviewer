import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from .prompts import evaluation_prompt, generation_prompt, validation_prompt
from .parsers import InterviewEvaluation, GeneratedQuestion, QuestionValidationResult

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    google_api_key=os.environ.get("GEMINI_API_KEY"),
    temperature=0.7,
    max_output_tokens=2048
)

def create_evaluation_chain():
    parser = JsonOutputParser(pydantic_object=InterviewEvaluation)
    prompt = evaluation_prompt.partial(format_instructions=parser.get_format_instructions())
    chain = prompt | llm | parser
    return chain

def create_generation_chain():
    parser = JsonOutputParser(pydantic_object=GeneratedQuestion)
    prompt = generation_prompt.partial(format_instructions=parser.get_format_instructions())
    chain = prompt | llm | parser
    return chain

def create_validation_chain():
    parser = JsonOutputParser(pydantic_object=QuestionValidationResult)
    prompt = validation_prompt.partial(format_instructions=parser.get_format_instructions())
    chain = prompt | llm | parser
    return chain

evaluation_chain = create_evaluation_chain()
generation_chain = create_generation_chain()
validation_chain = create_validation_chain()
