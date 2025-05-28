from block.transaction import Transaction
import numpy as np

class BlockData:
  transactions: np.typing.NDArray
  count: int = 0
  limit: int
  def __init__(self, limit: int = 10):
    self.transactions = np.ndarray(limit, dtype=Transaction)
    self.limit = limit

  def add_transaction(self, frm: str, to: str, amnt: float, key:str) -> bool:
    if (self.count >= self.limit):
      return True
    else:
      self.transactions[self.count] = Transaction(frm, to, amnt, key)
      self.count += 1
      return self.count >= self.limit
    
  def is_full(self) -> bool:
    return self.count >= self.limit

  def __str__(self):
    return '\n'.join(self.transactions.astype(str))
