import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()
ID1inch = os.getenv("ID1inch")
RPS1inch = float(os.getenv("RPS1inch"))

RPSOdos = float(os.getenv("RPSOdos"))

ID0xSwap = os.getenv("ID0xSwap")
RPS0xSwap = float(os.getenv("RPS0xSwap"))

RPSLiFi = float(os.getenv("RPSLiFi"))
from_address_LiFi = os.getenv("FromAddressLiFi")


@dataclass
class Mainnet:
    symbol: str
    token_address: str
    decimals: int


class ArbiscanMainnet:
    WETH = Mainnet("WETH", "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1", 18)
    WBTC = Mainnet("WBTC", "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f", 8)
    USDC = Mainnet("USDC", "0xaf88d065e77c8cC2239327C5EDb3A432268e5831", 6)
    USDT = Mainnet("USDT", "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9", 6)
    ARB = Mainnet("ARB", "0x912CE59144191C1204E64559FE8253a0e49E6548", 18)
    WSTETH = Mainnet("WSTETH", "0x0fBcbaEA96Ce0cF7Ee00A8c19c3ab6f5Dc8E1921", 18)


class EtherscanMainnet:
    WETH = Mainnet("WETH", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", 18)
    WBTC = Mainnet("WBTC", "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", 8)
    USDC = Mainnet("USDC", "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", 6)
    USDT = Mainnet("USDT", "0xdAC17F958D2ee523a2206206994597C13D831ec7", 6)
    ARB = Mainnet("ARB", "0xB50721BCf8d664c30412Cfbc6cf7a15145234ad1", 18)
    WSTETH = Mainnet("WSTETH", "0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0", 18)
    MKR = Mainnet("MKR", "0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2", 18)
    DAI = Mainnet("DAI", "0x6B175474E89094C44Da98b954EedeAC495271d0F", 18)
    PEPE = Mainnet("PEPE", "0x6982508145454Ce325dDbE47a25d4ec3d2311933", 18)


class AmountCategory:
    stable_coin = [100, 1000, 10000, 100000, 1000000]
    WETH = [0.01, 0.1, 1, 10, 100, 1000, 10000]
    WBTC = [0.01, 0.1, 1, 10, 100, 1000, 10000]


@dataclass
class Chain:
    ID: int
    name: str


class ChainList:
    ETH = Chain(1, "ETH")
    BSC = Chain(56, "BSC")
    ARBITRUM = Chain(42161, "ARBITRUM")
    OPTIMISM = Chain(10, "OPTIMISM")
    POLYGON = Chain(137, "POLYGON")
    FANTOM = Chain(250, "FANTOM")
    AVALANCHE = Chain(43114, "AVALANCHE")
