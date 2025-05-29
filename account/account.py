from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
import secrets
from block.transaction import Transaction

class Account:
  id: str
  balance: float

  def __init__(self):
    self.id = str(secrets.randbits(40))
    self.balance = 0
    self.__private_key = rsa.generate_private_key(65537, 1024)
    self.public_key = self.__private_key.public_key()
    self.__signature_padding = padding.PSS(
      mgf=padding.MGF1(hashes.SHA256()),
      salt_length=padding.PSS.MAX_LENGTH
    )
    self.__signature_algorithm = hashes.SHA256()

  def __sign_bytes(self, data: bytes):
    return self.__private_key.sign(
      data, 
      padding=self.__signature_padding,
      algorithm=self.__signature_algorithm
    )
  
  def prepare_transaction(self, to: str, amnt: float) -> Transaction:
    transaction = Transaction(self.id, to, amnt)
    signature = self.__sign_bytes(transaction.to_unsigned_bytes())
    return transaction.sign(signature)
  
  def verify_transaction(self, transaction:Transaction) -> bool:
    try:
      self.public_key.verify(
        transaction.signature,
        transaction.to_unsigned_bytes(),
        padding = self.__signature_padding,
        algorithm=self.__signature_algorithm
      )
      return True
    except InvalidSignature:
      return False




