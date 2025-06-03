import asyncio
import random
import secrets
from account.account import Account
from block.block import Block
from blockchain.blockchain import BlockChain
from network.network import Network


async def main():
    owen = Account()
    brad = Account()

    network = Network()
    network.register_node(owen)
    network.register_node(brad)
    
    asyncio.create_task(owen.send_transaction(owen.prepare_transaction('brad', 10)))
    asyncio.create_task(brad.send_transaction(brad.prepare_transaction('owen', 5))).add_done_callback(lambda: print(owen.blockchain))

if __name__ == "__main__":
    asyncio.run(main())
