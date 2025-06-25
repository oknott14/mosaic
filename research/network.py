from abc import ABC
from typing import List
from node import Node

class Network(ABC):

  nodes: List[Node] = []

  def register_node(self, node: Node):
    if not (node in self.nodes):
      print(f'Registering node {node}')
      for registered_node in self.nodes:
        print(f'\tConnecting {node} to {registered_node}')
        registered_node.on_new_transaction.subscribe(node.add_transaction)
        registered_node.on_proposed_block.subscribe(node.add_block)
        node.on_new_transaction.subscribe(registered_node.add_transaction)
        node.on_proposed_block.subscribe(registered_node.add_block)

      self.nodes.append(node)
    

  def remove_node(self, node: Node):
    if node in self.nodes:
      self.nodes.remove(node)

      for registered_node in self.nodes:
        registered_node.on_new_transaction.remove(node.add_transaction)
        registered_node.on_proposed_block.remove(node.add_block)
        node.on_new_transaction.remove(registered_node.add_transaction)
        node.on_proposed_block.remove(registered_node.add_block)