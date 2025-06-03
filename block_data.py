from typing import TypeVar, Generic
import numpy as np
from transaction import Transaction

TTransaction = TypeVar('TTransaction')
class BlockData(Generic[TTransaction]):
  transactions: np.typing.NDArray
  count: int = 0
  limit: int
  def __init__(self, limit: int = 10):
    self.transactions = np.ndarray(limit, dtype=TTransaction)
    self.limit = limit

  def add_transaction(self, transaction: TTransaction) -> bool:
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
