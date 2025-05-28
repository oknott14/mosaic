import random
from block.block import Block
import secrets

def main():
    
    block = Block()

    while(not create_random_transaction(block)):
        continue

    block.calculate_hash()

    print(block)
    

def create_random_transaction(block: Block) -> bool:
    return block.add_transaction(['Owen', 'Brad','Billy'][random.randint(0, 2)], ['Owen', 'Brad','Billy'][random.randint(0, 2)], random.randint(0, 100), str(secrets.randbits(80)))

if __name__ == "__main__":
    main()
