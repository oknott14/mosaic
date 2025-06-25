from os import environ

import uvicorn
from fastapi import FastAPI

from .models.registry import NodeRegistry
from .routers import discover
from .services.discover import NodeDiscoveryService

app = FastAPI()
app.include_router(discover.router)

print("Finding Nodes")
registry = NodeRegistry()
discovery_service = NodeDiscoveryService()
for node in registry.list():
    discovered = discovery_service.introduce(node)

    if discovered is not None:
        registry.register(discovered)
print("Nodes Found")


@app.get("/health")
async def health_check():
    return {"success": True}


if __name__ == "__main__":
    host = environ.get("HOST", default="0.0.0.0")
    port = int(environ.get("PORT", default=3000))
    uvicorn.run(app, host=host, port=port)
