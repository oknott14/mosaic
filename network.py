from abc import ABC
import asyncio
from typing import List
from block import Block, PublishedBlock
from event import Event
from node import Node


class Network(ABC):

  nodes: List[Node] = []
  on_new_block: Event[Block] = Event()

  def __init__(self):
    self.on_new_block.subscribe(self.notify_new_block)

  def register_node(self, node: Node):
    if not node in self.nodes:
      self.nodes.append(node)
      node.register_publish_block(self.on_new_block).subscribe(self.notify_new_block)

  def notify_new_block(self, block: Block):
    self.on_new_block.emit(block)

  