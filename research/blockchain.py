from abc import ABC
from typing import List
from block import Block

class BlockChain(ABC):
  chain: List[Block] = []
  difficulty: int
  
  @property
  def blocks(self) -> int:
    return len(self.chain)
  
  @property
  def current_block(self) -> Block:
    return self.chain[self.blocks - 1]
  
  def __init__(self, difficulty: int = 4):
    self.difficulty = difficulty

  def add_block(self, block: Block) -> Block:
    if (not block.is_valid_and_complete()):
      raise Exception('Failed to add block - block is either invalid or incomplete')

    if self.blocks and block == self.current_block:
      return self.current_block

    self.chain.append(block)
    return block

  def create_genesis_block(self) -> Block:
    starting_hash = '0'*64
    return Block(index=self.blocks, difficulty=self.difficulty, previous_hash=starting_hash)
    
  def get_next_block(self) -> Block:
    if self.blocks == 0:
      raise Exception('Failed to get next block - blockchain is empty') 
    
    return Block(index = self.blocks, previous_hash=self.current_block.hash, difficulty=self.difficulty)

  def __str__(self):
    return ('\n' + '-'*30+'\n').join(self.chain.astype(str))