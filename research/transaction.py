class Transaction:
  def __init__(self, frm: str, to: str, amnt: float, signature: bytes = ''.encode()):
    self.frm = frm
    self.to = to
    self.amnt = amnt
    self.signature = signature

  def __str__(self):
    return f'{self.frm} => {self.to} - {self.amnt}'
  
  def sign(self, signature: bytes):
    self.signature = signature
    return self
  
  def to_unsigned_bytes(self) -> bytes:
    return f'{self.frm} => {self.to} - {self.amnt}'.encode('utf-8')