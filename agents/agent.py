from langchain.agents import Tool
#from langchain_community.llms import Ollama
from my_tools.ContextPresenceJudge import ContextPresenceJudgeTool
from my_tools.WebSearch import WebSearchTool
from my_tools.RelevanceChecker import RelevanceCheckerTool
from my_tools.ContextSplitter import ContextSplitterTool
#from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from typing import Dict, Any


llm = OllamaLLM(model="llama3:8b")

class ConditionalAgentExecutor:
    """Custom agent executor that enforces conditional tool usage"""
    
    def __init__(self, tools, verbose=True):
        self.tools = {tool.name: tool for tool in tools}
        self.context_judge = ContextPresenceJudgeTool
        self.web_search = WebSearchTool
        self.relevance_context = RelevanceCheckerTool
        self.splitter = ContextSplitterTool
        self.verbose = verbose
        self.llm = llm
    
    def invoke(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the agent with conditional logic"""
        user_input = inputs["input"]
        
        if self.verbose:
            print(f"\n> Starting agent with input: {user_input}")
        
        # Step 1: Always start with context judge
        if self.verbose:
            print(f"\n> Step 1: Checking context with ContextPresenceJudgeTool")
        
        context_result = self.context_judge.func(user_input)
        
        if self.verbose:
            print({"Context_Judge_Result": context_result})

        
        # Step 2: Decide based on context judge result
        context_result_lower = context_result.strip().lower()
        
        if "context_missing" in context_result_lower:
            # Context is missing, use web search
            if self.verbose:
                print(f"\n> Step 2: Context is missing. Using WebSearchTool to search for: {user_input}")
            
            web_results = self.web_search.func(user_input)
            
            if self.verbose:
                print(f"> Web Search Results: {web_results}")
            
            final_answer = f"Based on the web search results:\n\n{web_results}\n\nThis information helps answer your question: {user_input}"
            
            return {
                "Context_Judge_Result": context_result_lower,
                "web_result": web_results,
                "output": self.llm(final_answer)
                }
            
        elif "context_provided" in context_result_lower:
            # Context is provided, don't use web search
            if self.verbose:
                print(f"\n> Step 2: Context is sufficient. No web search needed.")
            
            final_answer = f"Based on the context judge, sufficient context is provided to answer this question the question: '{user_input}'. The question contains enough information and doesn't require additional web search."
            
            return {
                "Context_Judge_Result": context_result_lower,
                "context": self.splitter.func(user_input),
                "Relevance" : self.relevance_context.func(user_input),
                "output": self.llm(final_answer)}
            
        else:
            # Unclear response from context judge
            if self.verbose:
                print(f"\n> Step 2: Context judge result was unclear: {context_result}")
            
            return {"output": f"Unable to determine context status clearly. Context judge returned: {context_result}"}

# Initialize the tools
tools = [ContextPresenceJudgeTool, WebSearchTool]

# Create the custom agent executor
agent_executor = ConditionalAgentExecutor(tools=tools, verbose=True)

