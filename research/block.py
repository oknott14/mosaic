from abc import ABC
import hashlib
import time
from typing import Callable, Self
from block_data import BlockData
from transaction import Transaction
import asyncio

class Block(ABC):
  index: int
  timestamp: float
  previous_hash: str
  nonce: int = 0
  data: BlockData
  hash: str | None
  hash_validation_str: str
  difficulty: int

  p_hash_calculation: asyncio.Task[Self] | None

  def __init__(self, index: int = 0, data: BlockData = BlockData(), previous_hash: str ='', difficulty: int = 4):
    self.timestamp = time.time()
    self.data = data
    self.previous_hash = previous_hash
    self.difficulty = difficulty
    self.difficulty = difficulty
    self.hash_validation_str = '0'*difficulty
    self.index = index
    self.hash = None
    self.p_hash_calculation = None
    
  def add_transaction(self, transaction: Transaction) -> bool:
    return self.data.add_transaction(transaction)

  def calculate_hash(self, then: Callable[[Self], None] | None = None, err: Callable[[Exception], None] | None = None):
    self.p_hash_calculation = asyncio.create_task(self.__calculate_hash())
    self.p_hash_calculation.add_done_callback(self.__on_hash_calculated(then, err))
    return self.p_hash_calculation
    
  async def __calculate_hash(self):
    print(f'Calculating Hash for Block {self.index}')
    if (self.has_max_transactions() and not self.has_valid_hash()):
      hash_string = self.get_hash_string()
      self.hash = hashlib.sha256(hash_string.format(nonce = self.nonce).encode()).hexdigest()
      while (not self.has_valid_hash()):
        self.nonce += 1
        self.hash = hashlib.sha256(hash_string.format(nonce = self.nonce).encode()).hexdigest()
    
    print(f'Hash Calculated for Block {self.index}')
    self.p_hash_calculation = None
    return self

  def __on_hash_calculated(self, then: Callable[[Self], None] | None, err: Callable[[Exception], None] | None):
    def on_hash_calculated(task: asyncio.Task[Self]):
      if task.exception() and err:
        err(task.exception())

      if not task.cancelled() and task.done() and then:
        then(task.result())

    return on_hash_calculated
    
  def has_valid_hash(self) -> bool:
    return self.hash is not None and self.hash[0:self.difficulty] == self.hash_validation_str

  def has_max_transactions(self) -> bool:
    return self.data.is_full()
  
  def is_valid_and_complete(self) -> bool:
    return self.data.is_full() and self.has_valid_hash()
  
  def get_hash_string(self):
    return f'''index: {self.index}
    timestamp: {self.timestamp}
    nonce: {{nonce}}
    previous_hash: {self.previous_hash}
    data: {self.data}'''
  
  def __str__(self):
    return f'''index: {self.index}
    timestamp: {self.timestamp}
    nonce: {self.nonce}
    previous_hash: {self.previous_hash}
    data: {self.data}
    hash: {self.hash}'''