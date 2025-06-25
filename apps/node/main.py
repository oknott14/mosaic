import uvicorn
from fastapi import FastAPI

from util.environment import Environment

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"success": True}


if __name__ == "__main__":
    env = Environment()
    host = env.get_or_default_to("HOST", default="0.0.0.0")
    port = env.get_or_default_to("PORT", default=3000, cast_to=int)
    uvicorn.run(app, host=host, port=port)
