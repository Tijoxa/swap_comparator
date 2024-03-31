import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()
ID1inch = os.getenv("ID1inch")


@dataclass
class MainnetAddress:
    token_address: str
    decimals: int


MAINNET_ADDRESS = {
    "WETH": MainnetAddress("0xC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2", 18),
    "WBTC": MainnetAddress("0x2260FAC5E5542A773AA44FBCFEDF7C193BC2C599", 8),
    "USDC": MainnetAddress("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", 6),
    "USDT": MainnetAddress("0xdAC17F958D2ee523a2206206994597C13D831ec7", 6),
    "MKR": MainnetAddress("0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2", 18),
    "ARB": MainnetAddress("0x7ceb23fd6bc0add59e62ac25578270cff1b9f619", 18),
    "WSTETH": MainnetAddress("0x7f39C581F595B53c5CeB19Ee6B41CEfeE6F570A3", 18),
}


class AmountCategory:
    StableCoin = [100, 1000, 10000, 100000, 1000000]
    WETH = [0.01, 0.1, 1, 10, 100, 1000, 10000]
    WBTC = [0.01, 0.1, 1, 10, 100, 1000, 10000]
