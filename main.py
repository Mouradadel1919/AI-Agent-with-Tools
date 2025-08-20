from agents.agent import agent_executor
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os


app = FastAPI()

# Setup templates

current_dir = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(current_dir, "templates")
static_path = os.path.join(current_dir, "static")

# Debug paths
print(f"Current directory: {current_dir}")
print(f"Templates path: {templates_path}")
print(f"Static path: {static_path}")

# Check if directories exist
print(f"Templates exists: {os.path.exists(templates_path)}")
print(f"Static exists: {os.path.exists(static_path)}")

if os.path.exists(templates_path):
    print(f"Template files: {os.listdir(templates_path)}")
if os.path.exists(static_path):
    print(f"Static files: {os.listdir(static_path)}")

# Setup templates with absolute path
templates = Jinja2Templates(directory=templates_path)

# Mount static files with absolute path
app.mount("/static", StaticFiles(directory=static_path), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    return templates.TemplateResponse("predict.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, user_input: str = Form(...)):
    # Run your custom agent
    result = agent_executor.invoke({"input": user_input})

    # Ensure consistent keys
    judge = result.get("Context_Judge_Result")
    search = result.get("web_result", "No search needed")
    context = result.get("context", "No context extracted.")
    relevance = result.get("Relevance", "No relevance score.")
    output = result.get("output", "No output generated.")

    return templates.TemplateResponse(
        "predict.html",
        {
            "request": request,
            "judge": judge,
            "search": search,
            "user_input": user_input,
            "context": context,
            "relevance": relevance,
            "output": output,
        },
    )

@app.get("/about",  response_class=HTMLResponse)
async def predict(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080
    )