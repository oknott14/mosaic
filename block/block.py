import hashlib
import time
from block.data import BlockData

class Block:
  index: int
  timestamp: float
  previous_hash: str
  nonce: int = 0
  data: BlockData
  hash: str | None = None
  hash_validation_str: str
  difficulty: int
  def __init__(self, index: int = 0, data: BlockData = BlockData(), previous_hash: str ='', difficulty: int = 4):
    self.timestamp = time.time()
    self.data = data
    self.previous_hash = previous_hash
    self.difficulty = difficulty
    self.difficulty = difficulty
    self.hash_validation_str = '0'*difficulty
    self.index = index
    
  def add_transaction(self, frm: str, to: str, amnt: float, key:str) -> bool:
    return self.data.add_transaction(frm, to, amnt, key)


  def calculate_hash(self) -> bool:
    if (self.data.is_full() and not self.has_valid_hash()):
      hash_string = self.get_hash_string()
      self.hash = hashlib.sha256(hash_string.format(nonce = self.nonce).encode()).hexdigest()
      while (not self.has_valid_hash()):
        self.nonce += 1
        self.hash = hashlib.sha256(hash_string.format(nonce = self.nonce).encode()).hexdigest()
    
    return self.has_valid_hash()
    
  def has_valid_hash(self) -> bool:
    return self.hash is not None and self.hash[0:self.difficulty] == self.hash_validation_str

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