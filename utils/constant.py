import os

from dotenv import load_dotenv

load_dotenv()
ID1inch = os.getenv("ID1inch")


class MainnetAddress:
    WETH = "0xC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2"
    WBTC = "0x2260FAC5E5542A773AA44FBCFEDF7C193BC2C599"
