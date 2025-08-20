from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.tools import Tool
#from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3:8b")
prompt = PromptTemplate.from_template(open("prompts/context_judge_prompt.txt").read())
chain = LLMChain(llm=llm, prompt=prompt)



ContextPresenceJudgeTool =  Tool.from_function(
        func=chain.run,
        name="ContextPresenceJudgeTool",
        description="Use this tool first to determine whether the question has enough context. "
                "Input should be the user's full question. It will return either 'context_provided' or 'context_missing'.")




