import aiohttp
import asyncio
import datetime

from swap_comparator.utils.constant import ID1inch, AmountCategory, Mainnet, ArbiscanMainnet, EtherscanMainnet, ChainList, Chain


async def run_1inch(data: list[dict], timestamp: datetime.datetime):
    tasks = []

    for amount_stable_coin in AmountCategory.stable_coin:
        tasks.append(update_data(data, timestamp, ChainList.ARBITRUM, ArbiscanMainnet.USDC, ArbiscanMainnet.USDT, amount_stable_coin))

        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.USDC, EtherscanMainnet.USDT, amount_stable_coin))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.USDC, EtherscanMainnet.DAI, amount_stable_coin))

    for amount_WETH in AmountCategory.WETH:
        tasks.append(update_data(data, timestamp, ChainList.ARBITRUM, ArbiscanMainnet.WETH, ArbiscanMainnet.USDC, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ARBITRUM, ArbiscanMainnet.WETH, ArbiscanMainnet.USDT, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ARBITRUM, ArbiscanMainnet.WETH, ArbiscanMainnet.ARB, amount_WETH))

        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.WBTC, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.USDC, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.USDT, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.WSTETH, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.MKR, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.PEPE, amount_WETH))

    for amount_WBTC in AmountCategory.WBTC:
        pass

    for task in tasks:
        await task
        await asyncio.sleep(1)


async def update_data(
    data: list[dict],
    timestamp: datetime.datetime,
    chain: Chain,
    token_in: Mainnet,
    token_out: Mainnet,
    amount_stable_coin: float,
):
    to_add = await get_1inch_price(
        chain=chain,
        token_in=token_in,
        token_out=token_out,
        amount_in=int(amount_stable_coin * 10**token_in.decimals),
    )
    try:
        amountOut = to_add["dstAmount"]
        elem = {
            "timestamp": timestamp,
            "platform": "1inch",
            "chainId": chain.ID,
            "fromToken": token_in.symbol,
            "toToken": token_out.symbol,
            "gasCost": "",
            "amountIn": amount_stable_coin,
            "amountOut": int(amountOut / 10**token_out.decimals),
        }
        data.append(elem)
    except KeyError:
        print(f"KeyError on response {to_add}")


async def get_1inch_price(
    chain: Chain,
    token_in: Mainnet,
    token_out: Mainnet,
    amount_in: float,
    method: str = "get",
) -> dict:
    api_url = f"https://api.1inch.dev/swap/v6.0/{chain.ID}/quote"
    headers = {"Authorization": f"Bearer {ID1inch}"}
    body = {}
    params = {
        "src": token_in.token_address,
        "dst": token_out.token_address,
        "amount": amount_in,
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api_url, headers=headers, params=params) as response:
                if response.status != 200:
                    print(
                        f"""Error {response.status} while fetching {api_url}
The parameters were: {params}
The response was: {await response.text()}
"""
                    )
                    return {}
                return await response.json()
        except asyncio.TimeoutError:
            print(f"Timeout error occurred while fetching {api_url}")
