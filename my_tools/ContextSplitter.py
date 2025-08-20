from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.tools import Tool
#from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3:8b")
prompt = PromptTemplate.from_template(open("prompts/context_splitter_prompt.txt").read())
chain = LLMChain(llm=llm, prompt=prompt)

ContextSplitterTool = Tool.from_function(
    func= chain.run,
    name="ContextSplitterTool",
    description="Use this tool to extract context from the question input. "
            "Input should be the user's full question. It will return context extracted from input.")
