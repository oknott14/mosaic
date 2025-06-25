from abc import ABC
import secrets
from block import Block
from blockchain import BlockChain
from event import Event
from transaction import Transaction

class Node(ABC):
  __id: str
  blockchain: BlockChain
  current_block: Block | None = None
  on_new_transaction: Event[Transaction]
  on_proposed_block: Event[Block]

  def __init__(self, difficulty: int = 4):
    self.blockchain = BlockChain(difficulty)
    self.__id = str(secrets.randbits(32))
    self.on_new_transaction = Event[Transaction]()
    self.on_proposed_block = Event[Block]()


  def add_transaction(self, transaction: Transaction):
    if not self.current_block:
      self.current_block = self.blockchain.get_next_block()
    
    print(f'{self} is adding transaction {transaction}')
    self.current_block.add_transaction(transaction)

    if self.current_block.has_max_transactions():
      self.current_block.calculate_hash(self.propose_block)

  def send_transaction(self, transaction: Transaction):
    print(f'{self} is sending transaction {transaction}')
    self.add_transaction(transaction)
    self.on_new_transaction.emit(transaction)


  def add_block(self, block: Block):
    print(f'{self} is adding block {block.hash}')
    if block.is_valid_and_complete():
      self.blockchain.add_block(block)

    elif self.current_block is None:
      self.current_block = block

  def propose_block(self, block: Block):
    print(f'{self} is proposing block {block.hash}')
    self.add_block(block)
    self.on_proposed_block.emit(block)

  def __str__(self):
    return self.__id