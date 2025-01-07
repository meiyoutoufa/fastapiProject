import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from common.exception import MyException
from common.response import Response
from routers import user_router

app = FastAPI()

app.include_router(user_router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(MyException)
async def exception_handler(request: Request, exc: MyException):
    return JSONResponse(
        status_code=exc.code,
        content=Response(code=exc.code,message= exc.detail, data=None).model_dump()
    )

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
