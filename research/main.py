import asyncio
from account import Account
from network import Network


async def main():
    owen = Account('Owen')
    gen_block = owen.blockchain.create_genesis_block()
    brad = Account('Brad')
    
    owen.add_block(gen_block)
    brad.add_block(gen_block)

    network = Network()
    network.register_node(owen)
    network.register_node(brad)
    
    owen.send_transaction(owen.prepare_transaction('brad', 10))
    brad.send_transaction(brad.prepare_transaction('owen', 5))
    owen.send_transaction(owen.prepare_transaction('brad', 20))
    await asyncio.sleep(10000)
    brad.send_transaction(brad.prepare_transaction('owen', 10))
    owen.send_transaction(owen.prepare_transaction('brad', 5))
    owen.send_transaction(owen.prepare_transaction('brad', 5))
    brad.send_transaction(brad.prepare_transaction('owen', 25))
    owen.send_transaction(owen.prepare_transaction('brad', 5))


if __name__ == "__main__":
    asyncio.run(main())
