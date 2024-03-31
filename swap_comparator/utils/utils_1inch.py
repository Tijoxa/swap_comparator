import aiohttp
import asyncio

from swap_comparator.utils.constant import ID1inch, ARBISCAN_MAINNET_ADDRESS, AmountCategory


async def run_1inch(data: list[dict]):
    for amount_stable_coin in AmountCategory.stable_coin:
        to_add = await get_1inch_price(
            token_in=ARBISCAN_MAINNET_ADDRESS["USDC"],
            token_out=ARBISCAN_MAINNET_ADDRESS["USDT"],
            amount_in=amount_stable_coin,
        )
        # TODO: modify to fit expected keys
        data.append(to_add)

    for amount_WETH in AmountCategory.WETH:
        pass

    for amount_WBTC in AmountCategory.WBTC:
        pass


async def get_1inch_price(
    token_in: str,
    token_out: str,
    amount_in: float,
    method: str = "get",
    api_url: str = "https://api.1inch.dev/swap/v6.0/1/quote",
) -> dict:
    headers = {"Authorization": f"Bearer {ID1inch}"}
    body = {}
    params = {
        "src": token_in,
        "dst": token_out,
        "amount": amount_in,
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api_url, headers=headers, params=params) as response:
                return await response.json()
        except asyncio.TimeoutError:
            print(f"Timeout error occurred while fetching {api_url}")
