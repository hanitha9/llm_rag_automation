from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_engine import RAGEngine
from code_generator import CodeGenerator
from automation_functions import FUNCTION_METADATA
import uvicorn
import logging
from datetime import datetime

logging.basicConfig(
    filename='api_execution.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()
code_generator = CodeGenerator()
chat_history = []
execution_log = []
rag_engine = RAGEngine()

class PromptRequest(BaseModel):
    prompt: str

class FunctionRegisterRequest(BaseModel):
    name: str
    description: str
    params: list[str] = None

@app.post("/execute")
async def execute_function(request: PromptRequest):
    try:
        logger.info(f"Received prompt: {request.prompt}")
        function_name = rag_engine.maintain_context(chat_history, request.prompt)
        if not function_name:
            raise ValueError("No function retrieved")
        logger.info(f"Retrieved function: {function_name} for prompt: {request.prompt}")

        params = None
        if "params" in FUNCTION_METADATA[function_name]:
            prompt_lower = request.prompt.lower()
            if "file" in prompt_lower:
                params = ["example.txt"]
            elif "command" in prompt_lower:
                params = ["dir"]
            elif "say_hello" in function_name:
                if "world" in prompt_lower:
                    params = ["world"]
                elif chat_history and "world" in chat_history[-1]["prompt"].lower():
                    params = ["world"]

        generated_code = code_generator.generate_code(function_name, params)
        chat_history.append({"prompt": request.prompt})

        execution_log.append({
            "timestamp": datetime.now().isoformat(),
            "prompt": request.prompt,
            "function": function_name,
            "params": params
        })
        logger.info(f"Generated code for {function_name} with params: {params}")

        return {
            "function": function_name,
            "code": generated_code
        }
    except Exception as e:
        logger.error(f"Error processing prompt '{request.prompt}': {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/monitor")
async def get_execution_log():
    logger.info("Accessed execution log endpoint")
    return {"executions": execution_log[-10:]}

@app.post("/register_function")
async def register_function(request: FunctionRegisterRequest):
    try:
        if request.name in FUNCTION_METADATA:
            logger.warning(f"Function {request.name} already exists")
            raise HTTPException(status_code=400, detail="Function already exists")
        
        FUNCTION_METADATA[request.name] = {"description": request.description}
        if request.params:
            FUNCTION_METADATA[request.name]["params"] = request.params

        rag_engine.function_names = list(FUNCTION_METADATA.keys())
        rag_engine._build_index()
        logger.info(f"Registered new function: {request.name} - {request.description}")
        
        return {"message": f"Function '{request.name}' registered successfully"}
    except Exception as e:
        logger.error(f"Error registering function '{request.name}': {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
