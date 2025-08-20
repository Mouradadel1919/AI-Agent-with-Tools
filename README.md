# AI Agent with Tools (End-to-End Project)

This project is an **end-to-end AI Agent** powered by **Llama 3 (8B)** running locally with **Ollama**.  
The agent is designed with **4 specialized tools** that enhance its ability to understand and process user queries intelligently.  
It is deployed via **FastAPI** and packaged into a **Docker image** so anyone can run it easily.

---

## Features

### Model
- **Llama 3 (8B)** running locally using [Ollama](https://ollama.ai/).

### Tools
1. **Context Judge Tool** → Determines whether the input question has enough context.  
2. **Context Relevant Tool** → Checks if the provided context is relevant to the question.  
3. **Context Splitter Tool** → Splits the context from the question.  
4. **Web Search Tool** → If context is missing, the agent performs a web search to gather more information.

### Deployment
- Built with **FastAPI** for serving the AI Agent.  
- Packaged into a **Docker container** for easy use and portability.  
- Available on **Docker Hub**:  
  [mouradadel313/ai_agent_with_tools](https://hub.docker.com/repository/docker/mouradadel313/ai_agent_with_tools/tags)

---

## Run with Docker

You can quickly get started with just two commands:

```bash
# 1. Pull the latest image
docker pull mouradadel313/ai_agent_with_tools:latest

# 2. Run the container
docker run -d -p 8080:8080 mouradadel313/ai_agent_with_tools:latest
```
## Click 

<img width="1593" height="570" alt="Capture" src="https://github.com/user-attachments/assets/20d6005d-928c-43fb-a8b4-76ead7e2d2e5" />
