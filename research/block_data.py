from abc import ABC
import numpy as np
from transaction import Transaction

class BlockData(ABC):
  transactions: np.typing.NDArray
  count: int
  limit: int
  
  def __init__(self, limit: int = 3):
    self.transactions = np.ndarray(limit, dtype=Transaction)
    self.limit = limit
    self.count = 0

  def add_transaction(self, transaction: Transaction) -> bool:
    if (self.is_full()):
      return False
    else:
      self.transactions[self.count] = transaction
      self.count += 1
      return True
    
  def is_full(self) -> bool:
    return self.count >= self.limit

  def __str__(self):
    return '\n'.join(self.transactions.astype(str))
