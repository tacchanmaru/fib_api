from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, PositiveInt

app = FastAPI()

class FibonacciResponse(BaseModel):
    result: int

def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 下の様に書くと、全てのエラーがこのハンドラで処理されるので、拡張性が低い

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=422,
#         content={"status": 422, "message": "n must be PositiveInt"}
#     )

@app.get("/fib")
def read_fib(n = None):
    if n is None:
        return JSONResponse(
            status_code=422,
            content = {"status": 422, "message": "need query parameter n"}
        )
    try:
        n = int(n)
    except ValueError:
        return JSONResponse(
            status_code=422,
            content = {"status": 422, "message": "n must be PositiveInt"}
        )
    if n <= 0:
        return JSONResponse(
            status_code=400,
            content = {"status": 422, "message": "n must be PositiveInt"}
        )
    result = fibonacci(n)
    return FibonacciResponse(result=result)