from swap_comparator.utils.utils_1inch import get_1inch_price
from swap_comparator.utils.constant import MAINNET_ADDRESS


def test_get_1inch_price():
    get_1inch_price(
        token_in=MAINNET_ADDRESS["WETH"],
        token_out=MAINNET_ADDRESS["WBTC"],
        amount_in=1e18,
    )
