from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, PositiveInt
import math
from decimal import Decimal, getcontext, Overflow

app = FastAPI()

class FibonacciResponse(BaseModel):
    result: int

# def fibonacci(n: int) -> int:
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b

def fibonacci(n: int, max_digits: int = 4300) -> Decimal:
    getcontext().prec = max_digits  # 計算精度を設定
    a, b = Decimal(0), Decimal(1)
    
    try:
        for _ in range(2, n + 1):
            a, b = b, a + b
            if b.adjusted() > max_digits:  # adjusted() は指数部を返し、桁数がこれを超えたかを確認
                # print(b)
                raise OverflowError("The number has exceeded the maximum allowed digits: {}".format(max_digits))
    except Overflow:
        print("Calculation stopped due to overflow: digits limit exceeded")
        return Decimal('Infinity')  # 無限大を示す値を返すか、適切な値または状態を設定
        
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
    try:
        result = fibonacci(n)
    except OverflowError:
        return JSONResponse(
            status_code=400,
            content = {"status": 400, "message": "The number has exceeded the maximum allowed digits"}
        )

    return FibonacciResponse(result=result)