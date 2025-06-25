from fastapi import APIRouter

from ..models.node import MyNode, Node

router = APIRouter(
  prefix='/discover',
  tags=['discover','networking']
)

@router.post('/')
async def discover_node(node: Node):

    print(node)

    return MyNode()
