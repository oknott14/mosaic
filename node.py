from abc import ABC
from typing import TypeVar, Generic
import asyncio
import secrets
from block import Block, PublishedBlock
from block.transaction import Transaction
from blockchain import BlockChain
from event import Event

TTransaction = TypeVar('TTransaction')
class BaseNode(Generic[TTransaction]):
  __id: str
  blockchain: BlockChain[TTransaction]

  def __init__(self, difficulty: int = 4):
    self.blockchain = BlockChain(4)

  def add_transaction(self, transaction: TTransaction):
    pass

  def send_transaction(self, transaction: TTransaction):
    pass

  def add_block(self, block: Block[TTransaction]):
    pass

  def propose_block(self, block: Block[TTransaction]):
    pass