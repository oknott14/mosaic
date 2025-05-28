import random
from block.block import Block
import secrets

from blockchain.blockchain import BlockChain

def main():
    
    blockchain = BlockChain() 

    try:
        while(True):
            create_random_transaction(blockchain)
    except Exception as err:
        print(blockchain)


    

    

def create_random_transaction(blockchain: BlockChain) -> Block:
    return blockchain.add_transaction(['Owen', 'Brad','Billy'][random.randint(0, 2)], ['Owen', 'Brad','Billy'][random.randint(0, 2)], random.randint(0, 100), str(secrets.randbits(80)))

if __name__ == "__main__":
    main()
