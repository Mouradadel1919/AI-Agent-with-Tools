from langchain_core.tools import Tool
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3:8b")
prompt = PromptTemplate.from_template(open("prompts/relevance_checker_prompt.txt").read())
chain = LLMChain(llm=llm, prompt=prompt)
'''
def relevance_checker_func(question, context):
    return chain.run({"question": question, "context": context})
'''

RelevanceCheckerTool=  Tool.from_function(
    func=chain.run,
    name="ContextRelevanceChecker",
    description="Determines if provided context is relevant to answer a question. Returns 'relevant' or 'irrelevant'."
)