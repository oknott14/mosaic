import hashlib
import numpy as np
from block.block import Block


class BlockChain:
  chain = np.arange(5, dtype=Block)
  difficulty: int
  blocks: int = 0
  
  @property
  def current_block(self) -> Block:
    return self.chain[self.blocks - 1]
  
  def __init__(self, difficulty: int = 4):
    self.difficulty = difficulty
    self.create_genesis_block()

  def create_genesis_block(self) -> Block:
    starting_hash = '0'*self.difficulty + hashlib.sha256().hexdigest()[self.difficulty:]
    return self.add_block(Block(index=self.blocks, difficulty=self.difficulty, previous_hash=starting_hash))
  
  def create_new_block(self) -> Block:
    if (not self.current_block.is_valid_and_complete()):
      raise Exception(message = 'Failed to create new block -> the previous block is invalid')
    
    return Block(index = self.blocks, previous_hash=self.current_block.hash, difficulty=self.difficulty)

  def add_block(self, block: Block | None = None) -> Block:
    if (self.blocks >= len(self.chain)):
      raise Exception(message = 'Failed to add new block -> block limit reached')
    
    if (block == None):
      block = self.create_new_block()

    self.chain[self.blocks] = block
    self.blocks += 1
    return block
    
    

  def add_transaction(self, frm: str, to: str, amnt: float, key:str) -> Block:
    if (self.blocks > 0):
      if (not self.current_block.add_transaction(frm, to, amnt, key)):
        self.current_block.calculate_hash()
        print(self.current_block)
        block = self.add_block()
        block.add_transaction(frm, to, amnt, key)
        return block
      else:
        return self.current_block
    else:
      block = self.create_genesis_block()
      block.add_transaction(frm, to, amnt, key)
      return block

  def __str__(self):
    return ('\n' + '-'*30+'\n').join(self.chain.astype(str))