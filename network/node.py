from abc import ABC
from typing import TypeVar, Generic
import asyncio
import secrets
from block.block import Block, PublishedBlock
from block.transaction import Transaction
from blockchain.blockchain import BlockChain
from event import Event

class Node(ABC):
  id: str
  blockchain: BlockChain = BlockChain(4)
  __on_send_transaction: Event[Transaction] = Event()
  __on_publish_block: Event[Block] = Event()

  def __init__(self):
    self.id = str(secrets.randbits(40))

  async def add_transaction(self, transaction: Transaction):
    block = self.blockchain.add_transaction(transaction)
    
    if block.has_max_transactions():
      asyncio.shield(
        asyncio.create_task(
          block.calculate_hash()
        ).add_done_callback(self.publish_block)
      )

  async def send_transaction(self, transaction:Transaction):
    if self.__on_send_transaction:
      self.__on_send_transaction.emit(transaction)

  async def add_block(self, block: Block):
    if not self.blockchain.current_block == block:
      self.blockchain.add_block(block)

  async def publish_block(self, block: Block):
    if self.__on_publish_block:
      self.__on_publish_block.emit(block)

  def register_send_transaction(self, event: Event[Transaction]):
    event.subscribe(self.add_transaction)
    return self.__on_send_transaction

  def register_publish_block(self, event: Event[Block]):
    event.subscribe(self.add_block)
    return self.__on_publish_block

TTransaction = TypeVar('TTransaction')
class BaseNode(Generic[TTransaction]):
  blockchain: BlockChain
  def add_transaction(self, transaction: TTransaction):
    pass

  def send_transaction(self, transaction: TTransaction):
    pass

class MiningNode(BaseNode[TTransaction]):

  def add_block(self, block: Block[TTransaction]):
    pass

  def propose_block(self, block: Block[TTransaction]):
    pass