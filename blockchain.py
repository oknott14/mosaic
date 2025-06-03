from typing import List, TypeVar, Generic
from block import Block
from block.transaction import Transaction

TTransaction = TypeVar("TTransaction")
class BlockChain(Generic[TTransaction]):
  chain: List[Block[TTransaction]] = []
  difficulty: int
  
  @property
  def current_block(self) -> Block[TTransaction]:
    return self.chain[self.blocks - 1]
  
  def __init__(self, difficulty: int = 4):
    self.difficulty = difficulty

  def add_block(self, block: Block[TTransaction] | None = None) -> Block:
    if (block == self.current_block):
      return self.current_block

    self.chain.append(block)
    return block

  def add_transaction(self, transaction: Transaction) -> Block:
    if (self.blocks > 0):
      if (not self.current_block.add_transaction(transaction)):
        self.current_block.calculate_hash()
        print(self.current_block)
        block = self.add_block()
        block.add_transaction(transaction)
        return block
      else:
        return self.current_block
    else:
      block = self.create_genesis_block()
      block.add_transaction(transaction)
      return block

  def create_genesis_block(self) -> Block[TTransaction]:
    starting_hash = '0'*64
    return self.add_block(Block(index=self.blocks, difficulty=self.difficulty, previous_hash=starting_hash))
    
  def create_new_block(self) -> Block:
    if (not self.current_block.is_valid_and_complete()):
      raise Exception(message = 'Failed to create new block -> the previous block is invalid')
    
    return Block(index = self.blocks, previous_hash=self.current_block.hash, difficulty=self.difficulty)

  def __str__(self):
    return ('\n' + '-'*30+'\n').join(self.chain.astype(str))