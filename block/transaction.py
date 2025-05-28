class Transaction:
  def __init__(self, frm: str, to: str, amnt: str, key: str):
    self.frm = frm
    self.to = to
    self.amnt = amnt
    self.key = key

  def __str__(self):
    return f'{self.frm} => {self.to} - {self.amnt} ({self.key})'