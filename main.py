import random
import secrets
from account.account import Account
from block.block import Block
from blockchain.blockchain import BlockChain


def main():
    owen = Account()
    brad = Account()
    # blockchain = BlockChain() 

    # try:
    #     while(True):
    #         create_random_transaction(blockchain)
    # except Exception as err:
    #     print(blockchain)

    transaction = owen.prepare_transaction(brad.id, 10.43)
    transaction.amnt = 1000
    print(owen.verify_transaction(transaction))
    

    

def create_random_transaction(blockchain: BlockChain) -> Block:
    return blockchain.add_transaction(['Owen', 'Brad','Billy'][random.randint(0, 2)], ['Owen', 'Brad','Billy'][random.randint(0, 2)], random.randint(0, 100), str(secrets.randbits(80)))

if __name__ == "__main__":
    main()
