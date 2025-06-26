# Mosaic

A lightweight blockchain implementation built with Python.

## Overview

Mosaic is a educational blockchain project designed to demonstrate core blockchain concepts including block creation, proof-of-work consensus, and transaction validation. Built from the ground up in Python, it provides a clear and accessible implementation of blockchain fundamentals.

## Features

- **Block Creation**: Create and validate blocks with transaction data
- **Proof of Work**: Secure consensus mechanism with adjustable difficulty
- **Transaction System**: Send, receive, and validate transactions
- **Chain Validation**: Ensure blockchain integrity and immutability
- **Mining**: Mine new blocks and earn rewards
- **Persistence**: Save and load blockchain state

## Requirements

- Python 3.12+
- Docker 28.2.2+

## Installation

1. Clone the repository:

```bash
git clone https://github.com/oknott14/mosaic.git
cd mosaic
```

2. Run `docker compose up` to start the container(s)

## Project Structure

```
mosaic/
├── mosaic/
│   ├── __init__.py
│   ├── blockchain.py     # Core blockchain logic
│   ├── block.py          # Block implementation
│   ├── transaction.py    # Transaction handling
│   ├── miner.py          # Mining functionality
│   ├── wallet.py         # Wallet management
│   ├── cli.py            # Command line interface
│   └── api.py            # REST API
├── tests/
│   ├── test_blockchain.py
│   ├── test_block.py
│   └── test_transaction.py
├── requirements.txt
├── setup.py
└── README.md
```

## Testing

<!-- TODO: Testing -->
<!-- Run the test suite:

```bash
python -m pytest tests/
```

Run with coverage:

```bash
python -m pytest --cov=mosaic tests/
``` -->

## Configuration

Configuration options can be set in `config.py`:

- Mining difficulty
- Block reward amount
- Maximum transactions per block
- Network settings

## Roadmap

- [ ] Peer-to-peer networking
- [ ] Smart contracts
- [ ] Web-based explorer
- [ ] Performance optimizations
- [ ] Additional consensus algorithms

<!-- ## License -->

## Acknowledgments

- Inspired by Bitcoin's original whitepaper
- Built for educational purposes
- Thanks to the open-source blockchain community

## Contact

- [Email](oknott2000@gmail.com)
