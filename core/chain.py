import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import JsonOutputParser
from .prompts import evaluation_prompt, generation_prompt, validation_prompt
from .parsers import InterviewEvaluation, GeneratedQuestion, QuestionValidationResult

load_dotenv()

repo_id = "deepseek-ai/DeepSeek-R1" 

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    max_length=2048,
    temperature=0.7,
    huggingfacehub_api_token=os.environ.get("HUGGINGFACEHUB_API_TOKEN")
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
